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


class webPage_W_40_WearableTest(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        with open('../TextFolder/Test_InputFile_URLSegment.txt')as f:
            urls = f.read().splitlines()
            for url in urls:
                if ReadConfig.read_w40_Wearable_configData('WearableData', 'url') in url:
                    option = webdriver.ChromeOptions()
                    option.add_experimental_option('excludeSwitches', ['enable-logging'])
                    self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver1'), options=option)
                    warnings.filterwarnings(action="ignore", message="unclosed",category=ResourceWarning)
                    self.driver.maximize_window()
                    self.driver.get(url)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_a_Wearable_WebLandingPage_URL_validation(self):
        logger.info(': '+self.test_a_Wearable_WebLandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        Wearable_WebPage_URL = self.driver.current_url
        self.assertEqual(ReadConfig.read_w40_Wearable_configData('WearableData', 'url'), Wearable_WebPage_URL, msg="Wearable Web Landing page URL not Matched.")
        logger.info(': assertion complete with: ' + Wearable_WebPage_URL)
        logger.info('####  TEST Complete  ####')

    def test_b_Wearable_CertificateOffer_ReserveNowLink_validation(self):
        logger.info(': '+self.test_b_Wearable_CertificateOffer_ReserveNowLink_validation.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        logger.info(": Navigate to All Watches Landing Page")
        self.driver.find_element_by_xpath("//*[@class='cta-button ']").click()
        logger.info(": Click from Galaxy Watch3 Banner Titanium Reserve Now Button")
        time.sleep(6)
        offer_price = self.driver.find_element_by_xpath("//*[@class='banner-initial']").text
        logger.info(": Navigate to check out Page.")
        time.sleep(3)
        self.assertIn(ReadConfig.read_w40_Wearable_configData('WearableData', 'certificate_price'), offer_price, msg="Watch certificate Offer Price is not Matched. ")
        logger.info(": Successfully verified Certificate Offer Price: " + ReadConfig.read_w40_Wearable_configData('WearableData', 'certificate_price'))
        logger.info('####  TEST Complete  ####')

    def test_c_Wearable_CertificateOffer_ReserveLink_validation(self):
        logger.info(': '+self.test_c_Wearable_CertificateOffer_ReserveLink_validation.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        logger.info(": Navigate to All Watches Landing Page")
        self.driver.find_element_by_xpath("//*[@class='Product-card__button-main cta-button']").click()
        logger.info(": Click Galaxy Watch3 Titanium Mystic Black (Bluetooth) Reserve Button")
        time.sleep(6)
        offer_price = self.driver.find_element_by_xpath("//*[@class='banner-initial']").text
        logger.info(": Navigate to check out Page.")
        time.sleep(3)
        self.assertIn(ReadConfig.read_w40_Wearable_configData('WearableData', 'certificate_price'), offer_price, msg="Watch certificate Offer Price is not Matched. ")
        logger.info(": Successfully verified Certificate Offer Price: " + ReadConfig.read_w40_Wearable_configData('WearableData', 'certificate_price'))
        logger.info('####  TEST Complete  ####')


if __name__ == '__main__':
    unittest.main()


