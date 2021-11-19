import sys
import datetime
from PyQt5.QtWidgets import (QSlider, QCheckBox, QGroupBox, QHBoxLayout, QMainWindow, qApp, QWidget, QPushButton, QApplication, QAction, QLabel, QFileDialog, QStyle, QVBoxLayout)
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.uic import loadUi
from gui_media import CMultiMedia
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


class CWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()

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
        self.check_improper = QCheckBox("Improper")
        
        self.slider_time = QSlider(Qt.Horizontal, self)
        self.slider_time.move(30, 30)
        self.slider_time.setRange(0, 100)
        self.slider_time.setSingleStep(1)
        self.label2 = QLabel("시간", self)

        self.label1 = QLabel("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t볼륨", self)
        self.slider_vol = QSlider(Qt.Horizontal, self)
        self.slider_vol.move(30, 30)
        self.slider_vol.setRange(0, 50)
        self.slider_vol.setSingleStep(1)

        topInnerLayout = QHBoxLayout()
        topInnerLayout.addWidget(self.check_face)
        topInnerLayout.addWidget(self.check_body)
        topInnerLayout.addWidget(self.check_improper)
        groupBox.setLayout(topInnerLayout)

        topLayout = QVBoxLayout()
        topLayout.addWidget(groupBox)

        firstLayout = QHBoxLayout()
        firstLayout.addWidget(self.slider_time)
        firstLayout.addWidget(self.label2)

        secondLayout = QHBoxLayout()
        secondLayout.addWidget(self.label1)
        secondLayout.addWidget(self.slider_vol)

        thirdLayout = QHBoxLayout()
        thirdLayout.addWidget(self.playButton, 1)
        thirdLayout.addWidget(self.stopButton, 1)
        thirdLayout.addWidget(self.pauseButton, 1)

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
        filename, ext = QFileDialog.getOpenFileName(self, 'Open File', ''
                                             , ''
                                             , 'Video (*.mp4 *.mpg *.mpeg *.avi *.wma)')
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
        filename = QFileDialog.getSaveFileName(self, 'Save File', ''
                                             , ''
                                             , 'Video (*.mp4 *.mpg *.mpeg *.avi *.wma)')

    def add_saveas(self):
        filename = QFileDialog.getSaveFileName(self, 'Save as File', ''
                                             , ''
                                             , 'Video (*.mp4 *.mpg *.mpeg *.avi *.wma)')
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CWidget()
    ex.resize(1500, 900)
    ex.show()
    sys.exit(app.exec_())