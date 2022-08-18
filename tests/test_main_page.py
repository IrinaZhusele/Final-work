import random
import time
import urllib.request

from config.config import TestData
from pages.main_page import MainPage


# 1 Open landing page and that it's loaded in 3 sec.
def test_landing_page_open_success(web_browser):
    page = MainPage(web_browser)

    page.wait_page_loaded(3)


# 2 Checking that landing page title is valid
def test_landing_page_title_correct(web_browser):
    page = MainPage(web_browser)
    title = page.get_current_title()
    assert title == 'МНОГОКНИГ.lv - Книжный интернет-магазин'


# 3 Contacts info existence on landing page
def test_landing_page_contacts_exists(web_browser):
    page = MainPage(web_browser)
    is_visible = page.is_contact_lang_info_visible()
    assert is_visible


# 4 Existence of 2 languages on landing page
def test_landing_page_languages_count_2(web_browser):
    page = MainPage(web_browser)
    result = page.languages_count()
    assert result == 2


# 5 Existence languages links LV/RU
def test_landing_page_languages_visible(web_browser):
    page = MainPage(web_browser)
    result = page.is_language_with_path_visible('lv')
    assert result
    result = page.is_language_with_path_visible('ru')
    assert result


# 6 Existence of 3 links(of profile, preorder and cart) quantity
def test_landing_page_links_count_equal_3(web_browser):
    page = MainPage(web_browser)
    result = page.links_count()
    assert result == 3


# 7 Existence of links of profile, preorder and cart
def test_landing_page_links_visible(web_browser):
    page = MainPage(web_browser)
    result = page.is_link_with_path_visible('profile')
    assert result
    result = page.is_link_with_path_visible('preorder')
    assert result
    result = page.is_link_with_path_visible('cart')
    assert result


# 8 Title change depending on selected language
def test_landing_page_language_change(web_browser):
    page = MainPage(web_browser)
    page.click_lang('lv')
    assert page.get_current_title() == 'MNOGOKNIG.lv - Grāmatu interneta veikals'
    page.click_lang('ru')
    assert page.get_current_title() == 'МНОГОКНИГ.lv - Книжный интернет-магазин'


# 9 Existence of 7 menu urls
def test_landing_page_menu_count(web_browser):
    page = MainPage(web_browser)
    count = page.get_menu_count()
    assert count == 7


# 10 Existence of menu urls and their sequence
def test_landing_page_menu_visible(web_browser):
    page = MainPage(web_browser)
    result = page.is_menu_with_path_visible('o-nas', 1)
    assert result
    result = page.is_menu_with_path_visible('dostavka-i-oplata', 2)
    assert result
    result = page.is_menu_with_path_visible('magazini', 3)
    assert result
    result = page.is_menu_with_path_visible('optovikam', 4)
    assert result
    result = page.is_menu_with_path_visible('voprosi', 5)
    assert result
    result = page.is_menu_with_path_visible('info', 6)
    assert result
    result = page.is_menu_with_path_visible('kontakti', 7)
    assert result


# 11 Existence of search on landing page
def test_landing_page_search_exists(web_browser):
    page = MainPage(web_browser)
    is_visible = page.is_search_visible()
    assert is_visible


# 12 Counting and existence of 20 displayed product cards on landing page
def test_landing_page_products_count(web_browser):
    page = MainPage(web_browser)
    count = page.get_products_count()
    assert count == 20


# 13 Displaying the 20 titles of product cards on landing page
def test_landing_page_product_cards_titles(web_browser):
    page = MainPage(web_browser)
    titles = page.get_product_titles().get_text()

    assert len(titles) == 20
    assert len([x for x in titles if x]) == len(titles)


# 14 Existence of 20 images of product cards on landing page
def test_landing_page_product_cards_images(web_browser):
    page = MainPage(web_browser)
    images = page.get_product_images().get_attribute('src')

    assert len(images) == 20
    assert len([x for x in images if x]) == len(images)


# 15 Displaying the 20 prices of product cards on landing page
def test_landing_page_product_cards_prices(web_browser):
    page = MainPage(web_browser)
    prices = page.get_product_prices_elements().get_text()

    assert len(prices) == 20
    assert len([x for x in prices if x.startswith('€') and float(x.replace('€', '')) > 0]) == len(prices)


# 16 Changing page
def test_landing_page_change_page(web_browser):
    page_number = 3
    page = MainPage(web_browser)
    page1_titles = page.get_product_titles().get_text()
    page.change_page(page_number)
    url = page.get_current_url()
    page3_titles = page.get_product_titles().get_text()
    assert set(page1_titles).issubset(set(page3_titles)) is False
    assert 'page={number}'.format(number=page_number) in url


# 17 Existence of categories, opening of all submenu
def test_landing_page_categories(web_browser):
    page = MainPage(web_browser)
    # print(main_page_categories.get_categories_links_text())
    categories_links = page.get_categories_links()

    # open all sub categories
    elements = categories_links.find()
    for element in elements:
        element.click()

    categories_texts = categories_links.get_text()
    expected_categories = TestData.CATEGORIES_RU
    assert expected_categories == ','.join(categories_texts)


# 18 Opening each subcategories on landing page
def test_landing_page_sub_categories(web_browser):
    page = MainPage(web_browser)
    sub_categories_names = page.get_default_subcategories_links().get_text()

    for name in sub_categories_names:
        element = page.get_sub_category_element(name)
        element.click()


# 19 Existence of information of footer on landing page
def test_landing_page_logo_footer_info_exists(web_browser):
    page = MainPage(web_browser)
    is_visible = page.is_logo_footer_info_visible()
    assert is_visible


# 20 Existence of 3 links of footer information on landing page
def test_landing_page_footer_info_count_equal_3(web_browser):
    page = MainPage(web_browser)
    result = page.footer_info_count()
    assert result == 3


# 21 Existence of links of information in footer, delivery and payment, terms of use, privacy policy
def test_landing_page_footer_info_visible(web_browser):
    page = MainPage(web_browser)
    result = page.is_footer_info_with_path_visible('dostavka-i-oplata')
    assert result
    result = page.is_footer_info_with_path_visible('uslovija-ispoljzovanija-lv')
    assert result
    result = page.is_footer_info_with_path_visible('politika-konfidencialjnosti')
    assert result


# 22 Existence of 3 social icons on landing page in footer
def test_landing_page_social_icons_count_equal_3(web_browser):
    page = MainPage(web_browser)
    result = page.social_icons_count()
    assert result == 3


# 23 Existence of social icons with correct urls on landing page in footer
def test_landing_page_social_icons_visible(web_browser):
    page = MainPage(web_browser)
    result = page.is_social_icon_with_path_visible('facebook')
    assert result
    result = page.is_social_icon_with_path_visible('instagram')
    assert result
    result = page.is_social_icon_with_path_visible('whatsapp')
    assert result


# 24 Existence of valid facebook url on landing page in footer
def test_landing_page_facebook_url(web_browser):
    page = MainPage(web_browser)
    assert page.get_facebook_url() == TestData.FACEBOOK_URL


# 25 Existence of valid instagram url on landing page in footer
def test_landing_page_instagram_url(web_browser):
    page = MainPage(web_browser)
    assert page.get_instagram_url() == TestData.INSTAGRAM_URL


# 26 Existence of valid whatsup url on landing page in footer
def test_landing_page_whatsup_url(web_browser):
    page = MainPage(web_browser)
    assert page.get_whatsup_url() == TestData.WHATSUP_URL
