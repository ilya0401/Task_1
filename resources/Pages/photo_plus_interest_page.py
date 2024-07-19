from enum import Enum
from random import random
from typing import List
from py_selenium_auto.elements.button import Button
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from py_selenium_auto_core.elements.element_factory import ElementFactory
from resources.Pages.creds_generator import Creds_Generator



class Interest_page(Form):

    def __init__(self):
        super().__init__(Locator(By.XPATH, '//*[contains(@class, "login-form__container")][1]'), 'Login form')
        self.checkboxes = self._element_factory.find_elements(self, list, Locator('//*[contains(@class, "checkbox__box")]'), 21)
        self.unselect_all_BTN = self._element_factory.get_check_box(Locator(By.XPATH, '//span[contains(text(), "Unselect all")]/preceding::*[contains(@class, "checkbox small")][1]'), 'Unselect_all_BTN')


    def  select_checkboxes(self):
        res = self.checkboxes[::-1]
        for checkbox in random.shuffle(res):
            checkbox.click()







