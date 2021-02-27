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


class webPage_W_39_SeroTVTest(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        with open('../TextFolder/TestIn_UniqueURL_List.txt')as f:
            urls = f.read().splitlines()
            for url in urls:
                if ReadConfig.read_w39_configData('SeroTVData', 'url') in url:
                    option = webdriver.ChromeOptions()
                    option.add_experimental_option('excludeSwitches', ['enable-logging'])
                    self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver1'), options=option)
                    warnings.filterwarnings(action="ignore", message="unclosed",category=ResourceWarning)
                    self.driver.maximize_window()
                    self.driver.get(url)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_a_SeroTV_WebLandingPage_URL_validation(self):
        logger.info(': '+self.test_a_SeroTV_WebLandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        SeroTV_WebPage_URL = self.driver.current_url
        self.assertEqual(ReadConfig.read_w39_configData('SeroTVData', 'url'), SeroTV_WebPage_URL, msg="Sero TV Web Landing page URL not Matched.")
        logger.info(': assertion complete with: ' + SeroTV_WebPage_URL)
        logger.info('####  TEST Complete  ####')

    def test_b_SeroTV_price_validation_BuyNow_TopButton(self):
        logger.info(': '+self.test_b_SeroTV_price_validation_BuyNow_TopButton.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        self.driver.find_element_by_xpath("(//p[@class='type-p2'])[2]").click()
        logger.info(": Navigate to Cart Total Page")
        time.sleep(5)
        SeroTV_price = self.driver.find_element_by_xpath("(//*[@class='os-price-value'])[4]")
        time.sleep(3)
        SeroTV_price_Text = SeroTV_price.text
        logger.info(": Identify Samsung Sero Tv Price: "+SeroTV_price_Text)
        self.driver.find_element_by_xpath("//*[@class='btn btn-remove']").click()
        logger.info(": Navigate back to Sero TV Landing Page")
        self.driver.back()
        time.sleep(3)
        self.driver.find_element_by_xpath("(//p[@class='type-p2'])[2]").click()
        time.sleep(5)
        logger.info(": Navigate to Sero TV Cart Page")
        self.assertIn(ReadConfig.read_w39_configData('SeroTVData', 'total_tv_price'), SeroTV_price_Text, msg="Samsung Sero Tv Price is not matching from samsung CART Total Page ")
        logger.info(": Successfully verified Samsung Sero Tv Total Price: " + ReadConfig.read_w39_configData('SeroTVData', 'total_tv_price'))
        time.sleep(5)
        try:
            Credittxt = self.driver.find_element_by_xpath("(//*[@class='cart-total-savings'])")
            time.sleep(5)
        except:
            Credittxt = self.driver.find_element_by_xpath("(//*[@class='os-price-value'])[5]")
            time.sleep(5)
        TotalPrice = Credittxt.text
        logger.info(": Identify TotalSaving price from samsung CART Total Page Text: "+TotalPrice)
        time.sleep(5)
        self.assertIn(ReadConfig.read_w39_configData('SeroTVData', 'saving_price'), TotalPrice, msg="Sero TV Total saving value is not matching in samsung Web Cart Page ")
        logger.info(": Successfully verified SeroTV Total saving from samsung CART Total Page is: " + ReadConfig.read_w39_configData('SeroTVData', 'saving_price'))
        logger.info('####  TEST Complete  ####')

    def test_c_SeroTV_price_validation_BuyNow_BelowButton(self):
        logger.info(': '+self.test_c_SeroTV_price_validation_BuyNow_BelowButton.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@class='cta-button product-details__info-add product-details__info-buyNow']").click()
        time.sleep(5)
        logger.info(": Navigate to Cart Total Page")
        SeroTV_price = self.driver.find_element_by_xpath("(//*[@class='os-price-value'])[4]")
        time.sleep(3)
        SeroTV_price_Text = SeroTV_price.text
        logger.info(": Identify Samsung Sero Tv Price: "+SeroTV_price_Text)
        self.driver.find_element_by_xpath("//*[@class='btn btn-remove']").click()
        self.driver.back()
        logger.info(": Navigate back to Sero TV Landing Page")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@class='cta-button product-details__info-add product-details__info-buyNow']").click()
        logger.info(": Navigate to Sero TV Cart Page")
        time.sleep(5)
        self.assertIn(ReadConfig.read_w39_configData('SeroTVData', 'total_tv_price'), SeroTV_price_Text, msg="Samsung Sero Tv Price is not matching from samsung CART Total Page ")
        logger.info(": Successfully verified Samsung Sero Tv Total Price: " + ReadConfig.read_w39_configData('SeroTVData', 'total_tv_price'))
        time.sleep(5)
        try:
            Credittxt = self.driver.find_element_by_xpath("(//*[@class='cart-total-savings'])")
            time.sleep(5)
        except:
            Credittxt = self.driver.find_element_by_xpath("(//*[@class='os-price-value'])[5]")
            time.sleep(5)
        TotalPrice = Credittxt.text
        logger.info(": Identify TotalSaving price from samsung CART Total Page Text: "+TotalPrice)
        time.sleep(5)
        self.assertIn(ReadConfig.read_w39_configData('SeroTVData', 'saving_price'), TotalPrice, msg="Sero TV Total saving value is not matching in samsung Web Cart Page ")
        logger.info(": Successfully verified SeroTV Total saving from samsung CART Total Page is: " + ReadConfig.read_w39_configData('SeroTVData', 'saving_price'))
        logger.info('####  TEST Complete  ####')


    # def test_d_SeroTV_Samsung_Credit_validation_inCart_Page(self):
    #     logger.info(': '+self.test_d_SeroTV_Samsung_Credit_validation_inCart_Page.__name__ + "\n #####  Starting TEST  ##### ")
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath("(//p[@class='type-p2'])[2]").click()
    #     logger.info(": Navigate to Cart Total Page")
    #     time.sleep(5)
    #     try:
    #         Credittxt = self.driver.find_element_by_xpath("(//*[@_target='_blank'])")
    #         time.sleep(3)
    #     except:
    #         Credittxt = self.driver.find_element_by_xpath("(//*[@class='ec-cart-prd-name'])[2]/span")
    #         time.sleep(3)
    #     SamsungCredit_Text = Credittxt.text
    #     logger.info(": Identify Samsung Gift Vaucher Text: "+SamsungCredit_Text)
    #     time.sleep(5)
    #     self.assertIn(ReadConfig.read_w39_configData('SeroTVData', 'Samsung_credit'), SamsungCredit_Text, msg="Samsung Instant Credit is not matching from samsung CART Total Page ")
    #     logger.info(": Successfully verified Samsung Instant Credit from Cart Total Page is: " + ReadConfig.read_w39_configData('SeroTVData', 'Samsung_credit'))
    #     logger.info('####  TEST Complete  ####')
    #
    # def test_e_SeroTV_Total_Saving_validation_inCart_Page(self):
    #     logger.info(': '+self.test_e_SeroTV_Total_Saving_validation_inCart_Page.__name__ + "\n #####  Starting TEST  ##### ")
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath("(//p[@class='type-p2'])[2]").click()
    #     logger.info(": Navigate to Cart Total Page")
    #     time.sleep(5)
    #     try:
    #         Credittxt = self.driver.find_element_by_xpath("(//*[@class='cart-total-savings'])")
    #         time.sleep(5)
    #     except:
    #         Credittxt = self.driver.find_element_by_xpath("(//*[@class='os-price-value'])[5]")
    #         time.sleep(5)
    #     TotalPrice = Credittxt.text
    #     logger.info(": Identify TotalSaving price from samsung CART Total Page Text: "+TotalPrice)
    #     time.sleep(5)
    #     self.assertIn(ReadConfig.read_w39_configData('SeroTVData', 'saving_price'), TotalPrice, msg="Sero TV Total saving value is not matching in samsung Web Cart Page ")
    #     logger.info(": Successfully verified SeroTV Total saving from samsung CART Total Page is: " + ReadConfig.read_w39_configData('SeroTVData', 'saving_price'))
    #     logger.info('####  TEST Complete  ####')


if __name__ == '__main__':
    unittest.main()


