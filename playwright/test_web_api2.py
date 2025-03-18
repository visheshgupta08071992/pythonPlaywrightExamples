import time

from playwright.sync_api import Page, expect , Playwright

from utils.apiBase import APIUtils

#https://rahulshettyacademy.com/client/dashboard/order-details/67d51e0ac019fb1ad62737ed

def intercept(route):
    route.continue_(url="https://rahulshettyacademy.com/client/dashboard/order-details/67d51e0ac019fb1ad62737ed")

def test_net2(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept)
    # rahulshetty@gmail.com
    # Iamking@000
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.locator("#userPassword").fill("Iamking@000")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button",name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)


def test_session(playwright:Playwright):
    api_utils=APIUtils()
    token = api_utils.createToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token','{token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()




