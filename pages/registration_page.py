import os
from datetime import datetime

import allure
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    def __init__(self, browser, url, first_name, last_name, email, phone, year, subject, address):
        super().__init__(browser, url)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = "Male"
        self.phone = phone
        now = datetime.now()
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        current_month_name = months[now.month - 1]
        self.birth_date = {"day": "07",
                           "month": current_month_name,
                           "year": year
                           }
        self.subject = subject
        self.hobby = "Sports"
        self.picture = "ulcamp-simbirsoft.jpg"
        self.address = address
        self.state = "Haryana"
        self.city = "Karnal"

    def enter_full_name(self):
        assert self.is_element_present(*RegistrationPageLocators.FIRST_NAME_INPUT), "Нет поля ввода имени"
        name_input = self.browser.find_element(*RegistrationPageLocators.FIRST_NAME_INPUT)
        name_input.send_keys(self.first_name)
        assert self.is_element_present(*RegistrationPageLocators.LAST_NAME_INPUT), "Нет поля ввода фамилии"
        last_name_input = self.browser.find_element(*RegistrationPageLocators.LAST_NAME_INPUT)
        last_name_input.send_keys(self.last_name)

    def enter_email(self):
        assert self.is_element_present(*RegistrationPageLocators.EMAIL_INPUT), "Нет поля ввода email"
        email_input = self.browser.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        email_input.send_keys(self.email)

    def choose_male_gender(self):
        assert self.is_element_present(*RegistrationPageLocators.GENDER_MALE_RADIO), "Нет радиобаттона Мужчина"
        male_radio = self.browser.find_element(*RegistrationPageLocators.GENDER_MALE_RADIO)
        male_radio.click()

    def enter_phone(self):
        assert self.is_element_present(*RegistrationPageLocators.PHONE_INPUT), "Нет поля ввода телефона"
        phone_input = self.browser.find_element(*RegistrationPageLocators.PHONE_INPUT)
        phone_input.send_keys(self.phone)

    def enter_birth_date(self):
        assert self.is_element_present(*RegistrationPageLocators.DATE_OF_BIRTH_INPUT), "Нет поля с датой рождения"
        date_of_birth = self.browser.find_element(*RegistrationPageLocators.DATE_OF_BIRTH_INPUT)
        date_of_birth.click()
        assert self.is_element_present(*RegistrationPageLocators.DATEPICKER), "Не появился календарь"
        datepicker_year = Select(self.browser.find_element(*RegistrationPageLocators.DATEPICKER_YEAR))
        datepicker_year.select_by_visible_text(self.birth_date["year"])
        seventh_day = self.browser.find_element(*RegistrationPageLocators.DATEPICKER_DAY)
        seventh_day.click()

    def choose_subject(self):
        assert self.is_element_present(*RegistrationPageLocators.SUBJECTS_INPUT), "Нет поля для ввода предметов"
        subjects_input = self.browser.find_element(*RegistrationPageLocators.SUBJECTS_INPUT)
        subjects_input.send_keys(self.subject)
        assert self.is_element_present(*RegistrationPageLocators.AUTOCOMPLETE_FIRST_ITEM), "Не появилcя автокомплит"
        autocomplete_item = self.browser.find_element(*RegistrationPageLocators.AUTOCOMPLETE_FIRST_ITEM)
        autocomplete_item.click()

    def enter_hobby(self):
        assert self.is_element_present(*RegistrationPageLocators.HOBBIES_CHECKBOX_SPORT), "Нет чекбокса для хобби"
        hobbie_checkbox = self.browser.find_element(*RegistrationPageLocators.HOBBIES_CHECKBOX_SPORT)
        hobbie_checkbox.click()

    def load_picture(self):
        assert self.is_element_present(*RegistrationPageLocators.FILE_INPUT), "Нет поля для загрузки файла"
        file_input = self.browser.find_element(*RegistrationPageLocators.FILE_INPUT)
        file_input.send_keys(f"{os.getcwd()}/files/{self.picture}")

    def enter_address(self):
        assert self.is_element_present(*RegistrationPageLocators.ADDRESS_INPUT), "Нет поля для ввода адреса"
        address_input = self.browser.find_element(*RegistrationPageLocators.ADDRESS_INPUT)
        address_input.send_keys(self.address)

    def choose_state(self):
        assert self.is_element_present(*RegistrationPageLocators.STATE_SELECT), "Нет поля для выбора штата"
        state_select = self.browser.find_element(*RegistrationPageLocators.STATE_SELECT)
        self.scroll_to_element(state_select)
        state_select.click()
        assert self.is_element_present(*RegistrationPageLocators.STATE_SELECT_THIRD_ITEM), \
            "Не появился выпадающий список"
        state_select_third = self.browser.find_element(*RegistrationPageLocators.STATE_SELECT_THIRD_ITEM)
        state_select_third.click()

    def choose_city(self):
        assert self.is_element_present(*RegistrationPageLocators.CITY_SELECT), "Нет поля для выбора города"
        city_input = self.browser.find_element(*RegistrationPageLocators.CITY_SELECT)
        city_input.click()
        assert self.is_element_present(*RegistrationPageLocators.CITY_SELECT_FIRST_ITEM), \
            "Не появился выпадающий список"
        city_select_first = self.browser.find_element(*RegistrationPageLocators.CITY_SELECT_FIRST_ITEM)
        city_select_first.click()

    def submit_form(self):
        assert self.is_element_present(*RegistrationPageLocators.SUBMIT_BUTTON), "У формы нет кнопки отправить"
        submit_button = self.browser.find_element(*RegistrationPageLocators.SUBMIT_BUTTON)
        submit_button.click()
        assert (self.presence_of_element_located(*RegistrationPageLocators.DIALOG_TITLE) and
                self.presence_of_element_located(*RegistrationPageLocators.RESULT_TABLE)), \
            "Не открылось диалоговое окно с подтверждением отправки формы"

    @allure.step('Проверяем данные формы')
    def check_form_data(self):
        dialog_title = self.browser.find_element(*RegistrationPageLocators.DIALOG_TITLE)
        confirmation_header = 'Thanks for submitting the form'
        assert dialog_title.text == confirmation_header, \
            f"Заголовок диалогового окна = '{dialog_title.text}' вместо '{confirmation_header}'"
        assert self.is_element_present(*RegistrationPageLocators.RESULT_TABLE), "Нет итоговой таблицы"
        student_name = self.browser.find_element(*RegistrationPageLocators.STUDENT_NAME_TABLE).text
        assert student_name == self.first_name + " " + self.last_name, f"Student Name неверное значение: {student_name}"
        student_email = self.browser.find_element(*RegistrationPageLocators.STUDENT_EMAIL_TABLE).text
        assert student_email == self.email, f"Student Email неверное значение: {student_email}"
        gender = self.browser.find_element(*RegistrationPageLocators.GENDER_TABLE).text
        assert gender == self.gender, f"Gender неверное значение: {gender}"
        mobile = self.browser.find_element(*RegistrationPageLocators.MOBILE_TABLE).text
        assert mobile == self.phone, f"Mobile неверное значение: {mobile}"
        birthdate = self.browser.find_element(*RegistrationPageLocators.DATE_OF_BIRTH_TABLE).text
        assert birthdate == self.birth_date["day"] + " " + self.birth_date["month"] + "," + self.birth_date["year"], \
            f"Date of Birth неверное значение: {birthdate}"
        subjects = self.browser.find_element(*RegistrationPageLocators.SUBJECTS_TABLE).text
        assert subjects == self.subject, f"Subjects неверное значение: {subjects}"
        hobbies = self.browser.find_element(*RegistrationPageLocators.HOBBIES_TABLE).text
        assert hobbies == self.hobby, f"Hobbies неверное значение: {hobbies}"
        picture = self.browser.find_element(*RegistrationPageLocators.PICTURE_TABLE).text
        assert picture == self.picture, f"Picture неверное значение: {picture}"
        address = self.browser.find_element(*RegistrationPageLocators.ADDRESS_TABLE).text
        assert address == self.address, f"Address неверное значение: {address}"
        state_and_city = self.browser.find_element(*RegistrationPageLocators.STATE_AND_CITY_TABLE).text
        assert state_and_city == self.state + " " + self.city, f"State and City неверное значение: {state_and_city}"
        close_button = self.browser.find_element(*RegistrationPageLocators.CLOSE_TABLE_BUTTON)
        close_button.click()
