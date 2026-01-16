import pytest

import settings
from data import StellarBurgersTestData
from locators import ConstructorLocators, LoginLocators, ProfilePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructorPage:
    # Успешный вход через кнопкки "Личный кабинет" и "Войти в аккаунт" на главной (конструктор) странице
    @pytest.mark.parametrize('button', [ConstructorLocators.BUTTON_PERSONAL_ACCOUNT,
                                        ConstructorLocators.BUTTON_LOG_IN_ACCOUNT])
    def test_log_in_by_click_on_buttons_in_constructor_page(self, driver, button):
        driver.find_element(*button).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.text_to_be_present_in_element(LoginLocators.LOGIN_TITLE, "Вход"))

        driver.find_element(*LoginLocators.LOGIN_EMAIL_INPUT).send_keys(*StellarBurgersTestData.AUTH_EMAIL)
        driver.find_element(*LoginLocators.LOGIN_PASSWORD_INPUT).send_keys(*StellarBurgersTestData.AUTH_PASSWORD)
        driver.find_element(*LoginLocators.LOGIN_SUBMIT).click()
        driver.find_element(*ConstructorLocators.BUTTON_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.text_to_be_present_in_element(ProfilePage.LINK_PROFILE, "Профиль"))

        assert driver.current_url == settings.URL + settings.ACCOUNT_PROFILE_PAGE

    # Переход в личный кабинет
    def test_go_to_personal_account_page(self, driver, log_in):
        driver.find_element(*ConstructorLocators.BUTTON_PERSONAL_ACCOUNT).click()

        assert driver.current_url == settings.URL + settings.ACCOUNT_PROFILE_PAGE

        # Переход к разделу Булки
    def test_go_to_section_rolls(self, driver):
        rolls_tab = driver.find_element(*ConstructorLocators.NAME_BUTTON_SECTION_ROLLS)
        rolls_tab.click()
    
        assert "tab_tab_type_current__2BEPc" in rolls_tab.get_attribute("class"), "Таб 'Булки' не стал активным"
    
        assert WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.visibility_of_element_located(ConstructorLocators.SECTION_ROLLS)
        ).is_displayed(), "Контент раздела 'Булки' не отображается"

    # Переход к разделу Соусы
    def test_go_to_section_sauces(self, driver):
        sauces_tab = driver.find_element(*ConstructorLocators.NAME_BUTTON_SECTION_SAUCES)
        sauces_tab.click()
    
        assert "tab_tab_type_current__2BEPc" in sauces_tab.get_attribute("class"), "Таб 'Соусы' не стал активным"
    
        assert WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.visibility_of_element_located(ConstructorLocators.SECTION_SAUCES)
        ).is_displayed(), "Контент раздела 'Соусы' не отображается"

    # Переход к разделу Начинки
    def test_go_to_section_fillings(self, driver):
        fillings_tab = driver.find_element(*ConstructorLocators.NAME_BUTTON_SECTION_FILLINGS)
        fillings_tab.click()
    
        assert "tab_tab_type_current__2BEPc" in fillings_tab.get_attribute("class"), "Таб 'Начинки' не стал активным"
    
        assert WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            EC.visibility_of_element_located(ConstructorLocators.SECTION_FILLINGS)
        ).is_displayed(), "Контент раздела 'Начинки' не отображается"
