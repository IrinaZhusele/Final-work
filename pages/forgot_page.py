#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os, pickle
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import TestData
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
from typing import List

from pages.shopping_cart_page import ShoppingCartPage


class ForgotPage(WebPage):
    email = WebElement(xpath='//input[@name="email"]')
    button = WebElement(xpath='//button[@type="submit"]')
    back_button = WebElement(xpath='//a[contains(@href,"login")]')
    login_alert = WebElement(xpath='//div[@class="alert alert-warning"]')

    def __init__(self, web_driver):
        super().__init__(web_driver, TestData.BASE_URL + '/forgot')

    def enter_email(self, text):
        self.email.send_keys(text)

    def click_button(self):
        self.button.click()

    def get_error_text(self):
        return self.login_alert.get_text()

    def back_button_valid(self):
        return self.back_button.is_visible() and self.back_button.is_clickable()
