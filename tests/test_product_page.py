import random
from pages.main_page import MainPage
from pages.product_page import ProductPage


# 1
def test_product_page_header_exists(web_browser):
    page = MainPage(web_browser)
    i = random.randint(0, 19)
    title = page.get_product_title_at(i)
    product_page = page.click_product_at(i)

    assert product_page.get_page_header_text() == title


# 2
def test_product_page_has_price(web_browser):
    page = open_random_product(web_browser)
    assert page.has_correct_price()


# 3
def test_product_page_has_image(web_browser):
    page = open_random_product(web_browser)
    assert page.has_valid_img()


# 4
def test_product_page_has_isbn(web_browser):
    page = open_random_product(web_browser)
    assert page.has_isbn()


# 4
def test_product_page_buy(web_browser):
    page = open_random_product(web_browser)
    page.buy_button_click()

    assert page.cart_items_count() == 1


def open_random_product(web_browser):
    page = MainPage(web_browser)
    i = random.randint(0, 19)
    return page.click_product_at(i)
