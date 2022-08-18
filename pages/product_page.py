import os, pickle
import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import TestData
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class ProductPage(WebPage):
    header = WebElement(xpath='//h1')
    price = WebElement(xpath='//div[@class="productprice"]')
    isbn = WebElement(xpath='//span[@itemprop="isbn"]')
    image = WebElement(xpath='//img[@id="product_mainimage"]')
    buy_button = WebElement(xpath='//a[@id="buy"]')
    card_items_count = WebElement(xpath='//span[@class="count"]')

    def __init__(self, web_driver):
        super().__init__(web_driver, '')

    def get_page_header_text(self):
        return self.header.get_text()

    def has_correct_price(self):
        price = self.price.get_text()
        return price.startswith("€") and float(price.replace('€', '')) > 0

    def buy_button_click(self):
        self.buy_button.click()
        time.sleep(3)

    def cart_items_count(self):
        return int(self.card_items_count.get_text())

    def has_isbn(self):
        return self.isbn.get_text() != ''

    def has_valid_img(self):
        url = self.image.get_attribute("src")
        alt = self.image.get_attribute("alt")
        image_extensions = ('.jpg', '.png', '.jpeg')
        return url.startswith(TestData.IMG_BASE_URL) and url.endswith(image_extensions) and alt != ''
