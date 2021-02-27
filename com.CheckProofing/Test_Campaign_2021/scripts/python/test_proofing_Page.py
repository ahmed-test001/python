import unittest
import sys
import os
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import warnings



sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
os.path.join(os.getcwd())
from Test_Campaign_2021.scripts.python.Page.CopyTextPage import CopyTextPage
from Test_Campaign_2021.scripts.python.Page.FooterLinkPage_extra import FooterLinkPage_extra
from Test_Campaign_2021.scripts.python.Page.ModuleURLPage import ModuleURLPage
from Test_Campaign_2021.scripts.python.Page.TermsConditionPage import TermsConditionPage
from Test_Campaign_2021.scripts.python.Util_Data import ReadConfig
from Test_Campaign_2021.scripts.python.Util_Data.HTMLTestRunner import stdout_redirector

logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class Proofing_Page_Test(unittest.TestCase):
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
        with open(ReadConfig.readFilePathData('FilePaths', 'url_list'))as f:
            urls = f.read().splitlines()
            self.url = urls[0]
            self.driver.get(self.url)

    def readTermsConfig_data(self,function_name):
        sheet_name = ReadConfig.readTermsConditionData(function_name, 'sheet_name')
        sheet_row1 = ReadConfig.readTermsConditionData(function_name, 'sheet_row1')
        sheet_row_NR = ReadConfig.readTermsConditionData(function_name, 'sheet_row_NR')
        sheet_column1 = ReadConfig.readTermsConditionData(function_name, 'sheet_column1')
        sheet_column_NR = ReadConfig.readTermsConditionData(function_name, 'sheet_column_NR')
        xpath_loc = ReadConfig.readTermsConditionData(function_name, 'xpath_loc')
        return sheet_name,sheet_row1,sheet_row_NR,sheet_column1,sheet_column_NR,xpath_loc

    def readFooter_data(self,function_name):
        sheet_name = ReadConfig.readfooterData(function_name, 'sheet_name')
        sheet_row = ReadConfig.readfooterData(function_name, 'sheet_row')
        sheet_column = ReadConfig.readfooterData(function_name, 'sheet_column')
        xpath_loc = ReadConfig.readfooterData(function_name, 'xpath_loc')
        return sheet_name,sheet_row,sheet_column,xpath_loc

    def readModuleURL_data(self,function_name):
        sheet_name = ReadConfig.readModuleURLData(function_name, 'sheet_name')
        sheet_row = ReadConfig.readModuleURLData(function_name, 'sheet_row')
        sheet_column = ReadConfig.readModuleURLData(function_name, 'sheet_column')
        xpath_loc = ReadConfig.readModuleURLData(function_name, 'xpath_loc')
        return sheet_name,sheet_row,sheet_column,xpath_loc

    # def test_a1_SubjectLine_Text_Validation(self):
    #     logger.info(': ' + self.test_a1_SubjectLine_Text_Validation.__name__)
    #     ccpage=CopyTextPage(self.driver)
    #     ccpage.get_CC_subjectLine_text_validation()
    #
    # def test_a2_pre_header_text_validation(self):
    #     logger.info(': ' + self.test_a2_pre_header_text_validation.__name__)
    #     ccpage=CopyTextPage(self.driver)
    #     ccpage.get_CC_pre_header_text_validation()

    # @unittest.skipUnless(ReadConfig.readModuleURLData("get_pre_header_link_validation", 'sheet_row') != "",'Skip test case.')
    # def test_a1_pre_header_link_validation(self):
    #     logger.info(': ' + self.test_a1_pre_header_link_validation.__name__)
    #     Mpage=ModuleURLPage(self.driver)
    #     data = self.readModuleURL_data("get_pre_header_link_validation")
    #     Mpage.get_pre_header_link_validation(data[0], data[1], data[2], data[3])
    #
    # print(sys.path.append(os.path.join(os.path.dirname(__file__), "..")))
    # print(os.path.join(os.getcwd()))
    @unittest.skipUnless(ReadConfig.checkSectionModuleExistance("get_Top_Hero_CTA_validation"), 'Skip test case.')
    def test_a2_Top_Hero_CTA_verification(self):
        logger.info(': ' + self.test_a2_Top_Hero_CTA_verification.__name__)
        Mpage=ModuleURLPage(self.driver)
        data = self.readModuleURL_data("get_Top_Hero_CTA_validation")
        Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    #
    # # def test_a3_Module1_Banner_link_verification(self):
    # #     logger.info(': ' + self.test_a3_Module1_Banner_link_verification.__name__)
    # #     Mpage=ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module1_Banner_link_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    #
    # # def test_a4_Module1_CTA_link_verification(self):
    # #     logger.info(': ' + self.test_a4_Module1_CTA_link_verification.__name__)
    # #     Mpage=ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module1_CTA_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_a5_Module1_mini_CTA1_link_verification(self):
    # #     logger.info(': ' + self.test_a5_Module1_mini_CTA1_link_verification.__name__)
    # #     Mpage=ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module1_mini_CTA1_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_a6_Module1_mini_CTA2_link_verification(self):
    # #     logger.info(': ' + self.test_a6_Module1_mini_CTA2_link_verification.__name__)
    # #     Mpage=ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module1_mini_CTA2_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_a7_Module1_mini_CTA3_link_verification(self):
    # #     logger.info(': ' + self.test_a7_Module1_mini_CTA3_link_verification.__name__)
    # #     Mpage=ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module1_mini_CTA3_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_b1_Module2_Banner_link_verification(self):
    # #     logger.info(': ' + self.test_b1_Module2_Banner_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module2_Banner_link_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_b2_Module2_CTA_link_verification(self):
    # #     logger.info(': ' + self.test_b2_Module2_CTA_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module2_CTA_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_b3_Module2_mini_CTA1_link_verification(self):
    # #     logger.info(': ' + self.test_b3_Module2_mini_CTA1_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module2_mini_CTA1_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_b4_Module2_mini_CTA2_link_verification(self):
    # #     logger.info(': ' + self.test_b4_Module2_mini_CTA2_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module2_mini_CTA2_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_b5_Module2_mini_CTA3_link_verification(self):
    # #     logger.info(': ' + self.test_b5_Module2_mini_CTA3_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module2_mini_CTA3_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_c1_Module3_Banner_link_verification(self):
    # #     logger.info(': ' + self.test_c1_Module3_Banner_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module3_Banner_link_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_c2_Module3_CTA_link_verification(self):
    # #     logger.info(': ' + self.test_c2_Module3_CTA_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module3_CTA_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_c3_Module3_mini_CTA1_link_verification(self):
    # #     logger.info(': ' + self.test_c3_Module3_mini_CTA1_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module3_mini_CTA1_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_c4_Module3_mini_CTA2_link_verification(self):
    # #     logger.info(': ' + self.test_c4_Module3_mini_CTA2_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module3_mini_CTA2_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_c5_Module3_mini_CTA3_link_verification(self):
    # #     logger.info(': ' + self.test_c5_Module3_mini_CTA3_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module3_mini_CTA3_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_d1_Module4_Banner_link_verification(self):
    # #     logger.info(': ' + self.test_d1_Module4_Banner_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module4_Banner_link_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_d2_Module4_CTA_link_verification(self):
    # #     logger.info(': ' + self.test_d2_Module4_CTA_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module4_CTA_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_d3_Module4_mini_CTA1_link_verification(self):
    # #     logger.info(': ' + self.test_d3_Module4_mini_CTA1_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module4_mini_CTA1_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_d4_Module4_mini_CTA2_link_verification(self):
    # #     logger.info(': ' + self.test_d4_Module4_mini_CTA2_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module4_mini_CTA2_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_d5_Module3_mini_CTA3_link_verification(self):
    # #     logger.info(': ' + self.test_d5_Module3_mini_CTA3_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module4_mini_CTA3_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_e1_Module5_Banner_link_verification(self):
    # #     logger.info(': ' + self.test_e1_Module5_Banner_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module5_Banner_link_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_e2_Module5_CTA_link_verification(self):
    # #     logger.info(': ' + self.test_e2_Module5_CTA_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module5_CTA_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_e3_Module5_mini_CTA1_link_verification(self):
    # #     logger.info(': ' + self.test_e3_Module5_mini_CTA1_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module5_mini_CTA1_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_e4_Module5_mini_CTA2_link_verification(self):
    # #     logger.info(': ' + self.test_e4_Module5_mini_CTA2_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module5_mini_CTA2_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_e5_Module5_mini_CTA3_link_verification(self):
    # #     logger.info(': ' + self.test_e5_Module5_mini_CTA3_link_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Module5_mini_CTA3_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    # # def test_f1_Footer_Hero_CTA_verification(self):
    # #     logger.info(': ' + self.test_f1_Footer_Hero_CTA_verification.__name__)
    # #     Mpage = ModuleURLPage(self.driver)
    # #     data = self.readModuleURL_data("get_Footer_Hero_CTA_validation")
    # #     Mpage.get_Top_Hero_CTA_validation(data[0], data[1], data[2], data[3])
    # #
    #
    # @unittest.skipUnless(ReadConfig.checkSectionFooterExistance("get_google_play_button_LandingPage_URL_validation"), 'Skip test case.')
    # def test_i1_google_play_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_i1_google_play_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readFooter_data("get_google_play_button_LandingPage_URL_validation")
    #     footerPage.get_google_play_button_LandingPage_URL_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.checkSectionFooterExistance("get_apple_store_button_LandingPage_URL_validation"), 'Skip test case.')
    # def test_i2_apple_store_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_i2_apple_store_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readFooter_data("get_apple_store_button_LandingPage_URL_validation")
    #     footerPage.get_apple_store_button_LandingPage_URL_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.checkSectionFooterExistance("get_ShopApp_LandingPage_URL_validation"),'Skip test case.')
    # def test_i3_shop_App_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_i3_shop_App_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readFooter_data("get_ShopApp_LandingPage_URL_validation")
    #     footerPage.get_ShopApp_LandingPage_URL_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.checkSectionFooterExistance("get_pay_later_icon_LandingPage_URL_validation"),'Skip test case.')
    # def test_j1_pay_later_icon_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_j1_pay_later_icon_LandingPage_URL_validation.__name__)
    #     footerPage=FooterLinkPage_extra(self.driver)
    #     data = self.readFooter_data("get_pay_later_icon_LandingPage_URL_validation")
    #     footerPage.get_pay_later_icon_LandingPage_URL_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.checkSectionFooterExistance("get_free_shipping_icon_LandingPage_URL_validation"),'Skip test case.')
    # def test_j2_free_shipping_icon_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_j2_free_shipping_icon_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readFooter_data("get_free_shipping_icon_LandingPage_URL_validation")
    #     footerPage.get_free_shipping_icon_LandingPage_URL_validation(data[0],data[1],data[2],data[3])
    #
    # @unittest.skipUnless(ReadConfig.checkSectionFooterExistance("get_GetRewarded_icon_LandingPage_URL_validation"),'Skip test case.')
    # def test_j3_Get_Rewarded_icon_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_j3_Get_Rewarded_icon_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readFooter_data("get_GetRewarded_icon_LandingPage_URL_validation")
    #     footerPage.get_GetRewarded_icon_LandingPage_URL_validation(data[0],data[1],data[2],data[3])

    # @unittest.skipUnless(ReadConfig.checkSectionFooterExistance("get_HaveQuestions_icon_LandingPage_URL_validation"),'Skip test case.')
    # def test_j4_Get_HaveQuestions_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_j4_Get_HaveQuestions_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readFooter_data("get_HaveQuestions_icon_LandingPage_URL_validation")
    #     footerPage.get_HaveQuestions_icon_LandingPage_URL_validation(data[0],data[1],data[2],data[3])

    @unittest.skipUnless(ReadConfig.checkSectionFooterExistance("get_free_shipping_details_button_LandingPage_URL_validation"),'Skip test case.')
    def test_k1_free_shipping_details_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k1_free_shipping_details_button_LandingPage_URL_validation.__name__)
        footerPage = FooterLinkPage_extra(self.driver)
        data = self.readFooter_data("get_free_shipping_details_button_LandingPage_URL_validation")
        footerPage.get_free_shipping_details_button_LandingPage_URL_validation(data[0],data[1],data[2],data[3])

    # @unittest.skipUnless(ReadConfig.checkSectionFooterExistance("get_Mobile_button_LandingPage_URL_validation"),'Skip test case.')
    # def test_k2_Mobile_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_k2_Mobile_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readFooter_data("get_Mobile_button_LandingPage_URL_validation")
    #     footerPage.get_Mobile_button_LandingPage_URL_validation(data[0], data[1], data[2], data[3])
    #
    # @unittest.skipUnless(ReadConfig.checkSectionFooterExistance("get_TV_Audio_button_LandingPage_URL_validation"),'Skip test case.')
    # def test_k3_TV_Audio_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_k3_TV_Audio_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readFooter_data("get_TV_Audio_button_LandingPage_URL_validation")
    #     footerPage.get_TV_Audio_button_LandingPage_URL_validation(data[0], data[1], data[2], data[3])
    #
    # @unittest.skipUnless(ReadConfig.checkSectionFooterExistance("get_computing_button_LandingPage_URL_validation"),'Skip test case.')
    # def test_k4_computing_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_k4_computing_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readFooter_data("get_computing_button_LandingPage_URL_validation")
    #     footerPage.get_computing_button_LandingPage_URL_validation(data[0], data[1], data[2], data[3])
    #
    # @unittest.skipUnless(ReadConfig.checkSectionFooterExistance("get_appliances_button_LandingPage_URL_validation"),'Skip test case.')
    # def test_k5_appliances_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_k5_appliances_button_LandingPage_URL_validation.__name__ )
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readFooter_data("get_appliances_button_LandingPage_URL_validation")
    #     footerPage.get_appliances_button_LandingPage_URL_validation(data[0], data[1], data[2], data[3])
    #
    # @unittest.skipUnless(ReadConfig.checkSectionFooterExistance("get_weekly_offer_button_LandingPage_URL_validation"),'Skip test case.')
    # def test_k6_weekly_offer_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_k6_weekly_offer_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readFooter_data("get_weekly_offer_button_LandingPage_URL_validation")
    #     footerPage.get_weekly_offer_button_LandingPage_URL_validation(data[0], data[1], data[2], data[3])
    #
    # @unittest.skipUnless(ReadConfig.checkSectionFooterExistance("get_facebook_button_LandingPage_URL_validation"),'Skip test case.')
    # def test_l1_facebook_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_l1_facebook_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readFooter_data("get_facebook_button_LandingPage_URL_validation")
    #     footerPage.get_facebook_button_LandingPage_URL_validation(data[0], data[1], data[2], data[3])
    #
    # @unittest.skipUnless(ReadConfig.checkSectionFooterExistance("get_instagram_button_LandingPage_URL_validation"),'Skip test case.')
    # def test_l2_instagram_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_l2_instagram_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readFooter_data("get_instagram_button_LandingPage_URL_validation")
    #     footerPage.get_instagram_button_LandingPage_URL_validation(data[0], data[1], data[2], data[3])
    #
    # @unittest.skipUnless(ReadConfig.checkSectionFooterExistance("get_twitter_button_LandingPage_URL_validation"),'Skip test case.')
    # def test_l3_twitter_button_LandingPage_URL_validation(self):
    #     logger.info(': ' + self.test_l3_twitter_button_LandingPage_URL_validation.__name__)
    #     footerPage = FooterLinkPage_extra(self.driver)
    #     data = self.readFooter_data("get_twitter_button_LandingPage_URL_validation")
    #     footerPage.get_twitter_button_LandingPage_URL_validation(data[0], data[1], data[2], data[3])

    @unittest.skipUnless(ReadConfig.checkSectionTermsExistance("get_ConditionText1_validation"), 'Skip test case.')
    def test_m1_ConditionText1_Validation(self):
        logger.info(': ' + self.test_m1_ConditionText1_Validation.__name__)
        tcpage=TermsConditionPage(self.driver)
        data = self.readTermsConfig_data("get_ConditionText1_validation")
        tcpage.get_ConditionText1_validation(data[0], data[1], data[2], data[3], data[4], data[5])

    # @unittest.skipUnless(ReadConfig.checkSectionTermsExistance("get_ConditionText2_validation"), 'Skip test case.')
    # def test_m2_ConditionText2_Validation(self):
    #     logger.info(': ' + self.test_m2_ConditionText2_Validation.__name__)
    #     tcpage=TermsConditionPage(self.driver)
    #     data = self.readTermsConfig_data("get_ConditionText2_validation")
    #     tcpage.get_ConditionText2_validation(data[0], data[1], data[2], data[3], data[4], data[5])
    #
    # @unittest.skipUnless(ReadConfig.checkSectionTermsExistance("get_ConditionText3_validation"), 'Skip test case.')
    # def test_m3_ConditionText3_Validation(self):
    #     logger.info(': ' + self.test_m3_ConditionText3_Validation.__name__)
    #     tcpage=TermsConditionPage(self.driver)
    #     data = self.readTermsConfig_data("get_ConditionText3_validation")
    #     tcpage.get_ConditionText3_validation(data[0], data[1], data[2], data[3], data[4], data[5])
    #
    # @unittest.skipUnless(ReadConfig.checkSectionTermsExistance("get_ConditionText4_validation"), 'Skip test case.')
    # def test_m4_ConditionText4_Validation(self):
    #     logger.info(': ' + self.test_m4_ConditionText4_Validation.__name__)
    #     tcpage=TermsConditionPage(self.driver)
    #     data = self.readTermsConfig_data("get_ConditionText4_validation")
    #     tcpage.get_ConditionText4_validation(data[0], data[1], data[2], data[3], data[4], data[5])
    #
    # def test_n1_ExtractText_Validation(self):
    #     logger.info(': ' + self.test_n1_ExtractText_Validation.__name__)
    #     t1=extract_images()
    #     t1.extract_images()
    #     # t2=extract_text()
    #     # t2.extract_text()
    # def test_n1_Text1_Validation(self):
    #     logger.info(': ' + self.test_n1_Text1_Validation.__name__)
    #     tcpage=extract_images(self.driver)
    #     tcpage.extract_images()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        logger.info(': #####  Test Complete  #####')


if __name__ == '__main__':
    unittest.main()
