from enum import Enum
from typing import List

from py_selenium_auto.elements.button import Button
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import time


class TypeOfTesting(Enum):
    Functional = "/functional_testing/"
    Automation = "/services/testing_automation/"
    Mobile = "/services/mobile_application_testing/"

class Page2(Form):

    PASSWD_FLD = (By.XPATH, '//*[contains(@placeholder, "Choose")]')
    YOUR_EMAIL_FLD = (By.XPATH, '//*[contains(@placeholder, "Your email")]')
    DOMAIN_FLD = (By.XPATH, '//*[contains(@placeholder, "Domain")')
    DROPDWN_FLD = (By.XPATH, '//*[contains(@class, "dropdown__field")]')
    DROPDOWN_VALUE = (By.LINK_TEXT, '.com') # (By.XPATH, '//div[contains(@class, "dropdown__list-item")][9]')
    CHECK_BOX = (By.XPATH, '//input[contains(@type, "checkbox")]')
    NEXT_BTN = (By.LINK_TEXT, 'Next')

    # описал кнопки. теперь привязать их именно к странице 2: через конструктор класса Page2


    # 2 варианта локатора на поле ввода пароля:
    PASSWORD_FIELD = (By.XPATH, "//input[contains(@class, \"input input--blue input--gray\") and contains(@placeholder, \"Choose\")]")
        # внутри комбинированного локатора сделал экранирование с помощью "\"
        # потом плэйсхолжер буду удалять - возможно не найдет потом этот элемент,
        # пэтому +1 вариация локатора этого же элемента:

    PASSWORD_FIELD_2 = (By.XPATH, "//div[starts-with(@class, \"login-form__field-row\")]/following::input[contains(@class, \"input input--blue input--gray\")][1]")
        # с помощью /following::
        # в первой части локатора поиск по названию класса, начинающегося с "..."
        # если сделать просто contains - то выдаст 2 результата
        # потом с помощью /following::input[contains(@class, "...")]
        # опускаюсь до тэга input, который содержит название класса "..."

    def __init__(self):
        #super().__init__(Locator(By.CLASS_NAME, "main-intro__wrapper"), "Main form") -что делает строка?
        self.__passwd_fld = Button(*self.PASSWD_FLD) #создаю переменную класса, которая есть объект класса Button, правильно понимаю?
        self.__your_email_fld = Button(*self.YOUR_EMAIL_FLD)
        self.__domain_fld = Button(*self.DOMAIN_FLD)
        self.__dropdwn_fld = Button(*self.DROPDWN_FLD)
        self.__dropdwn_value = Button(*self.DROPDOWN_VALUE)
        self.__check_box = Button(*self.CHECK_BOX)
        self.__next_btn = Button(*self.NEXT_BTN)

    #проинициализировал атрибуты класса
    # теперь создать методы

    def fill_passwd_fld(self):
        self.__passwd_fld.click()
        #self.__passwd_fld.clear() #не определен метод clear в родительском классе Element
        while len(self.__passwd_fld.get_attribute("Choose Password")) > 0: #удаляю введенное значение вручную
            self.__passwd_fld.send_keys(Keys.BACK_SPACE)
            time.sleep(0.1)
        self.__passwd_fld.send_keys("QwertyP1234")

    def fill_email(self):
        self.__your_email_fld.click()
        while len(self.__passwd_fld.get_attribute("Your email")) > 0: #удаляю введенное значение вручную
            self.__passwd_fld.send_keys(Keys.BACK_SPACE)
            time.sleep(0.1)
        self.__passwd_fld.send_keys("testmail1")

# добавить декоратор для очищения поля, на которое кликнул

    def fill_domain(self):
        self.__domain_fld.click()
        while len(self.__domain_fld.get_attribute("Domain")) > 0: #удаляю введенное значение вручную
            self.__domain_fld.send_keys(Keys.BACK_SPACE)
            time.sleep(0.1)
        self.__domain_fld.send_keys("mail")

    def choose_root_domain(self):
        self.__dropdwn_fld.click()
        time.sleep(0.1)
        self.__dropdwn_value.click()

    def click_check_box(self):
        self.__check_box.click()

    def click_next(self):
        self.__next_btn.click()