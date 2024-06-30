from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestStellarBurgers:
    def test_login_personal_account_button(self, driver):
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(Locators.LOGIN_IN_ACCOUNT))
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys('elizavetavinogradova10562@yandex.ru')
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT))
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert WebDriverWait(driver, 17).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))

    def test_login_in_account_button(self, driver):
        WebDriverWait(driver, 7).until(EC.presence_of_element_located(Locators.LOGIN_IN_ACCOUNT))
        driver.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        WebDriverWait(driver, 7).until(EC.presence_of_element_located(Locators.LOGIN_EMAIL_INPUT))
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys('elizavetavinogradova10562@yandex.ru')
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT))
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert WebDriverWait(driver, 17).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))

    def test_login_button_on_registration_page(self, driver):
        WebDriverWait(driver, 7).until(EC.presence_of_element_located(Locators.LOGIN_IN_ACCOUNT))
        driver.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        WebDriverWait(driver, 7).until(EC.presence_of_element_located(Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE))
        driver.find_element(*Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE).click()
        WebDriverWait(driver, 7).until(EC.presence_of_element_located(Locators.LOGIN_BUTTON_ON_PAGES))
        driver.find_element(*Locators.LOGIN_BUTTON_ON_PAGES).click()
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys('elizavetavinogradova10562@yandex.ru')
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT))
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert WebDriverWait(driver, 17).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))

    def test_login_restore_password_page(self, driver):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_IN_ACCOUNT))
        driver.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.RESTORE_PASSWORD_BUTTON))
        driver.find_element(*Locators.RESTORE_PASSWORD_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_ON_PAGES))
        driver.find_element(*Locators.LOGIN_BUTTON_ON_PAGES).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL_INPUT))
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys('elizavetavinogradova10562@yandex.ru')
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT))
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))