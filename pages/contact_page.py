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


class ContactPage(WebPage):
    header = WebElement(xpath='//h1')
    content_paragraphs = ManyWebElements(xpath='//content//p')
    images = ManyWebElements(xpath='//content//img')

    def __init__(self, web_driver):
        super().__init__(web_driver, TestData.BASE_URL + '/o-nas')

    def get_page_header_text(self):
        return self.header.get_text()

    def get_page_content_text(self):
        return self.content_paragraphs.get_text()

    def get_page_images_src(self):
        return self.images.get_attribute('src')
