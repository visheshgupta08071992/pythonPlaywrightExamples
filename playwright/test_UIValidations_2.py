import time

from playwright.sync_api import Page, expect


def test_UIChecks(page:Page):
    #hide/display and placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #Alert boxes
    page.on("dialog",lambda dialog:dialog.accept())
    page.get_by_role("button",name="Confirm").click()
    time.sleep(5)


# The following code listens for any dialog (alert, confirmation, or prompt) that appears on the page.
# It then automatically accepts the dialog.

# page.on("dialog", lambda dialog: dialog.accept())

# Breakdown of the code:

# 1. `page.on("dialog", ...)`
#    - This sets up an event listener on the `page` object.
#    - The `"dialog"` event is triggered whenever an alert, confirmation, or prompt dialog appears.
#    - The second argument is a function (callback) that handles the dialog when it appears.

# 2. `lambda dialog: dialog.accept()`
#    - This is an **anonymous function (lambda function)** in Python.
#    - `dialog` is the parameter representing the dialog box object.
#    - `dialog.accept()` is a method that **automatically clicks "OK" or "Accept"** on the dialog.

# Equivalent Expanded Code:
# Instead of using a lambda function, we can use a normal function:

# def handle_dialog(dialog):
#     dialog.accept()
#
# page.on("dialog", handle_dialog)

# Key Takeaways:
# - The `lambda` function is a compact way to define a function inline.
# - `dialog.accept()` ensures that any alert or confirmation dialog is automatically accepted.
# - If you wanted to **dismiss** the dialog instead of accepting it, you could do:
#
#   page.on("dialog", lambda dialog: dialog.dismiss())
