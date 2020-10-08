import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


from PyQt5.QtCore import QDate, Qt, QTime, QDateTime

#QDate 클래스를 이용해서 날짜를 출력
now = QDate.currentDate()
print(now.toString()) #목 10 8 2020
print(now.toString('d.M.yy')) #8.10.20
print(now.toString('dd.MM.yyyy')) #08.10.2020
print(now.toString('ddd.MMMM.yyyy')) #목.10월.2020
print(now.toString(Qt.ISODate)) #2020-10-08
print(now.toString(Qt.DefaultLocaleLongDate)) #2020년 10월 8일 목요일

print("\n")

time = QTime.currentTime()
print(time.toString())#16:52:10
print(time.toString('h.m.s')) #16.52.10
print(time.toString('hh.mm.ss')) #16.52.10
print(time.toString('hh.mm.ss.zzz')) #16.52.10.014
print(time.toString(Qt.DefaultLocaleLongDate)) #오후 4:52:10
print(time.toString(Qt.DefaultLocaleShortDate)) #오후 4:52

print("\n")

datetime = QDateTime.currentDateTime()
print(datetime.toString()) #목 10 8 16:53:24 2020
print(datetime.toString('d.M.yy hh:mm:ss')) #8.10.20 16:53:36
print(datetime.toString('dd.MM.yyyy, hh:mm:ss')) #08.10.2020, 16:53:36
print(datetime.toString(Qt.DefaultLocaleLongDate)) #2020년 10월 8일 목요일 오후 4:53:36
print(datetime.toString(Qt.DefaultLocaleShortDate)) #2020-10-08 오후 4:53
