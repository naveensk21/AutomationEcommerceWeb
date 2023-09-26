from amazon.amazon_test import AmazonTest

with AmazonTest() as bot:
    bot.land_first_page()
    # bot.login()
    # bot.search()
    bot.add_to_cart()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
#
# driver = webdriver.Firefox()
# driver.get('https://demoqa.com/automation-practice-form')
#
# dob = '29 Sep 2023'
# date = driver.find_element(By.ID, 'dateOfBirthInput')
# date.send_keys('29 Sep 2023')

