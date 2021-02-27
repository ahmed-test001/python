import time
import unittest
import sys
import os
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import warnings
from PageClass.HomeAppliancePage import HomeAppliancePage
from PageClass.ImageTextExtract import ImageTextExtract
from PageClass.TabletPage import TabletPage
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from PageClass.TVHomeTheaterPage import TVHomeTheaterPage
from PageClass.MobileAccessoriesPage import MobileAccessoriesPage
from PageClass.ComputingPage import ComputingPage
from PageClass.FooterLinkPage import FooterLinkPage
from PageClass.SmartPhonePage import SmartPhonePage
from Test_w_53_NewYears_Holiday_Offers_Email.Page.CC_CreativePage import CC_CreativePage
from Utility_Files import ReadConfig
from Utility_Files.HTMLTestRunner import stdout_redirector
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class W_53_NewYear_Holiday_Offers_Email_Page_Test(unittest.TestCase):

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

    def test_a_SubjectLine_Text_Validation(self):
        logger.info(': ' + self.test_a_SubjectLine_Text_Validation.__name__)
        t1=ImageTextExtract(self.driver)
        t1.get_Text()

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
        ccpage = CC_CreativePage(self.driver)
        ccpage.get_EPP_or_NonEPP_verification()

    def test_a5_Top_Hero_link_verification(self):
        logger.info(': ' + self.test_a5_Top_Hero_link_verification.__name__)
        ccpage=CC_CreativePage(self.driver)
        ccpage.get_Top_Hero_link_validation()

    def test_b3_Module1_SubCopy_Text_Validation(self):
        logger.info(': ' + self.test_b3_Module1_SubCopy_Text_Validation.__name__)
        ddpage=CC_CreativePage(self.driver)
        ddpage.get_Module1_SubCopyText()

    def test_c3_Dynamic_ModuleLink_Validation(self):
        time.sleep(2)
        logger.info(': ' + self.test_c3_Dynamic_ModuleLink_Validation.__name__)
        # if "CC" in self.url:
        # ddpage = CC_CreativePage(self.driver)
        # ddpage.get_Module1_SubCopyText()
        MBpage = SmartPhonePage(self.driver)
        MBpage.get_A71_Mod()
        # ddpage.get_Module1_SubCopyText()
        MBpage.get_CPO_Mod()

        TVpage = TVHomeTheaterPage(self.driver)
        TVpage.get_Q50R_QLED_4kTV()
        TVpage.get_TU800_UHD_TV()

        mbWearpage = MobileAccessoriesPage(self.driver)
        mbWearpage.get_Buds_live()
        mbWearpage.get_Galaxy_watch3()

        Tabletpage = TabletPage(self.driver)
        Tabletpage.get_Tablet_Mod()

        CEpage = ComputingPage(self.driver)
        CEpage.get_SSD_Mod()

        HApage = HomeAppliancePage(self.driver)
        HApage.get_jetStick_Mod()
        time.sleep(5)

    def test_d1_Bottom_Hero_link_validation(self):
        logger.info(': ' + self.test_d1_Bottom_Hero_link_validation.__name__)
        ccpage=CC_CreativePage(self.driver)
        ccpage.get_Bottom_Hero_link_validation()

    def test_d2_Palette_Reserve_Banner_link_validation(self):
        logger.info(': ' + self.test_d2_Palette_Reserve_Banner_link_validation.__name__)
        ccpage=CC_CreativePage(self.driver)
        ccpage.get_Palette_Reserve_Banner_link_validation()

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
