import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('야 이놈들아 아이콘안뜨잖아')
        self.setWindowIcon(QIcon("\web.png")) #경로 명에 "."이 있어서 잘 안됨ㅠㅠ
        self.setGeometry(300, 300, 1000, 200)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
