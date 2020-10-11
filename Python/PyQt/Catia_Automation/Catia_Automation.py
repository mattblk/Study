import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QCheckBox, QSizePolicy
from io import TextIOWrapper
import win32com.client
from PyQt5.QtCore import QCoreApplication

#한글 안깨지게 하는 부분
sys.stdout = TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# Catia 연결
CATIA = win32com.client.Dispatch('CATIA.application')


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        h_box_lv2_1 = QHBoxLayout() #프로그램 영역
        h_box_lv2_2 = QHBoxLayout() #close button 영역
        v_box_lv3_1 = QVBoxLayout() # 체크박스 들어가는 영역
        v_box_lv3_2 = QVBoxLayout() # 모드 버튼 들어가는 영역

        #닫기 버튼
        btn_close_main = QPushButton('Quit') #QPushButton 클래스 생성
        btn_close_main.clicked.connect(QCoreApplication.instance().quit) #클릭하면 어플리케이션 종료

        #최상단 label1
        str_label_Top_1="연결된 Catia 문서 : "
        Catia_Opened=CATIA.ActiveDocument.Name
        label_Top_1=QLabel(str_label_Top_1+Catia_Opened)
        font_label_Top = label_Top_1.font()
        font_label_Top.setFamily('Consolas')
        font_label_Top.setBold(False)
        label_Top_1.setFont(font_label_Top)

        #최상단 label2
        str_label_Top_2="Catia 문서 타입 : "
        Catia_Opened_Type = Catia_Opened.split(".")[1]
        label_Top_2=QLabel(str_label_Top_2+Catia_Opened_Type)
        label_Top_2.setFont(font_label_Top)


        #체크박스들
        self.checkbox_01 = QCheckBox('#Final Part')
        self.checkbox_02 = QCheckBox('#Standard Part')
        self.checkbox_03 = QCheckBox('#Final Shape')
        self.checkbox_04 = QCheckBox('#External Geometry')
        self.checkbox_05 = QCheckBox('#Standards and Informations')
        self.checkbox_06 = QCheckBox('#Annotation for Informations')
        self.checkbox_07 = QCheckBox('#Shape Definition')
        self.checkbox_08 = QCheckBox('Annotation Set')


        v_box_lv3_1.addWidget(self.checkbox_01)
        v_box_lv3_1.addWidget(self.checkbox_02)
        v_box_lv3_1.addWidget(self.checkbox_03)
        v_box_lv3_1.addWidget(self.checkbox_04)
        v_box_lv3_1.addWidget(self.checkbox_05)
        v_box_lv3_1.addWidget(self.checkbox_06)
        v_box_lv3_1.addWidget(self.checkbox_07)
        v_box_lv3_1.addWidget(self.checkbox_08)

        # 모드 버튼
        mode_button_01 = QPushButton('출도',self)
        mode_button_02 = QPushButton('Thickness 데이터만',self)
        mode_button_03 = QPushButton('편집',self)
        mode_button_04 = QPushButton('Hide all',self)
        mode_button_05 = QPushButton('Show all',self)

        v_box_lv3_2.addWidget(mode_button_01)
        v_box_lv3_2.addWidget(mode_button_02)
        v_box_lv3_2.addWidget(mode_button_03)
        v_box_lv3_2.addWidget(mode_button_04)
        v_box_lv3_2.addWidget(mode_button_05)


        h_box_lv2_1.addStretch(1)
        h_box_lv2_1.addLayout(v_box_lv3_1)
        h_box_lv2_1.addStretch(1)
        h_box_lv2_1.addLayout(v_box_lv3_2)
        h_box_lv2_1.addStretch(1)

        h_box_lv2_2.addStretch(1)
        h_box_lv2_2.addWidget(btn_close_main)
        # h_box_lv2_2.addStretch(1)

        #메인 (최상위 Vbox 선언)
        v_box_Lv1 = QVBoxLayout()
        v_box_Lv1.addWidget(label_Top_1, stretch = 0)
        v_box_Lv1.addWidget(label_Top_2, stretch = 0)
        v_box_Lv1.addStretch(1)
        v_box_Lv1.addLayout(h_box_lv2_1, stretch = 1)
        v_box_Lv1.addStretch(1)
        v_box_Lv1.addLayout(h_box_lv2_2, stretch = 0)

        #체크박스 상태 초기화
        self.Vis_state_Initializer()


        self.checkbox_01.stateChanged.connect(self.Search_and_Change_Visibility_01)
        self.checkbox_02.stateChanged.connect(self.Search_and_Change_Visibility_02)
        self.checkbox_03.stateChanged.connect(self.Search_and_Change_Visibility_03)
        self.checkbox_04.stateChanged.connect(self.Search_and_Change_Visibility_04)
        self.checkbox_05.stateChanged.connect(self.Search_and_Change_Visibility_05)
        self.checkbox_06.stateChanged.connect(self.Search_and_Change_Visibility_06)
        self.checkbox_07.stateChanged.connect(self.Search_and_Change_Visibility_07)
        self.checkbox_08.stateChanged.connect(self.Search_and_Change_Visibility_08)

        mode_button_01.clicked.connect(self.button_release)
        mode_button_02.clicked.connect(self.button_thickness)
        mode_button_03.clicked.connect(self.button_edit)
        mode_button_04.clicked.connect(self.button_hide_all)
        mode_button_05.clicked.connect(self.button_show_all)


        #lv1 수직박스를 메인 레이아웃으로 설정
        self.setLayout(v_box_Lv1)

        self.setWindowTitle('Catia Automation Tools (V_0.1)')
        self.setGeometry(300, 300, 600, 420)
        self.show()


    def Search_and_Change_Visibility_01(self,state):
        Search_Text = self.checkbox_01.text()
        self.Search_and_Change_Visibility(state,Search_Text)
    def Search_and_Change_Visibility_02(self,state):
        Search_Text = self.checkbox_02.text()
        self.Search_and_Change_Visibility(state,Search_Text)
    def Search_and_Change_Visibility_03(self,state):
        Search_Text = self.checkbox_03.text()
        self.Search_and_Change_Visibility(state,Search_Text)
    def Search_and_Change_Visibility_04(self,state):
        Search_Text = self.checkbox_04.text()
        self.Search_and_Change_Visibility(state,Search_Text)
    def Search_and_Change_Visibility_05(self,state):
        Search_Text = self.checkbox_05.text()
        self.Search_and_Change_Visibility(state,Search_Text)
    def Search_and_Change_Visibility_06(self,state):
        Search_Text = self.checkbox_06.text()
        self.Search_and_Change_Visibility(state,Search_Text)
    def Search_and_Change_Visibility_07(self,state):
        Search_Text = self.checkbox_07.text()
        self.Search_and_Change_Visibility(state,Search_Text)
    def Search_and_Change_Visibility_08(self,state):
        Search_Text = self.checkbox_08.text()
        self.Search_and_Change_Visibility(state,Search_Text)

    def Search_and_Change_Visibility(self,state, Search_Text):
        Search_Query = "Name=*" + Search_Text + "*" + ",all"
        Active_Document_Selection = CATIA.ActiveDocument.Selection
        Active_Document_Selection.Search(Search_Query)
        VisProperties1 = Active_Document_Selection.VisProperties
        if state : VisProperties1.SetShow(0)
        else : VisProperties1.SetShow(1)

    #체크박스 체크 여부 초기화
    def Vis_state_Initializer(self):
        CATIA.RefreshDisplay = False
        self.Vis_state_Initializer_item(self.checkbox_01)
        self.Vis_state_Initializer_item(self.checkbox_02)
        self.Vis_state_Initializer_item(self.checkbox_03)
        self.Vis_state_Initializer_item(self.checkbox_04)
        self.Vis_state_Initializer_item(self.checkbox_05)
        self.Vis_state_Initializer_item(self.checkbox_06)
        self.Vis_state_Initializer_item(self.checkbox_07)
        self.Vis_state_Initializer_item(self.checkbox_08)
        CATIA.RefreshDisplay = True

    def Vis_state_Initializer_item(self, checkbox):
        if self.Search_and_Select(checkbox.text()) >= 1 :
            checkbox.setEnabled(True)
            showstate = CATIA.ActiveDocument.Selection.VisProperties.GetShow()
            if showstate[1] == 0 : checkbox.setChecked(True)
            else : checkbox.setChecked(False)
        else :
            checkbox.setChecked(False)
            checkbox.setEnabled(False)


    def Search_and_Select(self, Search_Text):
        Search_Query = "Name=*" + Search_Text + "*" + ",all"
        Active_Document_Selection = CATIA.ActiveDocument.Selection
        Active_Document_Selection.clear()
        Active_Document_Selection.Search(Search_Query)
        return Active_Document_Selection.count

    def button_release(self):
        self.checkbox_01.setChecked(True)
        self.checkbox_02.setChecked(True)
        self.checkbox_03.setChecked(True)
        self.checkbox_04.setChecked(False)
        self.checkbox_05.setChecked(True)
        self.checkbox_06.setChecked(False)
        self.checkbox_07.setChecked(False)
        self.checkbox_08.setChecked(True)
    def button_edit(self):
        self.checkbox_01.setChecked(False)
        self.checkbox_02.setChecked(False)
        self.checkbox_03.setChecked(False)
        self.checkbox_04.setChecked(False)
        self.checkbox_05.setChecked(False)
        self.checkbox_06.setChecked(False)
        self.checkbox_07.setChecked(True)
        self.checkbox_08.setChecked(False)
    def button_thickness(self):
        self.checkbox_01.setChecked(True)
        self.checkbox_02.setChecked(True)
        self.checkbox_03.setChecked(False)
        self.checkbox_04.setChecked(False)
        self.checkbox_05.setChecked(False)
        self.checkbox_06.setChecked(False)
        self.checkbox_07.setChecked(False)
        self.checkbox_08.setChecked(False)
    def button_hide_all(self):
        self.checkbox_01.setChecked(False)
        self.checkbox_02.setChecked(False)
        self.checkbox_03.setChecked(False)
        self.checkbox_04.setChecked(False)
        self.checkbox_05.setChecked(False)
        self.checkbox_06.setChecked(False)
        self.checkbox_07.setChecked(False)
        self.checkbox_08.setChecked(False)
    def button_show_all(self):
        self.checkbox_01.setChecked(True)
        self.checkbox_02.setChecked(True)
        self.checkbox_03.setChecked(True)
        self.checkbox_04.setChecked(True)
        self.checkbox_05.setChecked(True)
        self.checkbox_06.setChecked(True)
        self.checkbox_07.setChecked(True)
        self.checkbox_08.setChecked(True)



if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
