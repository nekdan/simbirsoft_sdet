from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def presence_of_element_located(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout). \
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def scroll_to_element(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -50);", element)
