import allure

from pages.registration_page import RegistrationPage
from utils.employee import employee_data


@allure.feature('Регистрация')
@allure.story('Проверка формы регистрации')
def test_registration_form(browser, config):
    registration_page = RegistrationPage(browser, config['URL'], **employee_data)
    registration_page.open()
    registration_page.enter_full_name()
    registration_page.enter_email()
    registration_page.choose_male_gender()
    registration_page.enter_phone()
    registration_page.enter_birth_date()
    registration_page.choose_subject()
    registration_page.enter_hobby()
    registration_page.load_picture()
    registration_page.enter_address()
    registration_page.choose_state()
    registration_page.choose_city()
    registration_page.submit_form()
    registration_page.check_form_data()
