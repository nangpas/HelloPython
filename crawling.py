import requests
from bs4 import BeautifulSoup

import sys
from PyQt5.QtWidgets import *

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.setWindowTitle('App')
        self.statusBar().showMessage('준비 완료!!')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()