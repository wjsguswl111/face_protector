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

        tab.addTab(tab_1, "이름설정")

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab)

        self.setLayout(main_layout)
        self.resize(600, 600)
        self.show()

    def create_tab_1(self):
        formlayout = QFormLayout()
        self.btn = QPushButton('이름설정', self);
        formlayout.addRow(self.btn)
        self.btn.clicked.connect(self.clickedBTN)

        li = imgDB.fromStar()
        self.line = []
        self.tname = []
        timg = []
        
        
        for x in li:
            self.line.append(QLineEdit(x, self))
            self.tname.append(x)
            timg.append(QLabel(self))
 
        for x in range(len(self.line)):
            array = imgDB.showimg(self.tname[x])
            imageio.imwrite(self.tname[x]+'.jpeg', array)
            pm = QPixmap(self.tname[x]+'.jpeg')
            pm = pm.scaledToHeight(100)
            timg[x].setPixmap(pm)
            os.remove(self.tname[x]+'.jpeg')
        
        for x in range(len(self.line)):
            formlayout.addRow(self.line[x])
            formlayout.addRow(timg[x])
            
        
        widget = QWidget()
        widget.setLayout(formlayout)
        scroll_area = QScrollArea()
        scroll_area.setWidget(widget)
        scroll_area.setWidgetResizable(True)
        return scroll_area
    
    
    def clickedBTN(self):
        self.text = []
        for x in range(len(self.line)):
            self.text.append(self.line[x].text())
        
        btnReply = QMessageBox.information(self, "message", str(self.text),QMessageBox.Yes)
        if btnReply==QMessageBox.Yes:
            for x in range(len(self.line)):
                imgDB.rename(self.tname[x],self.text[x])
                imgDB.reStar(self.tname[x],self.text[x])
    
                

if __name__ == '__main__':
    imgDB.creStarTable()
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())