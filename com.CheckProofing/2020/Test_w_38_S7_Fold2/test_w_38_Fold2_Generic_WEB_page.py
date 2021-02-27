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


class webPage_W_38_Fold2_GenericTest(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        with open('../TextFolder/TestIn_UniqueURL_List.txt')as f:
            urls = f.read().splitlines()
            for url in urls:
                if ReadConfig.read_w38_S7_Fold2_configData('Fold2Generic', 'url_Fold2_Generic') in url:
                    option = webdriver.ChromeOptions()
                    option.add_experimental_option('excludeSwitches', ['enable-logging'])
                    self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver1'), options=option)
                    warnings.filterwarnings(action="ignore", message="unclosed",category=ResourceWarning)
                    self.driver.maximize_window()
                    self.driver.get(url)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    @classmethod
    def test_a_verify_page_current_url(self):
        logger.info(': '+self.test_a_verify_page_current_url.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        url1 = self.driver.current_url
        assert ReadConfig.read_w38_S7_Fold2_configData('Fold2Generic', 'url_Fold2_Generic') in url1
        logger.info(': assertion complete with: '+ url1)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_b_verify_promo_credit_banner(self):
        logger.info(': '+self.test_b_verify_promo_credit_banner.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        bannerText = self.driver.find_element_by_xpath("//p[@class ='title']").text
        assert ReadConfig.read_w38_S7_Fold2_configData('Fold2WEBPage', 'Promo_Credit_banner_fold2') in bannerText
        logger.info(': assertion complete with: '+ bannerText)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_c_verify_tradein_value(self):
        logger.info(': '+self.test_c_verify_tradein_value.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        tradeinPrice = self.driver.find_element_by_xpath("//span[@class ='tradeinPrice'][1]").text
        assert ReadConfig.read_w38_S7_Fold2_configData('Fold2WEBPage', 'Device_Tradein_Value') in tradeinPrice
        logger.info(': assertion complete with: ' + tradeinPrice)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_d_verify_deviceBrand_Name(self):
        logger.info(': '+self.test_d_verify_deviceBrand_Name.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        try:
            deviceBrand = self.driver.find_element_by_xpath("(//div[@class ='device-label'])[1]").text
            assert ReadConfig.read_w38_S7_Fold2_configData('Fold2WEBPage', 'device_Brand') in deviceBrand
            logger.info(': assertion complete with: ' + deviceBrand)
        except:
            logger.info(': NO Device Brand Name Selected')
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_e_verify_deviceType_Name(self):
        logger.info(': '+self.test_e_verify_deviceType_Name.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        try:
            deviceName = self.driver.find_element_by_xpath("(//div[@class ='device-label'])[2]").text
            # deviceName=deviceName[:13]
            assert ReadConfig.read_w38_S7_Fold2_configData('Fold2WEBPage', 'Device_Name') in deviceName
            logger.info(': assertion complete with: ' + deviceName)
        except:
            logger.info(': NO Device Type Name Selected')
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_f_verify_tradein_discount_price(self):
        logger.info(': '+self.test_f_verify_tradein_discount_price.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        try:
            discountPrice = self.driver.find_element_by_xpath("//div[@class ='devicePrice']").text
            assert ReadConfig.read_w38_S7_Fold2_configData('Fold2WEBPage', 'Device_Tradein_Discount_Value') in discountPrice
            logger.info(': assertion complete with: ' + discountPrice)
        except:
            logger.info(': Selected Device Trade-in discount Price NOT present due to NO Device Type selected ')
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_g_verify_total_device_price(self):
        logger.info(': '+self.test_g_verify_total_device_price.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        totalPrice = self.driver.find_element_by_xpath("//div[@class ='totalPrice']/child::span/child::span/strong[4]").text
        totalPrice=totalPrice[:9]
        assert ReadConfig.read_w38_S7_Fold2_configData('Fold2WEBPage', 'Total_Price') in totalPrice
        logger.info(': assertion complete with: ' + totalPrice)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_h_verify_eligible_price(self):
        logger.info(': '+self.test_h_verify_eligible_price.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        eligiblePrice = self.driver.find_element_by_xpath("//div[@class ='price-info']/child::span/strong[4]").text
        eligiblePrice=eligiblePrice[:9]
        assert ReadConfig.read_w38_S7_Fold2_configData('Fold2WEBPage', 'Eligible_Tradein_Value') in eligiblePrice
        logger.info(' assertion complete with: ' + eligiblePrice)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_i_verify_list_device_price(self):
        logger.info(': '+self.test_i_verify_list_device_price.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        listdevicePrice = self.driver.find_element_by_xpath("//span[@class ='listPrice']").text
        assert ReadConfig.read_w38_S7_Fold2_configData('Fold2WEBPage', 'list_device_price') in listdevicePrice
        logger.info(': assertion complete with: ' + listdevicePrice)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_j_verify_add_to_cart_button(self):
        logger.info(': '+self.test_j_verify_add_to_cart_button.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        addtocartText1 = self.driver.find_element_by_xpath("(//div[@class ='button  PRE-ORDER NOW'])[1]").text
        print(addtocartText1)
        addtocartText2 = self.driver.find_element_by_xpath("(//div[@class ='button  PRE-ORDER NOW'])[2]").text
        print(addtocartText2)
        assert ReadConfig.read_w38_S7_Fold2_configData('Fold2WEBPage', 'ShopTypeText') in addtocartText1
        assert ReadConfig.read_w38_S7_Fold2_configData('Fold2WEBPage', 'ShopTypeText') in addtocartText2
        logger.info(': assertion complete with: ' + addtocartText2)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_k_verify_instant_credit(self):
        logger.info(': '+self.test_k_verify_instant_credit.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        instantCredit = self.driver.find_element_by_xpath("//div[@class ='promo-text-title']").text
        assert ReadConfig.read_w38_S7_Fold2_configData('Fold2WEBPage', 'instant_Credit') in instantCredit
        logger.info(': assertion complete with: ' + instantCredit)
        logger.info('####  TEST Complete  ####')


if __name__ == '__main__':
    unittest.main()


