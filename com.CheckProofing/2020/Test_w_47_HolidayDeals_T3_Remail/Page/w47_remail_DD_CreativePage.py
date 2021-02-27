import json
import os
import sys
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Utility_Files.ExcelReaderUtil import ExcelUtil
from PageClass.UrlSegmentPage import URLSegemntPage
from PageClass.BasePageClass import BasePage
from Utility_Files import ReadConfig
from Utility_Files.HTMLTestRunner import stdout_redirector
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class W47_remail_DD_CreativePage(BasePage):

    def get_EPP_or_NonEPP_verification(self):
        logger.info(": ##### Started EPP version verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/1d3e0fa7a0ebb224c043e8d8a33533a5.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), "Web Element not Displayed."
            logger.info(": successfully verified EPP version is present.")
        else:
            logger.info(': successfully verified EPP version NOT present.')
        logger.info(': #####  Verification Complete  #####\n')

    def get_DD_subjectLine_text_validation(self):
        logger.info(": ##### Started subjectLine_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text

        if "MB" in subjectlineTxt:
            if "NOTE" in subjectlineTxt:
                if "EPP" in subjectlineTxt:
                    self.PH_Note = ExcelUtil(tc_name="").read_from_excel("SL_PH", 10, 8)
                    # print("there is still time to shop early Black Friday offers.")
                    # print(subjectlineTxt)
                    # assert "there is still time to shop early Black Friday offers. " in subjectlineTxt, "Subject Line Text Not Matching"
                elif "EPP" not in subjectlineTxt:
                    self.PH_Note = ExcelUtil(tc_name="").read_from_excel("SL_PH", 10, 8)
                    # assert "there is still time to shop early Black Friday offers. While supplies last.  " in subjectlineTxt, "Subject Line Text Not Matching"
                    # assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH','note_nr') in subjectlineTxt, "Subject Line Text Not Matching"

            elif "GALAXY" in subjectlineTxt:
                if "EPP" in subjectlineTxt:
                    if "Reservers" in subjectlineTxt:
                        self.PH_Galaxy1 = ExcelUtil(tc_name="").read_from_excel("SL_PH", 17, 8)
                        print(self.PH_Galaxy1)
                        print(subjectlineTxt)
                        assert " there is still time to shop early Black Friday offers. " in subjectlineTxt, "Subject Line Text Not Matching"
                elif "EPP" not in subjectlineTxt:
                    if "Reservers" in subjectlineTxt:
                        self.PH_Galaxy2 = ExcelUtil(tc_name="").read_from_excel("SL_PH", 10, 8)
                        print(self.PH_Galaxy2)
                        print(subjectlineTxt)
                        assert "there is still time to shop early Black Friday offers. While supplies last." in subjectlineTxt, "Subject Line Text Not Matching"


            else:
                self.PH_Note = ExcelUtil(tc_name="").read_from_excel("SL_PH", 14, 8)
                print(self.PH_Note)
                print(subjectlineTxt)
                assert " there is still time to shop early Black Friday offers." in subjectlineTxt, "Subject Line Text Not Matching"

        elif "TV" in subjectlineTxt:
            self.PH_TV_QLED = ExcelUtil(tc_name="").read_from_excel("SL_PH", 11, 8)
            # assert self.PH_TV_QLED in subjectlineTxt, "Subject Line Text Not Matching"
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH','CC_SL_EPP') in subjectlineTxt, "Subject Line Text Not Matching"

        elif "CE" in subjectlineTxt:
            if "COMPUTER" in subjectlineTxt:
                self.PH_TV_CE = ExcelUtil(tc_name="").read_from_excel("SL_PH", 13, 8)
                assert self.PH_TV_CE in subjectlineTxt, "Subject Line Text Not Matching"

        elif "HA" in subjectlineTxt:
            if "LAUNDRY" in subjectlineTxt:
                self.PH_HA_LAUNDRY = ExcelUtil(tc_name="").read_from_excel("SL_PH", 16, 8)
                assert self.PH_HA_LAUNDRY in subjectlineTxt, "Subject Line Text Not Matching"
            elif "KITCHEN" in subjectlineTxt:
                self.PH_HA_KITCHEN = ExcelUtil(tc_name="").read_from_excel("SL_PH", 17, 8)
                assert self.PH_HA_KITCHEN in subjectlineTxt, "Subject Line Text Not Matching"

        logger.info(": Subject Line text assert with : " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_DD_pre_header_text_validation(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        logger.info(": ##### Started pre_header_text verification #####")
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        if "MB" in subjectlineTxt:
            if "NOTE" in subjectlineTxt:
                if "Non_Reservers" in subjectlineTxt:
                    self.PH_Note_NR = ExcelUtil(tc_name="").read_from_excel("SL_PH", 10, 9)
                    assert self.PH_Note_NR in pheaderTxt, "Pre Header Text Not Matching"
                elif "Reservers" in subjectlineTxt:
                    self.PH_Note_R = ExcelUtil(tc_name="").read_from_excel("SL_PH", 9, 9)
                    assert self.PH_Note_R in pheaderTxt, "Pre Header Text Not Matching"
            elif "GALAXY" in subjectlineTxt:
                self.PH_Galaxy_R = ExcelUtil(tc_name="").read_from_excel("SL_PH", 8, 9)
                assert self.PH_Galaxy_R in pheaderTxt, "Pre Header Text Not Matching"
            elif "WEAR" in subjectlineTxt:
                self.PH_ME = ExcelUtil(tc_name="").read_from_excel("SL_PH", 14, 9)
                assert "Skip the lines. Shop smart. Save on tablets, earbuds and more. Plus, shop Galaxy Watch3 with our new Samsung Design Studio." in pheaderTxt, "Pre Header Text Not Matching"
            elif "ACCESSORY" in subjectlineTxt:
                self.PH_ME = ExcelUtil(tc_name="").read_from_excel("SL_PH", 14, 9)
                assert "Skip the lines. Shop smart. Save on tablets, earbuds and more. Plus, shop Galaxy Watch3 with our new Samsung Design Studio." in pheaderTxt, "Pre Header Text Not Matching"

        elif "TV" in subjectlineTxt:
            if "QLED" in subjectlineTxt:
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH', 'tv') in pheaderTxt, "Pre Header Text Not Matching"
            elif "ACCESSORY" in subjectlineTxt:
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH','tv_accessory') in pheaderTxt, "Pre Header Text Not Matching"

        elif "CE" in subjectlineTxt:
            if "COMPUTER" in subjectlineTxt:
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH','COMPUTER') in pheaderTxt, "Pre Header Text Not Matching"

        elif "HA" in subjectlineTxt:
            if "LAUNDRY" in subjectlineTxt:
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH','LAUNDRY') in pheaderTxt, "Pre Header Text Not Matching"
            elif "KITCHEN" in subjectlineTxt:
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH','KITCHEN') in pheaderTxt, "Pre Header Text Not Matching"

        logger.info(": Pre-Header text assert with : " + pheaderTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_DD_pre_header_link_validation(self):
        logger.info(": ##### Started pre_header_link_validation verification #####")
        self.PH_URL = ExcelUtil(tc_name="").read_from_excel("FINAL_MODULE_All_Versions", 2, 7)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@target='_blank'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        self.url_list.append(URL)
        assert self.PH_URL in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_giveWonder_link_validation(self):
        logger.info(": ##### Started GiveWonder Module URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FINAL_MODULE_All_Versions", 3, 7)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/964160ea34117060e7eb9df0f08d4100.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        givewonderURL = self.driver.current_url
        assert self.url_path in givewonderURL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Web Landing page URL:\n" + givewonderURL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(givewonderURL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Top_Hero_link_validation(self):
        logger.info(": ##### Started Top_Hero Module URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FINAL_MODULE_All_Versions", 2, 7)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/884ca6bb27194595642c98ab3cc679ee.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        TopHeroURL = self.driver.current_url
        assert self.url_path in TopHeroURL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Web Landing page URL:\n" + TopHeroURL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(TopHeroURL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    # def get_ModuleTextValidation(self):
    #     logger.info(": ##### Started Text verification #####")
    #     # self.Mod1_txt = ExcelUtil(tc_name="").read_from_excel("FINAL_MODULE_All_Versions", 2, 8)
    #     txt1 = self.driver.find_element_by_xpath("(//a[@_label='Mod_Headline'])[2]").text
    #     print("Proof :"+ txt1)
    #     print("Reference :"+ ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH','mtxt1'))
    #     # assert self.Mod1_txt in txt1, "Web Landing Page Text NOT Matching."
    #     assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH','mtxt1') in txt1, "Pre Header Text Not Matching"
    #     logger.info(': #####  Verification Complete  #####\n')

    def get_ModuleTextValidation(self):
        logger.info(": ##### Started Text verification #####")
        self.Mod1_txt = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 49, 5)
        txt1 = self.driver.find_element_by_xpath("//*[@_label='Hero_Text']").text.encode('utf-8')
        # txt1 = self.driver.find_element_by_xpath("//*[@_label='Module_Text']").text
        print(txt1)
        print(self.Mod1_txt)
        # assert self.Mod1_txt in txt1, "Web Landing Page Text NOT Matching."
        logger.info(': #####  Verification Complete  #####\n')
    def get_SL(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "Non_Reservers" in subjectlineTxt:
            print("Non Reservers Selected.")
        elif "Non_Reservers" in subjectlineTxt:
            print("Non Reservers Selected.")













