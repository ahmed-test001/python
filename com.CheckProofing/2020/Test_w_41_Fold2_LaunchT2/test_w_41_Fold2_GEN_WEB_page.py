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


class webPage_W_41_Fold2_Gen_Test(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        with open('../TextFolder/TestIn_UniqueURL_List.txt')as f:
            urls = f.read().splitlines()
            for url in urls:
                if ReadConfig.read_w41_Fold2_configData('Fold2DataGEN', 'url') in url:
                    option = webdriver.ChromeOptions()
                    option.add_experimental_option('excludeSwitches', ['enable-logging'])
                    self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver1'), options=option)
                    warnings.filterwarnings(action="ignore", message="unclosed",category=ResourceWarning)
                    self.driver.maximize_window()
                    self.driver.get(url)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_a_GalaxyFOld2_WebLandingPage_URL_validation(self):
        logger.info(': '+self.test_a_GalaxyFOld2_WebLandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        GalaxyTabS7_WebPage_URL = self.driver.current_url
        self.assertEqual(ReadConfig.read_w41_Fold2_configData('Fold2DataGEN', 'url'), GalaxyTabS7_WebPage_URL, msg="Web Landing page URL not Matched.")
        logger.info(': assertion complete with: ' + GalaxyTabS7_WebPage_URL)
        logger.info('####  TEST Complete  ####')

    def test_b_GalaxyFold2_tradeinValue_validation(self):
        logger.info(': '+self.test_b_GalaxyFold2_tradeinValue_validation.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        tradein_price = self.driver.find_element_by_xpath("//*[@class='banner-initial']").text
        logger.info(": Navigate to Fold2  Web Page.")
        time.sleep(3)
        self.assertIn(ReadConfig.read_w41_Fold2_configData('WEBPage', 'trade_in_value'), tradein_price, msg="Tradein Value is not Matched. ")
        logger.info(": Successfully verified Tradein Value: " + ReadConfig.read_w41_Fold2_configData('WEBPage', 'trade_in_value'))
        logger.info('####  TEST Complete  ####')
        

if __name__ == '__main__':
    unittest.main()


