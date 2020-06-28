import sys
import os.path

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

CURRENT_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))

class UI_btn(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(UI_btn, self).__init__(parent)

        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, 'sample_ui.ui'))
        self.setCentralWidget(self.ui)

        #シグナルの設定
        self.ui.pushButton_5.clicked.connect(self.click_btn)
        self.ui.pushButton_9.clicked.connect(self.click_btn)
        self.ui.pushButton_10.clicked.connect(self.click_btn)
        self.ui.pushButton_11.clicked.connect(self.click_btn)
        self.ui.pushButton_12.clicked.connect(self.click_btn)

        
        
    def click_btn(self):
        # 押したときの動作
        print("Push!!")
        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, 'kadai_detaile.ui'))
        self.setCentralWidget(self.ui)

    def click_test(self):
        print("push!!")
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = UI_btn()
    a.show()
    sys.exit(app.exec_())
    
