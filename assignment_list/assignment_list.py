#!python3
# -*- coding: utf-8 -*-

import sys
import os.path

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *

CURRENT_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))

class AssignmentListUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AssignmentListUI, self).__init__(parent)

        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, 'assignment_list.ui'))
        self.setCentralWidget(self.ui)
        self.resize(900, 700)

        # not_submitted = QPushButton("＞ 未提出 ( 2 )")
        # layout = QVBoxLayout()
        # layout.addWidget(not_submitted)
        # self.setLayout(layout)

        # Signal作成
        # self.ui.not_submitted.clicked.connect(self.click_not_submitted)
        self.ui.task1.clicked.connect(self.click_btn)
        self.ui.task2.clicked.connect(self.click_btn)
        self.ui.task3.clicked.connect(self.click_btn)

        self.setCSS()

    def setCSS(self):
        with open("assignment_list.css","r") as f:
            self.setStyleSheet("".join(f.readlines()))

    def click_not_submitted(self):
        not_submitted.setText('∧ 未提出 ( 2 )')


    def click_btn(self):
        # 押したときの動作
        print("push!!")
        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, 'assignment_details.ui'))
        self.setCentralWidget(self.ui)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    AssignmentListUI = AssignmentListUI()
    p = AssignmentListUI.palette()
    p.setColor(AssignmentListUI.backgroundRole(), QtGui.QColor('#201f1f'))
    AssignmentListUI.setPalette(p)
    AssignmentListUI.show()

    sys.exit(app.exec_())
