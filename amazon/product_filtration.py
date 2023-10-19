import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import amazon.constants as const


class ProductFiltration():
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def star_rating(self, star_value):
        star_filtration_box = self.driver.find_element(By.ID, 'reviewsRefinements')
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')

        for star_element in star_child_elements:
            if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} Stars &amp; Up':
                self.driver.execute_script("arguments[0].click();", star_element)

        time.sleep(3)
        # verify the filteration
        product_ratings = []
        product_rating_values = []

        items = self.driver.find_elements(By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')
        for item in items:
            ratings_box = item.find_elements(By.XPATH, './/div[contains(@class, "a-row a-size-small")]/span')
            if ratings_box != []:
                ratings = ratings_box[0].get_attribute('aria-label')
                ratings_value = ratings_box[1].get_attribute('aria-label')
            else:
                ratings, ratings_value = 0, 0

            product_ratings.append(ratings)
            product_rating_values.append(ratings_value)

        print(f'rating score: {star_value}')
        print(f'Product rating: {[x[:3]for x in product_ratings]}')
        print(f'product_rating_values: {product_rating_values}')

        for x in product_ratings:
            if int(x[:3]) >= star_value:
                print('Star Filtration Successful!')
            else:
              print("Star Filtration Unsuccessful!")
