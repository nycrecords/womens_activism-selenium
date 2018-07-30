from selenium import webdriver
import unittest
import time

class Subscribe(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def sub(self, user_type):
        time.sleep(1)
        self.driver.find_element_by_link_text('SUBSCRIBE').click()
        self.driver.find_element_by_xpath('//*[@id="user-first-name-field"]').send_keys('Mary Mary')
        self.driver.find_element_by_xpath('//*[@id="user-last-name-field"]').send_keys('Mary Mary')
        self.driver.find_element_by_xpath('//*[@id="user-email-field"]').send_keys('smith@smith.com')
        self.driver.find_element_by_xpath('//*[@id="user-phone-field"]').send_keys("5555555555")
        self.driver.find_element_by_xpath('//*[@id="subscribe-btn"]').click()
        time.sleep(5)
