from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import PROFILE_CABINET

class TestStellarBurgers:
    def test_login(self, driver, logged_user):
        WebDriverWait(driver, 17).until(EC.presence_of_element_located((Locators.PERSONAL_ACCOUNT)))
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 17).until(EC.presence_of_element_located((Locators.LOGOUT_BUTTON)))
        assert PROFILE_CABINET == driver.current_url