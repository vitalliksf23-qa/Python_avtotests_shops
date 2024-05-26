import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    driver.maximize_window()

    #  Все что до yield выполняется перед тестом
    yield driver  # - это ключевое слово указывающий на закрытие браузера при любом исходе
    driver.close()  # Нужно прописывать чтоб в  диспетчере задач не копились процессы Chromedriver
    driver.quit()
