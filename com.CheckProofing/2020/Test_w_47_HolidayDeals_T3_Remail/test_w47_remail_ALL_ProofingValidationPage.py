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
from Test_w_47_HolidayDeals_T3_Remail.Page.MobileAccessoriesPage import MobileAccessoriesPage
from Test_w_47_HolidayDeals_T3_Remail.Page.SmartPhonePage import SmartPhonePage
from Test_w_47_HolidayDeals_T3_Remail.Page.TVHomeTheaterPage import TVHomeTheaterPage
from Test_w_47_HolidayDeals_T3_Remail.Page.w47_remail_CC_CreativePage import W47_remail_CC_CreativePage
from Test_w_47_HolidayDeals_T3_Remail.Page.w47_remail_FooterLinkPage import W_47_remail_FooterLinkPage
from Utility_Files import ReadConfig
from Utility_Files.HTMLTestRunner import stdout_redirector
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class W_47_remail_ALL_ProofingValidationPage_Test(unittest.TestCase):

    url=""
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

    def test_a1_Top_Hero_verification(self):
        logger.info(': ' + self.test_a1_Top_Hero_verification.__name__)
        if "All" in self.url:
            ccpage=W47_remail_CC_CreativePage(self.driver)
            ccpage.get_Top_Hero_link_validation()

    def test_a2_EPP_or_NonEPP_verification(self):
        logger.info(': ' + self.test_a2_EPP_or_NonEPP_verification.__name__)
        if "All" in self.url:
            ccpage=W47_remail_CC_CreativePage(self.driver)
            ccpage.get_EPP_or_NonEPP_verification()

    def test_a3_SubjectLine_Text_Validation(self):
        logger.info(': ' + self.test_a3_SubjectLine_Text_Validation.__name__)
        if "All" in self.url:
            ccpage=W47_remail_CC_CreativePage(self.driver)
            ccpage.get_CC_subjectLine_text_validation()

    def test_a4_pre_header_text_validation(self):
        logger.info(': ' + self.test_a4_pre_header_text_validation.__name__)
        if "All" in self.url:
            ccpage=W47_remail_CC_CreativePage(self.driver)
            ccpage.get_CC_pre_header_text_validation()

    def test_a5_pre_header_link_validation(self):
        logger.info(': ' + self.test_a5_pre_header_link_validation.__name__)
        if "All" in self.url:
            ccpage=W47_remail_CC_CreativePage(self.driver)
            ccpage.get_CC_pre_header_link_validation()

    def test_b1_Dynamic_Module_Validation(self):
        logger.info(': ' + self.test_b1_Dynamic_Module_Validation.__name__)

        if "All" in self.url:
            if "OTHER" in self.url:
                mbpage = SmartPhonePage(self.driver)
                mbpage.get_SMARTPHONE_ShopAll()
                mbpage.get_SmartPhoneModule()

                tvpage = TVHomeTheaterPage(self.driver)
                tvpage.get_TVHomeTheater_ShopAll()
                tvpage.get_TV_HomeTheaterModule()

                mbwearpage = MobileAccessoriesPage(self.driver)
                mbwearpage.get_MobileAccessories_ShopAll()
                mbwearpage.get_MobileAccessories_Module()

                cepage = ComputingPage(self.driver)
                cepage.get_Computing_ShopAll()
                cepage.get_Computing_Module()

                HApage = HomeAppliancePage(self.driver)
                HApage.get_HomeAppliance_ShopAll()
                HApage.get_HomeAppliance_Module()

            # if "TV" in self.url:
            #     if "QLED" in self.url:
            #         tvpage = TVHomeTheaterPage(self.driver)
            #         tvpage.get_TVHomeTheater_ShopAll()
            #         tvpage.get_TV_HomeTheaterModule()
            #
            #         mbpage = SmartPhonePage(self.driver)
            #         mbpage.get_SMARTPHONE_ShopAll()
            #         mbpage.get_SmartPhoneModule()
            #
            #         mbwearpage = MobileAccessoriesPage(self.driver)
            #         mbwearpage.get_MobileAccessories_ShopAll()
            #         mbwearpage.get_MobileAccessories_Module()
            #
            #         cepage = ComputingPage(self.driver)
            #         cepage.get_Computing_ShopAll()
            #         cepage.get_Computing_Module()
            #
            #         HApage = HomeAppliancePage(self.driver)
            #         HApage.get_HomeAppliance_ShopAll()
            #         HApage.get_HomeAppliance_Module()
            #
            #     elif "ACCESSORY" in self.url:
            #         tvpage = TVHomeTheaterPage(self.driver)
            #         tvpage.get_TVHomeTheater_ShopAll()
            #         tvpage.get_TV_HomeTheaterModule()
            #
            #         mbpage = SmartPhonePage(self.driver)
            #         mbpage.get_SMARTPHONE_ShopAll()
            #         mbpage.get_SmartPhoneModule()
            #
            #         mbwearpage = MobileAccessoriesPage(self.driver)
            #         mbwearpage.get_MobileAccessories_ShopAll()
            #         mbwearpage.get_MobileAccessories_Module()
            #
            #         cepage = ComputingPage(self.driver)
            #         cepage.get_Computing_ShopAll()
            #         cepage.get_Computing_Module()
            #
            #         HApage = HomeAppliancePage(self.driver)
            #         HApage.get_HomeAppliance_ShopAll()
            #         HApage.get_HomeAppliance_Module()
            #
            # elif "MB" in self.url:
            #     # if "NOTE" or "GALAXY" in self.url:
            #     if "NOTE" in self.url:
            #         mbpage = SmartPhonePage(self.driver)
            #         mbpage.get_SMARTPHONE_ShopAll()
            #         mbpage.get_SmartPhoneModule()
            #
            #         tvpage = TVHomeTheaterPage(self.driver)
            #         tvpage.get_TVHomeTheater_ShopAll()
            #         tvpage.get_TV_HomeTheaterModule()
            #
            #         mbwearpage = MobileAccessoriesPage(self.driver)
            #         mbwearpage.get_MobileAccessories_ShopAll()
            #         mbwearpage.get_MobileAccessories_Module()
            #
            #         cepage = ComputingPage(self.driver)
            #         cepage.get_Computing_ShopAll()
            #         cepage.get_Computing_Module()
            #
            #         HApage = HomeAppliancePage(self.driver)
            #         HApage.get_HomeAppliance_ShopAll()
            #         HApage.get_HomeAppliance_Module()
            #
            #     elif "GALAXY" in self.url:
            #         mbpage = SmartPhonePage(self.driver)
            #         mbpage.get_SMARTPHONE_ShopAll()
            #         mbpage.get_SmartPhoneModule()
            #
            #         tvpage = TVHomeTheaterPage(self.driver)
            #         tvpage.get_TVHomeTheater_ShopAll()
            #         tvpage.get_TV_HomeTheaterModule()
            #
            #         mbwearpage = MobileAccessoriesPage(self.driver)
            #         mbwearpage.get_MobileAccessories_ShopAll()
            #         mbwearpage.get_MobileAccessories_Module()
            #
            #         cepage = ComputingPage(self.driver)
            #         cepage.get_Computing_ShopAll()
            #         cepage.get_Computing_Module()
            #
            #         HApage = HomeAppliancePage(self.driver)
            #         HApage.get_HomeAppliance_ShopAll()
            #         HApage.get_HomeAppliance_Module()
            #
            #     # elif "WEAR" or "TABLET" in self.url:
            #     elif "TABLET" in self.url:
            #         mbwearpage = MobileAccessoriesPage(self.driver)
            #         mbwearpage.get_MobileAccessories_ShopAll()
            #         mbwearpage.get_MobileAccessories_Module()
            #
            #         mbpage = SmartPhonePage(self.driver)
            #         mbpage.get_SMARTPHONE_ShopAll()
            #         mbpage.get_SmartPhoneModule()
            #
            #         tvpage = TVHomeTheaterPage(self.driver)
            #         tvpage.get_TVHomeTheater_ShopAll()
            #         tvpage.get_TV_HomeTheaterModule()
            #
            #         cepage = ComputingPage(self.driver)
            #         cepage.get_Computing_ShopAll()
            #         cepage.get_Computing_Module()
            #
            #         HApage = HomeAppliancePage(self.driver)
            #         HApage.get_HomeAppliance_ShopAll()
            #         HApage.get_HomeAppliance_Module()
            #
            #     elif "WEAR" in self.url:
            #         mbwearpage = MobileAccessoriesPage(self.driver)
            #         mbwearpage.get_MobileAccessories_ShopAll()
            #         mbwearpage.get_MobileAccessories_Module()
            #
            #         mbpage = SmartPhonePage(self.driver)
            #         mbpage.get_SMARTPHONE_ShopAll()
            #         mbpage.get_SmartPhoneModule()
            #
            #         tvpage = TVHomeTheaterPage(self.driver)
            #         tvpage.get_TVHomeTheater_ShopAll()
            #         tvpage.get_TV_HomeTheaterModule()
            #
            #         cepage = ComputingPage(self.driver)
            #         cepage.get_Computing_ShopAll()
            #         cepage.get_Computing_Module()
            #
            #         HApage = HomeAppliancePage(self.driver)
            #         HApage.get_HomeAppliance_ShopAll()
            #         HApage.get_HomeAppliance_Module()
            #
            # elif "CE" in self.url:
            #     if "COMPUTER" in self.url:
            #         cepage = ComputingPage(self.driver)
            #         cepage.get_Computing_ShopAll()
            #         cepage.get_Computing_Module()
            #
            #         mbpage = SmartPhonePage(self.driver)
            #         mbpage.get_SMARTPHONE_ShopAll()
            #         mbpage.get_SmartPhoneModule()
            #
            #         tvpage = TVHomeTheaterPage(self.driver)
            #         tvpage.get_TVHomeTheater_ShopAll()
            #         tvpage.get_TV_HomeTheaterModule()
            #
            #         mbpage = SmartPhonePage(self.driver)
            #         mbpage.get_SMARTPHONE_ShopAll()
            #         mbpage.get_SmartPhoneModule()
            #
            #         HApage = HomeAppliancePage(self.driver)
            #         HApage.get_HomeAppliance_ShopAll()
            #         HApage.get_HomeAppliance_Module()
            #
            # elif "HA" in self.url:
            #     if "HA" in self.url:
            #         HApage = HomeAppliancePage(self.driver)
            #         HApage.get_HomeAppliance_ShopAll()
            #         HApage.get_HomeAppliance_Module()
            #
            #         mbpage = SmartPhonePage(self.driver)
            #         mbpage.get_SMARTPHONE_ShopAll()
            #         mbpage.get_SmartPhoneModule()
            #
            #         tvpage = TVHomeTheaterPage(self.driver)
            #         tvpage.get_TVHomeTheater_ShopAll()
            #         tvpage.get_TV_HomeTheaterModule()
            #
            #         mbwearpage = MobileAccessoriesPage(self.driver)
            #         mbwearpage.get_MobileAccessories_ShopAll()
            #         mbwearpage.get_MobileAccessories_Module()
            #
            #         cepage = ComputingPage(self.driver)
            #         cepage.get_Computing_ShopAll()
            #         cepage.get_Computing_Module()
            else:
                print("NONE All option got selected.")
        time.sleep(5)

    def test_c1_giveWonder_link_validation(self):
        logger.info(': ' + self.test_c1_giveWonder_link_validation.__name__)
        if "All" in self.url:
            ccpage=W47_remail_CC_CreativePage(self.driver)
            ccpage.get_giveWonder_link_validation()

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
