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


class webPage_W_40_GW3Test(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        with open('../TextFolder/TestIn_UniqueURL_List.txt')as f:
            urls = f.read().splitlines()
            for url in urls:
                if ReadConfig.read_w40_GW3_configData('GW3Data', 'url') in url:
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
        self.assertEqual(ReadConfig.read_w40_GW3_configData('GW3Data', 'url'), WebPage_URL, msg="Web Landing page URL not Matched.")
        logger.info(': assertion complete with: ' + WebPage_URL)
        logger.info('####  TEST Complete  ####')

    def test_b_GW3_CertificateOffer_validation(self):
        logger.info(': ' + self.test_b_GW3_CertificateOffer_validation.__name__ + "\n #####  Starting TEST  ##### ")
        logger.info(": Navigate to Watches3 Landing Page")
        time.sleep(6)
        # offer_price = self.driver.find_element_by_xpath("//*[@class='banner-initial']").text
        # time.sleep(3)
        trade_in_price = self.driver.find_element_by_xpath("//span/strong[4]").text
        time.sleep(3)
        instant_credit = self.driver.find_element_by_xpath("(//*[@class='desc'])[1]").text
        time.sleep(3)
        # self.assertIn(ReadConfig.read_w40_GW3_configData('GW3Data', 'certificate_price'), offer_price,msg="Watch certificate Offer Price is not Matched. ")
        # logger.info(": Successfully verified Certificate Offer: " + ReadConfig.read_w40_GW3_configData('GW3Data', 'certificate_price'))
        # time.sleep(3)
        self.assertIn(ReadConfig.read_w40_GW3_configData('GW3Data', 'trade_in_price'), trade_in_price, msg="Watch Trade-In Price is not Matched. ")
        logger.info(": Successfully verified Trade-In Price: " + ReadConfig.read_w40_GW3_configData('GW3Data', 'trade_in_price'))
        time.sleep(3)
        self.assertIn(ReadConfig.read_w40_GW3_configData('GW3Data', 'instant_credit'), instant_credit, msg="Watch Instant Credit is not Matched. ")
        logger.info(": Successfully verified Instant Credit: " + ReadConfig.read_w40_GW3_configData('GW3Data', 'instant_credit'))
        logger.info('####  TEST Complete  ####')


if __name__ == '__main__':
    unittest.main()


