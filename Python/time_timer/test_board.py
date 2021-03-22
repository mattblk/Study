import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QComboBox, \
                            QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, QMetaObject, QCoreApplication, QTimer
from PyQt5.QtGui import QPalette, QColor, QFont

class tmp_class(QMainWindow):
    def __init__(self):
        super(tmp_class, self).__init__()

        self.tmp_timer = QTimer(self)
        self.tmp_timer.timeout.connect(self.fn_tmp)
        self.tmp_timer.start(1000)
        print("aa")

    def fn_tmp(self):
        print("웽알웽알")
        self.tmp_timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tmp_ex = tmp_class()

    tmp_ex.show()
    app.exec_()


