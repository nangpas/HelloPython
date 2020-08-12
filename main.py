## Ex 4-3. 그리드 레이아웃.

import sys
from urllib import error

from PyQt5.QtWidgets import *

from urllib.request import *
from urllib.error import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        label1 = QLabel('')
        label2 = QLabel('')
        edit1 = QLineEdit()
        edit2 = QLineEdit()
        btn1 = QPushButton('체크')
        btn2 = QPushButton('체크')

        btn1.clicked.connect(lambda: self.btn1_clicked(edit1.text(), label1))
        btn2.clicked.connect(lambda: self.btn2_clicked(edit2.text(), label2))

        grid.addWidget(QLabel('주소:'), 0, 0)
        grid.addWidget(label1, 1, 1)
        grid.addWidget(QLabel('태그:'), 2, 0)
        grid.addWidget(label2, 3, 1)

        grid.addWidget(edit1, 0, 1)
        grid.addWidget(edit2, 2, 1)

        grid.addWidget(btn1, 0, 2)
        grid.addWidget(btn2, 2, 2)

        self.setWindowTitle('APP')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def btn1_clicked(self, text, label):
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

    def btn2_clicked(self, text, label):
        if text == '':
            label.setText('태그를 입력해 주세요')
            return 0
        else:
            label.setText('ok')
            return 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())