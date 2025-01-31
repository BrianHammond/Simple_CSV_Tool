from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class About(QMainWindow):
    def __init__(self):
        super().__init__()

    def help_about(self):
        self.window = QMainWindow()
        uic.loadUi("about.ui", self.window) #load the UI file
        self.window.show()