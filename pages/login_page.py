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


class LoginPage(WebPage):
    email = WebElement(xpath='//input[@name="email"]')
    password = WebElement(xpath='//input[@name="password"]')
    login_button = WebElement(xpath='//button[@type="submit"]')
    login_alert = WebElement(xpath='//div[@class="alert alert-warning"]')

    def __init__(self, web_driver):
        super().__init__(web_driver, TestData.BASE_URL + '/login')

    def enter_email(self, text):
        self.email.send_keys(text)

    def enter_password(self, text):
        self.password.send_keys(text)

    def click_login(self):
        self.login_button.click()

    def get_error_text(self):
        return self.login_alert.get_text()
