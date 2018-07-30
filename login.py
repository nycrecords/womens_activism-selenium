from selenium import webdriver
import unittest
import time

# logs into the website

class Login(unittest.TestCase):

    admin_username = 'test@email.com'
    admin_password = '1234'
    
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def login(self, user_type):
        if user_type == 'admin':
            self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.admin_username)
            self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.admin_password)
            self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)