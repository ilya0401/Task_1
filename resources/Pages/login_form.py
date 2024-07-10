from enum import Enum
from typing import List

from py_selenium_auto.elements.button import Button
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from py_selenium_auto_core.elements.element_factory import ElementFactory

import time


class ROOT_DOMAIN(Enum):
    OTHER = "other"
    ORG = ".org"
    CO_UK = ".co.uk"
    NET = ".net"
    GOV = ".gov"
    DE = ".de"
    FR = ".fr"
    NL = ".nl"
    COM = ".com" # (By.LINK_TEXT, '.com')
    BE = ".be"
    #JPG = ".jpg"


class Login_Form(Form):

    PASSWD_FLD = (By.XPATH, '//*[contains(@placeholder, "Choose")]')
    YOUR_EMAIL_FLD = (By.XPATH, '//*[contains(@placeholder, "Your email")]')
    DOMAIN_FLD = (By.XPATH, '//*[contains(@placeholder,  "Domain")]')
    DROPDWN_FLD = (By.XPATH, '//*[contains(@class, "dropdown__field")]')
    DROPDOWN_VALUE = (By.LINK_TEXT, ROOT_DOMAIN.COM.value) # (By.XPATH, '//div[contains(@class, "dropdown__list-item")][9]')
    CHECK_BOX = (By.XPATH, '//input[contains(@type, "checkbox")]')
    NEXT_BTN = (By.LINK_TEXT, 'Next')


    def __init__(self):
        super().__init__(Locator(By.XPATH, '//*[contains(@class, "login-form__container")][1]'), 'Login form') # - что делает строка? - проверяет что страница загрузилась
        # для создания элемента пользую .._element_factory.get_(Locator, name) - при создании элемента передаю локатор и задаю имя элемента
        # при этом при создании элемента, по дефолту передается элемент state со значением по дефолту (state: ElementState = ElementState.Displayed)
        self.__passwd_fld = self._element_factory.get_text_box(Locator(*self.PASSWD_FLD), 'Password') # name можно не писать тут? так как оно содержится в распаковываемом *self.PASSWD_FLD?
        self.__your_email_fld = self._element_factory.get_text_box(Locator(*self.YOUR_EMAIL_FLD), 'Your email')
        self.__domain_fld = self._element_factory.get_text_box(Locator(By.XPATH, '//*[contains(@placeholder,  "Domain")]'), 'Domain field')
        self.__dropdwn_fld = self._element_factory.get_button(Locator(*self.DROPDWN_FLD), 'Dropdown with root domain options')
        self.__dropdwn_value = self._element_factory.get_button(Locator(*self.DROPDOWN_VALUE), 'Root domain value')
        self.__check_box = self._element_factory.get_check_box(Locator(*self.CHECK_BOX), 'Check box')
        self.__next_btn = self._element_factory.get_button(Locator(*self.NEXT_BTN), 'Next button')

    #проинициализировал атрибуты класса
    # теперь создать методы

    def fill_passwd_fld(self):
        self.__passwd_fld.click()
        self.__passwd_fld.clear()
        self.__passwd_fld.send_keys("QwertyP1234") # убрать хардкод

    def fill_email(self):
        self.__your_email_fld.click()
        self.__your_email_fld.clear()
        self.__passwd_fld.send_keys("testmail1")

# добавить декоратор

    def fill_domain(self):
        self.__domain_fld.click()
        self.__domain_fld.clear()
        self.__domain_fld.send_keys("mail")

    def choose_root_domain(self):
        self.__dropdwn_fld.click()
        self.__dropdwn_value.click()

        # проставить про выбор значения через Enum

    def click_check_box(self):
        self.__check_box.click()

    def click_next(self):
        self.__next_btn.click()