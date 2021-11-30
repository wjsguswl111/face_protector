import sys
import datetime
import cv2
import test_body
from PyQt5.QtWidgets import (QListWidget, QRadioButton, QSlider, QCheckBox, QGroupBox, QHBoxLayout, QMainWindow, qApp, QWidget, QPushButton, QApplication, QAction, QLabel, QFileDialog, QStyle, QVBoxLayout)
from PyQt5.QtGui import QPainter, QIcon, QPalette, QImage
from PyQt5.QtCore import QThread, QDir, QObject, QTimer, QEventLoop, Qt, QUrl, pyqtSignal
from PyQt5.uic import loadUi
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


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
        self.check_body = QCheckBox("Body")
        self.check_body.clicked.connect(self.body_blur)
        self.check_improper = QCheckBox("Improper")
        self.star_btn = QPushButton("즐겨찾기", self)
        self.star_btn.setEnabled(False)
        
        self.slider_time = QSlider(Qt.Horizontal, self)
        self.slider_time.sliderMoved.connect(self.timeChange)
        self.label2 = QLabel("시간", self)
        
        self.label3 = QLabel("", self)

        self.label1 = QLabel("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t볼륨", self)
        self.slider_vol = QSlider(Qt.Horizontal, self)
        self.slider_vol.setRange(0, 100)
        self.slider_vol.setValue(0)
        self.slider_vol.valueChanged.connect(self.volumeChanged)
        
        #self.list = QListWidget(self)
        #self.list.itemDoubleClicked.connect(self.dbClickList)

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
        #thirdLayout.addWidget(self.list, 1)

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

    def add_open(self):
        global filename
        global url
        filename, ext = QFileDialog.getOpenFileName(self, 'Open File', ''
                                             , ''
                                             , 'Video (*.mp4 *.mpg *.mpeg *.avi *.wma)')
        print(filename)
        if filename:
            #self.list.addItem(filename)
            #self.list.setCurrentRow(0)
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
        filesave = QFileDialog.getSaveFileName(self, 'Save as File', ''
                                             , ''
                                             , 'Video (*.mp4 *.mpg *.mpeg *.avi *.wma)')
        str(filesave)
        save = filesave.split('/')
        print(save[5])
    
    def volumeChanged(self, vol):
        self.mediaPlayer.setVolume(vol)
        #print(vol)

    def timeChange(self, pos):
        self.mediaPlayer.setPosition(pos)
        #print(pos)

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

    '''def dbClickList(self, item):
        row = self.list.row(item)
        self.list.setCurrentIndex(item)
        self.mediaPlayer.play()'''

    def body_blur(self):

        cap = cv2.VideoCapture(filename)
        font = cv2.FONT_HERSHEY_SIMPLEX #사람 감지 글씨체 정의

        cap.set(3, 960)
        cap.set(4, 480)

        fps = 20
        width = int(cap.get(3))
        height = int(cap.get(4))
        fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')

        out = cv2.VideoWriter(save, fcc, fps, (width, height))

        hog=cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
        lower_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')
        upper_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')

        while True:
            ret, frame = cap.read()
            grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(grayframe, 1.1, 2, 0, (20, 20))
            lower = lower_cascade.detectMultiScale(grayframe, 1.8, 2, 0, (30, 30))
            upper = upper_cascade.detectMultiScale(grayframe, 1.8, 2, 0, (30, 30))

            if not ret:
                break
    
            detected, _=hog.detectMultiScale(frame)

            for(x, y, w, h) in detected:
                body_img=frame[y:y+h,x:x+w]
                body_img=cv2.resize(body_img, dsize=(0, 0),fx=0.04,fy=0.04)
                body_img=cv2.resize(body_img, (w, h), interpolation=cv2.INTER_AREA)
                frame[y:y+h,x:x+w] = body_img

            for(x, y, w, h) in faces:
                body_img=frame[y:y+h,x:x+w]
                body_img=cv2.resize(body_img, dsize=(0, 0),fx=0.04,fy=0.04)
                body_img=cv2.resize(body_img, (w, h), interpolation=cv2.INTER_AREA)
                frame[y:y+h,x:x+w] = body_img

            for(x, y, w, h) in upper:
                body_img=frame[y:y+h,x:x+w]
                body_img=cv2.resize(body_img, dsize=(0, 0),fx=0.04,fy=0.04)
                body_img=cv2.resize(body_img, (w, h), interpolation=cv2.INTER_AREA)
                frame[y:y+h,x:x+w] = body_img

            for(x, y, w, h) in lower:
                body_img=frame[y:y+h,x:x+w]
                body_img=cv2.resize(body_img, dsize=(0, 0),fx=0.04,fy=0.04)
                body_img=cv2.resize(body_img, (w, h), interpolation=cv2.INTER_AREA)
                frame[y:y+h,x:x+w] = body_img

            cv2.imshow("Detect", frame)
            out.write(frame)
            if cv2.waitKey(10) == 27:
                break
        cap.release()
        out.release()
        cv2.destroyAllWindows()

    '''def body_blur(self):
        #file = filename
        test_body.blur()'''
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CWidget()
    ex.resize(1500, 900)
    ex.show()
    sys.exit(app.exec_())