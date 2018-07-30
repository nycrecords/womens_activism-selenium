from selenium import webdriver
import unittest
import time

class Story(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def makeStory(self, user_type):
        time.sleep(1)
        self.driver.find_element_by_link_text("SHARE A STORY").click()
        self.driver.find_element_by_xpath('//*[@id="first-name-field"]').send_keys('Mary')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="last-name-field"]').send_keys('Smith')
        self.driver.find_element_by_xpath('//*[@id="activist-start"]').send_keys('1940')
        self.driver.find_element_by_xpath('//*[@id="activist-end"]').send_keys('Today')
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="about-her"]/div[1]/div/div[2]/button[14]').click()
        self.driver.find_element_by_xpath('//*[@id="about-her"]/div[1]/div/div[2]/button[5]').click()
        self.driver.find_element_by_xpath('//*[@id="about-her"]/div[1]/div/div[2]/button[6]').click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="story-content"]').send_keys('THIS IS A TEST CONTENT')
        self.driver.find_element_by_xpath('//*[@id="activist-url"]').send_keys('https://en.wikipedia.org/wiki/Mary_Ellen_Smith')
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="image-upload-btn"]').click()
        self.driver.find_element_by_xpath('//*[@id="story-image-input-box"]').send_keys('https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg')
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="user-first-name-field"]').send_keys('Yarm')
        self.driver.find_element_by_xpath('//*[@id="user-last-name-field"]').send_keys('Htims')
        self.driver.find_element_by_xpath('//*[@id="user-email-field"]').send_keys('gmail@msmith.com')
        self.driver.find_element_by_xpath('//*[@id="user-phone-field"]').send_keys('5555555555')
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="user-subscription-btn"]').click()
        time.sleep(.5)

        self.driver.find_element_by_xpath('//*[@id="share-story-btn"]').click()
        time.sleep(3)