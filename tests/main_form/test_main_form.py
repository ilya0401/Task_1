import allure

from integration_template.forms.main_form import MainForm, TypeOfTesting
from tests.test_base import TestBase


class TestMainForm(TestBase):
    main_form = MainForm()

    def setup(self):
        with allure.step("Go to main page"):
            self.go_to_start_page()

        with allure.step("Main page is displayed"):
            assert self.main_form.state.is_displayed()
            assert self.main_form.label_nav_header.state.wait_for_displayed()

    def test_main_page(self):
        with allure.step("Check Navigation menu items"):
            assert len(self.main_form.nav_menu_buttons()) == 4

        with allure.step("Check base elements"):
            assert self.main_form.contact_us.state.is_displayed()
            for type_of_testing in TypeOfTesting:
                assert self.main_form.type_of_testing_button(type_of_testing).state.is_displayed()
