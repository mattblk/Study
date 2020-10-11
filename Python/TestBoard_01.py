import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QCheckBox, QSizePolicy
# from io import TextIOWrapper
import win32com.client
from PyQt5.QtCore import QCoreApplication

#한글 안깨지게 하는 부분
# sys.stdout = TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

arr=[0 for i in range(3)]
for i in arr :
    arr[i] = i

print(arr)
