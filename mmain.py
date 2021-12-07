import sys
import bookmark
from PyQt5.QtWidgets import *
import imgDB
if __name__ == '__main__':
    imgDB.creStarTable()
    app = QApplication(sys.argv)
    win = bookmark.Main1()
    win.show()
    sys.exit(app.exec_())