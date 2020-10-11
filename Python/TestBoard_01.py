import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QCheckBox, QSizePolicy
from io import TextIOWrapper
import win32com.client
from PyQt5.QtCore import QCoreApplication

#한글 안깨지게 하는 부분
sys.stdout = TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

CATIA = win32com.client.Dispatch('CATIA.application')

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        def Search_and_Select(Search_Text):
            Search_Query = "Name=*" + Search_Text + "*" + ",all"
            Active_Document_Selection = CATIA.ActiveDocument.Selection
            Active_Document_Selection.clear()
            Active_Document_Selection.Search(Search_Query)
            return Active_Document_Selection.count

        a = Search_and_Select("#Final Part")
        print(a)

        self.setWindowTitle('Catia Automation Tools (V_0.1)')
        self.setGeometry(300, 300, 600, 420)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
