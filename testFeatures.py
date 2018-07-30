from selenium import webdriver
import unittest
import time

class Features(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def hide_story(self, user_type):
        self.driver.find_element_by_link_text('CATALOG').click()
        time.sleep(.5)
        self.driver.find_element_by_xpath('//*[@id="home-stories"]/a[1]/div').click()
        time.sleep(.5)
        self.driver.find_element_by_link_text('Hide this Story').click()
        time.sleep(2)

    def feature_story(self, user_type):
        self.driver.find_element_by_link_text('CATALOG').click()
        time.sleep(.5)
        self.driver.find_element_by_xpath('//*[@id="home-stories"]/a[1]/div').click()
        time.sleep(.5)
        self.driver.find_element_by_link_text('Feature this Story').click()
        time.sleep(.5)
        self.driver.find_element_by_xpath('//*[@id="left_right-0"]').click()
        time.sleep(.5)
        self.driver.find_element_by_xpath('//*[@id="quote"]').send_keys("THIS IS FEATURED NOW")
        time.sleep(.5)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(2)

    def edit_story(self, user_type):
        self.driver.find_element_by_link_text('CATALOG').click()
        time.sleep(.5)
        self.driver.find_element_by_xpath('//*[@id="home-stories"]/a[1]/div').click()
        time.sleep(.5)
        self.driver.find_element_by_link_text('Edit this Story').click()
        time.sleep(.5)
        self.driver.find_element_by_xpath('//*[@id="story-content"]').send_keys("CUZ REASONs")

        
        self.driver.find_element_by_xpath('//*[@id="first-name-field"]').clear()
        self.driver.find_element_by_xpath('//*[@id="first-name-field"]').send_keys('Edit')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="last-name-field"]').clear()
        self.driver.find_element_by_xpath('//*[@id="activist-start"]').clear()
        self.driver.find_element_by_xpath('//*[@id="activist-end"]').clear()
        self.driver.find_element_by_xpath('//*[@id="last-name-field"]').send_keys('Edit')
        self.driver.find_element_by_xpath('//*[@id="activist-start"]').send_keys('2018')
        self.driver.find_element_by_xpath('//*[@id="activist-end"]').send_keys('Today')
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="about-her"]/div[1]/div/div[2]/button[14]').click()
        time.sleep(.5)
        self.driver.find_element_by_xpath('//*[@id="about-her"]/div[1]/div/div[2]/button[5]').click()
        time.sleep(.5)
        self.driver.find_element_by_xpath('//*[@id="about-her"]/div[1]/div/div[2]/button[6]').click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="about-her"]/div[1]/div/div[2]/button[3]').click()
        self.driver.find_element_by_xpath('//*[@id="about-her"]/div[1]/div/div[2]/button[5]').click()
        self.driver.find_element_by_xpath('//*[@id="about-her"]/div[1]/div/div[2]/button[9]').click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="story-content"]').clear()
        self.driver.find_element_by_xpath('//*[@id="story-content"]').send_keys('THIS IS A TEST EDIT: HAS BEEN EDITED')

        self.driver.find_element_by_xpath('//*[@id="activist-url"]').clear()
        self.driver.find_element_by_xpath('//*[@id="activist-url"]').send_keys('https://en.wikipedia.org/wiki/Banana')
        time.sleep(1)


        self.driver.find_element_by_xpath('//*[@id="user-first-name-field"]').clear()
        self.driver.find_element_by_xpath('//*[@id="user-last-name-field"]').clear()
        self.driver.find_element_by_xpath('//*[@id="user-email-field"]').clear()
        self.driver.find_element_by_xpath('//*[@id="user-first-name-field"]').send_keys('EDIT')
        self.driver.find_element_by_xpath('//*[@id="user-last-name-field"]').send_keys('EDIT')
        self.driver.find_element_by_xpath('//*[@id="user-email-field"]').send_keys('EDIT@EDIT.com')
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="share-story-btn"]').click()
        time.sleep(.5)

    def modify_featured(self, user_type):
        self.driver.find_element_by_link_text('FEATURES').click()
        self.driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr[1]/th/a/span').click()
        time.sleep(1)
        if self.driver.find_element_by_xpath('//*[@id="left_right-0"]').is_selected():
            self.driver.find_element_by_xpath('//*[@id="left_right-1"]').click()
            time.sleep(1)
        else:
            self.driver.find_element_by_xpath('//*[@id="left_right-0"]').click()
            time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="quote"]').clear()
        self.driver.find_element_by_xpath('//*[@id="quote"]').send_keys('THIS IS FEATURED NOW 2: EDIT BOOGALOO')
        time.sleep(1)
        if self.driver.find_element_by_xpath('//*[@id="is_visible-1"]').is_selected():
            self.driver.find_element_by_xpath('//*[@id="is_visible-0"]').click()
            time.sleep(1)
        else:
            self.driver.find_element_by_xpath('//*[@id="is_visible-1"]').click()
            time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(3)