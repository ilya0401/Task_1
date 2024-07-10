from enum import Enum
from typing import List

from py_selenium_auto.elements.button import Button
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By


class TypeOfTesting(Enum):
    Functional = "/functional_testing/"
    Automation = "/services/testing_automation/"
    Mobile = "/services/mobile_application_testing/"

class Page1(Form): #класс для описания страницы (а именно стартовой страницы), содержит элементы конкретной страницы. Действия, котрые могу с ними делать

    HERE_BTN = (By.XPATH, "//a[contains(@class, 'start__link')]")

    def __init__(self):
        self.__here_button = Button(*self.HERE_BTN) # инициализация приватной переменной, чтобы ее можно было менять только внутри класса, но не извне

    def click_HERE_BTN(self):
        self.__here_button.click()