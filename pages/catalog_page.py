import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains


class CatalogPage(BasePage):
    PAGE_URL = "https://testqastudio.me/"
    CATALOG_BUTTON = (By.LINK_TEXT, "Каталог")
    FOOTER_ELEMENT = (By.XPATH, "//*[@id='rz-shop-content']/div/div")
    NAME_SOFA = (By.XPATH, "(//a[text() = 'ЭППЛАРЮД Диван трёхместный'])")
    CART_BUTTON = (By.XPATH, "//button[@name = 'add-to-cart']")
    REMOVE_FROM_CART = (By.XPATH, "//span[@class='name']")
    CLOSE_CART = (By.XPATH, "//*[@id='cart-modal']/div[2]/div[1]/a/span")
    TEXT_RESULT = (By.XPATH, "//*[@id='cart-modal']/div[2]/div[2]/div/p/span")

    def product_catalog(self, driver):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.wait.until(EC.visibility_of_element_located(CatalogPage.NAME_SOFA)).click()
        self.element_is_visible(CatalogPage.CART_BUTTON).click()
        self.element_is_visible(CatalogPage.REMOVE_FROM_CART).click()
        # time.sleep(3)
        self.wait.until(EC.visibility_of_element_located(CatalogPage.TEXT_RESULT))  # Дожидаемся появления элемента "Ваша корзина пуста"
        assert self.driver.find_element(*CatalogPage.TEXT_RESULT).is_displayed()  # Проверяем появление элемента "Ваша корзина пуста
        # assert driver.find_element(By.XPATH, "//*[@id='cart-modal']/div[2]/div[2]/div/p/span").is_displayed()
        self.element_is_visible(CatalogPage.CLOSE_CART).click()


        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        # self.element_is_visible(CatalogPage.FOOTER_ELEMENT)
        # self.wait.until(EC.presence_of_element_located(CatalogPage.FOOTER_ELEMENT))


        # self.element_is_visible(CatalogPage.NAME_SOFA).click()