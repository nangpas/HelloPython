# 처음 해보는 프로젝트
# 파이썬으로 크롤링과 데이터 분석을 한번에 ..
# 완성하자..

# 기본패키지 import
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 소스 import
import crawling


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = crawling.App()
    sys.exit(app.exec_())