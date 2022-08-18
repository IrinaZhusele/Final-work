import random
import time
import urllib.request

from config.config import TestData
from pages.contact_page import ContactPage
from pages.main_page import MainPage


# 1
def test_contact_page_header(web_browser):
    page = ContactPage(web_browser)

    assert page.get_page_header_text() == 'О нас'


# 2
def test_contact_page_header(web_browser):
    page = ContactPage(web_browser)

    assert 'Сеть магазинов Mnogoknig' in page.get_page_content_text()
    assert 'Интернет-магазин Mnogoknig' in page.get_page_content_text()


# 3
def test_contact_page_images(web_browser):
    page = ContactPage(web_browser)
    images = page.get_page_images_src()
    assert len([x for x in images if x.startswith('data:image/png;base64,')]) == len(images)
