import time
from pages.catalog_page import CatalogPage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import pytest


class TestShops:
    """Добавление товара и удаление товара из корзины"""
    def test(self, driver):
        catalog_page = CatalogPage(driver, "https://testqastudio.me/")
        catalog_page.open()
        catalog_page.test_sofa(driver)

    """ Добавление товара в избранное и удаление из избранного """
    def test1(self, driver):
        catalog_page = CatalogPage(driver, "https://testqastudio.me/")
        catalog_page.open()
        catalog_page.test_cabinet(driver)

