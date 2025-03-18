
from playwright.sync_api import Page, expect


def test_UIValidationDynamicScript(page:Page):
    # Select iphone X and Nokia Edge and check two items are added within cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.locator("//input[@type='password']").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphone =page.locator("app-card").filter(has_text="iphone X")
    iphone.get_by_role("button").click()
    nokia = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator("//div[@class='media']")).to_have_count(2)
    expect(page.locator("//a[text()='iphone X']")).to_be_visible()
    expect(page.locator("//a[text()='Nokia Edge']")).to_be_visible()


def test_childWindowHandle(page:Page):

    with page.expect_popup() as newPage:
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        page.locator(".blinkingText").click()
        childPage = newPage.value
        text=childPage.locator(".red").text_content()
        print(text)
        assert "mentor@rahulshettyacademy.com"  in text
        words = text.split("at")
        email = words[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"
