from selenium import webdriver
import time
import sys
import unittest
import login
import addStory
import catalog
import subscribe
import testFeatures

class Test(unittest.TestCase):
    def test(self):
        self.driver = webdriver.Chrome('/Users/bzhuang/Downloads/chromedriver')
        self.driver.get("https://ec2-35-173-243-186.compute-1.amazonaws.com/login")

        loginn = login.Login(self.driver)
        loginn.login(self.user_type)
        time.sleep(1)

        # story = addStory.Story(self.driver)
        # story.makeStory(self.user_type)

        # catalog1 = catalog.Catalog(self.driver)
        # catalog1.catalog(self.user_type)

        # subbed = subscribe.Subscribe(self.driver)
        # subbed.sub(self.user_type)

        feature = testFeatures.Features(self.driver)
        # feature.hide_story(self.user_type)
        # feature.feature_story(self.user_type)
        # feature.edit_story(self.user_type)
        feature.modify_featured(self.driver)

        self.driver.find_element_by_link_text('LOGOUT').click()
        time.sleep(2)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        Test.user_type = sys.argv.pop()
    unittest.main()
