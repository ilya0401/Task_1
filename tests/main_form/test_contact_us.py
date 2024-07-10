from pathlib import Path

import allure
from py_selenium_auto_core.utilities.file_reader import FileReader
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper

from resources.forms.contact_us_modal import ContactUsModal, ContactUsTextField
from resources.forms.main_form import MainForm
from resources.models.contact_us_info import ContactUsInfo
from tests.test_base import TestBase


class TestMainForm(TestBase):
    main_form = MainForm()
    contact_us_modal = ContactUsModal()

    def setup(self):
        with allure.step("Go to main page"):
            self.go_to_start_page()

        with allure.step("Main page is displayed"):
            assert self.main_form.state.is_displayed()
            assert self.main_form.label_nav_header.state.wait_for_displayed()

    def test_contact_us(self):
        contact_us_info = ContactUsInfo(
            full_name="John Wick",
            phone="88888888",
            company="InterToInter",
            email="test@email.com",
            message="CustomMessage" * 5,
        )

        with allure.step("Check base elements"):
            self.main_form.contact_us.click()

        with allure.step("Contact Us modal is displayed"):
            assert self.contact_us_modal.state.wait_for_displayed()

        with allure.step("Fill data"):
            self.contact_us_modal.get_text_field(ContactUsTextField.FullName).type(contact_us_info.full_name)
            self.contact_us_modal.get_text_field(ContactUsTextField.Phone).type(contact_us_info.phone)
            self.contact_us_modal.get_text_field(ContactUsTextField.Company).type(contact_us_info.company)
            self.contact_us_modal.get_text_field(ContactUsTextField.Email).type(contact_us_info.email)
            self.contact_us_modal.get_text_field(ContactUsTextField.Message).type(contact_us_info.message)

        with allure.step("Check data data"):
            assert self.contact_us_modal.get_text_field(ContactUsTextField.FullName).value == contact_us_info.full_name
            assert self.contact_us_modal.get_text_field(ContactUsTextField.Phone).value == contact_us_info.phone
            assert self.contact_us_modal.get_text_field(ContactUsTextField.Company).value == contact_us_info.company
            assert self.contact_us_modal.get_text_field(ContactUsTextField.Email).value == contact_us_info.email
            assert self.contact_us_modal.get_text_field(ContactUsTextField.Message).value == contact_us_info.message

        with allure.step("Attach file"):
            file_name = "file_to_upload.pdf"
            test_file = FileReader.get_resource_file_path(
                str(Path("test_data", file_name)),
                RootPathHelper.calling_root_path(),
            )
            self.contact_us_modal.attach_file_input.send_keys(test_file)
            assert file_name in self.contact_us_modal.attach_file_input.value

        with allure.step("Close Contact Us modal"):
            self.contact_us_modal.close_button.click()

        with allure.step("Contact Us modal is not displayed"):
            assert self.contact_us_modal.state.wait_for_not_displayed()
