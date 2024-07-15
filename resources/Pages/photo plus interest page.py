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


class Check_Boxes_Name(Enum):
    Ponies = "Ponies"
    Polo = "Polo"
    Dough = "Dough"
    Snails = "Dough"
    Balls = "Balls"
    Post_its = "Post-its"
    Fausets = "Fausets"



class Checkboxes_Selector(Form):

    Check_Box_FORMAT = "//span[text()='{}']/preceding::span[contains(@class,'con icon-check checkbox__check')][1]"
    check_box_list = []
    for i in Check_Boxes_Name:
        check_box_list.append(Check_Box_FORMAT.format(i.value)) # создал cписок локаторов, теперь надо каждый локатор в конструктор каждого чек-бокса
    check_box_list_objects = [] # сюда помещу список объектов-чекбоксов

    def __init__(self):
        super().__init__(Locator(By.XPATH, '//*[contains(@class, "login-form__container")][1]'), 'Login form')
        for i in Check_Boxes_Name:
            self.check_box_list_objects.append(self._element_factory.get_check_box(Locator(self.check_box_list[i.value]), f'check_box_{i}'))

    # проинициализировал объекты через список
    # работаю со списком - каждый элемент которого - это обхект (чек-бокс) который можно нажимать

    # перемешиваю список
    random.shuffle(check_box_list_objects)

    # первые три чекбокса не кликаю (оставляю выбранныыми) - остальные кликаю

    for checkbox in check_box_list_objects[3:]:
        checkbox.click()








    def click_button_by_name(self, name: str):
        self._element_factory.get_button(Locator(By.XPATH, self.Check_Box_FORMAT.format(name)), name).click()



checkbox_selector = Checkboxes_Selector()
checkbox_selector.click_button_by_name(Check_Boxes_Name.Polo.value)


# class Checkboxes_Selector(Form):
#     Check_Box_FORMAT = "//span[text = '{}']/preceding::span[contains(@class,'con icon-check checkbox__check')][1]"
#
#     def click_button_by_name(self, name: Check_Boxes_Name):
#         q = self._element_factory.get_button(Locator(By.XPATH, self.Check_Box_FORMAT.format(name.value)), name.value).click()  # сразу создал и проинициализировал кнопку через шаблон
#         print(q)
#
#     click_button_by_name(Check_Boxes_Name.Polo.value)
