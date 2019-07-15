from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class  LoginPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTER_LINK = (By.CSS_SELECTOR, "#registration_link")
