import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage
from pages.shopping_cart_page import ShoppingCartPage


# 1
def test_shopping_cart_items_added(web_browser):
    page = MainPage(web_browser)
    buttons = page.get_product_buy_btns()
    indexes = random.sample(range(0, 19), 2)
    buttons[indexes[0]].click()
    buttons[indexes[1]].click()

    shopping_cart_page = page.click_shopping_cart()

    assert shopping_cart_page.get_cart_rows() == 2


# 2
def test_shopping_cart_total(web_browser):
    page = MainPage(web_browser)
    items = random.sample(range(20), random.randint(1, 5))
    total = 0
    for i in items:
        page.click_buy_button_at(i)
        price = page.get_product_price_at(i)
        total += price

    shopping_cart_page = page.click_shopping_cart()

    assert shopping_cart_page.get_total() == round(total, 2)


# 3
def test_shopping_cart_count(web_browser):
    page = MainPage(web_browser)
    items = random.sample(range(20), random.randint(1, 5))
    count = 0
    for i in items:
        page.click_buy_button_at(i)
        count += 1

    shopping_cart_page = page.click_shopping_cart()

    assert shopping_cart_page.get_count() == count


# 4
def test_shopping_cart_added_removed(web_browser):
    page = MainPage(web_browser)
    items = random.sample(range(20), random.randint(1, 5))
    count = 0
    for i in items:
        page.click_buy_button_at(i)
        count += 1

    shopping_cart_page = page.click_shopping_cart()

    for i in items:
        shopping_cart_page.remove_item()

    assert shopping_cart_page.get_count() == 0


# 5
def test_shopping_cart_clear_all(web_browser):
    page = MainPage(web_browser)
    page.click_buy_button_at(0)

    shopping_cart_page = page.click_shopping_cart()
    shopping_cart_page.clear()

    assert shopping_cart_page.get_count() == 0


# 6
def test_shopping_cart_coupon_negative(web_browser):
    page = MainPage(web_browser)
    page.click_buy_button_at(0)

    shopping_cart_page = page.click_shopping_cart()

    assert shopping_cart_page.coupon_error_shown() is False

    shopping_cart_page.apply_coupon_code('123')

    assert shopping_cart_page.coupon_error_shown()


# 7
def test_shopping_cart_make_order(web_browser):
    page = MainPage(web_browser)
    page.click_buy_button_at(0)

    shopping_cart_page = page.click_shopping_cart()

    assert shopping_cart_page.can_make_order()


# 8
def test_shopping_cart_empty(web_browser):
    page = ShoppingCartPage(web_browser)

    assert page.get_empty_label_text() == 'Ваша корзина пуста'


# 9
def test_shopping_cart_item_link_product(web_browser):
    page = MainPage(web_browser)
    page.click_buy_button_at(0)

    shopping_cart_page = page.click_shopping_cart()
    product_page = shopping_cart_page.click_product()

    assert 'products' in product_page.get_current_url()
