from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/h1')
    PRICE_BOOK = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]')
    MESSAGE_NAME_BOOK = (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/strong')
    BASKET_PRICE = (By.XPATH, '/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong')