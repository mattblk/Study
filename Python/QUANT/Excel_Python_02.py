import win32com.client
excel = win32com.client.Dispatch("Excel.Application")

#이거 끄니까 엑셀 창 안열고 실행 됨ㅇㅇ
# excel.Visible = True
#파일 열기
wb = excel.Workbooks.Open('E:\\01_Project\\00_GitHub_Repository\\Study\\Python\\QUANT\\test.xlsx')
# ActiveSheet?!
ws = wb.ActiveSheet
# (1,1) 위치의 값 읽어오기
print(ws.Cells(1,1).Value)
#엑셀 종료
excel.Quit()
