from config.config import TestData
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
from pages.product_page import ProductPage


class ShoppingCartPage(WebPage):
    cart_rows = ManyWebElements(xpath='//table[@class="cartproducts"]//tr[not(th)]')
    total_cell = WebElement(xpath='//table[@class="cartproducts"]//tr[last()]//td[last()-1]')
    count_cell = WebElement(xpath='//table[@class="cartproducts"]//tr[last()]//td[last()-2]')
    remove_button = WebElement(xpath='//table[@class="cartproducts"]//tr[last()-1]//td[last()]/a')
    clear_button = WebElement(xpath='//a[contains(@href,"empty")]')
    coupon_input = WebElement(id='coupon')
    coupon_apply = WebElement(xpath='//form//button[@type="submit"]')
    coupon_error = WebElement(xpath='//div[contains(@class,"alert")]')
    order_button = WebElement(xpath='//a[contains(@href,"/order")]')
    empty_label = WebElement(xpath='//content/div[@class="container"]/div/div[last()]/div[last()]')
    product_link = WebElement(xpath='//table[@class="cartproducts"]//tr[last()-1]//td//a')

    def __init__(self, web_driver):
        super().__init__(web_driver, TestData.BASE_URL + '/cart')

    def get_cart_rows(self):
        return self.cart_rows.count() - 1  # because last total (-1)

    def get_total(self):
        total = self.total_cell.get_text()
        return float(total.replace('€', ''))

    def get_count(self):
        if not self.count_cell.is_presented():
            return 0

        count_str = self.count_cell.get_text()
        return int(count_str)

    def remove_item(self):
        self.remove_button.click()

    def clear(self):
        self.clear_button.click()

    def apply_coupon_code(self, text):
        self.coupon_input.send_keys(text)
        self.coupon_apply.click()

    def coupon_error_shown(self):
        return self.coupon_error.is_visible()

    def can_make_order(self):
        return self.order_button.is_visible() and self.order_button.is_clickable()

    def get_empty_label_text(self):
        return self.empty_label.get_text()

    def click_product(self):
        self.product_link.click()
        return ProductPage(web_driver=self._web_driver)
