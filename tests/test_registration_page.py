import random
from pages.main_page import MainPage
from pages.product_page import ProductPage


from pages.registration_page import RegistrationPage


# 1 Negative test to check required fields validation
def test_registration_page_empty_fields_validation_errors(web_browser):
    page = RegistrationPage(web_browser)
    page.click_reg_btn()

    errors = page.get_validation_errors()

    assert 'Поле firstname обязательно для заполнения.' in errors
    assert 'Поле lastname обязательно для заполнения.' in errors
    assert 'Поле phone обязательно для заполнения.' in errors
    assert 'Поле email обязательно для заполнения.' in errors
    assert 'Поле password обязательно для заполнения.' in errors
    assert 'Поле password confirmation обязательно для заполнения.' in errors


# 2 Negative test to check validation message of invalid password
def test_registration_page_password_validation_errors(web_browser):
    page = RegistrationPage(web_browser)
    page.enter_password('123')
    page.click_reg_btn()

    errors = page.get_validation_errors()

    assert 'The password must be between 10 - 20 characters.' in errors


# 3 Negative test to check validation message of lastname field
def test_registration_page_password_last_name_error(web_browser):
    page = RegistrationPage(web_browser)
    page.enter_lastname('Z')
    page.click_reg_btn()

    errors = page.get_validation_errors()

    assert 'The lastname must be at least 2 characters.' in errors
