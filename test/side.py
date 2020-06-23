#!python3
# -*- coding: utf-8 -*-
 
import sys
import os
 
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
import test_pyside9
#from test_pyside9 import FrameLayout

CURRENT_PATH = os.path.dirname(__file__)
 
 
class Side(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Side, self).__init__(parent)
        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, 'side.ui'))
        self.setCentralWidget(self.ui)

        self.ui.pushButton.clicked.connect(self.click_side)

    def click_side(self):
        print("助けてください")
        test_pyside9.FrameLayout()
#        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, 'test_btn.ui')    )
#        self.setCentralWidget(self.ui)

def main():
    app = QtWidgets.QApplication(sys.argv)
    a = Side()
    a.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
#    app = QtWidgets.QApplication(sys.argv)
#    a = Side()
#    a.show()
#    sys.exit(app.exec_())
