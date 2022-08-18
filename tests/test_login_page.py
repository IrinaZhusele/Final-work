import random

from config.config import TestData
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


# 1
def test_login_failed(web_browser):
    page = LoginPage(web_browser)
    page.enter_email("asd@asd.com")
    page.enter_password("123")
    page.click_login()

    assert page.get_error_text() == 'Неверный email и/или пароль'


# 2
def test_login_success(web_browser):
    page = LoginPage(web_browser)
    page.enter_email(TestData.EMAIL)
    page.enter_password(TestData.PASSWORD)
    page.click_login()

    assert 'profile' in page.get_current_url()
