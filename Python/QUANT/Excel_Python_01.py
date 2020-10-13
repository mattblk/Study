import win32com.client
#COM객체 생성
excel = win32com.client.Dispatch("Excel.Application")
#엑셀 창 띄우기
excel.Visible = True
# print(excel.Visible)
#통합문서 생성
wb = excel.Workbooks.Add()
#Sheet1 바인딩
ws = wb.Worksheets("Sheet1")
# cells(1,1)에 "hello world 입력"
ws.Cells(1,1).Value = "hello world"
#파일 저장
wb.SaveAs('E:\\01_Project\\00_GitHub_Repository\\Study\\Python\\QUANT\\test.xlsx')
#엑셀 종료 라고 했지만 실제로 엑셀 창이 꺼지지는 않음 COM 객체만 사라지는 것 같음
excel.Quit
