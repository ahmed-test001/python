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


class webPage_W_39_Fold2_EPP_Test(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        with open('../TextFolder/TestIn_UniqueURL_List.txt')as f:
            urls = f.read().splitlines()
            for url in urls:
                if ReadConfig.read_w39_Fold2_configData('Fold2EPPData', 'url') in url:
                    option = webdriver.ChromeOptions()
                    option.add_experimental_option('excludeSwitches', ['enable-logging'])
                    self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver1'), options=option)
                    warnings.filterwarnings(action="ignore", message="unclosed",category=ResourceWarning)
                    self.driver.maximize_window()
                    self.driver.get(url)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_a_GalaxyTabS7_WebLandingPage_URL_validation(self):
        logger.info(': '+self.test_a_GalaxyTabS7_WebLandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        GalaxyTabS7_WebPage_URL = self.driver.current_url
        self.assertEqual(ReadConfig.read_w39_Fold2_configData('Fold2EPPData', 'url'), GalaxyTabS7_WebPage_URL, msg="Galaxy z Fold2 Web Landing page URL not Matched.")
        logger.info(': assertion complete with: ' + GalaxyTabS7_WebPage_URL)
        logger.info('####  TEST Complete  ####')

    def test_b_verify_tradein_price_validation(self):
        logger.info(': '+self.test_b_verify_tradein_price_validation.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        # tradein1 = self.driver.find_element_by_xpath("//*[@class ='tradeinPrice']").text
        # assert ReadConfig.read_w39_Fold2_configData('Fold2Webpage', 'tradein1_price') in tradein1
        tradein = self.driver.find_element_by_xpath("(//div[@class ='desc'])[1]").text
        self.assertIn(ReadConfig.read_w39_Fold2_configData('Fold2Webpage', 'tradein_price'), tradein, msg="Trade-In Price not Matched.")
        logger.info(': assertion complete with: ' + tradein)
        logger.info('####  TEST Complete  ####')

    def test_c_Redeem_instantcredit_option_validation(self):
        logger.info(': '+self.test_c_Redeem_instantcredit_option_validation.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        instantCredit = self.driver.find_element_by_xpath("(//div[@class ='promo-text-title'])[1]").text
        self.assertIn(ReadConfig.read_w39_Fold2_configData('Fold2Webpage', 'instant_Credit'), instantCredit, msg="Trade-In Price not Matched.")
        logger.info(': assertion instant credit with: ' + ReadConfig.read_w39_S7_configData('S7Webpage', 'instant_Credit'))
        time.sleep(3)
        MOGAText = self.driver.find_element_by_xpath("(//div[@class ='promo-text-title'])[3]").text
        self.assertIn(ReadConfig.read_w39_Fold2_configData('Fold2Webpage', 'MOGA_offer'), MOGAText, msg="MOGA Offer not Matched.")
        logger.info(': assertion MOGA offer with: ' + ReadConfig.read_w39_S7_configData('S7Webpage', 'MOGA_offer'))
        time.sleep(3)
        accessoriesText = self.driver.find_element_by_xpath("(//div[@class ='promo-text-title'])[5]").text
        self.assertIn(ReadConfig.read_w39_Fold2_configData('Fold2Webpage', 'accessories_offer'), accessoriesText, msg="Accesories Offer not Matched.")
        logger.info(': assertion accessories offer with: ' + ReadConfig.read_w39_S7_configData('S7Webpage', 'accessories_offer'))
        logger.info('####  TEST Complete  ####')


if __name__ == '__main__':
    unittest.main()


