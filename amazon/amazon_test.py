from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import amazon.constants as const


class AmazonTest(webdriver.Firefox):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(AmazonTest, self).__init__()
        self.implicitly_wait(15)
        # self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # shut down the firefox browser
        if self.teardown:
            self.quit()

    def land_first_page(self):
        # open the browser
        self.get(const.BASE_URL)

    # Scenario 1 - Login
    def login(self):
        login_element = self.find_element(By.XPATH, '//*[@id="nav-link-accountList"]')
        login_element.click()

        # enter valid email to continue with login
        email_text_field = self.find_element(By.ID, 'ap_email')
        email_text_field.click()
        email_text_field.send_keys('nvnsk24@gmail.com')
        email_btn = self.find_element(By.ID, 'continue')
        email_btn.click()

        # enter password to login
        pass_text_field = self.find_element(By.ID, 'ap_password')
        pass_text_field.click()
        pass_text_field.send_keys('Test123')

        submit_btn = self.find_element(By.ID, 'signInSubmit')
        submit_btn.click()

        # verify login
        username = 'naveen'
        login_verification = self.find_element(By.CSS_SELECTOR, '#nav-link-accountList-nav-line-1')
        if username in login_verification.text:
            print('Successfully logged in')
        else:
            print('Unsuccessful')

    def logout(self):
        signOut_element = self.find_element(By.ID, 'nav-item-signout')
        signOut_element.click()

    # Scenario 2
    def search(self):
        # search an item by sending its value
        search_bar = self.find_element(By.ID, 'twotabsearchtextbox')
        search_bar.click()
        search_bar.send_keys('iphone 12')

        # click the search button
        search_icon = self.find_element(By.ID, 'nav-search-submit-button')
        search_icon.click()

        # verify search
        item_list = []
        time.sleep(5)
        items = self.find_elements(By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')
        for item in items:
            item_list.append(item.text)

        if len(item_list) > 0:
            print('Search Successful')
        else:
            print('Search Unsuccessful')

    # Scenario 3
    def add_to_cart(self):
        hamburger = self.find_element(By.ID, 'nav-hamburger-menu')
        hamburger.click()
        time.sleep(5)

        # click on the electronic products
        electronics_menu = self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/ul[1]/li[7]/a')
        electronics_menu.click()
        time.sleep(5)

        # navigate to phone and accessories
        phone_menu = self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/ul[33]/li[6]/a')
        phone_menu.click()

        select_item = self.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]'
                                                  '/div[1]/div[9]/div/div/div/div/div[1]/span/a/div')
        select_item.click()

        # add to cart
        add = self.find_element(By.ID, 'add-to-cart-button')
        add.click()
        cart_btn = self.find_element(By.ID, 'nav-cart')
        cart_btn.click()

        # verify that the item is added to the cart
        cart_item_list = []
        item_name_list = []
        time.sleep(5)
        cart_items = self.find_elements(By.XPATH, '//div[contains(@class, "sc-list-item")]')
        for item in cart_items:
            cart_item_list.append(item.text)
            # item_name = item.find_element(By.XPATH, './/span[@class="a-truncate-cut"]')
            # item_name_list.append(item_name.text)

        item_names = self.find_elements(By.XPATH, './/span[@class="a-truncate-cut"]')
        for i in item_names:
            item_name_list.append(i.text)

        if len(cart_item_list) > 0:
            print("Item successfully added to cart")
            print(f'The items are: {item_name_list}')
        else:
            print("Item not added to cart")

        # nav-cart-count (another method to verify cart)
        nav_cart_count = self.find_element(By.ID, 'nav-cart-count')
        if int(nav_cart_count.text) > 0:
            print("Item successfully added to cart")
        else:
            print("Item not added to cart")

    # Scenario 4
    def verify_checkout(self, exp_date, exp_month):
        cart = self.find_element(By.ID, 'nav-cart')
        cart.click()

        checkout = self.find_element(By.XPATH, '//*[@id="sc-buy-box-ptc-button"]/span/input')
        checkout.click()

        # checkout form automation
        # Shipping address form
        country_element = self.find_element(By.XPATH, '//*[@id="address-ui-widgets-countryCode"]/span/span')
        country_element.click()
        select_country = self.find_element(By.XPATH, '//*[@id="address-ui-widgets-countryCode-dropdown-nativeId_82"]')
        select_country.click()

        name = self.find_element(By.ID, 'address-ui-widgets-enterAddressFullName')
        name.send_keys('Naveen')

        phone = self.find_element(By.ID, 'address-ui-widgets-enterAddressPhoneNumber')
        phone.send_keys('+4915224756907')

        address = self.find_element(By.ID, 'address-ui-widgets-enterAddressLine2')
        address.send_keys('Donau-Schwaeben-Strasse 16')

        postal_code = self.find_element(By.ID, 'address-ui-widgets-enterAddressPostalCode')
        postal_code.send_keys('94036')

        city = self.find_element(By.ID, 'address-ui-widgets-enterAddressCity')
        city.send_keys('Passau')

        submit_btn = self.find_element(By.XPATH, '//*[@id="address-ui-widgets-form-submit-button"]/span/input')
        submit_btn.click()

        # payment form
        add_card = self.find_element(By.ID, 'pp-aUAzxK-78')
        add_card.click()
        time.sleep(5)

        card_no = self.find_element(By.ID, 'pp-CYhAOh-17')
        card_no.send_keys('0000000000000000')

        card_name = self.find_element(By.ID, 'pp-CYhAOh-19')
        card_name.send_keys('Naveen Kularatne')

        card_expiration_date = self.find_element(By.XPATH, '//*[@id="pp-CYhAOh-23"]/span/span')
        card_expiration_date.click()
        # wait for item to be clickable
        time.sleep(5)

        # select the list of dates
        date_list = self.find_element(By.XPATH, '//*[@id="a-popover-4"]/div/div').text
        # iterate over the list of dates, verify the date and click
        for i in date_list:
            print(i)

        cvv = self.find_element(By.XPATH, '//*[@id="pp-hmfsH0-26"]')
        cvv.send_keys('0000')

        # Submit Payment Method
        submit_btn_card = self.find_element(By.XPATH, '//*[@id="pp-aUAzxK-93"]/span/input')
        submit_btn_card.click()


