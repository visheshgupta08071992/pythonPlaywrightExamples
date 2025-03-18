from playwright.sync_api import Page, expect , Playwright

from utils.apiBase import APIUtils


def test_e2e(playwright:Playwright):

    #create order through API and get orderId
    apiUtils=APIUtils()
    orderId=apiUtils.createOrder(playwright)

    #login
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    # rahulshetty@gmail.com
    # Iamking@000
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.locator("#userPassword").fill("Iamking@000")
    page.locator("#login").click()
    page.get_by_role("button",name="ORDERS").click()
    row=page.locator("tr").filter(has_text=orderId)


    #orders page -> order is present
