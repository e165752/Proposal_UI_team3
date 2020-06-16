import sys
from PySide import QtCore,QtGui

import ui

class MainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.verticalLayout.removeWidget(self.ui.graphicsView)
        self.ui.graphicsView.deleteLater()
        self.ui.verticalLayout.addWidget(MyGraphicsView(self))

class MyGraphicsView(QtGui.QGraphicsView):

    def __init__(self, parent):
        QtGui.QGraphicsView.__init__(self, parent)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        print('mouseMoveEvent: pos {}'.format(event.pos()))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())