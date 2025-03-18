import time

from playwright.sync_api import Page, expect , Playwright


def test_playwrightBasics(playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page = context.new_page()
    page.goto("https://www.linkedin.com/feed/")

#chromium headless mode, 1 single context
def test_playwrightShortCut(page:Page):
    page.goto("https://www.linkedin.com/feed/")


def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.locator("//input[@type='password']").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button",name="Sign In").click()
    time.sleep(5)



def test_coreLocatorsWrongCred(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.locator("//input[@type='password']").fill("learning124")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button",name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()


def test_firefoxBrowser(playwright:Playwright):
    browser=playwright.firefox.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.locator("//input[@type='password']").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    time.sleep(5)
