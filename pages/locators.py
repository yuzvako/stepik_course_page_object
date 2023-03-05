from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH, '/html/body/header/div[1]/div/div[2]/span/a')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FIELD = (By.ID, 'id_registration-email')
    PASSWORD_FIELD = (By.ID, 'id_registration-password1')
    PASSWORD_FIELD_SUBMIT = (By.ID, 'id_registration-password2')
    SUBMIT_BUTTON = (By.NAME, 'registration_submit')
    OK_SIGN = (By.CLASS_NAME, 'icon-ok-sign')

class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/h1')
    PRICE_BOOK = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]')
    MESSAGE_NAME_BOOK = (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/strong')
    BASKET_PRICE = (By.XPATH, '/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alertinner')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_LINK = (By.XPATH, '/html/body/header/div[1]/div/div[2]/span/a')
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')
    NOT_EMPTY_BASKET = (By.CLASS_NAME, 'col-sm-6 h3')
