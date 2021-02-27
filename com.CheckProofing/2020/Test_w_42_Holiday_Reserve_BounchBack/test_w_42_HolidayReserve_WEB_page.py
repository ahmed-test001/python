import time
import unittest
import sys
import os
import logging
import warnings
from selenium import webdriver
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from Utility_Files.HTMLTestRunner import stdout_redirector
from Utility_Files import ReadConfig
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class webPage_W_42_HolidayReserve_Test(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        with open('../TextFolder/TestIn_UniqueURL_List.txt')as f:
            urls = f.read().splitlines()
            for url in urls:
                if ReadConfig.read_w42_HolidayReserve_configData('RH_DATA', 'url') in url:
                    option = webdriver.ChromeOptions()
                    option.add_experimental_option('excludeSwitches', ['enable-logging'])
                    self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver1'), options=option)
                    warnings.filterwarnings(action="ignore", message="unclosed",category=ResourceWarning)
                    self.driver.maximize_window()
                    self.driver.get(url)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_a_WebLandingPage_URL_validation(self):
        logger.info(': '+self.test_a_WebLandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        WebPage_URL = self.driver.current_url
        self.assertEqual(ReadConfig.read_w42_HolidayReserve_configData('RH_DATA', 'url'), WebPage_URL, msg="Web Landing page URL not Matched.")
        logger.info(': assertion complete with: ' + WebPage_URL)
        logger.info('####  TEST Complete  ####')

    # def test_b_SendOffer_confirm_validation(self):
    #     logger.info(': '+self.test_b_SendOffer_confirm_validation.__name__ + "\n #####  Starting TEST  ##### ")
    #     time.sleep(3)
    #     logger.info(": Navigate to Early Offer Web Page.")
    #     self.driver.find_element_by_xpath("(//*[@class='heart'])[5]").click()
    #     self.driver.find_element_by_xpath("(//*[@class='heart'])[8]").click()
    #     self.driver.find_element_by_xpath("(//*[@class='heart'])[18]").click()
    #     self.driver.find_element_by_xpath("(//*[@class='cta-button primary-selection-new-variation__btn'])[1]").click()
    #     time.sleep(3)
    #     success_msg = self.driver.find_element_by_xpath("//*[@class='confirm-copy']").text
    #     time.sleep(2)
    #     self.assertIn(ReadConfig.read_w42_HolidayReserve_configData('WEBPage', 'confirm_msg'), success_msg,msg="Success Message is not Matched. ")
    #     logger.info(": Successfully verified confirm message: " + ReadConfig.read_w42_HolidayReserve_configData('WEBPage', 'confirm_msg'))
    #     logger.info('####  TEST Complete  ####')


if __name__ == '__main__':
    unittest.main()


