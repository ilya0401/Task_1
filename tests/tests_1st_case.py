import allure

from resources.Pages.start_page import Start_Page
from resources.Pages.login_form import Login_Form
from tests.test_base import TestBase
from resources.Pages.start_page import TypeOfTesting

class Test_main_work_flow(TestBase):
    start_page = Start_Page()
    login_page = Login_Form()

    def setup(self):
        with allure.step("Go to start page"):
            self.go_to_start_page()

        with allure.step("Start page is displayed"):
            assert self.page1.state.is_displayed() # проверяю что страница загрузилась
            assert self.page1.HERE_BTN.state.wait_for_displayed() # проверяю что нужная кнопка появилась / прогрузилась
            # assert self.main_form.label_nav_header.state.wait_for_displayed() - было так

    def test_main_work_flow(self):
        # тут пишу код проверки, шаги / действия с UI
        assert self.start_page.state.is_displayed() #проверяю загрузку страницы в тестовом методе. Также факт загрузки проверяется при обращении к странице. Статус загрузки проверяется в конструкторе
        self.start_page.click_HERE_BTN()

        assert self.login_page.state.is_displayed()
        self.login_page.fill_passwd_fld()
        self.login_page.fill_email()
        self.login_page.fill_domain()
        self.login_page.choose_root_domain()
        self.login_page.click_check_box()
        self.login_page.click_next()

