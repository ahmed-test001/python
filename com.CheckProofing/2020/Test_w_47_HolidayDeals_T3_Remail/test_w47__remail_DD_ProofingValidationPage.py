import time
import unittest
import sys
import os
import logging
import warnings
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Test_w_47_HolidayDeals_T3_Remail.Page.ComputingPage import ComputingPage
from Test_w_47_HolidayDeals_T3_Remail.Page.HomeAppliancePage import HomeAppliancePage
from Test_w_47_HolidayDeals_T3_Remail.Page.SmartPhonePage import SmartPhonePage
from Test_w_47_HolidayDeals_T3_Remail.Page.TVHomeTheaterPage import TVHomeTheaterPage
from Test_w_47_HolidayDeals_T3_Remail.Page.w47_remail_DD_CreativePage import W47_remail_DD_CreativePage
from Test_w_47_HolidayDeals_T3_Remail.Page.w47_remail_FooterLinkPage import W_47_remail_FooterLinkPage
from Utility_Files import ReadConfig
from Utility_Files.HTMLTestRunner import stdout_redirector
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class W_47_remail_DD_ProofingValidationPage_Test(unittest.TestCase):
    url_path = ""
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
        self.wait = WebDriverWait(self.driver, 10)
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            urls = f.read().splitlines()
            self.url=urls[0]
            self.driver.get(self.url)
            print("url: "+self.url)

    # def test_Text_verification(self):
    #     logger.info(': ' + self.test_Text_verification.__name__)
    #     if "DD" in self.url:
    #         ddpage=W47_DD_CreativePage(self.driver)
    #         ddpage.get_ModuleTextValidation()

    def test_a1_Top_Hero_verification(self):
        logger.info(': ' + self.test_a1_Top_Hero_verification.__name__)
        if "DD" in self.url:
            ddpage=W47_remail_DD_CreativePage(self.driver)
            ddpage.get_Top_Hero_link_validation()

    def test_a2_EPP_or_NonEPP_verification(self):
        logger.info(': ' + self.test_a2_EPP_or_NonEPP_verification.__name__)
        if "DD" in self.url:
            ddpage=W47_remail_DD_CreativePage(self.driver)
            ddpage.get_EPP_or_NonEPP_verification()

    def test_a3_SubjectLine_Text_Validation(self):
        logger.info(': ' + self.test_a3_SubjectLine_Text_Validation.__name__)
        if "DD" in self.url:
            ddpage=W47_remail_DD_CreativePage(self.driver)
            ddpage.get_DD_subjectLine_text_validation()

    def test_a4_pre_header_text_validation(self):
        logger.info(': ' + self.test_a4_pre_header_text_validation.__name__)
        if "DD" in self.url:
            ddpage=W47_remail_DD_CreativePage(self.driver)
            ddpage.get_DD_pre_header_text_validation()

    def test_a5_pre_header_link_validation(self):
        logger.info(': ' + self.test_a5_pre_header_link_validation.__name__)
        if "DD" in self.url:
            ddpage=W47_remail_DD_CreativePage(self.driver)
            ddpage.get_DD_pre_header_link_validation()

    def test_b1_Dynamic_Module_Validation(self):
        logger.info(': ' + self.test_b1_Dynamic_Module_Validation.__name__)
        time.sleep(4)

        if "DD" in self.url:
            if "TV" in self.url:
                if "QLED" in self.url:
                    tvPage=TVHomeTheaterPage(self.driver)
                    tvPage.get_TV_QLED_Module()
                elif "Accssry" in self.url:
                    tvPage = TVHomeTheaterPage(self.driver)
                    tvPage.get_TV_ACCESSORY_Module()

            elif "MB" in self.url:
                if "GALAXY" in self.url:
                    mbPage=SmartPhonePage(self.driver)
                    mbPage.get_MB_GALAXY_Module()
                elif "NOTE" in self.url:
                    mbPage = SmartPhonePage(self.driver)
                    mbPage.get_MB_NOTE_Module()
                elif "WEAR" in self.url:
                    mbPage = SmartPhonePage(self.driver)
                    mbPage.get_MB_WEAR_Module()
                elif "ACCESSORY" in self.url:
                    print(" NO Accessory Module selected.")

            elif "CE" in self.url:
                if "COMPUTER" in self.url:
                    cePage=ComputingPage(self.driver)
                    cePage.get_CE_COMPUTER_Module()

            elif "HA" in self.url:
                if "KITCHEN" in self.url:
                    HAPage=HomeAppliancePage(self.driver)
                    HAPage.get_HA_KITCHEN_Module()
                elif "LAUNDRY" in self.url:
                    HAPage = HomeAppliancePage(self.driver)
                    HAPage.get_HA_LAUNDRY_Module()
        time.sleep(5)

    def test_c1_giveWonder_link_validation(self):
        logger.info(': ' + self.test_c1_giveWonder_link_validation.__name__)
        if "DD" in self.url:
            ddpage=W47_remail_DD_CreativePage(self.driver)
            ddpage.get_giveWonder_link_validation()

    def test_i1_pay_later_icon_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_i1_pay_later_icon_LandingPage_URL_validation.__name__)
        footerPage=W_47_remail_FooterLinkPage(self.driver)
        footerPage.get_pay_later_icon_LandingPage_URL_validation()

    def test_i2_free_shipping_icon_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_i2_free_shipping_icon_LandingPage_URL_validation.__name__)
        footerPage = W_47_remail_FooterLinkPage(self.driver)
        footerPage.get_free_shipping_icon_LandingPage_URL_validation()

    def test_j1_google_play_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_j1_google_play_button_LandingPage_URL_validation.__name__)
        footerPage = W_47_remail_FooterLinkPage(self.driver)
        footerPage.get_google_play_button_LandingPage_URL_validation()

    def test_j2_apple_store_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_j2_apple_store_button_LandingPage_URL_validation.__name__)
        footerPage = W_47_remail_FooterLinkPage(self.driver)
        footerPage.get_apple_store_button_LandingPage_URL_validation()

    def test_k1_free_shipping_details_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k1_free_shipping_details_button_LandingPage_URL_validation.__name__)
        footerPage = W_47_remail_FooterLinkPage(self.driver)
        footerPage.get_free_shipping_details_button_LandingPage_URL_validation()

    def test_k2_Mobile_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k2_Mobile_button_LandingPage_URL_validation.__name__)
        footerPage = W_47_remail_FooterLinkPage(self.driver)
        footerPage.get_Mobile_button_LandingPage_URL_validation()

    def test_k3_TV_Audio_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k3_TV_Audio_button_LandingPage_URL_validation.__name__)
        footerPage = W_47_remail_FooterLinkPage(self.driver)
        footerPage.get_TV_Audio_button_LandingPage_URL_validation()

    def test_k4_computing_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k4_computing_button_LandingPage_URL_validation.__name__)
        footerPage = W_47_remail_FooterLinkPage(self.driver)
        footerPage.get_computing_button_LandingPage_URL_validation()

    def test_k5_appliances_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k5_appliances_button_LandingPage_URL_validation.__name__ )
        footerPage = W_47_remail_FooterLinkPage(self.driver)
        footerPage.get_appliances_button_LandingPage_URL_validation()

    def test_k6_weekly_offer_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k6_weekly_offer_button_LandingPage_URL_validation.__name__)
        footerPage = W_47_remail_FooterLinkPage(self.driver)
        footerPage.get_weekly_offer_button_LandingPage_URL_validation()

    def test_l1_facebook_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_l1_facebook_button_LandingPage_URL_validation.__name__)
        footerPage = W_47_remail_FooterLinkPage(self.driver)
        footerPage.get_facebook_button_LandingPage_URL_validation()

    def test_l2_instagram_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_l2_instagram_button_LandingPage_URL_validation.__name__)
        footerPage = W_47_remail_FooterLinkPage(self.driver)
        footerPage.get_instagram_button_LandingPage_URL_validation()

    def test_l3_twitter_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_l3_twitter_button_LandingPage_URL_validation.__name__)
        footerPage = W_47_remail_FooterLinkPage(self.driver)
        footerPage.get_twitter_button_LandingPage_URL_validation()


    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        logger.info(': \n#####  Test Complete  #####')


if __name__ == '__main__':
    unittest.main()
