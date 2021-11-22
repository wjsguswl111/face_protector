import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QCheckBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('choun1')
        lb1_img = QLabel()
        lb1_img.setPixmap(pixmap)
        lb1_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        lb

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())