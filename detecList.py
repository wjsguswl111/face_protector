import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from numpy.lib import polynomial
import imgDB
import imageio
import os
from PyQt5 import QtCore

import deleteFile
import face_classifier
import insName

class Main2(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        tab = QTabWidget()

        tab_1 = self.create_tab_1()

        tab.addTab(tab_1, "검출결과")

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab)

        self.setLayout(main_layout)
        self.resize(600, 600)
        self.show()
        

    def create_tab_1(self):
        formlayout = QFormLayout()
        self.btn = QPushButton('체크제외 모자이크', self);
        formlayout.addRow(self.btn)
        self.btn.clicked.connect(self.clickedBTN)

        li = imgDB.showTable()
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
    
    
    def clickedBTN(self):
        for x in range(len(self.checking)):
            imgDB.intoStar(self.checking[x],imgDB.callResult2(self.checking[x]))
        btnReply = QMessageBox.information(self, "message", str(self.checking),QMessageBox.Yes)
        li = imgDB.showTable()
        lili = [];
        if btnReply==QMessageBox.Yes:
            for x in range(len(self.checking)):
                if self.checking[x] in li:
                    lili.append(li.index(self.checking[x]))
                else:
                    print(self.checking[x])
            for x in range(len(li)):
                if x in lili:
                    continue
                else:
                    imgDB.delTable(li[x])
                    imgDB.delMember(li[x])
                    deleteFile.delYml(li[x])
            face_classifier.classify()
        win = insName.Main3()
        win.showModal2()

    def showModal(self):
        return super().exec_()


#     imgDB.creStarTable()
#     app = QApplication(sys.argv)
#     main = Main()
#     sys.exit(app.exec_())
# if __name__ == '__main__':
#     main()