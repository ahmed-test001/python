import time
import unittest
import sys
import os
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import warnings
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from PageClass.FooterLinkPage import FooterLinkPage
from Test_w_06_Palette_PO_Launch_T3.Page.CreativePage import CreativePage
from Utility_Files import ReadConfig
from Utility_Files.HTMLTestRunner import stdout_redirector
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class W_06_Palette_PO_Launch_T3_Page_Test(unittest.TestCase):

    url = ""
    driver = None
    url_list = []
    method_list_in_Url = []

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

    # def test_a1_EPP_or_NonEPP_verification(self):
    #     logger.info(': ' + self.test_a1_EPP_or_NonEPP_verification.__name__)
    #     ccpage = CreativePage(self.driver)
    #     ccpage.get_EPP_or_NonEPP_verification()

    def test_a2_SubjectLine_Text_Validation(self):
        logger.info(': ' + self.test_a2_SubjectLine_Text_Validation.__name__)
        ccpage=CreativePage(self.driver)
        ccpage.get_subjectLine_text_validation()

    def test_a3_pre_header_text_validation(self):
        logger.info(': ' + self.test_a3_pre_header_text_validation.__name__)
        ccpage=CreativePage(self.driver)
        ccpage.get_pre_header_text_validation()

    def test_a4_pre_header_link_validation(self):
        logger.info(': ' + self.test_a4_pre_header_link_validation.__name__)
        ccpage=CreativePage(self.driver)
        ccpage.get_pre_header_link_validation()

    def test_a5_hero_SH_validation(self):
        logger.info(': ' + self.test_a5_hero_SH_validation.__name__)
        ccpage=CreativePage(self.driver)
        ccpage.get_Hero_SH_Text_verification()

    def test_c1_Module1_link_verification(self):
        logger.info(': ' + self.test_c1_Module1_link_verification.__name__)
        ccpage=CreativePage(self.driver)
        ccpage.get_Module1_link_verification()

    def test_c2_Module1_KV_SC_verification(self):
        logger.info(': ' + self.test_c2_Module1_KV_SC_verification.__name__)
        ccpage=CreativePage(self.driver)
        ccpage.get_Module1_KV_SC_verification()

    def test_c3_Module2_link_verification(self):
        logger.info(': ' + self.test_c3_Module2_link_verification.__name__)
        ccpage=CreativePage(self.driver)
        ccpage.get_Module2_link_verification()

    def test_c4_Module3_link_Validation(self):
        logger.info(': ' + self.test_c4_Module3_link_Validation.__name__)
        ccpage=CreativePage(self.driver)
        ccpage.get_Module3_link_verification()

    def test_c5_Galaxy_Z_FLip_Module_link_Validation(self):
        logger.info(': ' + self.test_c5_Galaxy_Z_FLip_Module_link_Validation.__name__)
        ccpage=CreativePage(self.driver)
        ccpage.get_Galaxy_Z_FLip_Module_link_verification()

    def test_c6_Galaxy_Z_FLip_SC_Validation(self):
        logger.info(': ' + self.test_c6_Galaxy_Z_FLip_SC_Validation.__name__)
        ccpage=CreativePage(self.driver)
        ccpage.get_Galaxy_Z_FLip_Text_verification()

    def test_e1_ShopApp_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_e1_ShopApp_LandingPage_URL_validation.__name__)
        footerPage = FooterLinkPage(self.driver)
        footerPage.get_ShopApp_LandingPage_URL_validation()

    def test_i1_pay_later_icon_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_i1_pay_later_icon_LandingPage_URL_validation.__name__)
        footerPage=FooterLinkPage(self.driver)
        footerPage.get_pay_later_icon_LandingPage_URL_validation()

    def test_i2_free_shipping_icon_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_i2_free_shipping_icon_LandingPage_URL_validation.__name__)
        footerPage = FooterLinkPage(self.driver)
        footerPage.get_free_shipping_icon_LandingPage_URL_validation()

    def test_i3_Get_Rewarded_icon_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_i3_Get_Rewarded_icon_LandingPage_URL_validation.__name__)
        footerPage = FooterLinkPage(self.driver)
        footerPage.get_GetRewarded_icon_LandingPage_URL_validation()

    def test_j1_google_play_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_j1_google_play_button_LandingPage_URL_validation.__name__)
        footerPage = FooterLinkPage(self.driver)
        footerPage.get_google_play_button_LandingPage_URL_validation()

    def test_j2_apple_store_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_j2_apple_store_button_LandingPage_URL_validation.__name__)
        footerPage = FooterLinkPage(self.driver)
        footerPage.get_apple_store_button_LandingPage_URL_validation()

    def test_k1_free_shipping_details_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k1_free_shipping_details_button_LandingPage_URL_validation.__name__)
        footerPage = FooterLinkPage(self.driver)
        footerPage.get_free_shipping_details_button_LandingPage_URL_validation()

    def test_k2_Mobile_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k2_Mobile_button_LandingPage_URL_validation.__name__)
        footerPage = FooterLinkPage(self.driver)
        footerPage.get_Mobile_button_LandingPage_URL_validation()

    def test_k3_TV_Audio_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k3_TV_Audio_button_LandingPage_URL_validation.__name__)
        footerPage = FooterLinkPage(self.driver)
        footerPage.get_TV_Audio_button_LandingPage_URL_validation()

    def test_k4_computing_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k4_computing_button_LandingPage_URL_validation.__name__)
        footerPage = FooterLinkPage(self.driver)
        footerPage.get_computing_button_LandingPage_URL_validation()

    def test_k5_appliances_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k5_appliances_button_LandingPage_URL_validation.__name__ )
        footerPage = FooterLinkPage(self.driver)
        footerPage.get_appliances_button_LandingPage_URL_validation()

    def test_k6_weekly_offer_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k6_weekly_offer_button_LandingPage_URL_validation.__name__)
        footerPage = FooterLinkPage(self.driver)
        footerPage.get_weekly_offer_button_LandingPage_URL_validation()

    def test_l1_facebook_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_l1_facebook_button_LandingPage_URL_validation.__name__)
        footerPage = FooterLinkPage(self.driver)
        footerPage.get_facebook_button_LandingPage_URL_validation()

    def test_l2_instagram_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_l2_instagram_button_LandingPage_URL_validation.__name__)
        footerPage = FooterLinkPage(self.driver)
        footerPage.get_instagram_button_LandingPage_URL_validation()

    def test_l3_twitter_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_l3_twitter_button_LandingPage_URL_validation.__name__)
        footerPage = FooterLinkPage(self.driver)
        footerPage.get_twitter_button_LandingPage_URL_validation()

    def test_m1_ConditionText1_Validation(self):
        logger.info(': ' + self.test_m1_ConditionText1_Validation.__name__)
        ccpage=CreativePage(self.driver)
        ccpage.get_m1_Conditiontext1_validation()

    def test_m2_ConditionText2_Validation(self):
        logger.info(': ' + self.test_m2_ConditionText2_Validation.__name__)
        ccpage=CreativePage(self.driver)
        ccpage.get_m2_Conditiontext2_validation()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        logger.info(': \n#####  Test Complete  #####')


if __name__ == '__main__':
    unittest.main()
