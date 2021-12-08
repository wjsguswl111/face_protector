import sys
import datetime
import cv2
import numpy as np
import imutils
from PIL import ImageGrab, Image, ImageDraw
from pymysql import connect
import imgDB
import deleteFile
import pymysql
from os import listdir
from os.path import isfile, join
import os
import imageio
#from PyQt5.QtWidgets import (QListWidget, QRadioButton, QSlider, QCheckBox, QGroupBox, QHBoxLayout, QMainWindow, qApp, QWidget, QPushButton, QApplication, QAction, QLabel, QFileDialog, QStyle, QVBoxLayout)
from PyQt5.QtGui import QPixmap, QPainter, QIcon, QPalette, QImage
from PyQt5.QtCore import QThread, QDir, QObject, QTimer, QEventLoop, Qt, QUrl, pyqtSignal
from PyQt5.uic import loadUi
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *
from numpy.lib import polynomial
from array import array
import time
from io import BytesIO
import requests
import io
import test3
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import bookmark



class CWidget(QMainWindow):
    state_signal = pyqtSignal(str)
    duration_signal = pyqtSignal(int)
    position_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global videoWidget
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        
        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.black)
        videoWidget.setAutoFillBackground(True);
        videoWidget.setPalette(pal)

        self.duration = ''

        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.stateChanged.connect(self.stateChanged)
            
        self.duration_signal.connect(self.updateBar)
        self.position_signal.connect(self.updatePos)

        self.playButton = QPushButton()
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)
        self.stopButton = QPushButton()
        self.stopButton.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.stopButton.clicked.connect(self.stop)
        self.pauseButton = QPushButton()
        self.pauseButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        self.pauseButton.clicked.connect(self.pause)

        openAction = QAction('Open File', self)
        openAction.setStatusTip('Open New File')
        openAction.triggered.connect(self.add_open)
        saveAction = QAction('Save File', self)
        saveAction.setStatusTip('Save File')
        saveAction.triggered.connect(self.add_save)
        saveasAction = QAction('Save as File', self)
        saveasAction.setStatusTip('Save as File')
        saveasAction.triggered.connect(self.add_saveas)
        exitAction = QAction('Exit', self)
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        widget = QWidget(self)
        self.setCentralWidget(widget)
        
        groupBox = QGroupBox("모자이크 선택")
        self.check_face = QCheckBox("Face")
        
        
        self.check_face.clicked.connect(self.ddd)
        self.check_body = QCheckBox("Body")
        self.check_body.clicked.connect(self.isSugg)
        self.check_improper = QCheckBox("Improper")
        self.star_btn = QPushButton("즐겨찾기", self)
        #self.star_btn.clicked.connect(self.face_detection)
        
        self.slider_time = QSlider(Qt.Horizontal, self)
        self.slider_time.sliderMoved.connect(self.timeChange)
        self.label2 = QLabel("시간", self)
        
        self.label3 = QLabel("", self)

        self.label1 = QLabel("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t볼륨", self)
        self.slider_vol = QSlider(Qt.Horizontal, self)
        self.slider_vol.setRange(0, 100)
        self.slider_vol.setValue(0)
        self.slider_vol.valueChanged.connect(self.volumeChanged)

        topInnerLayout = QHBoxLayout()
        topInnerLayout.addWidget(self.check_face)
        topInnerLayout.addWidget(self.check_body)
        topInnerLayout.addWidget(self.check_improper)
        topInnerLayout.addWidget(self.star_btn)

        groupBox.setLayout(topInnerLayout)

        topLayout = QVBoxLayout()
        topLayout.addWidget(groupBox)

        firstLayout = QHBoxLayout()
        firstLayout.addWidget(self.slider_time)
        firstLayout.addWidget(self.label2)

        secondLayout = QHBoxLayout()
        secondLayout.addWidget(self.label3)
        secondLayout.addWidget(self.label1)
        secondLayout.addWidget(self.slider_vol)

        thirdLayout = QHBoxLayout()
        thirdLayout.addWidget(self.playButton, 1)
        thirdLayout.addWidget(self.pauseButton, 1)
        thirdLayout.addWidget(self.stopButton, 1)
        layout = QVBoxLayout()
        layout.addLayout(topLayout, 1)
        layout.addWidget(videoWidget, 1200)
        layout.addLayout(firstLayout, 1)
        layout.addLayout(secondLayout, 1)
        layout.addLayout(thirdLayout, 1)
        
        self.statusBar().showMessage('준비')
        
        widget.setLayout(layout)
        
        self.mediaPlayer.setVideoOutput(videoWidget)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('파일')
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveasAction)
        fileMenu.addAction(exitAction)

        self.setWindowTitle('Face Protector')
        self.setGeometry(50, 50, 1500, 900)
        self.show()

    def ddd(self):
        win = bookmark.Main1()
        win.showModal3()
        
    def add_open(self):
        global filename
        global url
        filename, ext = QFileDialog.getOpenFileName(self, 'Open File', ''
                                                , ''
                                                , 'Video (*.mp4 *.mpg *.mpeg *.avi *.wma)')
        print(filename)
        if filename:
            for f in filename:
                url = QUrl.fromLocalFile(f)
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
    
    def play(self):
        self.mediaPlayer.play()

    def stop(self):
        self.mediaPlayer.stop()
        
    def pause(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

    def add_save(self):
        return filename

    def add_saveas(self):
        global filesave
        global save
        filesave, ext = QFileDialog.getSaveFileName(self, 'Save as File', ''
                                             , ''
                                             , 'Video (*.mp4 *.mpg *.mpeg *.avi *.wma)')
    
    def volumeChanged(self, vol):
        self.mediaPlayer.setVolume(vol)

    def timeChange(self, pos):
        self.mediaPlayer.setPosition(pos)

    def durationChanged(self, duration):
        self.duration_signal.emit(duration)

    def positionChanged(self, pos):
        self.position_signal.emit(pos)

    def updateBar(self, duration):
        self.slider_time.setRange(0, duration)
        self.slider_time.setSingleStep(int(duration/10))
        self.slider_time.setPageStep(int(duration/10))
        self.slider_time.setTickInterval(int(duration/10))
        td = datetime.timedelta(milliseconds=duration)
        stime = str(td)
        idx = stime.rfind('.')
        self.duration = stime[:idx]

    def updatePos(self, pos):
        self.slider_time.setValue(pos)
        td = datetime.timedelta(milliseconds=pos)
        stime = str(td)
        idx = stime.rfind('.')
        stime = f'{stime[:idx]} / {self.duration}'
        self.label2.setText(stime)

    def stateChanged(self, state):
        msg = ''
        if state == QMediaPlayer.StoppedState:
            msg = '초기화'
            self.label3.setText(msg)
        elif state == QMediaPlayer.PlayingState:
            msg = '재생'
            self.label3.setText(msg)
        else:
            msg = '멈춤'
            self.label3.setText(msg)
        self.state_signal.emit(msg)

    def isSugg(self):
        cnt=0
        cap = cv2.VideoCapture(filename)
        wid = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        hei = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
        out = cv2.VideoWriter(filesave, fourcc, 30.0, (int(wid), int(hei)))
        x=1
        y=1
        w=1
        h=1

        while True:
            ret, frame = cap.read()
            #frame = imutils.resize(frame, width=600)

            if(cnt % 30 == 0):
                cnt=0

                cv2.imwrite("b1.jpg", frame)

                subscription_key = "49476384fc2548968bfc09ab465229ca"
                endpoint = "https://seungjoolee.cognitiveservices.azure.com/"

                print("===== Detect objects =====")
                analyze_url = endpoint + "vision/v3.1/analyze"
                image_data = open("b1.jpg", "rb").read()
                headers = {'Ocp-Apim-Subscription-Key': subscription_key,
                    'Content-Type': 'application/octet-stream'}
                params = {'visualFeatures': 'objects'}
                response = requests.post(
                    analyze_url, headers=headers, params=params, data=image_data)
                response.raise_for_status()
                analysis = response.json()
                #print(analysis.get('objects'))
                #li = []
            # draw = ImageDraw.Draw(image_data)

                objects = analysis['objects']
                name=0
                for obj in objects:
                    if obj['object'] == 'person':
                        name+=1
                        rect = obj['rectangle']
                        x = rect['x']
                        y = rect['y']
                        w = rect['w']
                        h = rect['h']

                        #cv2.imwrite("ad1.jpg", frame[y:y+h, x:x+w])
                        ad, ra = test3.adult(frame[y:y+h, x:x+w], name)
                        if(ad == True or ra == True):
                            face_region = frame[y:y+h, x:x+w]
                            M = face_region.shape[0]
                            N = face_region.shape[1]
                            face_region = cv2.resize(face_region, None, fx=0.05, fy=0.05, interpolation=cv2.INTER_AREA)
                            face_region = cv2.resize(face_region, (N, M), interpolation=cv2.INTER_AREA)
                            frame[y:y+h, x:x+w] = face_region
                        else:
                            x=1
                            y=1
                            w=1
                            h=1
                        
                os.remove("b1.jpg")
                #draw.rectangle(((x,y), (x+w, y+h)), outline='yellow')
            if x!=1 and y!=1 and w!=1 and h!=1:        
                face_region = frame[y:y+h, x:x+w]
                M = face_region.shape[0]
                N = face_region.shape[1]
                face_region = cv2.resize(face_region, None, fx=0.05, fy=0.05, interpolation=cv2.INTER_AREA)
                face_region = cv2.resize(face_region, (N, M), interpolation=cv2.INTER_AREA)
                frame[y:y+h, x:x+w] = face_region
            
            cnt+=1
            if not ret:
                break
            cv2.imshow("body", frame)
            if cv2.waitKey(1)==27:
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        
    def show(self):
        super().show()
        

# if __name__ == '__main__':
#     imgDB.creStarTable()
#     app = QApplication(sys.argv)
#     ex = CWidget()
#     ex.resize(1500, 900)
#     ex.show()
    
#     sys.exit(app.exec_())