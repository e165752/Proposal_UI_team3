#!python3
# -*- coding: utf-8 -*-

import sys
import os.path

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

CURRENT_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))


class UISample(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(UISample, self).__init__(parent)

        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, 'test_buttons.ui'))
        self.widget1 = QUiLoader().load(os.path.join(CURRENT_PATH, 'test2.ui'))
        self.widget2 = QUiLoader().load(os.path.join(CURRENT_PATH, 'page3_main.ui'))
        self.ui.scrollArea.setWidget(self.widget1)
        # self.ui.verticalLayout.addWidget(self.widget2)
        self.setCentralWidget(self.ui)
        # Signal作成
        self.ui.pushButton_1.clicked.connect(self.click_btn1)
        self.ui.pushButton_2.clicked.connect(self.click_btn2)
        
    def click_btn1(self):
        # 押したときの動作
        print("pushed1")
        self.ui.scrollArea.takeWidget()
        self.ui.scrollArea.setWidget(self.widget1)

    def click_btn2(self):
        # 押したときの動作
        print("pushed2")
        self.ui.scrollArea.takeWidget()
        self.ui.scrollArea.setWidget(self.widget2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = UISample()
    a.show()
    sys.exit(app.exec_())

