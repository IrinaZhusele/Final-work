import random
from pages.main_page import MainPage
from pages.product_page import ProductPage


# 1 Checking that page title is valid on product page for random product
def test_product_page_header_exists(web_browser):
    page = MainPage(web_browser)
    i = random.randint(0, 19)
    title = page.get_product_title_at(i)
    product_page = page.click_product_at(i)

    assert product_page.get_page_header_text() == title


# 2 Existence of price of product on product page
def test_product_page_has_price(web_browser):
    page = open_random_product(web_browser)
    assert page.has_correct_price()


# 3 Existence of image of product on product page
def test_product_page_has_image(web_browser):
    page = open_random_product(web_browser)
    assert page.has_valid_img()


# 4 Existence of ISBN code of product on product page
def test_product_page_has_isbn(web_browser):
    page = open_random_product(web_browser)
    assert page.has_isbn()


# 5 Pressing buy button is adding product to a shopping cart
def test_product_page_buy(web_browser):
    page = open_random_product(web_browser)
    page.buy_button_click()

    assert page.cart_items_count() == 1

# Opening random product from landing page
def open_random_product(web_browser):
    page = MainPage(web_browser)
    i = random.randint(0, 19)
    return page.click_product_at(i)
