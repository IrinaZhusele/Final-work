import random

from pages.forgot_page import ForgotPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


# 1 Negative test to check if message that user is not found displayed when invalid data is entered (email)
def test_forgot_wrong_email(web_browser):
    page = ForgotPage(web_browser)
    page.enter_email('asd@asd.com')
    page.click_button()

    assert page.get_error_text() == 'Пользователь не найден'


# 2 Positive test on entering with valid email when user forgot his data
def test_forgot_correct_email(web_browser):
    page = ForgotPage(web_browser)
    page.enter_email('izhusele@gmail.com')
    page.click_button()

    assert page.get_error_text() == 'Новый пароль отправлен на указанный еmail адрес'


# 3 Checking the back button on the forgot page exists
def test_forgot_correct_back_button(web_browser):
    page = ForgotPage(web_browser)

    assert page.back_button_valid()
