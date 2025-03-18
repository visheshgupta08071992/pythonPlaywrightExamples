from playwright.sync_api import Playwright

loginData = {"userEmail":"rahulshetty@gmail.com","userPassword":"Iamking@000"}

ordersPayload={"orders":[{"country":"India","productOrderedId":"67a8dde5c0d3e6622a297cc8"}]}


class APIUtils:

    def createToken(self, playwright: Playwright):
        apiLoginContext=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        loginResponse=apiLoginContext.post("/api/ecom/auth/login",
                             data=loginData)
        loginResponse.ok
        loginResponseBody=loginResponse.json()
        token = loginResponseBody["token"]
        return token



    def createOrder(self,playwright:Playwright):
        token=self.createToken(playwright)
        apiContext=playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response=apiContext.post("/api/ecom/order/create-order",
                        data=ordersPayload,
                        headers={
                            "Authorization":token,
                            "content-length":"application/json"
                        })
        responseBody=response.json()
        orderList=responseBody["orders"]
        orderId=orderList[0]
        print(orderId)
        return orderId
