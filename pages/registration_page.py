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


class RegistrationPage(WebPage):
    reg_button = WebElement(xpath='//button[@type="submit"]')
    email = WebElement(xpath='//input[@name="email"]')
    password = WebElement(xpath='//input[@name="password"]')
    lastname = WebElement(xpath='//input[@name="lastname"]')
    validation_errors = ManyWebElements(xpath='//span[@class="help-block"]')

    def __init__(self, web_driver):
        super().__init__(web_driver, TestData.BASE_URL + '/register')

    def click_reg_btn(self):
        self.reg_button.click()

    def enter_email(self, text):
        self.email.send_keys(text)

    def enter_lastname(self, text):
        self.lastname.send_keys(text)

    def enter_password(self, text):
        self.password.send_keys(text)

    def get_validation_errors(self):
        return self.validation_errors.get_text()
