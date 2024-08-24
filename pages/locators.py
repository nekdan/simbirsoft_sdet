from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#lastName")
    EMAIL_INPUT = (By.ID, "userEmail")
    GENDER_MALE_RADIO = (By.XPATH, "//input[@id='gender-radio-1'] /parent::div")
    PHONE_INPUT = (By.XPATH, "//input[@id='userNumber']")
    DATE_OF_BIRTH_INPUT = (By.CSS_SELECTOR, "#dateOfBirthInput")
    DATEPICKER = (By.CSS_SELECTOR, ".react-datepicker__month-container")
    DATEPICKER_YEAR = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    DATEPICKER_DAY = (By.CSS_SELECTOR, ".react-datepicker__day.react-datepicker__day--007")
    SUBJECTS_INPUT = (By.CSS_SELECTOR, "#subjectsInput")
    AUTOCOMPLETE_FIRST_ITEM = (By.CSS_SELECTOR, "#react-select-2-option-0")
    HOBBIES_CHECKBOX_SPORT = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    FILE_INPUT = (By.CSS_SELECTOR, "#uploadPicture")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "#currentAddress")
    STATE_SELECT = (By.CSS_SELECTOR, "#state")
    STATE_SELECT_THIRD_ITEM = (By.CSS_SELECTOR, "#react-select-3-option-2")
    CITY_SELECT = (By.CSS_SELECTOR, "#city")
    CITY_SELECT_FIRST_ITEM = (By.CSS_SELECTOR, "#react-select-4-option-0")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")
    DIALOG_TITLE = (By.CSS_SELECTOR, "#example-modal-sizes-title-lg")
    RESULT_TABLE = (By.CSS_SELECTOR, ".table.table-dark.table-striped.table-bordered.table-hover")
    STUDENT_NAME_TABLE = (By.CSS_SELECTOR, "tbody tr:nth-child(1) td:nth-child(2)")
    STUDENT_EMAIL_TABLE = (By.CSS_SELECTOR, "tbody tr:nth-child(2) td:nth-child(2)")
    GENDER_TABLE = (By.CSS_SELECTOR, "tbody tr:nth-child(3) td:nth-child(2)")
    MOBILE_TABLE = (By.CSS_SELECTOR, "tbody tr:nth-child(4) td:nth-child(2)")
    DATE_OF_BIRTH_TABLE = (By.CSS_SELECTOR, "tbody tr:nth-child(5) td:nth-child(2)")
    SUBJECTS_TABLE = (By.CSS_SELECTOR, "tbody tr:nth-child(6) td:nth-child(2)")
    HOBBIES_TABLE = (By.CSS_SELECTOR, "tbody tr:nth-child(7) td:nth-child(2)")
    PICTURE_TABLE = (By.CSS_SELECTOR, "tbody tr:nth-child(8) td:nth-child(2)")
    ADDRESS_TABLE = (By.CSS_SELECTOR, "tbody tr:nth-child(9) td:nth-child(2)")
    STATE_AND_CITY_TABLE = (By.CSS_SELECTOR, "tbody tr:nth-child(10) td:nth-child(2)")
    CLOSE_TABLE_BUTTON = (By.CSS_SELECTOR, "#closeLargeModal")
