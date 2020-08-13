## Ex 4-3. 그리드 레이아웃.

import sys
from urllib import error

import sys
from PyQt5.QtWidgets import *

from urllib.request import *
from urllib.error import *

import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 버튼1 이벤트
def btn1_clicked(text, label):
    if text == '':
        label.setText('주소를 입력해주세요!')
        return 0
    else:
        try:
            res = urlopen(text)
            state = res.status
        except:
            state = 0

        if state != 200:
            label.setText('주소를 다시 한번 확인해주세요')
            return 0
        else:
            label.setText('연결확인!')
            return 1


# 버튼2 이벤트
def btn2_clicked(text, label):
    if text == '':
        label.setText('태그를 입력해 주세요')
        return 0
    else:
        label.setText('ok')
        return 1


# 클롤링 시작 버튼 이벤트
def selenium_crawling(url, type, name, tag):
    chrome_driver = webdriver.chrome()
    chrome_driver.get(url)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # 상태바
        status_label = QLabel('준비!')

        # 주소 관련 ui
        edit1 = QLineEdit()
        btn1 = QPushButton('체크')

        # 태그 관련 UI
        edit2 = QLineEdit()
        btn2 = QPushButton('체크')

        # 크롤링 관련 UI
        btn3 = QPushButton('크롤링 시작')
        rbtn1 = QRadioButton('class', self)
        rbtn2 = QRadioButton('id', self)
        rbtn3 = QRadioButton('name', self)

        btn1.clicked.connect(lambda: btn1_clicked(edit1.text(), status_label))
        btn2.clicked.connect(lambda: btn2_clicked(edit2.text(), status_label))

        # 상태바 배치
        grid.addWidget(status_label, 100, 0, 1, 3)

        # 주소 관련 배치
        grid.addWidget(QLabel('주소:'), 0, 0)
        grid.addWidget(edit1, 0, 1)
        grid.addWidget(btn1, 0, 2)

        # 태그 관련 배치
        grid.addWidget(QLabel('태그:'), 1, 0)
        grid.addWidget(edit2, 1, 1)
        grid.addWidget(btn2, 1, 2)
        grid.addWidget(rbtn1, 2, 0)
        grid.addWidget(rbtn2, 2, 1)
        grid.addWidget(rbtn3, 2, 2)

        # 크롤링 관련 배치
        grid.addWidget(btn3, 3, 1)

        self.setWindowTitle('APP')
        self.setGeometry(800, 500, 500, 100)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
