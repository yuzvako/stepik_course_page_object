from selenium.webdriver.common.by import By
import time

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)