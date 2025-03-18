import time

from playwright.sync_api import Page, expect

def test_UIChecks1(page:Page):

    #MouseHover
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()
    time.sleep(2)

    #Frames: Frames are nothing but child html page embedded in another parent html page
    pageFrame=page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link",name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")
    expect(pageFrame.get_by_text("Happy Subscibers!")).to_be_visible()

    #Check the price of rice is equal to 37 given that the Table is dynamic
    #Identify the position of price column
    #Identify the position of rice row
    #Then extract price of row.

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range(page.locator("//table//thead//tr//th").count()):
        index = index + 1
        if page.locator(f"//table//thead//tr//th[{index}]").text_content() == "Price":
            priceColIndex = index
            break

    for index1 in range(page.locator("//table//tbody//tr").count()):
        index = index + 1
        if page.locator(f"//table//tbody//tr[{index1}]").filter(has_text="Rice").count() > 0:
            riceRowIndex = index1
            break

    price=page.locator(f"//table//tbody//tr[{riceRowIndex}]//td[{priceColIndex}]").text_content()
    assert price == "37"
