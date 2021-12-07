import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from numpy.lib import polynomial
import imgDB
import imageio
import os
   
class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        tab = QTabWidget()

        tab_1 = self.create_tab_1()

        tab.addTab(tab_1, "즐겨찾기")

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab)

        self.setLayout(main_layout)
        self.resize(600, 600)
        self.show()

    def create_tab_1(self):
        formlayout = QFormLayout()
        self.btn1 = QPushButton('체크제외 모자이크', self);
        formlayout.addRow(self.btn1)
        self.btn1.clicked.connect(self.clickedBTN1)
        
        self.btn2 = QPushButton('추가로 모자이크 제외할 사람이 있습니다.', self);
        formlayout.addRow(self.btn2)
        self.btn2.clicked.connect(self.clickedBTN2)

        li = imgDB.fromStar()
        self.chk = []
        self.tname = []
        timg = []
        
        for x in li:
            self.chk.append(QCheckBox(x, self))
            self.tname.append(x)
            timg.append(QLabel(self))
 
        for x in range(len(self.chk)):
            array = imgDB.showimg(self.tname[x])
            imageio.imwrite(self.tname[x]+'.jpeg', array)
            pm = QPixmap(self.tname[x]+'.jpeg')
            pm = pm.scaledToHeight(100)
            timg[x].setPixmap(pm)
            os.remove(self.tname[x]+'.jpeg')
        
        for x in range(len(self.chk)):
            formlayout.addRow(self.chk[x])
            self.chk[x].clicked.connect(self.checkedCHK)
            formlayout.addRow(timg[x])
            
        
        widget = QWidget()
        widget.setLayout(formlayout)
        scroll_area = QScrollArea()
        scroll_area.setWidget(widget)
        scroll_area.setWidgetResizable(True)
        return scroll_area
    
    def checkedCHK(self):
        self.checking = []
        for x in range(len(self.chk)):
            if self.chk[x].isChecked():
                self.checking.append(self.tname[x])
        print(self.checking)
    
    
    def clickedBTN1(self):
        for x in range(len(self.checking)):
            imgDB.intoStar(self.checking[x])
        QMessageBox.about(self, "message", str(self.checking))
    
    def clickedBTN2(self):
        print("동영상 검출 돌림")
                

if __name__ == '__main__':
    imgDB.creStarTable()
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())