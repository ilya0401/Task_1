import enum

from py_selenium_auto.elements.button import Button
from py_selenium_auto.elements.text_box import TextBox
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By


class ContactUsTextField(enum.Enum):
    FullName = "PROPERTY[NAME][0]"
    Phone = "PROPERTY[8][0]"
    Company = "PROPERTY[7][0]"
    Email = "PROPERTY[9][0]"
    Message = "PROPERTY[10][0]"


class ContactUsModal(Form):

    def __init__(self):
        super().__init__(
            Locator(By.CSS_SELECTOR, ".modal-open"),
            "Contact US modal",
        )

    @property
    def close_button(self) -> Button:
        return self._form_element.find_child_element(
            Button,
            Locator.by_css_selector(".button-reset"),
            "Close button"
        )

    def get_text_field(self, name: ContactUsTextField) -> TextBox:
        return self._form_element.find_child_element(
            TextBox,
            Locator.by_name(name.value),
            f"TextBox: {name}"
        )

    @property
    def attach_file_input(self):
        return self._form_element.find_child_element(
            TextBox,
            Locator.by_name("PROPERTY_FILE_11_0"),
            "Attach file"
        )
