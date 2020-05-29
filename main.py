import csv
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Classification Labeling Tool')
        self.center()
        self.resize(1000, 800)
        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        print(frameGm)
        centerPoint = QDesktopWidget().availableGeometry().center()
        print(centerPoint)
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
