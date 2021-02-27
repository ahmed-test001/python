import time
import unittest
import sys
import os
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import warnings
# sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from PageClass.FooterLinkPage_extra import FooterLinkPage_extra
from Test_w_06_TerraQ_Reserve_T2_extra.Page.CreativePage import CreativePage
from Utility_Files import ReadConfig
from Utility_Files.HTMLTestRunner import stdout_redirector
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class W_06_TerraQ_Reserve_T2_extra_Test(unittest.TestCase):

    url = ""
    driver = None
    url_list = []
    method_list_in_Url = []
    a=0
    @classmethod
    def setUpClass(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver'), options=option)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        warnings.filterwarnings("ignore")
        self.wait = WebDriverWait(self.driver, 10)
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            urls = f.read().splitlines()
            self.url = urls[0]
            self.driver.get(self.url)

    def readconfig_data(self,function_name):
        sheet_name = ReadConfig.readabcData(function_name, 'sheet_name')
        sheet_row = ReadConfig.readabcData(function_name, 'sheet_row')
        sheet_column = ReadConfig.readabcData(function_name, 'sheet_column')
        xpath_loc = ReadConfig.readabcData(function_name, 'xpath_loc')
        return sheet_name,sheet_row,sheet_column,xpath_loc

    # @unittest.skipUnless(ReadConfig.Data('get_CC_subjectLine_text_validation') ==ReadConfig.Data.emp )
    def test_a1_SubjectLine_Text_Validation(self):
        # logger.info(': ' + self.test_a1_SubjectLine_Text_Validation.__name__)
        # ccpage=CreativePage(self.driver)
        # data = self.readconfig_data("get_CC_subjectLine_text_validation")
        # # print("data:"+ data[0]+data[1]+data[2])
        # ccpage.get_CC_subjectLine_text_validation(data[0],data[1],data[2],data[3])
        print(sys.path.append(os.path.join(os.path.dirname(__file__), "..")))
        print(os.path.join(os.getcwd()))

    @unittest.skip(ReadConfig.Data('get_CC_pre_header_text_validation') == False)
    def test_a2_pre_header_text_validation(self):
        logger.info(': ' + self.test_a2_pre_header_text_validation.__name__)
        ccpage=CreativePage(self.driver)
        data = self.readconfig_data("get_CC_pre_header_text_validation")
        ccpage.get_CC_pre_header_text_validation(data[0],data[1],data[2],data[3])

    @unittest.skip(ReadConfig.Data('get_CC_pre_header_link_validation') == False)
    def test_a3_pre_header_link_validation(self):
        logger.info(': ' + self.test_a3_pre_header_link_validation.__name__)
        ccpage=CreativePage(self.driver)
        data = self.readconfig_data("get_CC_pre_header_link_validation")
        ccpage.get_CC_pre_header_link_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.Data('get_Hero_image_Text_validation') == "", "Condition not Matched.")
    # def test_a4_Hero_image_Text_verification(self):
    #     logger.info(': ' + self.test_a4_Hero_image_Text_verification.__name__)
    #     ccpage=CreativePage(self.driver)
    #     data = self.readconfig_data("get_Hero_image_Text_validation")
    #     ccpage.get_Hero_image_Text_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.Data('get_Hero_image_SC_Text_validation') == "", "Condition not Matched.")
    # def test_a5_Top_Hero_image_SC_text_verification(self):
    #     logger.info(': ' + self.test_a5_Top_Hero_image_SC_text_verification.__name__)
    #     ccpage=CreativePage(self.driver)
    #     data = self.readconfig_data("get_Hero_image_SC_Text_validation")
    #     ccpage.get_Hero_image_SC_Text_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.Data('get_Top_Hero_link_validation') == "", "Condition not Matched.")
    # def test_a6_Top_Hero_link_verification(self):
    #     logger.info(': ' + self.test_a6_Top_Hero_link_verification.__name__)
    #     ccpage=CreativePage(self.driver)
    #     data = self.readconfig_data("get_Top_Hero_link_validation")
    #     ccpage.get_Top_Hero_link_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.Data('get_Hero_SC_Text_validation') == "", "Condition not Matched.")
    # def test_a7_Top_Hero_SC_text_verification(self):
    #     logger.info(': ' + self.test_a7_Top_Hero_SC_text_verification.__name__)
    #     ccpage=CreativePage(self.driver)
    #     data = self.readconfig_data("get_Hero_SC_Text_validation")
    #     ccpage.get_Hero_SC_Text_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.Data('get_pay_later_icon_LandingPage_URL_validation') == "", "Condition not Matched.")
    # def test_i1_pay_later_icon_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_i1_pay_later_icon_LandingPage_URL_validation.__name__)
    #     footerPage=FooterLinkPage_extra(self.driver)
    #     data = self.readconfig_data("get_pay_later_icon_LandingPage_URL_validation")
    #     footerPage.get_pay_later_icon_LandingPage_URL_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.Data('get_free_shipping_icon_LandingPage_URL_validation') == "", "Condition not Matched.")
    # def test_i2_free_shipping_icon_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_i2_free_shipping_icon_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readconfig_data("get_free_shipping_icon_LandingPage_URL_validation")
    #     footerPage.get_free_shipping_icon_LandingPage_URL_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.Data('get_GetRewarded_icon_LandingPage_URL_validation') == "", "Condition not Matched.")
    # def test_i3_Get_Rewarded_icon_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_i3_Get_Rewarded_icon_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readconfig_data("get_GetRewarded_icon_LandingPage_URL_validation")
    #     footerPage.get_GetRewarded_icon_LandingPage_URL_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.Data('get_google_play_button_LandingPage_URL_validation') == "", "Condition not Matched.")
    # def test_j1_google_play_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_j1_google_play_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readconfig_data("get_google_play_button_LandingPage_URL_validation")
    #     footerPage.get_google_play_button_LandingPage_URL_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.Data('get_apple_store_button_LandingPage_URL_validation') == "", "Condition not Matched.")
    # def test_j2_apple_store_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_j2_apple_store_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readconfig_data("get_apple_store_button_LandingPage_URL_validation")
    #     footerPage.get_apple_store_button_LandingPage_URL_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.Data('get_free_shipping_details_button_LandingPage_URL_validation') == "", "Condition not Matched.")
    # def test_k1_free_shipping_details_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_k1_free_shipping_details_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readconfig_data("get_free_shipping_details_button_LandingPage_URL_validation")
    #     footerPage.get_free_shipping_details_button_LandingPage_URL_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.Data('get_Mobile_button_LandingPage_URL_validation') == "", "Condition not Matched.")
    # def test_k2_Mobile_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_k2_Mobile_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readconfig_data("get_Mobile_button_LandingPage_URL_validation")
    #     footerPage.get_Mobile_button_LandingPage_URL_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.Data('get_TV_Audio_button_LandingPage_URL_validation') == "", "Condition not Matched.")
    # def test_k3_TV_Audio_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_k3_TV_Audio_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readconfig_data("get_TV_Audio_button_LandingPage_URL_validation")
    #     footerPage.get_TV_Audio_button_LandingPage_URL_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.Data('get_computing_button_LandingPage_URL_validation') == "", "Condition not Matched.")
    # def test_k4_computing_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_k4_computing_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readconfig_data("get_computing_button_LandingPage_URL_validation")
    #     footerPage.get_computing_button_LandingPage_URL_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.Data('get_appliances_button_LandingPage_URL_validation') == "", "Condition not Matched.")
    # def test_k5_appliances_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_k5_appliances_button_LandingPage_URL_validation.__name__ )
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readconfig_data("get_appliances_button_LandingPage_URL_validation")
    #     footerPage.get_appliances_button_LandingPage_URL_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.Data('get_weekly_offer_button_LandingPage_URL_validation') == "", "Condition not Matched.")
    # def test_k6_weekly_offer_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_k6_weekly_offer_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readconfig_data("get_weekly_offer_button_LandingPage_URL_validation")
    #     footerPage.get_weekly_offer_button_LandingPage_URL_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.Data('get_facebook_button_LandingPage_URL_validation') == "", "Condition not Matched.")
    # def test_l1_facebook_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_l1_facebook_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readconfig_data("get_facebook_button_LandingPage_URL_validation")
    #     footerPage.get_facebook_button_LandingPage_URL_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.Data('get_instagram_button_LandingPage_URL_validation') == "", "Condition not Matched.")
    # def test_l2_instagram_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_l2_instagram_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readconfig_data("get_instagram_button_LandingPage_URL_validation")
    #     footerPage.get_instagram_button_LandingPage_URL_validation(data[0],data[1],data[2],data[3])

    @unittest.skip(ReadConfig.Data('get_twitter_button_LandingPage_URL_validation') == False)
    def test_l3_twitter_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_l3_twitter_button_LandingPage_URL_validation.__name__)
        footerPage = FooterLinkPage_extra(self.driver)
        data = self.readconfig_data("get_twitter_button_LandingPage_URL_validation")
        footerPage.get_twitter_button_LandingPage_URL_validation(data[0],data[1],data[2],data[3])

    @unittest.skip(ReadConfig.Data('get_CC_m1_Conditiontext1_validation') == False)
    def test_m1_ConditionText1_Validation(self):
        logger.info(': ' + self.test_m1_ConditionText1_Validation.__name__)
        ccpage=CreativePage(self.driver)
        data = self.readconfig_data("get_CC_m1_Conditiontext1_validation")
        ccpage.get_CC_m1_Conditiontext1_validation(data[0],data[1],data[2],data[3])

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        logger.info(': \n#####  Test Complete  #####')


if __name__ == '__main__':
    unittest.main()
