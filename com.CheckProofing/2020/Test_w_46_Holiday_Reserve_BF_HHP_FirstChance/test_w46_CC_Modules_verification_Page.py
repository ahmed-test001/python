import time
import unittest
import sys
import os
import logging
import warnings
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Test_w_46_Holiday_Reserve_BF_HHP_FirstChance.Page.FooterLinkPage import FooterLinkPage
from Test_w_46_Holiday_Reserve_BF_HHP_FirstChance.Page.w46_smartphoneCreativePage import w46_SmartphoneCreativePage
from Utility_Files import ReadConfig
from Utility_Files.HTMLTestRunner import stdout_redirector
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class W_46_CC_Module_Verify_Test(unittest.TestCase):

    driver = None
    url_list = []
    method_list_in_Url = []

    @classmethod
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver1'), options=option)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        self.wait = WebDriverWait(self.driver, 10)


    @classmethod
    def tearDown(self):
        self.driver.quit()
        logger.info(': \n#####  Test Complete  #####')

    def test_W46_ModuleVerification_URL1(self):
        logger.info(': ' + self.test_W46_ModuleVerification_URL1.__name__ + "\n #####  Starting TEST  ##### ")
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            urls = f.read().splitlines()
            url=urls[0]
            self.driver.get(url)

            if "EPP_Reservers" in url:
                logger.info(": ##Select EPP_Reserve URL PATH : " + url +"\n")
                MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                MB_smartphone.get_EPP_or_NonEPP_verification()
                MB_smartphone.get_pre_header_text_validation()
                MB_smartphone.get_subjectLine_text_validation()
                MB_smartphone.get_pre_header_link_validation()
                if "MB" in url:
                    try:
                        if "MB_FOLD" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_FOLD_Module()
                        elif "MB_NOTE" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_NOTE_Module()
                        elif "MB_GALAXY" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_GALAXY_Module()
                        elif "MB_MIDTIER" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_MIDTIER_Module()
                    except:
                        raise ValueError
                MB_smartphone.get_giveWonder_link_validation()
                link_footer=FooterLinkPage(self.driver)
                link_footer.get_pay_later_icon_LandingPage_URL_validation()
                link_footer.get_free_shipping_icon_LandingPage_URL_validation()
                link_footer.get_google_play_button_LandingPage_URL_validation()
                link_footer.get_apple_store_button_LandingPage_URL_validation()
                link_footer.get_free_shipping_details_button_LandingPage_URL_validation()
                link_footer.get_Mobile_button_LandingPage_URL_validation()
                link_footer.get_TV_Audio_button_LandingPage_URL_validation()
                link_footer.get_computing_button_LandingPage_URL_validation()
                link_footer.get_appliances_button_LandingPage_URL_validation()
                link_footer.get_weekly_offer_button_LandingPage_URL_validation()
                link_footer.get_facebook_button_LandingPage_URL_validation()
                link_footer.get_instagram_button_LandingPage_URL_validation()
                link_footer.get_twitter_button_LandingPage_URL_validation()
                link_footer.get_youtube_button_LandingPage_URL_validation()

            elif "Reservers" in url:
                logger.info(": ##Select only Reserve URL PATH : " + url +"\n")
                MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                MB_smartphone.get_EPP_or_NonEPP_verification()
                MB_smartphone.get_pre_header_text_validation()
                MB_smartphone.get_subjectLine_text_validation()
                MB_smartphone.get_pre_header_link_validation()
                if "MB" in url:
                    try:
                        if "MB_FOLD" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_FOLD_Module()
                        elif "MB_NOTE" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_NOTE_Module()
                        elif "MB_GALAXY" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_GALAXY_Module()
                        elif "MB_MIDTIER" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_MIDTIER_Module()
                    except:
                        raise ValueError
                MB_smartphone.get_giveWonder_link_validation()
                link_footer = FooterLinkPage(self.driver)
                link_footer.get_pay_later_icon_LandingPage_URL_validation()
                link_footer.get_free_shipping_icon_LandingPage_URL_validation()
                link_footer.get_google_play_button_LandingPage_URL_validation()
                link_footer.get_apple_store_button_LandingPage_URL_validation()
                link_footer.get_free_shipping_details_button_LandingPage_URL_validation()
                link_footer.get_Mobile_button_LandingPage_URL_validation()
                link_footer.get_TV_Audio_button_LandingPage_URL_validation()
                link_footer.get_computing_button_LandingPage_URL_validation()
                link_footer.get_appliances_button_LandingPage_URL_validation()
                link_footer.get_weekly_offer_button_LandingPage_URL_validation()
                link_footer.get_facebook_button_LandingPage_URL_validation()
                link_footer.get_instagram_button_LandingPage_URL_validation()
                link_footer.get_twitter_button_LandingPage_URL_validation()
                link_footer.get_youtube_button_LandingPage_URL_validation()
            else:
                print("NO URL Selected.")

    def test_W46_ModuleVerification_URL2(self):
        logger.info(': ' + self.test_W46_ModuleVerification_URL2.__name__ + "\n #####  Starting TEST  ##### ")
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            urls = f.read().splitlines()
            url = urls[1]
            self.driver.get(url)

            if "EPP_Reservers" in url:
                logger.info(": ##Select EPP_Reserve URL PATH : " + url +"\n")
                MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                MB_smartphone.get_EPP_or_NonEPP_verification()
                MB_smartphone.get_pre_header_text_validation()
                MB_smartphone.get_subjectLine_text_validation()
                MB_smartphone.get_pre_header_link_validation()
                if "MB" in url:
                    try:
                        if "MB_FOLD" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_FOLD_Module()
                        elif "MB_NOTE" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_NOTE_Module()
                        elif "MB_GALAXY" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_GALAXY_Module()
                        elif "MB_MIDTIER" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_MIDTIER_Module()
                    except:
                        raise ValueError
                MB_smartphone.get_giveWonder_link_validation()
                link_footer=FooterLinkPage(self.driver)
                link_footer.get_pay_later_icon_LandingPage_URL_validation()
                link_footer.get_free_shipping_icon_LandingPage_URL_validation()
                link_footer.get_google_play_button_LandingPage_URL_validation()
                link_footer.get_apple_store_button_LandingPage_URL_validation()
                link_footer.get_free_shipping_details_button_LandingPage_URL_validation()
                link_footer.get_Mobile_button_LandingPage_URL_validation()
                link_footer.get_TV_Audio_button_LandingPage_URL_validation()
                link_footer.get_computing_button_LandingPage_URL_validation()
                link_footer.get_appliances_button_LandingPage_URL_validation()
                link_footer.get_weekly_offer_button_LandingPage_URL_validation()
                link_footer.get_facebook_button_LandingPage_URL_validation()
                link_footer.get_instagram_button_LandingPage_URL_validation()
                link_footer.get_twitter_button_LandingPage_URL_validation()
                link_footer.get_youtube_button_LandingPage_URL_validation()

            elif "Reservers" in url:
                logger.info(": ##Select only Reserve URL PATH : " + url +"\n")
                MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                MB_smartphone.get_EPP_or_NonEPP_verification()
                MB_smartphone.get_pre_header_text_validation()
                MB_smartphone.get_subjectLine_text_validation()
                MB_smartphone.get_pre_header_link_validation()
                if "MB" in url:
                    try:
                        if "MB_FOLD" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_FOLD_Module()
                        elif "MB_NOTE" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_NOTE_Module()
                        elif "MB_GALAXY" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_GALAXY_Module()
                        elif "MB_MIDTIER" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_MIDTIER_Module()
                    except:
                        raise ValueError
                MB_smartphone.get_giveWonder_link_validation()
                link_footer = FooterLinkPage(self.driver)
                link_footer.get_pay_later_icon_LandingPage_URL_validation()
                link_footer.get_free_shipping_icon_LandingPage_URL_validation()
                link_footer.get_google_play_button_LandingPage_URL_validation()
                link_footer.get_apple_store_button_LandingPage_URL_validation()
                link_footer.get_free_shipping_details_button_LandingPage_URL_validation()
                link_footer.get_Mobile_button_LandingPage_URL_validation()
                link_footer.get_TV_Audio_button_LandingPage_URL_validation()
                link_footer.get_computing_button_LandingPage_URL_validation()
                link_footer.get_appliances_button_LandingPage_URL_validation()
                link_footer.get_weekly_offer_button_LandingPage_URL_validation()
                link_footer.get_facebook_button_LandingPage_URL_validation()
                link_footer.get_instagram_button_LandingPage_URL_validation()
                link_footer.get_twitter_button_LandingPage_URL_validation()
                link_footer.get_youtube_button_LandingPage_URL_validation()
            else:
                print("NO URL Selected.")

    def test_W46_ModuleVerification_URL3(self):
        logger.info(': ' + self.test_W46_ModuleVerification_URL3.__name__ + "\n #####  Starting TEST  ##### ")
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            urls = f.read().splitlines()
            url = urls[2]
            self.driver.get(url)

            if "EPP_Reservers" in url:
                logger.info(": ##Select EPP_Reserve URL PATH : " + url +"\n")
                MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                MB_smartphone.get_EPP_or_NonEPP_verification()
                MB_smartphone.get_pre_header_text_validation()
                MB_smartphone.get_subjectLine_text_validation()
                MB_smartphone.get_pre_header_link_validation()
                if "MB" in url:
                    try:
                        if "MB_FOLD" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_FOLD_Module()
                        elif "MB_NOTE" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_NOTE_Module()
                        elif "MB_GALAXY" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_GALAXY_Module()
                        elif "MB_MIDTIER" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_MIDTIER_Module()
                    except:
                        raise ValueError
                MB_smartphone.get_giveWonder_link_validation()
                link_footer=FooterLinkPage(self.driver)
                link_footer.get_pay_later_icon_LandingPage_URL_validation()
                link_footer.get_free_shipping_icon_LandingPage_URL_validation()
                link_footer.get_google_play_button_LandingPage_URL_validation()
                link_footer.get_apple_store_button_LandingPage_URL_validation()
                link_footer.get_free_shipping_details_button_LandingPage_URL_validation()
                link_footer.get_Mobile_button_LandingPage_URL_validation()
                link_footer.get_TV_Audio_button_LandingPage_URL_validation()
                link_footer.get_computing_button_LandingPage_URL_validation()
                link_footer.get_appliances_button_LandingPage_URL_validation()
                link_footer.get_weekly_offer_button_LandingPage_URL_validation()
                link_footer.get_facebook_button_LandingPage_URL_validation()
                link_footer.get_instagram_button_LandingPage_URL_validation()
                link_footer.get_twitter_button_LandingPage_URL_validation()
                link_footer.get_youtube_button_LandingPage_URL_validation()

            elif "Reservers" in url:
                logger.info(": ##Select only Reserve URL PATH : " + url +"\n")
                MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                MB_smartphone.get_EPP_or_NonEPP_verification()
                MB_smartphone.get_pre_header_text_validation()
                MB_smartphone.get_subjectLine_text_validation()
                MB_smartphone.get_pre_header_link_validation()
                if "MB" in url:
                    try:
                        if "MB_FOLD" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_FOLD_Module()
                        elif "MB_NOTE" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_NOTE_Module()
                        elif "MB_GALAXY" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_GALAXY_Module()
                        elif "MB_MIDTIER" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_MIDTIER_Module()
                    except:
                        raise ValueError
                MB_smartphone.get_giveWonder_link_validation()
                link_footer = FooterLinkPage(self.driver)
                link_footer.get_pay_later_icon_LandingPage_URL_validation()
                link_footer.get_free_shipping_icon_LandingPage_URL_validation()
                link_footer.get_google_play_button_LandingPage_URL_validation()
                link_footer.get_apple_store_button_LandingPage_URL_validation()
                link_footer.get_free_shipping_details_button_LandingPage_URL_validation()
                link_footer.get_Mobile_button_LandingPage_URL_validation()
                link_footer.get_TV_Audio_button_LandingPage_URL_validation()
                link_footer.get_computing_button_LandingPage_URL_validation()
                link_footer.get_appliances_button_LandingPage_URL_validation()
                link_footer.get_weekly_offer_button_LandingPage_URL_validation()
                link_footer.get_facebook_button_LandingPage_URL_validation()
                link_footer.get_instagram_button_LandingPage_URL_validation()
                link_footer.get_twitter_button_LandingPage_URL_validation()
                link_footer.get_youtube_button_LandingPage_URL_validation()
            else:
                print("NO URL Selected.")

    def test_W46_ModuleVerification_URL4(self):
        logger.info(': ' + self.test_W46_ModuleVerification_URL4.__name__ + "\n #####  Starting TEST  ##### ")
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            urls = f.read().splitlines()
            url = urls[3]
            self.driver.get(url)

            if "EPP_Reservers" in url:
                logger.info(": ##Select EPP_Reserve URL PATH : " + url +"\n")
                MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                MB_smartphone.get_EPP_or_NonEPP_verification()
                MB_smartphone.get_pre_header_text_validation()
                MB_smartphone.get_subjectLine_text_validation()
                MB_smartphone.get_pre_header_link_validation()
                if "MB" in url:
                    try:
                        if "MB_FOLD" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_FOLD_Module()
                        elif "MB_NOTE" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_NOTE_Module()
                        elif "MB_GALAXY" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_GALAXY_Module()
                        elif "MB_MIDTIER" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_MIDTIER_Module()
                    except:
                        raise ValueError
                MB_smartphone.get_giveWonder_link_validation()
                link_footer=FooterLinkPage(self.driver)
                link_footer.get_pay_later_icon_LandingPage_URL_validation()
                link_footer.get_free_shipping_icon_LandingPage_URL_validation()
                link_footer.get_google_play_button_LandingPage_URL_validation()
                link_footer.get_apple_store_button_LandingPage_URL_validation()
                link_footer.get_free_shipping_details_button_LandingPage_URL_validation()
                link_footer.get_Mobile_button_LandingPage_URL_validation()
                link_footer.get_TV_Audio_button_LandingPage_URL_validation()
                link_footer.get_computing_button_LandingPage_URL_validation()
                link_footer.get_appliances_button_LandingPage_URL_validation()
                link_footer.get_weekly_offer_button_LandingPage_URL_validation()
                link_footer.get_facebook_button_LandingPage_URL_validation()
                link_footer.get_instagram_button_LandingPage_URL_validation()
                link_footer.get_twitter_button_LandingPage_URL_validation()
                link_footer.get_youtube_button_LandingPage_URL_validation()

            elif "Reservers" in url:
                logger.info(": ##Select only Reserve URL PATH : " + url +"\n")
                MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                MB_smartphone.get_EPP_or_NonEPP_verification()
                MB_smartphone.get_pre_header_text_validation()
                MB_smartphone.get_subjectLine_text_validation()
                MB_smartphone.get_pre_header_link_validation()
                if "MB" in url:
                    try:
                        if "MB_FOLD" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_FOLD_Module()
                        elif "MB_NOTE" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_NOTE_Module()
                        elif "MB_GALAXY" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_GALAXY_Module()
                        elif "MB_MIDTIER" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_MIDTIER_Module()
                    except:
                        raise ValueError
                MB_smartphone.get_giveWonder_link_validation()
                link_footer = FooterLinkPage(self.driver)
                link_footer.get_pay_later_icon_LandingPage_URL_validation()
                link_footer.get_free_shipping_icon_LandingPage_URL_validation()
                link_footer.get_google_play_button_LandingPage_URL_validation()
                link_footer.get_apple_store_button_LandingPage_URL_validation()
                link_footer.get_free_shipping_details_button_LandingPage_URL_validation()
                link_footer.get_Mobile_button_LandingPage_URL_validation()
                link_footer.get_TV_Audio_button_LandingPage_URL_validation()
                link_footer.get_computing_button_LandingPage_URL_validation()
                link_footer.get_appliances_button_LandingPage_URL_validation()
                link_footer.get_weekly_offer_button_LandingPage_URL_validation()
                link_footer.get_facebook_button_LandingPage_URL_validation()
                link_footer.get_instagram_button_LandingPage_URL_validation()
                link_footer.get_twitter_button_LandingPage_URL_validation()
                link_footer.get_youtube_button_LandingPage_URL_validation()
            else:
                print("NO URL Selected.")

    def test_W46_ModuleVerification_URL5(self):
        logger.info(': ' + self.test_W46_ModuleVerification_URL5.__name__ + "\n #####  Starting TEST  ##### ")
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            urls = f.read().splitlines()
            url=urls[4]
            self.driver.get(url)

            if "EPP_Reservers" in url:
                logger.info(": ##Select EPP_Reserve URL PATH : " + url +"\n")
                MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                MB_smartphone.get_EPP_or_NonEPP_verification()
                MB_smartphone.get_pre_header_text_validation()
                MB_smartphone.get_subjectLine_text_validation()
                MB_smartphone.get_pre_header_link_validation()
                if "MB" in url:
                    try:
                        if "MB_FOLD" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_FOLD_Module()
                        elif "MB_NOTE" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_NOTE_Module()
                        elif "MB_GALAXY" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_GALAXY_Module()
                        elif "MB_MIDTIER" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_MIDTIER_Module()
                    except:
                        raise ValueError
                MB_smartphone.get_giveWonder_link_validation()
                link_footer=FooterLinkPage(self.driver)
                link_footer.get_pay_later_icon_LandingPage_URL_validation()
                link_footer.get_free_shipping_icon_LandingPage_URL_validation()
                link_footer.get_google_play_button_LandingPage_URL_validation()
                link_footer.get_apple_store_button_LandingPage_URL_validation()
                link_footer.get_free_shipping_details_button_LandingPage_URL_validation()
                link_footer.get_Mobile_button_LandingPage_URL_validation()
                link_footer.get_TV_Audio_button_LandingPage_URL_validation()
                link_footer.get_computing_button_LandingPage_URL_validation()
                link_footer.get_appliances_button_LandingPage_URL_validation()
                link_footer.get_weekly_offer_button_LandingPage_URL_validation()
                link_footer.get_facebook_button_LandingPage_URL_validation()
                link_footer.get_instagram_button_LandingPage_URL_validation()
                link_footer.get_twitter_button_LandingPage_URL_validation()
                link_footer.get_youtube_button_LandingPage_URL_validation()

            elif "Reservers" in url:
                logger.info(": ##Select only Reserve URL PATH : " + url +"\n")
                MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                MB_smartphone.get_EPP_or_NonEPP_verification()
                MB_smartphone.get_pre_header_text_validation()
                MB_smartphone.get_subjectLine_text_validation()
                MB_smartphone.get_pre_header_link_validation()
                if "MB" in url:
                    try:
                        if "MB_FOLD" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_FOLD_Module()
                        elif "MB_NOTE" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_NOTE_Module()
                        elif "MB_GALAXY" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_GALAXY_Module()
                        elif "MB_MIDTIER" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_MIDTIER_Module()
                    except:
                        raise ValueError
                MB_smartphone.get_giveWonder_link_validation()
                link_footer = FooterLinkPage(self.driver)
                link_footer.get_pay_later_icon_LandingPage_URL_validation()
                link_footer.get_free_shipping_icon_LandingPage_URL_validation()
                link_footer.get_google_play_button_LandingPage_URL_validation()
                link_footer.get_apple_store_button_LandingPage_URL_validation()
                link_footer.get_free_shipping_details_button_LandingPage_URL_validation()
                link_footer.get_Mobile_button_LandingPage_URL_validation()
                link_footer.get_TV_Audio_button_LandingPage_URL_validation()
                link_footer.get_computing_button_LandingPage_URL_validation()
                link_footer.get_appliances_button_LandingPage_URL_validation()
                link_footer.get_weekly_offer_button_LandingPage_URL_validation()
                link_footer.get_facebook_button_LandingPage_URL_validation()
                link_footer.get_instagram_button_LandingPage_URL_validation()
                link_footer.get_twitter_button_LandingPage_URL_validation()
                link_footer.get_youtube_button_LandingPage_URL_validation()
            else:
                print("NO URL Selected.")

    def test_W46_ModuleVerification_URL6(self):
        logger.info(': ' + self.test_W46_ModuleVerification_URL6.__name__ + "\n #####  Starting TEST  ##### ")
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            urls = f.read().splitlines()
            url = urls[5]
            self.driver.get(url)

            if "EPP_Reservers" in url:
                logger.info(": ##Select EPP_Reserve URL PATH : " + url +"\n")
                MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                MB_smartphone.get_EPP_or_NonEPP_verification()
                MB_smartphone.get_pre_header_text_validation()
                MB_smartphone.get_subjectLine_text_validation()
                MB_smartphone.get_pre_header_link_validation()
                if "MB" in url:
                    try:
                        if "MB_FOLD" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_FOLD_Module()
                        elif "MB_NOTE" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_NOTE_Module()
                        elif "MB_GALAXY" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_GALAXY_Module()
                        elif "MB_MIDTIER" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_MIDTIER_Module()
                    except:
                        raise ValueError
                MB_smartphone.get_giveWonder_link_validation()
                link_footer=FooterLinkPage(self.driver)
                link_footer.get_pay_later_icon_LandingPage_URL_validation()
                link_footer.get_free_shipping_icon_LandingPage_URL_validation()
                link_footer.get_google_play_button_LandingPage_URL_validation()
                link_footer.get_apple_store_button_LandingPage_URL_validation()
                link_footer.get_free_shipping_details_button_LandingPage_URL_validation()
                link_footer.get_Mobile_button_LandingPage_URL_validation()
                link_footer.get_TV_Audio_button_LandingPage_URL_validation()
                link_footer.get_computing_button_LandingPage_URL_validation()
                link_footer.get_appliances_button_LandingPage_URL_validation()
                link_footer.get_weekly_offer_button_LandingPage_URL_validation()
                link_footer.get_facebook_button_LandingPage_URL_validation()
                link_footer.get_instagram_button_LandingPage_URL_validation()
                link_footer.get_twitter_button_LandingPage_URL_validation()
                link_footer.get_youtube_button_LandingPage_URL_validation()

            elif "Reservers" in url:
                logger.info(": ##Select only Reserve URL PATH : " + url +"\n")
                MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                MB_smartphone.get_EPP_or_NonEPP_verification()
                MB_smartphone.get_pre_header_text_validation()
                MB_smartphone.get_subjectLine_text_validation()
                MB_smartphone.get_pre_header_link_validation()
                if "MB" in url:
                    try:
                        if "MB_FOLD" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_FOLD_Module()
                        elif "MB_NOTE" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_NOTE_Module()
                        elif "MB_GALAXY" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_GALAXY_Module()
                        elif "MB_MIDTIER" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_MIDTIER_Module()
                    except:
                        raise ValueError
                MB_smartphone.get_giveWonder_link_validation()
                link_footer = FooterLinkPage(self.driver)
                link_footer.get_pay_later_icon_LandingPage_URL_validation()
                link_footer.get_free_shipping_icon_LandingPage_URL_validation()
                link_footer.get_google_play_button_LandingPage_URL_validation()
                link_footer.get_apple_store_button_LandingPage_URL_validation()
                link_footer.get_free_shipping_details_button_LandingPage_URL_validation()
                link_footer.get_Mobile_button_LandingPage_URL_validation()
                link_footer.get_TV_Audio_button_LandingPage_URL_validation()
                link_footer.get_computing_button_LandingPage_URL_validation()
                link_footer.get_appliances_button_LandingPage_URL_validation()
                link_footer.get_weekly_offer_button_LandingPage_URL_validation()
                link_footer.get_facebook_button_LandingPage_URL_validation()
                link_footer.get_instagram_button_LandingPage_URL_validation()
                link_footer.get_twitter_button_LandingPage_URL_validation()
                link_footer.get_youtube_button_LandingPage_URL_validation()
            else:
                print("NO URL Selected.")

    def test_W46_ModuleVerification_URL7(self):
        logger.info(': ' + self.test_W46_ModuleVerification_URL7.__name__ + "\n #####  Starting TEST  ##### ")
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            urls = f.read().splitlines()
            url = urls[6]
            self.driver.get(url)

            if "EPP_Reservers" in url:
                logger.info(": ##Select EPP_Reserve URL PATH : " + url +"\n")
                MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                MB_smartphone.get_EPP_or_NonEPP_verification()
                MB_smartphone.get_pre_header_text_validation()
                MB_smartphone.get_subjectLine_text_validation()
                MB_smartphone.get_pre_header_link_validation()
                if "MB" in url:
                    try:
                        if "MB_FOLD" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_FOLD_Module()
                        elif "MB_NOTE" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_NOTE_Module()
                        elif "MB_GALAXY" in url:
                            MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_GALAXY_Module()
                        elif "MB_MIDTIER" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_MIDTIER_Module()
                    except:
                        raise ValueError
                MB_smartphone.get_giveWonder_link_validation()
                link_footer=FooterLinkPage(self.driver)
                link_footer.get_pay_later_icon_LandingPage_URL_validation()
                link_footer.get_free_shipping_icon_LandingPage_URL_validation()
                link_footer.get_google_play_button_LandingPage_URL_validation()
                link_footer.get_apple_store_button_LandingPage_URL_validation()
                link_footer.get_free_shipping_details_button_LandingPage_URL_validation()
                link_footer.get_Mobile_button_LandingPage_URL_validation()
                link_footer.get_TV_Audio_button_LandingPage_URL_validation()
                link_footer.get_computing_button_LandingPage_URL_validation()
                link_footer.get_appliances_button_LandingPage_URL_validation()
                link_footer.get_weekly_offer_button_LandingPage_URL_validation()
                link_footer.get_facebook_button_LandingPage_URL_validation()
                link_footer.get_instagram_button_LandingPage_URL_validation()
                link_footer.get_twitter_button_LandingPage_URL_validation()
                link_footer.get_youtube_button_LandingPage_URL_validation()

            elif "Reservers" in url:
                logger.info(": ##Select only Reserve URL PATH : " + url +"\n")
                MB_smartphone=w46_SmartphoneCreativePage(self.driver)
                MB_smartphone.get_EPP_or_NonEPP_verification()
                MB_smartphone.get_pre_header_text_validation()
                MB_smartphone.get_subjectLine_text_validation()
                MB_smartphone.get_pre_header_link_validation()
                if "MB" in url:
                    try:
                        if "MB_FOLD" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_FOLD_Module()
                        elif "MB_NOTE" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_NOTE_Module()
                        elif "MB_GALAXY" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_GALAXY_Module()
                        elif "MB_MIDTIER" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_MIDTIER_Module()
                    except:
                        raise ValueError
                MB_smartphone.get_giveWonder_link_validation()
                link_footer = FooterLinkPage(self.driver)
                link_footer.get_pay_later_icon_LandingPage_URL_validation()
                link_footer.get_free_shipping_icon_LandingPage_URL_validation()
                link_footer.get_google_play_button_LandingPage_URL_validation()
                link_footer.get_apple_store_button_LandingPage_URL_validation()
                link_footer.get_free_shipping_details_button_LandingPage_URL_validation()
                link_footer.get_Mobile_button_LandingPage_URL_validation()
                link_footer.get_TV_Audio_button_LandingPage_URL_validation()
                link_footer.get_computing_button_LandingPage_URL_validation()
                link_footer.get_appliances_button_LandingPage_URL_validation()
                link_footer.get_weekly_offer_button_LandingPage_URL_validation()
                link_footer.get_facebook_button_LandingPage_URL_validation()
                link_footer.get_instagram_button_LandingPage_URL_validation()
                link_footer.get_twitter_button_LandingPage_URL_validation()
                link_footer.get_youtube_button_LandingPage_URL_validation()
            else:
                print("NO URL Selected.")

    def test_W46_ModuleVerification_URL8(self):
        logger.info(': ' + self.test_W46_ModuleVerification_URL8.__name__ + "\n #####  Starting TEST  ##### ")
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            urls = f.read().splitlines()
            url = urls[7]
            self.driver.get(url)

            if "EPP_Reservers" in url:
                logger.info(": ##Select EPP_Reserve URL PATH : " + url + "\n")
                MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                MB_smartphone.get_EPP_or_NonEPP_verification()
                MB_smartphone.get_pre_header_text_validation()
                MB_smartphone.get_subjectLine_text_validation()
                MB_smartphone.get_pre_header_link_validation()
                if "MB" in url:
                    try:
                        if "MB_FOLD" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_FOLD_Module()
                        elif "MB_NOTE" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_NOTE_Module()
                        elif "MB_GALAXY" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_GALAXY_Module()
                        elif "MB_MIDTIER" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_MIDTIER_Module()
                    except:
                        raise ValueError
                MB_smartphone.get_giveWonder_link_validation()
                link_footer = FooterLinkPage(self.driver)
                link_footer.get_pay_later_icon_LandingPage_URL_validation()
                link_footer.get_free_shipping_icon_LandingPage_URL_validation()
                link_footer.get_google_play_button_LandingPage_URL_validation()
                link_footer.get_apple_store_button_LandingPage_URL_validation()
                link_footer.get_free_shipping_details_button_LandingPage_URL_validation()
                link_footer.get_Mobile_button_LandingPage_URL_validation()
                link_footer.get_TV_Audio_button_LandingPage_URL_validation()
                link_footer.get_computing_button_LandingPage_URL_validation()
                link_footer.get_appliances_button_LandingPage_URL_validation()
                link_footer.get_weekly_offer_button_LandingPage_URL_validation()
                link_footer.get_facebook_button_LandingPage_URL_validation()
                link_footer.get_instagram_button_LandingPage_URL_validation()
                link_footer.get_twitter_button_LandingPage_URL_validation()
                link_footer.get_youtube_button_LandingPage_URL_validation()

            elif "Reservers" in url:
                logger.info(": ##Select only Reserve URL PATH : " + url + "\n")
                MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                MB_smartphone.get_EPP_or_NonEPP_verification()
                MB_smartphone.get_pre_header_text_validation()
                MB_smartphone.get_subjectLine_text_validation()
                MB_smartphone.get_pre_header_link_validation()
                if "MB" in url:
                    try:
                        if "MB_FOLD" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_FOLD_Module()
                        elif "MB_NOTE" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_NOTE_Module()
                        elif "MB_GALAXY" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_GALAXY_Module()
                        elif "MB_MIDTIER" in url:
                            MB_smartphone = w46_SmartphoneCreativePage(self.driver)
                            MB_smartphone.get_W46_MB_MIDTIER_Module()
                    except:
                        raise ValueError
                MB_smartphone.get_giveWonder_link_validation()
                link_footer = FooterLinkPage(self.driver)
                link_footer.get_pay_later_icon_LandingPage_URL_validation()
                link_footer.get_free_shipping_icon_LandingPage_URL_validation()
                link_footer.get_google_play_button_LandingPage_URL_validation()
                link_footer.get_apple_store_button_LandingPage_URL_validation()
                link_footer.get_free_shipping_details_button_LandingPage_URL_validation()
                link_footer.get_Mobile_button_LandingPage_URL_validation()
                link_footer.get_TV_Audio_button_LandingPage_URL_validation()
                link_footer.get_computing_button_LandingPage_URL_validation()
                link_footer.get_appliances_button_LandingPage_URL_validation()
                link_footer.get_weekly_offer_button_LandingPage_URL_validation()
                link_footer.get_facebook_button_LandingPage_URL_validation()
                link_footer.get_instagram_button_LandingPage_URL_validation()
                link_footer.get_twitter_button_LandingPage_URL_validation()
                link_footer.get_youtube_button_LandingPage_URL_validation()
            else:
                print("NO URL Selected.")


if __name__ == '__main__':
    unittest.main()