from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, url):  # Прописываем то что будет инициализироваться при каждом тесте
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)  # Сокращаем WebDriverWait до wait, poll_frequency=1 аргумент который будет спрашивать драйвер раз в секунду о выполнении условия

    def open(self):  # Метод который открывает страницы
        self.driver.get(self.url)

    def is_opened(self):  # Метод который будет проверять правильная страница открыта или нет
        self.wait.until(EC.url_to_be(self.url))

    def element_is_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))  # Жди пока не появится елемент

    def elements_are_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator))  # Жди пока все елементы не появятся

    def element_is_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator))  # Искать элемент в дереве

    def elements_is_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator))  # Искать элементы в дереве

    def elements_is_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))  # Элемент должен быть кликабельный

    def go_to_element(self, element):
        self.driver.execute_script("argument[0].scrollIntoView();", element)  # Скролить до элемента
