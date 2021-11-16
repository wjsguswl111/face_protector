from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtCore import Qt, QUrlQuery
from PyQt5.QtGui import QPalette
from PyQt5.uic import loadUi
from media import CMultiMedia
import sys
import datetime

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

class CWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('face.ui', self)

        self.mp = CMultiMedia(self, self.view)

        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.black)
        self.view.setAutoFileBackground(True)
        self.view.setPalette(pal)

        self.vol.setRange(0, 100)
        self.vol.setValue(50)

        self.duration = ''

        self.btn_open.clicked.connect(self.clickOpen)
        self.btn_savd.clicked.connect(self.clickSave)
        self.btn_play.clicked.connect(self.clickPlay)
        self.btn_stop.clicked.connect(self.clickStop)
        self.btn_pause.clicked.connect(self.clickPause)

        self.list.itemDoubleClicked.connect(self.dbClickList)
        self.vol.valueChanged.connect(self.volumeChanged)
        self.bar.sliderMoved.connect(self.barchanged)

    def clickOpen(self):
        files, ext = QFileDialog.getOpenFileNames(self
                                             , 'Select one or more files to open'
                                             , ''
                                             , 'Video (*.mp4 *.mpg *.mpeg *.avi *.wma)') 
        if files:
            cnt = len(files)
            row = self.list.count()
            for i in range(row, row+cnt):
                self.list.addItem(files[i-row])
            self.list.setCurrentRow(0)
            self.mp.addMedia(files)
         
    def clickSave(self):
        print("ok")

    def clickPlay(self):
        index = self.list.currentRow()
        self.mp.playMedia(index)
    
    def clickStop(self):
        self.mp.stopMedia()
    
    def clickPause(self):
        self.mp.pauseMedia()

    def dbClickList(self, item):
        row = self.list.row(item)
        self.mp.playMedia(row)
    
    def volumeChanged(self, vol):
        self.mp.volumeMedia(vol)

    def barChanged(self, pos):
        print(pos)
        self.mp.posMoveMedia(pos)
    
    def updateState(self, msg):
        self.state.setText(msg)

    def updateBar(self, duration):
        self.bar.setRange(0,duration)
        self.bar_setSingleStep(int(duration/10))
        self.bar_setPageStep(int(duration/10))
        self.bar.setTickInterval(int(duration/10))
        td = datetime.timedelta(milliseconds=duration)
        stime = str(td)
        idx = stime.rfind('.')
        self.duration = stime[:idx]

    def updatePos(self, pos):
        self.bar.setValue(pos)
        td = datetime.timedelta(milliseconds=pos)
        stime = str(td)
        idx = stime.rfind('.')
        stime = f'{stime[:idx]} / {self.duration}'
        self.playtime.setText(stime)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    w.show()
    sys.exit(app.exec_())