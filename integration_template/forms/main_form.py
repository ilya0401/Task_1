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


class MainForm(Form):

    def __init__(self):
        super().__init__(Locator(By.CLASS_NAME, "main-intro__wrapper"), "Main form")
        self.label_nav_header = self._element_factory.get_label(
            Locator(By.XPATH, "//nav[contains(@class, 'header__nav')]"),
            "Navigation header"
        )
        self.contact_us = self._element_factory.get_button(
            Locator.by_class_name("header__btn-row"),
            "Contact US"
        )

    def nav_menu_buttons(self) -> List[Button]:
        return self.label_nav_header.find_child_elements(
            Button,
            Locator.by_class_name("nav__list-link"),
        )

    def type_of_testing_button(self, type_of_testing: TypeOfTesting):
        return self._element_factory.get_button(
            Locator.by_xpath(f"//li[@class='enumeration__item']/a[@href='{type_of_testing.value}']"),
            type_of_testing.name,
        )
