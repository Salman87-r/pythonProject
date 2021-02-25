from behave import *
from pywinauto import application, Desktop

app = application.Application()
dlg = Desktop(backend='uia').Calculator
@when(u'Launch the application')
def step_impl(context):
   app.Start(cmd_line=u"calc.exe")
@when(u'Click Scientic')
def step_impl(context):
    dlg.child_window(title="Open Navigation", auto_id="TogglePaneButton", control_type="Button").click()
    item = dlg.child_window(title="Scientific Calculator", auto_id="Scientific", control_type="ListItem")
    item.click_input(coords=(0, 0))
@given(u'Click Number you want square')
def step_impl(context):
    dlg.child_window(title="Seven", auto_id="num7Button", control_type="Button").click()

@given(u'Click square button')
def step_impl(context):
    dlg.child_window(title="Square", auto_id="xpower2Button", control_type="Button").click()

@then(u'Verify the  result')
def step_impl(context):

    pass

@when(u'Enter first number')
def step_impl(context):
    dlg.child_window(title="Nine", auto_id="num9Button", control_type="Button").click()


@when(u'ENter mode button')
def step_impl(context):
    dlg.child_window(title="Modulo", auto_id="modButton", control_type="Button").click()
@then(u'Enter second number')
def step_impl(context):
    dlg.child_window(title="Four", auto_id="num4Button", control_type="Button").click()
    dlg.child_window(title="Equals", auto_id="equalButton", control_type="Button").click()

@then(u'Close the application')
def step_impl(context):
    # item = dlg.child_window(ttitle="Standard Calculator", auto_id="Standard", control_type="ListItem")
    # item.click_input(coords=(0, 0))
    dlg.child_window(title="Close Calculator", auto_id="Close", control_type="Button").click()