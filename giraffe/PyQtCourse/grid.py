from PyQt5.QtWidgets import QApplication, QPushButton,QDialog, QGroupBox, QVBoxLayout, QGridLayout
from PyQt5 import QtGui, QtCore
import sys

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "My First Grid Layout"
        self.left = 200
        self.top = 200
        self.height = 200
        self.width = 200
        self.iconName = "real.jpg"
        self.InitWindow()

        self.show()


    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.height, self.width)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.CreatLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

    def CreatLayout(self):
        self.groupBox = QGroupBox("What is your favorite programming Language?")
        gridLayout = QGridLayout()
        button = QPushButton("My Grid",self)
        button.setIcon(QtGui.QIcon("real.jpg"))
        button.setIconSize(QtCore.QSize(40,40))
        button.setMinimumHeight(40)
        gridLayout.addWidget(button, 0,0)

        button1 = QPushButton("My Grid", self)
        button1.setIcon(QtGui.QIcon("real.jpg"))
        button1.setIconSize(QtCore.QSize(40, 40))
        button1.setMinimumHeight(40)
        gridLayout.addWidget(button1, 0, 1)

        button2 = QPushButton("My Grid", self)
        button2.setIcon(QtGui.QIcon("real.jpg"))
        button2.setIconSize(QtCore.QSize(40, 40))
        button2.setMinimumHeight(40)
        gridLayout.addWidget(button2, 1, 0)

        button3 = QPushButton("My Grid", self)
        button3.setIcon(QtGui.QIcon("real.jpg"))
        button3.setIconSize(QtCore.QSize(40, 40))
        button3.setMinimumHeight(40)
        gridLayout.addWidget(button3, 1, 1)

        self.groupBox.setLayout(gridLayout)



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())