import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import amazon.constants as const


class ProductFiltration():
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def star_rating(self):
        star_filtration_box = self.driver.find_element()
        pass
