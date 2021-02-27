import time
import unittest
import sys
import os
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import warnings
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from PageClass.TabletPage import TabletPage
from PageClass.ComputingPage import ComputingPage
from PageClass.FooterLinkPage import FooterLinkPage
from PageClass.HomeAppliancePage import HomeAppliancePage
from PageClass.MobileAccessoriesPage import MobileAccessoriesPage
from PageClass.SmartPhonePage import SmartPhonePage
from PageClass.TVHomeTheaterPage import TVHomeTheaterPage
from Test_w_49_CyberMonday_T1.Page.CC_CreativePage import CC_CreativePage
from Utility_Files import ReadConfig
from Utility_Files.HTMLTestRunner import stdout_redirector
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class W_49_CyberMonday_T1_ProofingValidationPage_Test(unittest.TestCase):

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
        warnings.filterwarnings("ignore")
        self.wait = WebDriverWait(self.driver, 10)
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            urls = f.read().splitlines()
            self.url=urls[0]
            self.driver.get(self.url)

    def test_a1_SubjectLine_Text_Validation(self):
        logger.info(': ' + self.test_a1_SubjectLine_Text_Validation.__name__)
        ccpage=CC_CreativePage(self.driver)
        ccpage.get_CC_subjectLine_text_validation()

    def test_a2_pre_header_text_validation(self):
        logger.info(': ' + self.test_a2_pre_header_text_validation.__name__)
        ccpage=CC_CreativePage(self.driver)
        ccpage.get_CC_pre_header_text_validation()

    def test_a3_pre_header_link_validation(self):
        logger.info(': ' + self.test_a3_pre_header_link_validation.__name__)
        ccpage=CC_CreativePage(self.driver)
        ccpage.get_CC_pre_header_link_validation()

    def test_a4_EPP_or_NonEPP_verification(self):
        logger.info(': ' + self.test_a4_EPP_or_NonEPP_verification.__name__)
        # if "CC" in self.url:
        ccpage = CC_CreativePage(self.driver)
        ccpage.get_EPP_or_NonEPP_verification()

    def test_a5_Top_Hero_link_verification(self):
        logger.info(': ' + self.test_a5_Top_Hero_link_verification.__name__)
        ccpage=CC_CreativePage(self.driver)
        ccpage.get_Top_Hero_link_validation2()

    # def test_b1_Module1_Header_Text_Validation(self):
    #     logger.info(': ' + self.test_b1_Module1_Header_Text_Validation.__name__)
    #     ddpage=CC_CreativePage(self.driver)
    #     ddpage.get_Module1_HeadLineText()

    # def test_b2_Module1_SubHeader_LineText_Validation(self):
    #     logger.info(': ' + self.test_b2_Module1_SubHeader_LineText_Validation.__name__)
    #     ddpage=CC_CreativePage(self.driver)
    #     ddpage.get_Module1_SubHeadLineText()
    #
    # def test_b3_Module1_SubCopy_Text_Validation(self):
    #     logger.info(': ' + self.test_b3_Module1_SubCopy_Text_Validation.__name__)
    #     ddpage=CC_CreativePage(self.driver)
    #     ddpage.get_Module1_SubCopyText()

    # def test_c1_Dynamic_Module_HeadLineText_Validation(self):
    #     logger.info(': ' + self.test_c1_Dynamic_Module_HeadLineText_Validation.__name__)
    #     if "CC" in self.url:
    #         ddpage = CC_CreativePage(self.driver)
    #         ddpage.get_CC_Dynamic_Module_HeadLineText()
    #     elif "DD" in self.url:
    #         ddpage = DD_CreativePage(self.driver)
    #         ddpage.get_DD_Dynamic_Module_HeadLineText()

    # def test_c2_Dynamic_Module_SubHead_LineText_Validation(self):
    #     logger.info(': ' + self.test_c2_Dynamic_Module_SubHead_LineText_Validation.__name__)
    #     if "CC" in self.url:
    #         logger.info(": No SubHead Line Text Present For CC version.")
    #     elif "DD" in self.url:
    #         ddpage = DD_CreativePage(self.driver)
    #         ddpage.get_DD_Dynamic_Module_SubHead_LineText()

    # def test_b2_Dynamic_Module_SubCopyText_Validation(self):
    #     logger.info(': ' + self.test_b2_Dynamic_Module_SubCopyText_Validation.__name__)
    #     # if "CC" in self.url:
    #     ddpage = CC_CreativePage(self.driver)
    #     ddpage.get_CC_Dynamic_Module_SubCopyText()

    def test_c3_Dynamic_ModuleLink_Validation(self):
        logger.info(': ' + self.test_c3_Dynamic_ModuleLink_Validation.__name__)

        if "CC" in self.url:
            if "TV" in self.url:
                tvpage = TVHomeTheaterPage(self.driver)
                tvpage.get_TV_HomeTheaterModule1()

                mbpage = SmartPhonePage(self.driver)
                mbpage.get_SmartPhoneModule2()

                mbwearpage = TabletPage(self.driver)
                mbwearpage.get_TABLET_Module3()

                mbwearpage = MobileAccessoriesPage(self.driver)
                mbwearpage.get_MobileAccessories_Module4()

                cepage = ComputingPage(self.driver)
                cepage.get_Computing_Module5()

                HApage = HomeAppliancePage(self.driver)
                HApage.get_HomeAppliance_Module6()

            elif "MB" in self.url:
                if "GALAXY" in self.url:
                    mbpage = SmartPhonePage(self.driver)
                    mbpage.get_SmartPhoneModule1()

                    tvpage = TVHomeTheaterPage(self.driver)
                    tvpage.get_TV_HomeTheaterModule2()

                    mbwearpage = TabletPage(self.driver)
                    mbwearpage.get_TABLET_Module3()

                    mbwearpage = MobileAccessoriesPage(self.driver)
                    mbwearpage.get_MobileAccessories_Module4()

                    cepage = ComputingPage(self.driver)
                    cepage.get_Computing_Module5()

                    HApage = HomeAppliancePage(self.driver)
                    HApage.get_HomeAppliance_Module6()

                if "NOTE" in self.url:
                    mbpage = SmartPhonePage(self.driver)
                    mbpage.get_SmartPhoneModule1()

                    tvpage = TVHomeTheaterPage(self.driver)
                    tvpage.get_TV_HomeTheaterModule2()

                    mbwearpage = TabletPage(self.driver)
                    mbwearpage.get_TABLET_Module3()

                    mbwearpage = MobileAccessoriesPage(self.driver)
                    mbwearpage.get_MobileAccessories_Module4()

                    cepage = ComputingPage(self.driver)
                    cepage.get_Computing_Module5()

                    HApage = HomeAppliancePage(self.driver)
                    HApage.get_HomeAppliance_Module6()

                elif "WEAR" in self.url:
                    mbwearpage = MobileAccessoriesPage(self.driver)
                    mbwearpage.get_MobileAccessories_Module1()

                    mbpage = SmartPhonePage(self.driver)
                    mbpage.get_SmartPhoneModule2()

                    tvpage = TVHomeTheaterPage(self.driver)
                    tvpage.get_TV_HomeTheaterModule3()

                    mbwearpage = TabletPage(self.driver)
                    mbwearpage.get_TABLET_Module4()

                    cepage = ComputingPage(self.driver)
                    cepage.get_Computing_Module5()

                    HApage = HomeAppliancePage(self.driver)
                    HApage.get_HomeAppliance_Module6()
                elif "TABLET" in self.url:
                    mbwearpage = TabletPage(self.driver)
                    mbwearpage.get_TABLET_Module1()

                    mbpage = SmartPhonePage(self.driver)
                    mbpage.get_SmartPhoneModule2()

                    tvpage = TVHomeTheaterPage(self.driver)
                    tvpage.get_TV_HomeTheaterModule3()

                    mbwearpage = MobileAccessoriesPage(self.driver)
                    mbwearpage.get_MobileAccessories_Module4()

                    cepage = ComputingPage(self.driver)
                    cepage.get_Computing_Module5()

                    HApage = HomeAppliancePage(self.driver)
                    HApage.get_HomeAppliance_Module6()

            elif "CE" in self.url:
                    cepage = ComputingPage(self.driver)
                    cepage.get_Computing_Module1()

                    mbpage = SmartPhonePage(self.driver)
                    mbpage.get_SmartPhoneModule2()

                    tvpage = TVHomeTheaterPage(self.driver)
                    tvpage.get_TV_HomeTheaterModule3()

                    mbwearpage = TabletPage(self.driver)
                    mbwearpage.get_TABLET_Module4()

                    mbwearpage = MobileAccessoriesPage(self.driver)
                    mbwearpage.get_MobileAccessories_Module5()

                    HApage = HomeAppliancePage(self.driver)
                    HApage.get_HomeAppliance_Module6()

            elif "HA" in self.url:
                    HApage = HomeAppliancePage(self.driver)
                    HApage.get_HomeAppliance_Module1()

                    mbpage = SmartPhonePage(self.driver)
                    mbpage.get_SmartPhoneModule2()

                    tvpage = TVHomeTheaterPage(self.driver)
                    tvpage.get_TV_HomeTheaterModule3()

                    mbwearpage = TabletPage(self.driver)
                    mbwearpage.get_TABLET_Module4()

                    mbwearpage = MobileAccessoriesPage(self.driver)
                    mbwearpage.get_MobileAccessories_Module5()

                    cepage = ComputingPage(self.driver)
                    cepage.get_Computing_Module6()

        elif "DD" in self.url:
            if "MB" in self.url:
                mbPage = SmartPhonePage(self.driver)
                mbPage.get_MB_NOTE1_Module_BlackFriday()
                mbPage.get_MB_NOTE2_Module_BlackFriday()
                mbPage.get_MB_NOTE3_Module_BlackFriday()
                mbPage.get_MB_NOTE4_Module_BlackFriday()

        if "ALL" in self.url:
                if "OTHER" in self.url:
                    mbpage = SmartPhonePage(self.driver)
                    mbpage.get_SmartPhoneModule1()

                    tvpage = TVHomeTheaterPage(self.driver)
                    tvpage.get_TV_HomeTheaterModule2()

                    mbwearpage = TabletPage(self.driver)
                    mbwearpage.get_TABLET_Module3()

                    mbwearpage = MobileAccessoriesPage(self.driver)
                    mbwearpage.get_MobileAccessories_Module4()

                    cepage = ComputingPage(self.driver)
                    cepage.get_Computing_Module5()

                    HApage = HomeAppliancePage(self.driver)
                    HApage.get_HomeAppliance_Module6()

        time.sleep(5)

    def test_d1_giveWonder_link_validation(self):
        logger.info(': ' + self.test_d1_giveWonder_link_validation.__name__)
        ccpage=CC_CreativePage(self.driver)
        ccpage.get_giveWonder_link_validation2()

    def test_i1_pay_later_icon_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_i1_pay_later_icon_LandingPage_URL_validation.__name__)
        footerPage=FooterLinkPage(self.driver)
        footerPage.get_pay_later_icon_LandingPage_URL_validation()

    def test_i2_free_shipping_icon_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_i2_free_shipping_icon_LandingPage_URL_validation.__name__)
        footerPage = FooterLinkPage(self.driver)
        footerPage.get_free_shipping_icon_LandingPage_URL_validation()

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


    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        logger.info(': \n#####  Test Complete  #####')


if __name__ == '__main__':
    unittest.main()
