import json

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    options.add_argument("start-maximized")
    options.page_load_strategy = 'eager'
    print(f"\nstart chrome browser for test")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="session")
def config():
    with open('config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
    return config
