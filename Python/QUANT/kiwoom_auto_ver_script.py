from pywinauto import application
from pywinauto import timings
import time
import os

app = application.Application()
# app.start("C:/Kiwoom/KiwoomFlash2/khministarter.exe") # Before Update
app.start("C:\\KiwoomFlash3\\bin\\nkministarter.exe")

# title = "번개 Login" # Before Update
title = "번개3 Login"
# dlg = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title=title)) # Before Update
dlg = timings.wait_until_passes(20, 0.5, lambda: app.window(title=title))

pass_ctrl = dlg.Edit2
pass_ctrl.set_focus()
pass_ctrl.type_keys('xxxxx')

cert_ctrl = dlg.Edit3
# SetFocus() ▶ set_focus()
cert_ctrl.set_focus()
# TypeKeys() ▶ type_keys()
cert_ctrl.type_keys('yyyy')

btn_ctrl = dlg.Button0
# Click() ▶ click()
btn_ctrl.click()

time.sleep(50)
# khmini.exe ▶ nkmini.exe
os.system("taskkill /im nkmini.exe")