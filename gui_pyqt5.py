import sys
import datetime
from PyQt5.QtWidgets import (QMainWindow, qApp, QWidget, QPushButton, QApplication, QAction, QLabel, QFileDialog, QStyle, QVBoxLayout)
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
        widget =QWidget(self)
        self.setCentralWidget(widget)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addWidget(self.playButton)

        widget.setLayout(layout)
        self.mediaPlayer.setVideoOutput(videoWidget)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('파일')
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveasAction)
        fileMenu.addAction(exitAction)

        self.setWindowTitle('Face Protector')
        self.setGeometry(50, 50, 1200, 700)
        self.show()

    def add_open(self):
        filename, ext = QFileDialog.getOpenFileName(self, 'Open File', ''
                                             , ''
                                             , 'Video (*.mp4 *.mpg *.mpeg *.avi *.wma)')
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
        
    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

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
    ex.resize(1200, 700)
    ex.show()
    sys.exit(app.exec_())