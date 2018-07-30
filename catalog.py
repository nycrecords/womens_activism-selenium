from selenium import webdriver
import unittest
import time

class Catalog(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    # catalog goes to the catalog page and cycles through the tags available there
    # currently does tags in sets of two, sets of three tags make the test take too long

    def catalog(self, user_type):
        self.driver.find_element_by_link_text('CATALOG').click()
        self.driver.find_element_by_xpath('//*[@id="search"]').clear()
        self.driver.find_element_by_xpath('//*[@id="search"]').send_keys('Mary Smith')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="search-btn"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="search"]').clear()
        for x in range(1,18):
            self.driver.find_element_by_xpath('//*[@id="search-tags"]/div[2]/button[' + str(x) + ']').click()
            time.sleep(.125)
            for y in range (1,18):
                if x == y:
                    continue
                else:
                    self.driver.find_element_by_xpath('//*[@id="search-tags"]/div[2]/button[' + str(y) + ']').click()
                    time.sleep(.125)
                    # the code below this tests all combinations of three tags in the catalog page
                    # but it makes the test take forever, even if all the sleeps are removed
                    # for z in range (1,18):
                    #     if (z == x) or (z==y):
                    #         continue
                    #     else:
                    #         self.driver.find_element_by_xpath('//*[@id="search-tags"]/div[2]/button[' + str(z) + ']').click()
                    #         time.sleep(.125)
                    #         self.driver.find_element_by_xpath('//*[@id="search-tags"]/div[2]/button[' + str(z) + ']').click()
                    #         time.sleep(.125) 
                    self.driver.find_element_by_xpath('//*[@id="search-tags"]/div[2]/button[' + str(y) + ']').click()
                    time.sleep(.125)
            self.driver.find_element_by_xpath('//*[@id="search-tags"]/div[2]/button[' + str(x) + ']').click()
            time.sleep(.125)

        time.sleep(3)
