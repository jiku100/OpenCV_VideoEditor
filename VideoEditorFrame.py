import cv2, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.toolbar = QToolBar(self)
        self.button = QToolButton(self.toolbar)
        self.button.setIcon(QIcon("./src/open.png"))
        self.button.setText("파일 열기")
        self.button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolbar.addWidget(self.button)
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)
        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())