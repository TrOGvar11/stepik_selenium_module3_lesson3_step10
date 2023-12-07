import time

from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_should_be_on_page(browser):
    browser.get(link)
    # time.sleep(8)
    button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(button) > 0, "Button NOT found"

