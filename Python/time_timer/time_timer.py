from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt, QRect, QTimer, QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog
# from ui_time_timer import Ui_Time_timer
# from ui_time_timer_options import Ui_time_timer_options

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

class Ui_time_timer_options(object):
    def setupUi(self, time_timer_options):
        time_timer_options.setObjectName("time_timer_options")
        time_timer_options.resize(733, 413)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(time_timer_options.sizePolicy().hasHeightForWidth())
        time_timer_options.setSizePolicy(sizePolicy)
        time_timer_options.setMinimumSize(QtCore.QSize(0, 0))
        time_timer_options.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(time_timer_options)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(time_timer_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(130, 40))
        self.label.setMaximumSize(QtCore.QSize(130, 40))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.btn_select_color_timer = QtWidgets.QPushButton(time_timer_options)
        self.btn_select_color_timer.setObjectName("btn_select_color_timer")
        self.gridLayout.addWidget(self.btn_select_color_timer, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(time_timer_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(130, 40))
        self.label_2.setMaximumSize(QtCore.QSize(130, 40))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(time_timer_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(130, 40))
        self.label_4.setMaximumSize(QtCore.QSize(130, 40))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineedit_timer_size = QtWidgets.QLineEdit(time_timer_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineedit_timer_size.sizePolicy().hasHeightForWidth())
        self.lineedit_timer_size.setSizePolicy(sizePolicy)
        self.lineedit_timer_size.setMinimumSize(QtCore.QSize(40, 0))
        self.lineedit_timer_size.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineedit_timer_size.setBaseSize(QtCore.QSize(0, 0))
        self.lineedit_timer_size.setObjectName("lineedit_timer_size")
        self.horizontalLayout_6.addWidget(self.lineedit_timer_size)
        self.slider_timer_size = QtWidgets.QSlider(time_timer_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_timer_size.sizePolicy().hasHeightForWidth())
        self.slider_timer_size.setSizePolicy(sizePolicy)
        self.slider_timer_size.setMinimum(200)
        self.slider_timer_size.setMaximum(1000)
        self.slider_timer_size.setProperty("value", 350)
        self.slider_timer_size.setSliderPosition(350)
        self.slider_timer_size.setOrientation(QtCore.Qt.Horizontal)
        self.slider_timer_size.setObjectName("slider_timer_size")
        self.horizontalLayout_6.addWidget(self.slider_timer_size)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_2 = QtWidgets.QFrame(time_timer_options)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.rad_mov_no = QtWidgets.QRadioButton(self.frame_2)
        self.rad_mov_no.setObjectName("rad_mov_no")
        self.horizontalLayout_9.addWidget(self.rad_mov_no)
        self.rad_mov_cont = QtWidgets.QRadioButton(self.frame_2)
        self.rad_mov_cont.setChecked(True)
        self.rad_mov_cont.setObjectName("rad_mov_cont")
        self.horizontalLayout_9.addWidget(self.rad_mov_cont)
        self.horizontalLayout_4.addWidget(self.frame_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(time_timer_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(130, 40))
        self.label_3.setMaximumSize(QtCore.QSize(130, 40))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineedit_timer_opacity = QtWidgets.QLineEdit(time_timer_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineedit_timer_opacity.sizePolicy().hasHeightForWidth())
        self.lineedit_timer_opacity.setSizePolicy(sizePolicy)
        self.lineedit_timer_opacity.setMinimumSize(QtCore.QSize(40, 0))
        self.lineedit_timer_opacity.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineedit_timer_opacity.setBaseSize(QtCore.QSize(0, 0))
        self.lineedit_timer_opacity.setObjectName("lineedit_timer_opacity")
        self.horizontalLayout_7.addWidget(self.lineedit_timer_opacity)
        self.slider_opacity = QtWidgets.QSlider(time_timer_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_opacity.sizePolicy().hasHeightForWidth())
        self.slider_opacity.setSizePolicy(sizePolicy)
        self.slider_opacity.setMaximum(100)
        self.slider_opacity.setSliderPosition(70)
        self.slider_opacity.setOrientation(QtCore.Qt.Horizontal)
        self.slider_opacity.setObjectName("slider_opacity")
        self.horizontalLayout_7.addWidget(self.slider_opacity)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(time_timer_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(130, 40))
        self.label_6.setMaximumSize(QtCore.QSize(130, 16777215))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame = QtWidgets.QFrame(time_timer_options)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.rad_timer_direction_cw = QtWidgets.QRadioButton(self.frame)
        self.rad_timer_direction_cw.setObjectName("rad_timer_direction_cw")
        self.horizontalLayout_8.addWidget(self.rad_timer_direction_cw)
        self.rad_timer_direction_ccw = QtWidgets.QRadioButton(self.frame)
        self.rad_timer_direction_ccw.setChecked(True)
        self.rad_timer_direction_ccw.setObjectName("rad_timer_direction_ccw")
        self.horizontalLayout_8.addWidget(self.rad_timer_direction_ccw)
        self.horizontalLayout_5.addWidget(self.frame)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(time_timer_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(130, 40))
        self.label_5.setMaximumSize(QtCore.QSize(130, 40))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.btn_select_color_text = QtWidgets.QPushButton(time_timer_options)
        self.btn_select_color_text.setObjectName("btn_select_color_text")
        self.gridLayout.addWidget(self.btn_select_color_text, 6, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(time_timer_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(130, 40))
        self.label_7.setMaximumSize(QtCore.QSize(130, 16777215))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(time_timer_options)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.rad_text_visible = QtWidgets.QRadioButton(self.frame_3)
        self.rad_text_visible.setChecked(True)
        self.rad_text_visible.setObjectName("rad_text_visible")
        self.horizontalLayout_10.addWidget(self.rad_text_visible)
        self.rad_text_invisible = QtWidgets.QRadioButton(self.frame_3)
        self.rad_text_invisible.setObjectName("rad_text_invisible")
        self.horizontalLayout_10.addWidget(self.rad_text_invisible)
        self.gridLayout.addWidget(self.frame_3, 4, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.check_box_always_on_top = QtWidgets.QCheckBox(time_timer_options)
        self.check_box_always_on_top.setChecked(True)
        self.check_box_always_on_top.setObjectName("check_box_always_on_top")
        self.horizontalLayout_2.addWidget(self.check_box_always_on_top)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_close = QtWidgets.QPushButton(time_timer_options)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_2.addWidget(self.btn_close)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(time_timer_options)
        QtCore.QMetaObject.connectSlotsByName(time_timer_options)

    def retranslateUi(self, time_timer_options):
        _translate = QtCore.QCoreApplication.translate
        time_timer_options.setWindowTitle(_translate("time_timer_options", "Options"))
        self.label.setText(_translate("time_timer_options", "투명도"))
        self.btn_select_color_timer.setText(_translate("time_timer_options", "Click to select color"))
        self.label_2.setText(_translate("time_timer_options", "텍스트 색상"))
        self.label_4.setText(_translate("time_timer_options", "자동움직임모드"))
        self.lineedit_timer_size.setText(_translate("time_timer_options", "350"))
        self.rad_mov_no.setText(_translate("time_timer_options", "없음"))
        self.rad_mov_cont.setText(_translate("time_timer_options", "연속적"))
        self.label_3.setText(_translate("time_timer_options", "타이머 크기"))
        self.lineedit_timer_opacity.setText(_translate("time_timer_options", "70"))
        self.label_6.setText(_translate("time_timer_options", "시계회전방향"))
        self.rad_timer_direction_cw.setText(_translate("time_timer_options", "시계방향"))
        self.rad_timer_direction_ccw.setText(_translate("time_timer_options", "반시계방향"))
        self.label_5.setText(_translate("time_timer_options", "시계 색상"))
        self.btn_select_color_text.setText(_translate("time_timer_options", "Click to select color"))
        self.label_7.setText(_translate("time_timer_options", "텍스트"))
        self.rad_text_visible.setText(_translate("time_timer_options", "보이기"))
        self.rad_text_invisible.setText(_translate("time_timer_options", "숨기기"))
        self.check_box_always_on_top.setText(_translate("time_timer_options", "항상 위에"))
        self.btn_close.setText(_translate("time_timer_options", "close"))

class my_Time_Timer(QWidget, Ui_Time_timer):
    def __init__(self):
        super(my_Time_Timer, self).__init__()
        self.setupUi(self)

        # Options_timetimer 선언하기
        self.options = options_timetimer()

        self.setMinimumSize(self.options.timer_size, self.options.timer_size)
        self.setMaximumSize(self.options.timer_size, self.options.timer_size)

        # time_remain 초기값 설정
        self.time_remain = 3000  # 기본값 50분 = 3000sec
        self.timer_status_start = False  # False 는 대기중 True 는 실행중

        # 마우스이벤트
        self.is_pressed = 0

        # 초기값으로는 Time_label 숨김
        self.label_hour.hide()
        self.label_min.hide()
        self.label_sec.hide()
        
        # 테두리 없는 창 모드 배경 투명으로
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Validator - lineedit
        self.line_edit_hour.setValidator(QtGui.QIntValidator(0, 60, self))  # 0 ~ 60까지의 정수
        self.line_edit_min.setValidator(QtGui.QIntValidator(0, 60, self))  # 0 ~ 60까지의 정수
        self.line_edit_sec.setValidator(QtGui.QIntValidator(0, 60, self))  # 0 ~ 60까지의 정수
        # 기능추가 : 분, 초 입력란에 60이상의 정수 입력 시 시, 분으로 변환해주는 기능 추가 필요

        # ---------- 타이머 모음 ---------
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeout_timer_end)
        self.timer_sec = QTimer(self)
        self.timer_sec.timeout.connect(self.timeout_timer)
        self.timer_mouse_movement = QTimer(self)
        self.timer_mouse_movement.timeout.connect(self.timeout_mouse_movement)
        self.timer_mouse_movement.start(2000)
        self.timer_move = QTimer(self)
        self.timer_move.timeout.connect(self.timeout_move)

        # --------시그널 보내 시그널 보내 찌릿찌릿찌릿찘--------
        # face_update 관련 시그널
        self.line_edit_hour.textChanged.connect(self.face_update)
        self.line_edit_min.textChanged.connect(self.face_update)
        self.line_edit_sec.textChanged.connect(self.face_update)
        self.line_edit_hour.editingFinished.connect(self.face_update)
        self.line_edit_min.editingFinished.connect(self.face_update)
        self.line_edit_sec.editingFinished.connect(self.face_update)
        # buttons 관련 시그널
        self.btn_start_stop.clicked.connect(self.fn_btn_start_stop)
        self.btn_close.clicked.connect(QCoreApplication.instance().quit)
        self.btn_options.clicked.connect(self.fn_btn_options)

        # 옵션 설정 관련 시그널
        self.options.slider_timer_size.valueChanged.connect(self.window_size_update)
        self.options.slider_opacity.valueChanged.connect(self.timer_opacity_update)
        self.options.btn_select_color_timer.clicked.connect(self.color_picker_bg)
        self.options.btn_select_color_text.clicked.connect(self.color_picker_text)
        self.options.rad_timer_direction_cw.clicked.connect(self.timer_direction_change)
        self.options.rad_timer_direction_ccw.clicked.connect(self.timer_direction_change)
        self.options.rad_text_visible.clicked.connect(self.text_visibility_change)
        self.options.rad_text_invisible.clicked.connect(self.text_visibility_change)
        self.options.rad_text_visible.clicked.connect(self.mouseMoveEvent)
        self.options.rad_text_invisible.clicked.connect(self.mouseMoveEvent)
        self.options.rad_mov_no.clicked.connect(self.timer_movement_change)
        self.options.rad_mov_cont.clicked.connect(self.timer_movement_change)
        self.options.check_box_always_on_top.stateChanged.connect(self.stays_on_top)

    def stays_on_top(self):
        if self.options.check_box_always_on_top.isChecked():
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            self.show()
        else:
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.show()

    def timer_movement_change(self):
        if self.options.rad_mov_no.isChecked():
            self.options.timer_movement = 0
        elif self.options.rad_mov_cont.isChecked():
            self.options.timer_movement = 1

    def text_visibility_change(self):
        if self.options.rad_text_visible.isChecked():
            self.options.text_visibility = 1
        else:
            self.options.text_visibility = 0
        self.update()

    def timer_direction_change(self):
        if self.options.rad_timer_direction_cw.isChecked():
            self.options.timer_direction = 1
        else:
            self.options.timer_direction = -1
        self.update()

    def color_picker_bg(self):
        if self.options.check_box_always_on_top.isChecked():
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.show()
        self.options.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint & ~Qt.FramelessWindowHint)
        self.options.show()

        color_diag = QColorDialog(self)
        color = color_diag.getColor()

        if color:
            self.options.timer_color = list(color.getRgb())
            self.options.btn_select_color_timer.setStyleSheet("color: white; background-color:rgb({r},{g},{b});"
                                                              .format(r=str(self.options.timer_color[0]),
                                                                      g=str(self.options.timer_color[1]),
                                                                      b=str(self.options.timer_color[2])))
            self.update()
        self.options.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.options.show()
        if self.options.check_box_always_on_top.isChecked():
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            self.show()

    def color_picker_text(self):
        color = QColorDialog.getColor()
        if color:
            self.options.text_color = list(color.getRgb())
            self.options.btn_select_color_text.setStyleSheet("color: white; background-color:rgb({r},{g},{b});"
                                                             .format(r=str(self.options.text_color[0]),
                                                                     g=str(self.options.text_color[1]),
                                                                     b=str(self.options.text_color[2])))
            self.label_hour.setStyleSheet("color:rgb({r},{g},{b});"
                                          .format(r=str(self.options.text_color[0]),
                                                  g=str(self.options.text_color[1]),
                                                  b=str(self.options.text_color[2])))
            self.label_min.setStyleSheet("color:rgb({r},{g},{b});"
                                         .format(r=str(self.options.text_color[0]),
                                                 g=str(self.options.text_color[1]),
                                                 b=str(self.options.text_color[2])))
            self.label_sec.setStyleSheet("color:rgb({r},{g},{b});"
                                         .format(r=str(self.options.text_color[0]),
                                                 g=str(self.options.text_color[1]),
                                                 b=str(self.options.text_color[2])))
            self.line_edit_hour.setStyleSheet("color:rgb({r},{g},{b});"
                                              .format(r=str(self.options.text_color[0]),
                                                      g=str(self.options.text_color[1]),
                                                      b=str(self.options.text_color[2])))
            self.line_edit_min.setStyleSheet("color:rgb({r},{g},{b});"
                                             .format(r=str(self.options.text_color[0]),
                                                     g=str(self.options.text_color[1]),
                                                     b=str(self.options.text_color[2])))
            self.line_edit_sec.setStyleSheet("color:rgb({r},{g},{b});"
                                             .format(r=str(self.options.text_color[0]),
                                                     g=str(self.options.text_color[1]),
                                                     b=str(self.options.text_color[2])))
            self.label.setStyleSheet("color:rgb({r},{g},{b});"
                                     .format(r=str(self.options.text_color[0]),
                                             g=str(self.options.text_color[1]),
                                             b=str(self.options.text_color[2])))
            self.label_2.setStyleSheet("color:rgb({r},{g},{b});"
                                       .format(r=str(self.options.text_color[0]),
                                               g=str(self.options.text_color[1]),
                                               b=str(self.options.text_color[2])))
            self.update()

    def window_size_update(self):
        self.setMinimumSize(self.options.timer_size, self.options.timer_size)
        self.setMaximumSize(self.options.timer_size, self.options.timer_size)
        self.update()

    def timer_opacity_update(self):
        self.timeout_mouse_movement()
        self.update()

    def fn_btn_options(self):
        self.options.show()

    def timeout_timer_end(self):
        self.time_remain = 3000
        self.fn_btn_start_stop()
        remain_hour = self.time_remain // 3600
        remain_min = (self.time_remain - (self.time_remain // 3600) * 3600) // 60
        remain_sec = (self.time_remain - (self.time_remain // 3600) * 3600) % 60

        str_remain_hour = '{0:02d}'.format(remain_hour)
        str_remain_min = '{0:02d}'.format(remain_min)
        str_remain_sec = '{0:02d}'.format(remain_sec)

        # 남아있는 시, 분, 초 구해서 label 에 입력
        self.label_hour.setText(str_remain_hour)
        self.label_min.setText(str_remain_min)
        self.label_sec.setText(str_remain_sec)
        # label 값을 line_edit 에 입력
        self.line_edit_hour.setText(str_remain_hour)
        self.line_edit_min.setText(str_remain_min)
        self.line_edit_sec.setText(str_remain_sec)

        self.update()

    def timeout_move(self):
        if self.options.timer_movement == 1:
            # 현재 screen 의 geometry 상태
            screen_width = self.screen().geometry().width()
            screen_height = self.screen().geometry().height()
            screen_pos_x = self.screen().geometry().x()
            screen_pos_y = self.screen().geometry().y()

            widget_pos_x = self.pos().x() - screen_pos_x
            widget_pos_y = self.pos().y() - screen_pos_y

            if self.options.timer_movement_dir_x == 1:
                if widget_pos_x + self.options.timer_size >= screen_width:
                    self.options.timer_movement_dir_x = -1
            else:
                if widget_pos_x <= 0:
                    self.options.timer_movement_dir_x = 1
            if self.options.timer_movement_dir_y == 1:
                if widget_pos_y + self.options.timer_size >= screen_height:
                    self.options.timer_movement_dir_y = -1
            else:
                if widget_pos_y <= 0:
                    self.options.timer_movement_dir_y =1

            x = self.window().pos().x()
            y = self.window().pos().y()
            self.move(x + 1*self.options.timer_movement_dir_x, y + 1*self.options.timer_movement_dir_y)

        elif self.options.timer_movement == 2:
            # 불연속 움직임 모드
            pass

    def timeout_timer(self):
        self.time_remain = int(round(self.timer.remainingTime()/1000, 0))
        remain_hour = self.time_remain // 3600
        remain_min = (self.time_remain - (self.time_remain // 3600)*3600) // 60
        remain_sec = (self.time_remain - (self.time_remain // 3600)*3600) % 60

        str_remain_hour = '{0:02d}'.format(remain_hour)
        str_remain_min = '{0:02d}'.format(remain_min)
        str_remain_sec = '{0:02d}'.format(remain_sec)

        # 남아있는 시, 분, 초 구해서 label 에 입력
        self.label_hour.setText(str_remain_hour)
        self.label_min.setText(str_remain_min)
        self.label_sec.setText(str_remain_sec)
        # label 값을 line_edit 에 입력
        self.line_edit_hour.setText(str_remain_hour)
        self.line_edit_min.setText(str_remain_min)
        self.line_edit_sec.setText(str_remain_sec)

        self.update()

    def timeout_mouse_movement(self):
        self.setWindowOpacity(self.options.timer_opacity)
        self.btn_start_stop.hide()  # start stop 버튼 숨기기
        self.btn_options.hide()  # options 버튼 숨기기
        self.btn_close.hide()  # close 버튼 숨기기
        if self.options.text_visibility == 0:
            self.hide_colon()
            self.hide_label()
            self.hide_line_edit()
        # hide colon
        self.timer_mouse_movement.stop()

    def opacity_reset(self):
        self.setWindowOpacity(1)

    def face_update(self):
        if not self.timer_status_start:
            # 대기중일 경우
            # line edit 에서 가져온 값들을 정수화
            if len(self.line_edit_hour.text()) == 0:
                remain_hour = 0
            else:
                remain_hour = int(self.line_edit_hour.text())
            if len(self.line_edit_min.text()) == 0:
                remain_min = 0
            else:
                remain_min = int(self.line_edit_min.text())
            if len(self.line_edit_sec.text()) == 0:
                remain_sec = 0
            else:
                remain_sec = int(self.line_edit_sec.text())

            str_remain_hour = '{0:02d}'.format(remain_hour)
            str_remain_min = '{0:02d}'.format(remain_min)
            str_remain_sec = '{0:02d}'.format(remain_sec)

            # 남아있는 시, 분, 초 구해서 label 에 입력
            self.label_hour.setText(str_remain_hour)
            self.label_min.setText(str_remain_min)
            self.label_sec.setText(str_remain_sec)
            # label 값을 line_edit 에 입력
            self.line_edit_hour.setText(str_remain_hour)
            self.line_edit_min.setText(str_remain_min)
            self.line_edit_sec.setText(str_remain_sec)

            self.time_remain = int(remain_hour*3600 + remain_min*60 + remain_sec)

        # 실행중일 경우는 뭐 그냥 업데이트만
        self.update()

    def fn_btn_start_stop(self):
        if self.timer_status_start:
            # 타이머 실행중인 상황
            self.show_line_edit()
            self.hide_label()
            self.btn_start_stop.setText("Start")
            self.timer.stop()
            self.timer_sec.stop()
            self.timer_move.stop()
            self.timer_status_start = False
        else:
            # 타이머 대기중인 상황
            # 실행하면 두개 타이머를 동시에 실행
            # timer 는 time_remain 만큼
            # timer_sec 은 1초
            self.timer.start(self.time_remain*1000)
            self.timer_sec.start(1000)
            self.timer_move.start(20)
            self.hide_line_edit()
            self.show_label()
            self.btn_start_stop.setText("Stop")
            self.timer_status_start = True

    def hide_label(self):
        self.label_hour.hide()
        self.label_min.hide()
        self.label_sec.hide()

    def show_label(self):
        self.label_hour.show()
        self.label_min.show()
        self.label_sec.show()

    def hide_line_edit(self):
        self.line_edit_hour.hide()
        self.line_edit_min.hide()
        self.line_edit_sec.hide()

    def show_line_edit(self):
        self.line_edit_hour.show()
        self.line_edit_min.show()
        self.line_edit_sec.show()

    def hide_colon(self):
        self.label.hide()
        self.label_2.hide()

    def show_colon(self):
        self.label.show()
        self.label_2.show()

    # Widget 의 전체 크기를 결정
    # def sizeHint(self):
    #     return QSize(self.options.timer_size, self.options.timer_size)
    #     # return QSize(500, 500)

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        rect = QRect(0, 0, self.options.timer_size, self.options.timer_size)

        qp.begin(self)  # QPainter 그리기 시작
        qp.setRenderHint(QtGui.QPainter.Antialiasing)  # Antialiasing 적용

        # 남은시간 파이 그리기
        qp.setPen(Qt.NoPen)
        qp.setBrush(QtGui.QColor(self.options.timer_color[0], self.options.timer_color[1], self.options.timer_color[2], 255))
        # qp.drawEllipse(0, 0, 300, 300)
        # qp.setPen(Qt.blue)
        # qp.drawLine(self.time_remain,10,100,40)
        # qp.setPen(QtGui.QColor(0, 0, 0, 0))  # Pie 그릴 때 펜 색 투명
        # drawPie(QRect, StartAngle, SpanAngle) 1/16deg 씩 움직임ㅇㅇㅇ
        qp.drawPie(rect, 90 * 16, int(self.time_remain / 10 * 16) * self.options.timer_direction)

        # 파이의 빈공간 칠하기
        qp.setBrush(QtGui.QColor(0, 0, 0, 1))
        qp.drawPie(rect, 90 * 16, 360*16 - int(self.time_remain / 10 * 16 * self.options.timer_direction * -1))
        # qp.drawPie(rect, 0, 180*16)
        qp.end()

    def mousePressEvent(self, event):
        self.offset = event.pos()
        self.is_pressed = 1

    def mouseReleaseEvent(self, event):
        self.is_pressed = 0

    def mouseMoveEvent(self, event):
        self.setWindowOpacity(1)
        self.timer_mouse_movement.start(3000)
        self.btn_start_stop.show()  # start stop 버튼 보이기
        self.btn_options.show()  # options 버튼 보이기
        self.btn_close.show()  # close 버튼 보이기
        self.show_colon()
        if not self.timer_status_start:
            self.show_line_edit()
        else:
            self.show_label()

        if self.is_pressed == 1:
            x = event.globalX()
            y = event.globalY()
            x_w = self.offset.x()
            y_w = self.offset.y()
            self.move(x-x_w, y-y_w)

class options_timetimer(QWidget, Ui_time_timer_options):
    def __init__(self):
        super(options_timetimer, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        
        # 옵션 초기값들 선언
        self.timer_size = 350
        self.timer_opacity = 0.7
        self.timer_movement = 1  # 0: 없음, 1:연속적, 2:불연속
        self.timer_movement_dir_x = 1
        self.timer_movement_dir_y = 1
        self.timer_color = [230, 70, 30, 255]
        self.text_color = [40, 40, 40, 255]
        self.timer_direction = -1  # -1:반시계방향, 1:시계방향
        self.text_visibility = 1  # 1:보이기 0:숨기기

        self.lineedit_timer_size.setValidator(QtGui.QIntValidator(300, 1000, self))  # 0 ~ 60까지의 정수
        self.lineedit_timer_opacity.setValidator(QtGui.QIntValidator(0, 100, self))  # 0 ~ 60까지의 정수

        # close 버튼
        self.btn_close.clicked.connect(self.close_window)
        self.slider_timer_size.valueChanged.connect(self.size_slider_value_change)
        self.slider_opacity.valueChanged.connect(self.opacity_slider_value_change)
        self.lineedit_timer_size.textChanged.connect(self.size_line_edit_change)
        self.lineedit_timer_opacity.textChanged.connect(self.opacity_line_edit_change)

        self.btn_select_color_timer.setStyleSheet("color: white; background-color:rgb({r},{g},{b});"
                                                  .format(r=str(self.timer_color[0]),
                                                          g=str(self.timer_color[1]),
                                                          b=str(self.timer_color[2])))
        self.btn_select_color_text.setStyleSheet("color: white; background-color:rgb({r},{g},{b});"
                                                 .format(r=str(self.text_color[0]),
                                                         g=str(self.text_color[1]),
                                                         b=str(self.text_color[2])))

    def close_window(self):
        self.close()

    def size_slider_value_change(self):
        self.lineedit_timer_size.setText(str(self.slider_timer_size.value()))
        self.timer_size = self.slider_timer_size.value()

    def opacity_slider_value_change(self):
        self.lineedit_timer_opacity.setText(str(self.slider_opacity.value()))
        self.timer_opacity = self.slider_opacity.value() / 100

    def size_line_edit_change(self):
        self.slider_timer_size.setValue(int(self.lineedit_timer_size.text()))
        self.timer_size = int(self.lineedit_timer_size.text())

    def opacity_line_edit_change(self):
        self.slider_opacity.setValue(int(self.lineedit_timer_opacity.text()))
        self.timer_opacity = int(self.lineedit_timer_opacity.text()) / 100


a = QApplication([])
myttm = my_Time_Timer()
myttm.show()
a.exec_()
