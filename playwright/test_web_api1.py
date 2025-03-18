from playwright.sync_api import Page, expect , Playwright

from utils.apiBase import APIUtils

fakePayloadResponse= {"message":"No Product in Cart"}


def test_net(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept)
    # rahulshetty@gmail.com
    # Iamking@000
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.locator("#userPassword").fill("Iamking@000")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    noOrderText=page.locator(".mt-4").text_content()
    print(noOrderText)
    expect(page.locator(".mt-4")).to_have_text("You have No Orders to show at this time. Please Visit Back Us")

def intercept(route):
    route.fulfill(
        json=fakePayloadResponse
    )



