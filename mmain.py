import sys
import GUI
from PyQt5.QtWidgets import *
import imgDB
import GUI
if __name__ == '__main__':
    imgDB.creStarTable()
    app = QApplication(sys.argv)
    win = GUI.CWidget()
    win.show()
    sys.exit(app.exec_())