import time

from behave import *
from pywinauto import application, Desktop


#from selenium import  webdriver


@given(u'Launch the application')
def step_impl(context):
    app1 = application.Application()
    app1.Start(cmd_line=u"calc.exe")
    dialog = Desktop(backend='uia').Calculator


@when(u'click first number for addition')
def step_impl(context):
    dialog = Desktop(backend='uia').Calculator
    dialog.child_window(title="Four", auto_id="num4Button", control_type="Button").click()
@when(u'click add')
def step_impl(context):
    dialog = Desktop(backend='uia').Calculator
    dialog.child_window(title="Plus", auto_id="plusButton", control_type="Button").click()

@when(u'click second number for addition')
def step_impl(context):
    dialog = Desktop(backend='uia').Calculator
    dialog.child_window(title="Four", auto_id="num4Button", control_type="Button").click()

@then(u'Verify the result')
def step_impl(context):
    dialog = Desktop(backend='uia').Calculator
    dialog.child_window(title="Equals", auto_id="equalButton", control_type="Button").click()
    # app1 = application.Application()
    #
    # if app1.Calculator.Static3.Texts() == "7":
    #     print("Test Case Passed")





@then(u'Close application')
def step_impl(context):
    dialog = Desktop(backend='uia').Calculator
    dialog.child_window(title="Close Calculator", auto_id="Close", control_type="Button").click()

