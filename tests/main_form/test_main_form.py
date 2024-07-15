# import allure
#
# from resources.Pages.start_page import Start_Page, TypeOfTesting
# from tests.test_base import TestBase
#
#
# class TestMainForm(TestBase):
#     page1 = Start_Page()
#
#     def setup(self):
#         with allure.step("Go to start page"):
#             self.go_to_start_page()
#
#         with allure.step("Start page is displayed"):
#             assert self.page1.state.is_displayed() # проверяю что страница загрузилась
#             assert self.page1.HERE_BTN.state.wait_for_displayed() # проверяю что нужная кнопка появилась / прогрузилась
#             # assert self.main_form.label_nav_header.state.wait_for_displayed() - было так
#
#     def test_main_page(self):
#         # тут пишу код проверки, шаги / действия с UI
#
#
#         with allure.step("Check Navigation menu items"):
#             assert len(self.main_form.nav_menu_buttons()) == 4
#
#         with allure.step("Check base elements"):
#             assert self.main_form.contact_us.state.is_displayed()
#             for type_of_testing in TypeOfTesting:
#                 assert self.main_form.type_of_testing_button(type_of_testing).state.is_displayed()
