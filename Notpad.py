import time

from pywinauto import application, Desktop, Application

app = Application(backend="uia").start('calc.exe')

dlg = Desktop(backend="uia").Calculator

dlg.child_window(title="Open Navigation", auto_id="TogglePaneButton", control_type="Button").click()

item=dlg.child_window(title="Scientific Calculator", auto_id="Scientific", control_type="ListItem")
item.click_input(coords=(0, 0))
dlg.child_window(title="Seven", auto_id="num7Button", control_type="Button").click()
dlg.child_window(title="Square", auto_id="xpower2Button", control_type="Button").click()
#dlg.child_window(title="Display is 0", auto_id="CalculatorResults", control_type="Text").Text()
dlg.print_control_identifiers()
time.sleep(3)

#app.Scientific.print_control_identifiers()
# time.sleep(3)
# app.Notepad.edit.TypeKeys("This  is  automation")
# time.sleep(2)
# app.Notepad.MenuSelect("File->Save")
# app.SaveAs.edit.SetText("Salman2.txt")
# app.SaveAs.Save.double_click()
# time.sleep(2)
# app.Notepad.Close()






