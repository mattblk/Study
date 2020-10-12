import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QCheckBox, QSizePolicy, QGridLayout, QGroupBox,QLineEdit
import win32com.client
from PyQt5.QtCore import QCoreApplication, Qt

#pycatia import
from pycatia import catia
# pycatia를 통해서 viewpoint_3d 지정

# Catia 연결
CATIA = win32com.client.Dispatch('CATIA.application')
def detact_CATIA() :
    try :
        t=CATIA.ActiveDocument.Name
        return True
    except :
        return False


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        #닫기 버튼
        btn_close_main = QPushButton('Close') #QPushButton 클래스 생성
        btn_close_main.clicked.connect(QCoreApplication.instance().quit) #클릭하면 어플리케이션 종료

        h_box_bottom = QHBoxLayout() #close button 영역
        h_box_bottom.addStretch(1)
        h_box_bottom.addWidget(btn_close_main)

        #전체 Update 버튼
        btn_Update_all = QPushButton('Update all')

        h_box_Top =QHBoxLayout() #최상단 h box
        v_box_Top = QVBoxLayout()

        self.isEnable_CATIA = detact_CATIA()

        self.label_Top_1 =QLabel("")
        self.label_Top_2 =QLabel("")
        #최상단 라벨 영역 변경

        self.Top_Label()

        btn_Update_all.clicked.connect(self.Update_all)

        v_box_Top.addWidget(self.label_Top_1)
        v_box_Top.addWidget(self.label_Top_2)

        h_box_Top.addLayout(v_box_Top)
        h_box_Top.addStretch(1)
        h_box_Top.addWidget(btn_Update_all)

        grid = QGridLayout()
        grid.addLayout(h_box_Top,1,0)
        grid.addWidget(self.Visibility_Mode_Group(), 2, 0)
        grid.addWidget(self.View_Control_Group(), 3, 0)
        grid.addLayout(h_box_bottom,8,0)

        self.setLayout(grid)

        self.setWindowTitle('Catia Automation Tools (V_0.1)')
        self.setGeometry(300, 300, 600, 420)
        self.show()

    def Update_all(self):
        self.Vis_state_Initializer()
        self.Top_Label()

    def Top_Label(self) :
        if self.isEnable_CATIA :
            #최상단 label1
            str_label_Top_1="Catia Document Name : "
            Catia_Opened=CATIA.ActiveDocument.Name
            self.label_Top_1.setText(str_label_Top_1+Catia_Opened)
            font_label_Top = self.label_Top_1.font()
            font_label_Top.setFamily('Consolas')
            font_label_Top.setBold(False)
            self.label_Top_1.setFont(font_label_Top)

            #최상단 label2
            str_label_Top_2="Catia Document Type : "
            Catia_Opened_Type = Catia_Opened.split(".")[1]
            self.label_Top_2.setText(str_label_Top_2+Catia_Opened_Type)
            self.label_Top_2.setFont(font_label_Top)


        else :
            self.label_Top_1.setText("열려있는 catia 문서 없음")
            font_label_Top = self.label_Top_1.font()
            font_label_Top.setFamily('Consolas')
            font_label_Top.setBold(True)
            self.label_Top_1.setFont(font_label_Top)

            self.label_Top_2.setText("")


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
        if self.isEnable_CATIA :
            Search_Query = "Name=*" + Search_Text + "*" + ",all"
            Active_Document_Selection = CATIA.ActiveDocument.Selection
            Active_Document_Selection.Search(Search_Query)
            VisProperties1 = Active_Document_Selection.VisProperties
            if state : VisProperties1.SetShow(0)
            else : VisProperties1.SetShow(1)

    #체크박스 체크 여부 초기화
    def Vis_state_Initializer(self):
        self.isEnable_CATIA = detact_CATIA()

        # CATIA.RefreshDisplay = False
        self.Vis_state_Initializer_item(self.checkbox_01)
        self.Vis_state_Initializer_item(self.checkbox_02)
        self.Vis_state_Initializer_item(self.checkbox_03)
        self.Vis_state_Initializer_item(self.checkbox_04)
        self.Vis_state_Initializer_item(self.checkbox_05)
        self.Vis_state_Initializer_item(self.checkbox_06)
        self.Vis_state_Initializer_item(self.checkbox_07)
        self.Vis_state_Initializer_item(self.checkbox_08)
        # CATIA.RefreshDisplay = True

    def Vis_state_Initializer_item(self, checkbox):
        if self.isEnable_CATIA :
            if self.Search_and_Select(checkbox.text()) >= 1 :
                checkbox.setEnabled(True)
                showstate = CATIA.ActiveDocument.Selection.VisProperties.GetShow()
                if showstate[1] == 0 : checkbox.setChecked(True)
                else : checkbox.setChecked(False)
            else :
                checkbox.setChecked(False)
                checkbox.setEnabled(False)
        else :
            checkbox.setChecked(False)
            checkbox.setEnabled(False)
        CATIA.ActiveDocument.Selection.clear()

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

    def Visibility_Mode_Group(self) :
        groupbox = QGroupBox('Visibility Mode')

        h_box_lv2_0 = QHBoxLayout() #프로그램 영역
        h_box_lv2_1 = QHBoxLayout() #프로그램 영역
        v_box_lv3_1 = QVBoxLayout() # 체크박스 들어가는 영역
        v_box_lv3_2 = QVBoxLayout() # 모드 버튼 들어가는 영역
        v_box_Lv1 = QVBoxLayout() #1레벨


        #체크박스들
        self.checkbox_01 = QCheckBox('#Final Part')
        self.checkbox_02 = QCheckBox('#Standard Part')
        self.checkbox_03 = QCheckBox('#Final Shape')
        self.checkbox_04 = QCheckBox('#External Geometry')
        self.checkbox_05 = QCheckBox('#Standards and Informations')
        self.checkbox_06 = QCheckBox('#Annotation for Informations')
        self.checkbox_07 = QCheckBox('#Shape Definition')
        self.checkbox_08 = QCheckBox('Annotation Set')

        #업데이트 버튼
        update_button= QPushButton('Update',self)

        v_box_lv3_1.addWidget(self.checkbox_01)
        v_box_lv3_1.addWidget(self.checkbox_02)
        v_box_lv3_1.addWidget(self.checkbox_03)
        v_box_lv3_1.addWidget(self.checkbox_04)
        v_box_lv3_1.addWidget(self.checkbox_05)
        v_box_lv3_1.addWidget(self.checkbox_06)
        v_box_lv3_1.addWidget(self.checkbox_07)
        v_box_lv3_1.addWidget(self.checkbox_08)
        # v_box_lv3_1.addWidget(update_button)

        # 모드 버튼
        mode_button_01 = QPushButton('Release Mode',self)
        mode_button_02 = QPushButton('Thickness Only',self)
        mode_button_03 = QPushButton('Edit Mode',self)
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

        h_box_lv2_0.addStretch(1)
        h_box_lv2_0.addWidget(update_button)
        h_box_lv2_0.addStretch(1)

        #메인 (최상위 Vbox 선언)

        v_box_Lv1.addStretch(1)
        v_box_Lv1.addLayout(h_box_lv2_0)
        v_box_Lv1.addLayout(h_box_lv2_1, stretch = 1)
        v_box_Lv1.addStretch(1)

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

        update_button.clicked.connect(self.Vis_state_Initializer)
        groupbox.setLayout(v_box_Lv1)

        return groupbox


    def View_Control_Group(self) :
        groupbox = QGroupBox('View Control')

        View_Ctrl_V_Box_0Lv = QVBoxLayout()
        View_Ctrl_H_Box_1Lv = QHBoxLayout()
        View_Ctrl_H_Box_1Lv_Update= QHBoxLayout()
        View_Ctrl_Grid_2Lv = QGridLayout()
        View_Ctrl_V_Box_2Lv = QVBoxLayout()

        self.View_Ctrl_Checkbox_Origin = QCheckBox('Origin',self)
        self.View_Ctrl_Checkbox_Updir = QCheckBox('Up-Dir',self)
        self.View_Ctrl_Checkbox_Sdir = QCheckBox('Sight-Dir',self)
        self.View_Ctrl_Checkbox_Zoom = QCheckBox('Zoom',self)
        self.View_Ctrl_Checkbox_Origin.setChecked(True)
        self.View_Ctrl_Checkbox_Updir.setChecked(True)
        self.View_Ctrl_Checkbox_Sdir.setChecked(True)
        self.View_Ctrl_Checkbox_Zoom.setChecked(True)
        View_Ctrl_Label_x = QLabel('x',self)
        View_Ctrl_Label_y = QLabel('y',self)
        View_Ctrl_Label_z = QLabel('z',self)

        View_Ctrl_Label_x.setAlignment(Qt.AlignHCenter)
        View_Ctrl_Label_y.setAlignment(Qt.AlignHCenter)
        View_Ctrl_Label_z.setAlignment(Qt.AlignHCenter)

        self.View_Ctrl_Line_Edit_O_x = QLineEdit()
        self.View_Ctrl_Line_Edit_O_y = QLineEdit()
        self.View_Ctrl_Line_Edit_O_z = QLineEdit()
        self.View_Ctrl_Line_Edit_U_x = QLineEdit()
        self.View_Ctrl_Line_Edit_U_y = QLineEdit()
        self.View_Ctrl_Line_Edit_U_z = QLineEdit()
        self.View_Ctrl_Line_Edit_S_x = QLineEdit()
        self.View_Ctrl_Line_Edit_S_y = QLineEdit()
        self.View_Ctrl_Line_Edit_S_z = QLineEdit()
        self.View_Ctrl_Line_Edit_Zoom = QLineEdit()

        View_Ctrl_Btn_Update=QPushButton('Update')
        View_Ctrl_Btn_Save=QPushButton('Save Current View')
        View_Ctrl_Btn_Restore=QPushButton('Restore View')
        View_Ctrl_Btn_Mirror=QPushButton('Mirror View')

        View_Ctrl_Btn_Save.clicked.connect(self.Get_View)
        View_Ctrl_Btn_Restore.clicked.connect(self.Set_View)
        View_Ctrl_Btn_Mirror.clicked.connect(self.Set_View_Mirror)

        View_Ctrl_Grid_2Lv.addWidget(self.View_Ctrl_Checkbox_Origin, 1, 0)
        View_Ctrl_Grid_2Lv.addWidget(self.View_Ctrl_Checkbox_Updir, 2, 0)
        View_Ctrl_Grid_2Lv.addWidget(self.View_Ctrl_Checkbox_Sdir, 3, 0)
        View_Ctrl_Grid_2Lv.addWidget(self.View_Ctrl_Checkbox_Zoom, 4, 0)
        View_Ctrl_Grid_2Lv.addWidget(self.View_Ctrl_Line_Edit_O_x, 1, 1)
        View_Ctrl_Grid_2Lv.addWidget(self.View_Ctrl_Line_Edit_O_y,1,2)
        View_Ctrl_Grid_2Lv.addWidget(self.View_Ctrl_Line_Edit_O_z,1,3)
        View_Ctrl_Grid_2Lv.addWidget(self.View_Ctrl_Line_Edit_U_x,2,1)
        View_Ctrl_Grid_2Lv.addWidget(self.View_Ctrl_Line_Edit_U_y,2,2)
        View_Ctrl_Grid_2Lv.addWidget(self.View_Ctrl_Line_Edit_U_z,2,3)
        View_Ctrl_Grid_2Lv.addWidget(self.View_Ctrl_Line_Edit_S_x,3,1)
        View_Ctrl_Grid_2Lv.addWidget(self.View_Ctrl_Line_Edit_S_y,3,2)
        View_Ctrl_Grid_2Lv.addWidget(self.View_Ctrl_Line_Edit_S_z,3,3)
        View_Ctrl_Grid_2Lv.addWidget(View_Ctrl_Label_x,0,1)
        View_Ctrl_Grid_2Lv.addWidget(View_Ctrl_Label_y,0,2)
        View_Ctrl_Grid_2Lv.addWidget(View_Ctrl_Label_z,0,3)
        View_Ctrl_Grid_2Lv.addWidget(self.View_Ctrl_Line_Edit_Zoom,4,1,1,3)

        View_Ctrl_V_Box_2Lv.addStretch(1)
        View_Ctrl_V_Box_2Lv.addWidget(View_Ctrl_Btn_Save)
        View_Ctrl_V_Box_2Lv.addWidget(View_Ctrl_Btn_Restore)
        View_Ctrl_V_Box_2Lv.addWidget(View_Ctrl_Btn_Mirror)

        View_Ctrl_H_Box_1Lv.addLayout(View_Ctrl_Grid_2Lv)
        View_Ctrl_H_Box_1Lv.addLayout(View_Ctrl_V_Box_2Lv)

        View_Ctrl_H_Box_1Lv_Update.addStretch(1)
        View_Ctrl_H_Box_1Lv_Update.addWidget(View_Ctrl_Btn_Update)
        View_Ctrl_H_Box_1Lv_Update.addStretch(1)

        View_Ctrl_V_Box_0Lv.addStretch(1)
        # View_Ctrl_V_Box_0Lv.addLayout(View_Ctrl_H_Box_1Lv_Update)
        View_Ctrl_V_Box_0Lv.addLayout(View_Ctrl_H_Box_1Lv)
        View_Ctrl_V_Box_0Lv.addStretch(1)

        groupbox.setLayout(View_Ctrl_V_Box_0Lv)


        return groupbox

    def Get_Origin(self) :
        view_point_3D = catia().active_window.active_viewer.create_viewer_3d().viewpoint_3d
        origin = view_point_3D.get_origin()
        self.View_Ctrl_Line_Edit_O_x.setText(str(origin[0]))
        self.View_Ctrl_Line_Edit_O_y.setText(str(origin[1]))
        self.View_Ctrl_Line_Edit_O_z.setText(str(origin[2]))
    def Set_Origin(self) :
        view_point_3D = catia().active_window.active_viewer.create_viewer_3d().viewpoint_3d
        origin=[0,0,0]
        origin[0] = float(self.View_Ctrl_Line_Edit_O_x.text())
        origin[1] = float(self.View_Ctrl_Line_Edit_O_y.text())
        origin[2] = float(self.View_Ctrl_Line_Edit_O_z.text())
        view_point_3D.put_origin(origin)
    def Set_Origin_Mirror(self) :
        view_point_3D = catia().active_window.active_viewer.create_viewer_3d().viewpoint_3d
        origin=[0,0,0]
        origin[0] = float(self.View_Ctrl_Line_Edit_O_x.text())
        origin[1] = - float(self.View_Ctrl_Line_Edit_O_y.text())
        origin[2] = float(self.View_Ctrl_Line_Edit_O_z.text())
        view_point_3D.put_origin(origin)
    def Get_UpDir(self) :
        view_point_3D = catia().active_window.active_viewer.create_viewer_3d().viewpoint_3d
        updir = view_point_3D.get_up_direction()
        self.View_Ctrl_Line_Edit_U_x.setText(str(updir[0]))
        self.View_Ctrl_Line_Edit_U_y.setText(str(updir[1]))
        self.View_Ctrl_Line_Edit_U_z.setText(str(updir[2]))
    def Set_UpDir(self) :
        view_point_3D = catia().active_window.active_viewer.create_viewer_3d().viewpoint_3d
        updir=[0,0,0]
        updir[0] = float(self.View_Ctrl_Line_Edit_U_x.text())
        updir[1] = float(self.View_Ctrl_Line_Edit_U_y.text())
        updir[2] = float(self.View_Ctrl_Line_Edit_U_z.text())
        view_point_3D.put_up_direction(updir)
    def Set_UpDir_Mirror(self) :
        view_point_3D = catia().active_window.active_viewer.create_viewer_3d().viewpoint_3d
        updir=[0,0,0]
        updir[0] = float(self.View_Ctrl_Line_Edit_U_x.text())
        updir[1] = - float(self.View_Ctrl_Line_Edit_U_y.text())
        updir[2] = float(self.View_Ctrl_Line_Edit_U_z.text())
        view_point_3D.put_up_direction(updir)
    def Get_SDir(self) :
        view_point_3D = catia().active_window.active_viewer.create_viewer_3d().viewpoint_3d
        sdir = view_point_3D.get_sight_direction()
        self.View_Ctrl_Line_Edit_S_x.setText(str(sdir[0]))
        self.View_Ctrl_Line_Edit_S_y.setText(str(sdir[1]))
        self.View_Ctrl_Line_Edit_S_z.setText(str(sdir[2]))
    def Set_SDir(self) :
        view_point_3D = catia().active_window.active_viewer.create_viewer_3d().viewpoint_3d
        sdir=[0,0,0]
        sdir[0] = float(self.View_Ctrl_Line_Edit_S_x.text())
        sdir[1] = float(self.View_Ctrl_Line_Edit_S_y.text())
        sdir[2] = float(self.View_Ctrl_Line_Edit_S_z.text())
        view_point_3D.put_sight_direction(sdir)
    def Set_SDir_Mirror(self) :
        view_point_3D = catia().active_window.active_viewer.create_viewer_3d().viewpoint_3d
        sdir=[0,0,0]
        sdir[0] = float(self.View_Ctrl_Line_Edit_S_x.text())
        sdir[1] = - float(self.View_Ctrl_Line_Edit_S_y.text())
        sdir[2] = float(self.View_Ctrl_Line_Edit_S_z.text())
        view_point_3D.put_sight_direction(sdir)
    def Get_Zoom(self) :
        Current_Zoom = CATIA.ActiveWindow.ActiveViewer.Viewpoint3D.Zoom
        self.View_Ctrl_Line_Edit_Zoom.setText(str(Current_Zoom))
    def Set_Zoom(self) :
        zoom = float(self.View_Ctrl_Line_Edit_Zoom.text())
        CATIA.ActiveWindow.ActiveViewer.Viewpoint3D.Zoom = zoom
    def Get_View(self) :
        self.Get_Zoom()
        self.Get_Origin()
        self.Get_UpDir()
        self.Get_SDir()
    def Set_View(self) :
        if self.View_Ctrl_Checkbox_Origin.isChecked() :
            self.Set_Origin()
        if self.View_Ctrl_Checkbox_Sdir.isChecked() :
            self.Set_SDir()
        if self.View_Ctrl_Checkbox_Updir.isChecked() :
            self.Set_UpDir()
        if self.View_Ctrl_Checkbox_Zoom.isChecked() :
            self.Set_Zoom()
        CATIA.ActiveDocument.Selection.Search("Name=*xy plane* ,all")
        CATIA.ActiveDocument.Selection.Clear()
    def Set_View_Mirror(self) :
        self.Get_View()
        self.Set_Origin_Mirror()
        self.Set_SDir_Mirror()
        self.Set_UpDir_Mirror()
        self.Set_Zoom()
        CATIA.ActiveDocument.Selection.Search("Name=*xy plane* ,all")
        CATIA.ActiveDocument.Selection.Clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
