import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from Kiwoom import *

form_class = uic.loadUiType("Pytrader_01.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.kiwoom = Kiwoom()
        self.kiwoom.comm_connect()

        self.trade_stocks_done = False

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        self.timer2 = QTimer(self)
        self.timer2.start(1000 * 10)  #10초에 한번임
        self.timer2.timeout.connect(self.timeout2)

        #계좌정보 관련련
        accouns_num = int(self.kiwoom.get_login_info("ACCOUNT_CNT"))
        accounts = self.kiwoom.get_login_info("ACCNO")

        accounts_list = accounts.split(';')[0:accouns_num]
        self.comboBox_Acc.addItems(accounts_list)

        #종목코드 입력하면 호출되는 슬롯
        self.lineEdit_Stock_Code.textChanged.connect(self.code_changed)
        #주문 버튼
        self.pushButton_order.clicked.connect(self.send_order)
        #조회버튼
        self.pushButton_look.clicked.connect(self.check_balance)

        # 선정 종목 정보 출력 메서드
        self.load_buy_sell_list()

    def timeout(self):
        market_start_time = QTime(9, 0, 0)
        current_time = QTime.currentTime()

        if current_time > market_start_time and self.trade_stocks_done is False:
            self.trade_stocks()
            self.trade_stocks_done = True

        text_time = current_time.toString("hh:mm:ss")
        time_msg = "현재시간: " + text_time

        state = self.kiwoom.GetConnectState()
        if state == 1:
            state_msg = "서버 연결 중"
        else:
            state_msg = "서버 미 연결 중"

        self.statusbar.showMessage(state_msg + " | " + time_msg)

    def timeout2(self):
        if self.checkBox.isChecked():
            self.check_balance()

    def code_changed(self):
        code = self.lineEdit_Stock_Code.text()
        name = self.kiwoom.get_master_code_name(code)
        self.lineEdit_Stock_Code_2.setText(name)

    def send_order(self):
        order_type_lookup = {'신규매수': 1, '신규매도': 2, '매수취소': 3, '매도취소': 4}
        hoga_lookup = {'지정가': "00", '시장가': "03"}

        account = self.comboBox_Acc.currentText()
        order_type = self.comboBox_order_type.currentText()
        code = self.lineEdit_Stock_Code.text()
        hoga = self.comboBox_hoga.currentText()
        num = self.spinBox_num.value()
        price = self.spinBox_price.value()

        self.kiwoom.send_order("send_order_req", "0101", account, order_type_lookup[order_type], code, num, price,hoga_lookup[hoga], "")

    def check_balance(self):
        # 데이터 초기화 먼저 하고
        self.kiwoom.reset_opw00018_output()
        # 계좌 정보 불러오고
        account_number = self.kiwoom.get_login_info("ACCNO")
        account_number = account_number.split(';')[0]

        # set_input_value
        self.kiwoom.set_input_value("계좌번호", account_number)
        # opw00018 실행
        self.kiwoom.comm_rq_data("opw00018_req", "opw00018", 0, "2000")
        # 보유종목이 20개이상일 경우 연속적으로 데이터 요청
        while self.kiwoom.remained_data:
            time.sleep(0.2)
            self.kiwoom.set_input_value("계좌번호", account_number)
            self.kiwoom.comm_rq_data("opw00018_req", "opw00018", 2, "2000")

        # opw00001 d+2추정예수금
        self.kiwoom.set_input_value("계좌번호", account_number)
        self.kiwoom.comm_rq_data("opw00001_req", "opw00001", 0, "2000")

        # balance
        item = QTableWidgetItem(self.kiwoom.d2_deposit)
        item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.tableWidget.setItem(0, 0, item)

        # 싱글데이터 (총매입, 총평가, 총손익, 총수익률, 추정자산)
        for i in range(1, 6):
            item = QTableWidgetItem(self.kiwoom.opw00018_output['single'][i - 1])
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
            self.tableWidget.setItem(0, i, item)

        # 아이템의 크기에 맞춰 행의 높이 조절
        self.tableWidget.resizeRowsToContents()

        # Item list
        item_count = len(self.kiwoom.opw00018_output['multi'])
        # 보유종목 수에 따라서 행의 개수 설정
        self.tableWidget_2.setRowCount(item_count)
        
        # QTableWidget에 아이템 추가
        for j in range(item_count):
            row = self.kiwoom.opw00018_output['multi'][j]
            for i in range(len(row)):
                item = QTableWidgetItem(row[i])
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
                self.tableWidget_2.setItem(j, i, item)
        # 아이템의 크기에 맞춰 행의 높이 조절
        self.tableWidget_2.resizeRowsToContents()


    def load_buy_sell_list(self):
        # 파일 읽어서 데이터 긁어오고 (인코딩에러 조심)
        # f = open("buy_list.txt", 'rt', encoding='UTF8')
        f = open("buy_list.txt", 'rt')
        buy_list = f.readlines()
        f.close()

        # f = open("sell_list.txt", 'rt', encoding='UTF8')
        f = open("sell_list.txt", 'rt')
        sell_list = f.readlines()
        f.close()
        
        # 데이터의 총 개수 확인
        row_count = len(buy_list) + len(sell_list)
        # 자동 선정 종목 리스트 행 수 적용
        self.tableWidget_3.setRowCount(row_count)

        # buy list
        for j in range(len(buy_list)):
            row_data = buy_list[j]
            split_row_data = row_data.split(';')
            # 종목 코드를 종목 명으로 바꿔줌
            split_row_data[1] = self.kiwoom.get_master_code_name(split_row_data[1].rsplit())

            for i in range(len(split_row_data)):
                item = QTableWidgetItem(split_row_data[i].rstrip())
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
                self.tableWidget_3.setItem(j, i, item)

        # sell list
        for j in range(len(sell_list)):
            row_data = sell_list[j]
            split_row_data = row_data.split(';')
            # 종목 코드를 종목 명으로 바꿔줌
            split_row_data[1] = self.kiwoom.get_master_code_name(split_row_data[1].rstrip())

            for i in range(len(split_row_data)):
                item = QTableWidgetItem(split_row_data[i].rstrip())
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
                self.tableWidget_3.setItem(len(buy_list) + j, i, item)

        self.tableWidget_3.resizeRowsToContents()

    def trade_stocks(self):
        hoga_lookup = {'지정가': "00", '시장가': "03"}

        # f = open("buy_list.txt", 'rt', encoding='UTF8')
        f = open("buy_list.txt", 'rt')
        buy_list = f.readlines()
        f.close()

        # f = open("sell_list.txt", 'rt', encoding='UTF8')
        f = open("sell_list.txt", 'rt')
        sell_list = f.readlines()
        f.close()

        # account
        account = self.comboBox_Acc.currentText()

        # buy list
        for row_data in buy_list:
            split_row_data = row_data.split(';')
            hoga = split_row_data[2]
            code = split_row_data[1]
            num = split_row_data[3]
            price = split_row_data[4]

            if split_row_data[-1].rstrip() == '매수전':
                self.kiwoom.send_order("send_order_req", "0101", account, 1, code, num, price, hoga_lookup[hoga], "")

        # sell list
        for row_data in sell_list:
            split_row_data = row_data.split(';')
            hoga = split_row_data[2]
            code = split_row_data[1]
            num = split_row_data[3]
            price = split_row_data[4]

            if split_row_data[-1].rstrip() == '매도전':
                self.kiwoom.send_order("send_order_req", "0101", account, 2, code, num, price, hoga_lookup[hoga], "")

        # buy list
        for i, row_data in enumerate(buy_list):
            buy_list[i] = buy_list[i].replace("매수전", "주문완료")

        # file update
        f = open("buy_list.txt", 'wt')
        for row_data in buy_list:
            f.write(row_data)
        f.close()

        # sell list
        for i, row_data in enumerate(sell_list):
            sell_list[i] = sell_list[i].replace("매도전", "주문완료")

        # file update
        f = open("sell_list.txt", 'wt')
        for row_data in sell_list:
            f.write(row_data)
        f.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()