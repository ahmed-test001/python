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


class DD_CreativePage(BasePage):

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
        assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH','SL') in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Subject Line text assert with : " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_DD_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        if "Non" in subjectlineTxt:
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH','PH_Non_Reserve') in pheaderTxt, "Pre Header Text Not Matching"
        else:
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH','PH_Reserve') in pheaderTxt, "Pre Header Text Not Matching"
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
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/a6f1b5509ab5137ea157700e97fbfe52.png']"))).click()
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
        self.Mod1_txt = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 54, 4)
        txt1 = self.driver.find_element_by_xpath("//*[@_label='Mod5_Headline']").text.encode('utf-8')
        print(self.Mod1_txt.encode('utf-8'))
        print(txt1)
        assert self.Mod1_txt.encode('utf-8') in txt1, "Web Landing Page Text NOT Matching."
        logger.info(': #####  Verification Complete  #####\n')
    def get_SL(self):
        self.Mod1_txt1 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 5, 2)
        # self.Mod1_txt2 = ExcelUtil(tc_name="").read_from_excel("Sheet1", 2, 11)
        # self.Mod1_txt3 = ExcelUtil(tc_name="").read_from_excel("Sheet1", 2, 13)

        # print(ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH','abc'))
        print(self.Mod1_txt1.encode('utf-8'))
        # print(self.Mod1_txt3)

        # subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        # if "Non_Reservers" in subjectlineTxt:
        #     print("Non Reservers Selected.")
        # elif "Non_Reservers" in subjectlineTxt:
        #     print("Non Reservers Selected.")

    def get_Module1_SubHeadLineText(self):
        logger.info(": ##### Started Text verification #####")
        self.Reserve = ExcelUtil(tc_name="").read_from_excel("SL_PH", 22, 13).strip()
        self.Non_Reserve = ExcelUtil(tc_name="").read_from_excel("SL_PH", 24, 13).strip()
        self.TV = ExcelUtil(tc_name="").read_from_excel("SL_PH", 25, 13).strip()
        self.HA_Kitchen = ExcelUtil(tc_name="").read_from_excel("SL_PH", 29, 13).strip()
        self.Common = ExcelUtil(tc_name="").read_from_excel("SL_PH", 35, 13).strip()
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        SubHeadLine_Txt = self.driver.find_element_by_xpath("//*[@_label='Hero_Text']").text.encode('utf-8')

        if "DD" in subjectlineTxt:
            if "TV" in subjectlineTxt:
                if "QLED" in subjectlineTxt:
                    print(self.TV.encode('utf-8'))
                    print(SubHeadLine_Txt)
                    assert self.TV.encode('utf-8') in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                elif "Accssry" in subjectlineTxt:
                    assert self.TV.encode('utf-8') in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."

            elif "MB" in subjectlineTxt:
                if "GALAXY" in subjectlineTxt:
                    assert self.Reserve.encode('utf-8') in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                elif "NOTE" in subjectlineTxt:
                    if "Non" in subjectlineTxt:
                        assert self.Non_Reserve.encode('utf-8') in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                    else:
                        assert self.Reserve.encode('utf-8') in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                elif "A71" in subjectlineTxt:
                    if "Non" in subjectlineTxt:
                        assert self.Non_Reserve.encode('utf-8') in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                    else:
                        assert self.Reserve.encode('utf-8') in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                elif "WEAR" in subjectlineTxt:
                    assert self.TV.encode('utf-8') in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."

            elif "CE" in subjectlineTxt:
                if "COMPUTER" in subjectlineTxt:
                    assert self.Common.encode('utf-8') in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."

            elif "HA" in subjectlineTxt:
                if "KITCHEN" in subjectlineTxt:
                    if "EPP" in subjectlineTxt:
                        assert self.Common.encode('utf-8') in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                    else:
                        assert self.HA_Kitchen.encode('utf-8') in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                elif "LAUNDRY" in subjectlineTxt:
                    assert self.Common.encode('utf-8') in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."

        logger.info(str(SubHeadLine_Txt,'utf-8'))
        logger.info(': #####  Verification Complete  #####\n')

    def get_DD_Dynamic_Module_HeadLineText(self):
        logger.info(": ##### Started Text verification #####")

        self.HL_N20 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 4, 4).strip()
        self.HL_G_FE = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 5, 4).strip()
        self.HL_Fold = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 6, 4).strip()
        self.HL_A71 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 7, 4).strip()

        Prod_Family1_Txt = self.driver.find_element_by_xpath("//*[@id='_x0000_i1037']").text.encode('utf-8')
        Prod_Family2_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline'])[2]").text.encode('utf-8')
        Prod_Family3_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline'])[3]").text.encode('utf-8')
        Prod_Family4_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline'])[4]").text.encode('utf-8')
        # subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        # if "Non" in subjectlineTxt:

        print(Prod_Family1_Txt)
        print(self.HL_N20)
        assert self.HL_N20.encode('utf-8') in Prod_Family1_Txt, "HeadLine Text NOT Matching."
        assert self.HL_G_FE.encode('utf-8') in Prod_Family2_Txt, "HeadLine Text NOT Matching."
        assert self.HL_Fold.encode('utf-8') in Prod_Family3_Txt, "HeadLine Text NOT Matching."
        assert self.HL_A71.encode('utf-8') in Prod_Family4_Txt, "HeadLine Text NOT Matching."
        logger.info(Prod_Family1_Txt)
        logger.info(Prod_Family2_Txt)
        logger.info(Prod_Family3_Txt)
        logger.info(Prod_Family4_Txt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_DD_Dynamic_Module_SubHead_LineText(self):
        logger.info(": ##### Started Text verification #####")

        self.HL_N20 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 4, 7).strip()
        self.HL_G_FE = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 5, 7).strip()
        self.HL_Fold = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 6, 7).strip()
        self.HL_A71 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 7, 7).strip()

        Prod_Family1_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline'])[1]").text.encode('utf-8')
        Prod_Family2_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline'])[2]").text.encode('utf-8')
        Prod_Family3_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline'])[3]").text.encode('utf-8')
        Prod_Family4_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline'])[4]").text.encode('utf-8')
        # subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        # if "Non" in subjectlineTxt:
        assert self.HL_N20.encode('utf-8') in Prod_Family1_Txt, "SubHead Line Text NOT Matching."
        assert self.HL_G_FE.encode('utf-8') in Prod_Family2_Txt, "SubHead Line Text NOT Matching."
        assert self.HL_Fold.encode('utf-8') in Prod_Family3_Txt, "SubHead Line Text NOT Matching."
        assert self.HL_A71.encode('utf-8') in Prod_Family4_Txt, "SubHead Line Text NOT Matching."
        logger.info(Prod_Family1_Txt)
        logger.info(Prod_Family2_Txt)
        logger.info(Prod_Family3_Txt)
        logger.info(Prod_Family4_Txt)
        logger.info(': #####  Verification Complete  #####\n')













