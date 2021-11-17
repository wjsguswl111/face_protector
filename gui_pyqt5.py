import sys
import datetime
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QAction, QVBoxLayout, qApp
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl
from PyQt5.uic import loadUi
from gui_media import CMultiMedia

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

class CWidget(QWidget):

    def __init__(self):
        super().__init__()
        loadUi('face.ui', self)

        self.mp = CMultiMedia(self, self.view)

        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.black)
        self.view.setAutoFillBackground(True);
        self.view.setPalette(pal)

        self.vol.setRange(0, 100)
        self.vol.setValue(50)

        self.duration = ''

        self.btn_add.clicked.connect(self.clickAdd)
        self.btn_save.clicked.connect(self.clickSave)
        self.btn_play.clicked.connect(self.clickPlay)
        self.btn_stop.clicked.connect(self.clickStop)
        self.btn_pause.clicked.connect(self.clickPause)
        self.list.itemDoubleClicked.connect(self.dbClickList)
        self.vol.valueChanged.connect(self.volumeChanged)
        self.bar.sliderMoved.connect(self.barChanged)
        
        '''openAction = QAction('Open File', self)
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
        exitAction.triggered.connect(qApp.quit)'''

        '''menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('파일')
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveasAction)
        fileMenu.addAction(exitAction)'''

    '''def add_open(self):
        filename, ext = QFileDialog.getOpenFileName(self, 'Open File', ''
                                             , ''
                                             , 'Video (*.mp4 *.mpg *.mpeg *.avi *.wma)')
        if filename:
            cnt = len(filename)
            row = self.list.count()
            for i in range(row, row+cnt):
                self.list.addItem(filename[i-row])
            self.list.setCurrentRow(0)
            self.mp.addMedia(filename)

    def add_save(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', ''
                                             , ''
                                             , 'Video (*.mp4 *.mpg *.mpeg *.avi *.wma)')

    def add_saveas(self):
        filename = QFileDialog.getSaveFileName(self, 'Save as File', ''
                                             , ''
                                             , 'Video (*.mp4 *.mpg *.mpeg *.avi *.wma)')'''
    def clickAdd(self):
        filename, ext = QFileDialog.getOpenFileNames(self
                                             , 'Select one or more files to open'
                                             , ''
                                             , 'Video (*.mp4 *.mpg *.mpeg *.avi *.wma)') 
        if filename:
            cnt = len(filename)
            row = self.list.count()
            for i in range(row, row+cnt):
                self.list.addItem(filename[i-row])
            self.list.setCurrentRow(0)
            self.mp.addMedia(filename)

    def clickSave(self):
        filename, ext = QFileDialog.getSaveFileName(self
                                             , 'Select one or more files to open'
                                             , ''
                                             , 'Video (*.mp4 *.mpg *.mpeg *.avi *.wma)') 

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
        self.bar.setRange(0, duration)
        self.bar.setSingleStep(int(duration/10))
        self.bar.setPageStep(int(duration/10))
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
    ex = CWidget()
    ex.show()
    sys.exit(app.exec_())

