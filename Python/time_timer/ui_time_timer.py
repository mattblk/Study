# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_time_timer.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Time_timer(object):
    def setupUi(self, Time_timer):
        Time_timer.setObjectName("Time_timer")
        Time_timer.resize(500, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Time_timer.sizePolicy().hasHeightForWidth())
        Time_timer.setSizePolicy(sizePolicy)
        Time_timer.setMinimumSize(QtCore.QSize(300, 300))
        Time_timer.setMaximumSize(QtCore.QSize(1000, 1000))
        Time_timer.setMouseTracking(True)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Time_timer)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.line_edit_hour = QtWidgets.QLineEdit(Time_timer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.line_edit_hour.sizePolicy().hasHeightForWidth())
        self.line_edit_hour.setSizePolicy(sizePolicy)
        self.line_edit_hour.setMinimumSize(QtCore.QSize(50, 30))
        self.line_edit_hour.setMaximumSize(QtCore.QSize(50, 30))
        self.line_edit_hour.setSizeIncrement(QtCore.QSize(50, 10))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.line_edit_hour.setFont(font)
        self.line_edit_hour.setMouseTracking(True)
        self.line_edit_hour.setFrame(False)
        self.line_edit_hour.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_hour.setObjectName("line_edit_hour")
        self.horizontalLayout_2.addWidget(self.line_edit_hour)
        self.label_hour = QtWidgets.QLabel(Time_timer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label_hour.sizePolicy().hasHeightForWidth())
        self.label_hour.setSizePolicy(sizePolicy)
        self.label_hour.setMinimumSize(QtCore.QSize(50, 30))
        self.label_hour.setMaximumSize(QtCore.QSize(50, 30))
        self.label_hour.setSizeIncrement(QtCore.QSize(50, 10))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_hour.setFont(font)
        self.label_hour.setMouseTracking(True)
        self.label_hour.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hour.setObjectName("label_hour")
        self.horizontalLayout_2.addWidget(self.label_hour)
        self.label = QtWidgets.QLabel(Time_timer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.line_edit_min = QtWidgets.QLineEdit(Time_timer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.line_edit_min.sizePolicy().hasHeightForWidth())
        self.line_edit_min.setSizePolicy(sizePolicy)
        self.line_edit_min.setMinimumSize(QtCore.QSize(50, 30))
        self.line_edit_min.setMaximumSize(QtCore.QSize(50, 30))
        self.line_edit_min.setSizeIncrement(QtCore.QSize(50, 10))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.line_edit_min.setFont(font)
        self.line_edit_min.setMouseTracking(True)
        self.line_edit_min.setFrame(False)
        self.line_edit_min.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_min.setReadOnly(False)
        self.line_edit_min.setObjectName("line_edit_min")
        self.horizontalLayout_2.addWidget(self.line_edit_min)
        self.label_min = QtWidgets.QLabel(Time_timer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label_min.sizePolicy().hasHeightForWidth())
        self.label_min.setSizePolicy(sizePolicy)
        self.label_min.setMinimumSize(QtCore.QSize(50, 30))
        self.label_min.setMaximumSize(QtCore.QSize(50, 30))
        self.label_min.setSizeIncrement(QtCore.QSize(50, 10))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_min.setFont(font)
        self.label_min.setMouseTracking(True)
        self.label_min.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_min.setAlignment(QtCore.Qt.AlignCenter)
        self.label_min.setObjectName("label_min")
        self.horizontalLayout_2.addWidget(self.label_min)
        self.label_2 = QtWidgets.QLabel(Time_timer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.line_edit_sec = QtWidgets.QLineEdit(Time_timer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.line_edit_sec.sizePolicy().hasHeightForWidth())
        self.line_edit_sec.setSizePolicy(sizePolicy)
        self.line_edit_sec.setMinimumSize(QtCore.QSize(50, 30))
        self.line_edit_sec.setMaximumSize(QtCore.QSize(50, 30))
        self.line_edit_sec.setSizeIncrement(QtCore.QSize(50, 10))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.line_edit_sec.setFont(font)
        self.line_edit_sec.setMouseTracking(True)
        self.line_edit_sec.setFrame(False)
        self.line_edit_sec.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_sec.setObjectName("line_edit_sec")
        self.horizontalLayout_2.addWidget(self.line_edit_sec)
        self.label_sec = QtWidgets.QLabel(Time_timer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label_sec.sizePolicy().hasHeightForWidth())
        self.label_sec.setSizePolicy(sizePolicy)
        self.label_sec.setMinimumSize(QtCore.QSize(50, 30))
        self.label_sec.setMaximumSize(QtCore.QSize(50, 30))
        self.label_sec.setSizeIncrement(QtCore.QSize(50, 10))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_sec.setFont(font)
        self.label_sec.setMouseTracking(True)
        self.label_sec.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sec.setObjectName("label_sec")
        self.horizontalLayout_2.addWidget(self.label_sec)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.btn_start_stop = QtWidgets.QPushButton(Time_timer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start_stop.sizePolicy().hasHeightForWidth())
        self.btn_start_stop.setSizePolicy(sizePolicy)
        self.btn_start_stop.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_start_stop.setFont(font)
        self.btn_start_stop.setDefault(False)
        self.btn_start_stop.setFlat(False)
        self.btn_start_stop.setObjectName("btn_start_stop")
        self.verticalLayout_2.addWidget(self.btn_start_stop)
        self.btn_options = QtWidgets.QPushButton(Time_timer)
        self.btn_options.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_options.setFont(font)
        self.btn_options.setObjectName("btn_options")
        self.verticalLayout_2.addWidget(self.btn_options)
        self.btn_close = QtWidgets.QPushButton(Time_timer)
        self.btn_close.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_close.setFont(font)
        self.btn_close.setCheckable(False)
        self.btn_close.setDefault(False)
        self.btn_close.setFlat(False)
        self.btn_close.setObjectName("btn_close")
        self.verticalLayout_2.addWidget(self.btn_close)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 2)

        self.retranslateUi(Time_timer)
        QtCore.QMetaObject.connectSlotsByName(Time_timer)

    def retranslateUi(self, Time_timer):
        _translate = QtCore.QCoreApplication.translate
        Time_timer.setWindowTitle(_translate("Time_timer", "Time Timer"))
        self.line_edit_hour.setText(_translate("Time_timer", "00"))
        self.label_hour.setText(_translate("Time_timer", "00"))
        self.label.setText(_translate("Time_timer", ":"))
        self.line_edit_min.setText(_translate("Time_timer", "50"))
        self.label_min.setText(_translate("Time_timer", "50"))
        self.label_2.setText(_translate("Time_timer", ":"))
        self.line_edit_sec.setText(_translate("Time_timer", "00"))
        self.label_sec.setText(_translate("Time_timer", "00"))
        self.btn_start_stop.setText(_translate("Time_timer", "Start"))
        self.btn_options.setText(_translate("Time_timer", "Options"))
        self.btn_close.setText(_translate("Time_timer", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Time_timer = QtWidgets.QWidget()
    ui = Ui_Time_timer()
    ui.setupUi(Time_timer)
    Time_timer.show()
    sys.exit(app.exec_())