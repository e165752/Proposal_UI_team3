#!python3
# -*- coding: utf-8 -*-
 
import sys
import os
 
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
#from side import Side

CURRENT_PATH = os.path.dirname(__file__)
 
 
class FrameLayout(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self.collapse1 = True
        self.collapse2 = True
        super(FrameLayout, self).__init__(parent)
 
        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, 'test_btn.ui'))
        self.setCentralWidget(self.ui)

        # Signal作成
        self.ui.pushButton.clicked.connect(self.click_btn)
        self.ui.btn_c.clicked.connect(self.click_btn2)
#        self.ui.pushButton_2.clicked.connect(self.click_side)
#        self.ui.pushButton_12.clicked.connect(self.click_menu)

#    def click_side(self):
#        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, 'side.ui'))
#        self.setCentralWidget(self.ui)
#        Side()
 
#    def click_menu(self):
#        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, 'menu.ui'))
#        self.setCentralWidget(self.ui)

    def click_btn(self):
        # 押したときの動作
        self.collapse1 = not self.collapse1 #ステータスの反転
        print(self.collapse1)
        self.ui.frame.setVisible(self.collapse1)
#        self.ui.frame.setHidden(self.collapse1)
        if self.collapse1 == True:
            print("open!!")
        else:
            print("close!!")

    def click_btn2(self):
        self.collapse2 = not self.collapse2
        print(self.collapse2)
        self.ui.frame_c.setVisible(self.collapse2)
        if self.collapse2 == True:
            print("クラス選択画面")
        else:
            print("クラス選択画面じゃないよ")

def main():
#    app = QtWidgets.QApplication(sys.argv)
     FrameLayout()
#    a = FrameLayout()
#    a.show()
#    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
#    app = QtWidgets.QApplication(sys.argv)
#    a = FrameLayout()
#    a.show()
#    sys.exit(app.exec_())
