import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication, Qt


class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      btn = QPushButton('Quit 고 자라', self) #QPushButton 클래스 생성
      #생성자 첫 번째 파라미터는 버튼에 입력될 텍스트, 두 번째는 버튼이 위치할 부모 위젯
      btn.move(50, 50)
      btn.resize(btn.sizeHint())
      btn.clicked.connect(QCoreApplication.instance().quit) #클릭하면 어플리케이션 종료

      self.setWindowTitle('Quit Button')
      self.setGeometry(300, 300, 300, 200)
      self.setWindowFlags(Qt.FramelessWindowHint)
      self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
