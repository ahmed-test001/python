import os
import sys
import logging
import time

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


class CC_CreativePage(BasePage):

    def get_EPP_or_NonEPP_verification(self):
        logger.info(": ##### Started EPP version verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1033']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), "Web Element not Displayed."
            logger.info(": successfully verified EPP version is present.")
        else:
            logger.info(': successfully verified EPP version NOT present.')
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_subjectLine_text_validation(self):
        logger.info(": ##### Started subjectLine_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text.encode('utf-8')
        self.SL = ExcelUtil(tc_name="").read_from_excel("SL_PH", 2, 8).strip()
        assert self.SL.encode('utf-8') in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Validated Subject Line Text:: " + str(subjectlineTxt,'utf-8'))
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text.encode('utf-8')
        self.PH = ExcelUtil(tc_name="").read_from_excel("SL_PH", 2, 9).strip()
        assert self.PH.encode('utf-8') in pheaderTxt, "Pre Header Text Not Matching"
        logger.info(": Validated Pre-Header Text:: " + str(pheaderTxt,'utf-8'))
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_link_validation(self):
        logger.info(": ##### Started pre_header_link_validation verification #####")
        self.PH_URL = ExcelUtil(tc_name="").read_from_excel("MiscModules", 2, 14)
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
        self.url_path = ExcelUtil(tc_name="").read_from_excel("MiscModules", 3, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/964160ea34117060e7eb9df0f08d4100.jpg']"))).click()
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

    def get_giveWonder_link_validation2(self):
        logger.info(": ##### Started GiveWonder Module URL verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "DD" in subjectlineTxt:
            self.url_path = ExcelUtil(tc_name="").read_from_excel("MiscModules", 3, 14)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1042']"))).click()
            givewonderURL = self.driver.current_url
            assert self.url_path in givewonderURL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Web Landing page URL:\n" + givewonderURL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(givewonderURL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
        else:
            self.url_path = ExcelUtil(tc_name="").read_from_excel("MiscModules", 3, 14)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1043']"))).click()
            givewonderURL = self.driver.current_url
            assert self.url_path in givewonderURL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Web Landing page URL:\n" + givewonderURL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(givewonderURL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
        logger.info(': #####  Verification Complete  #####\n')

    def get_Top_Hero_link_validation(self):
        logger.info(": ##### Started Top_Hero Module URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("MiscModules", 2, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/a9b96e25b407c0e94c0ce216c4d5c777.jpg']"))).click()
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

    def get_Top_Hero_link_validation2(self):
        logger.info(": ##### Started Top_Hero Module URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("MiscModules", 2, 14)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1034']"))).click()
        TopHeroURL = self.driver.current_url
        assert self.url_path in TopHeroURL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Web Landing page URL:\n" + TopHeroURL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(TopHeroURL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.back()
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module1_HeadLineText(self):
        logger.info(": ##### Started Text verification #####")
        self.Reserve = ExcelUtil(tc_name="").read_from_excel("SL_PH", 4, 13).strip()
        # self.Non_Reserve = ExcelUtil(tc_name="").read_from_excel("SL_PH", 5, 13).strip()

        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        SubHeadLine_Txt = self.driver.find_element_by_xpath("//*[@_label='Hero_Text']").text.encode('utf-8')

        if "CC" in subjectlineTxt:
                assert self.Reserve.encode('utf-8') in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                logger.info(": Validated Module-1 SubHeadLine Text:: " + self.Reserve)
        else:
            logger.info(': No Module-1 SubHeadLine Text Present.')
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module1_SubHeadLineText(self):
        logger.info(": ##### Started Text verification #####")
        self.SH_R = ExcelUtil(tc_name="").read_from_excel("SL_PH", 2, 13).strip()
        self.SH_Non_Reserve = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 13).strip()
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        # SubHeadLine_Txt = self.driver.find_element_by_xpath("//*[@_label='Hero_Text']").text.encode('utf-8')
        SubHeadLine_Txt = self.driver.find_element_by_xpath("//*[@_label='Hero_Text']").text

        if "Non" not in subjectlineTxt:
            assert self.SH_R in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
        else:
            assert self.SH_Non_Reserve in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
        logger.info(": Validated Module-1 SubHeadLine Text:: " + SubHeadLine_Txt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module1_SubCopyText(self):

        logger.info(": ##### Started Module_1 SubCopy_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        SubCopy = self.driver.find_element_by_xpath("//*[@_label='Hero_Text']").text.encode('utf-8')
        self.SC_Galaxy_R = ExcelUtil(tc_name="").read_from_excel("SL_PH1", 1, 10).strip()
        self.SC_Galaxy_NR = ExcelUtil(tc_name="").read_from_excel("SL_PH1", 1, 11).strip()
        self.SC_TV = ExcelUtil(tc_name="").read_from_excel("SL_PH1", 2, 10).strip()
        self.SC_TABLET = ExcelUtil(tc_name="").read_from_excel("SL_PH1", 3, 10).strip()
        self.SC_WEAR = ExcelUtil(tc_name="").read_from_excel("SL_PH1", 4, 10).strip()
        self.SC_COMPUTER = ExcelUtil(tc_name="").read_from_excel("SL_PH1", 5, 10).strip()
        self.SC_HA = ExcelUtil(tc_name="").read_from_excel("SL_PH1", 6, 10).strip()
        if "MB" in subjectlineTxt:
            if "GALAXY" in subjectlineTxt:
                if "Non" not in subjectlineTxt:
                    assert self.SC_Galaxy_R.encode('utf-8') in SubCopy, "SubCopy Text Not Matching"
                else:
                    assert self.SC_Galaxy_NR.encode('utf-8') in SubCopy, "SubCopy Text Not Matching"
            elif "TABLET" in subjectlineTxt:
                assert self.SC_TABLET.encode('utf-8') in SubCopy, "SubCopy Text Not Matching"
            elif "WEAR" in subjectlineTxt:
                assert self.SC_WEAR.encode('utf-8') in SubCopy, "SubCopy Text Not Matching"
        elif "CE" in subjectlineTxt:
            assert self.SC_COMPUTER.encode('utf-8') in SubCopy, "SubCopy Text Not Matching"
        elif "HA" in subjectlineTxt:
            assert self.SC_HA.encode('utf-8') in SubCopy, "SubCopy Text Not Matching"
        elif "TV" in subjectlineTxt:
            assert self.SC_TV.encode('utf-8') in SubCopy, "SubCopy Text Not Matching"

        logger.info(": Validated Module_1 Subcopy Text:: " + str(SubCopy,'utf-8'))
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_Dynamic_Module_HeadLineText(self):
        logger.info(": ##### Started Text verification #####")

        self.HL_MB = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 3).strip()
        self.HL_TV = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 7, 3).strip()
        self.HL_HA = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 9, 3).strip()
        self.HL_WEAR = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 11, 3).strip()
        self.HL_COM = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 13, 3).strip()
        self.HL_TABLET = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 15, 3).strip()

        Prod_Family1_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline_1'])[1]").text.encode('utf-8')
        Prod_Family2_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline'])[2]").text.encode('utf-8')
        Prod_Family3_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline'])[3]").text.encode('utf-8')
        Prod_Family4_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline'])[4]").text.encode('utf-8')
        Prod_Family5_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline'])[5]").text.encode('utf-8')
        Prod_Family6_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline'])[6]").text.encode('utf-8')
        # subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        # if "Non" in subjectlineTxt:
        assert self.HL_MB.encode('utf-8') in Prod_Family1_Txt, "HeadLine Text NOT Matching."
        assert self.HL_TV.encode('utf-8') in Prod_Family2_Txt, "HeadLine Text NOT Matching."
        assert self.HL_HA.encode('utf-8') in Prod_Family3_Txt, "HeadLine Text NOT Matching."
        assert self.HL_WEAR.encode('utf-8') in Prod_Family4_Txt, "HeadLine Text NOT Matching."
        assert self.HL_COM.encode('utf-8') in Prod_Family5_Txt, "HeadLine Text NOT Matching."
        assert self.HL_TABLET.encode('utf-8') in Prod_Family6_Txt, "HeadLine Text NOT Matching."
        logger.info(Prod_Family1_Txt)
        logger.info(Prod_Family2_Txt)
        logger.info(Prod_Family3_Txt)
        logger.info(Prod_Family4_Txt)
        logger.info(Prod_Family5_Txt)
        logger.info(Prod_Family6_Txt)
        logger.info(': #####  Verification Complete  #####\n')


    def get_CC_Dynamic_Module_SubCopyText(self):
        logger.info(": ##### Started Text verification #####")

        self.SC_MB = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 5).strip()
        self.SC_TV = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 4, 5).strip()
        self.SC_WEAR = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 5, 5).strip()
        self.SC_COM = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 5).strip()
        self.SC_HA = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 7, 5).strip()

        Prod_Family1_Txt = self.driver.find_element_by_xpath("(//*[@_label='Module_Text'])[1]").text.encode('utf-8')
        Prod_Family2_Txt = self.driver.find_element_by_xpath("(//*[@_label='Module_Text'])[2]").text.encode('utf-8')
        Prod_Family3_Txt = self.driver.find_element_by_xpath("(//*[@_label='Module_Text'])[3]").text.encode('utf-8')
        Prod_Family4_Txt = self.driver.find_element_by_xpath("(//*[@_label='Module_Text'])[4]").text.encode('utf-8')
        Prod_Family5_Txt = self.driver.find_element_by_xpath("(//*[@_label='Module_Text'])[5]").text.encode('utf-8')
        # # subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        #
        # # if "CC" in subjectlineTxt:
        # print(self.SC_MB.encode('utf-8'))
        # print(Prod_Family1_Txt)
        assert self.SC_MB.encode('utf-8') in Prod_Family1_Txt, "SubCopy Text NOT Matching."
        assert self.SC_TV.encode('utf-8') in Prod_Family2_Txt, "SubCopy Text NOT Matching."
        assert self.SC_WEAR.encode('utf-8') in Prod_Family3_Txt, "SubCopy Text NOT Matching."
        assert self.SC_COM.encode('utf-8') in Prod_Family4_Txt, "SubCopy Text NOT Matching."
        assert self.SC_HA.encode('utf-8') in Prod_Family5_Txt, "SubCopy Text NOT Matching."
        # else:
        # assert self.SC_MB.encode('utf-8') in Prod_Family1_Txt, "SubCopy Text NOT Matching."
        # assert self.SC_TV.encode('utf-8') in Prod_Family2_Txt, "SubCopy Text NOT Matching."
        # assert self.SC_WEAR.encode('utf-8') in Prod_Family3_Txt, "SubCopy Text NOT Matching."
        # assert self.SC_COM.encode('utf-8') in Prod_Family4_Txt, "SubCopy Text NOT Matching."
        # assert self.SC_HA.encode('utf-8') in Prod_Family5_Txt, "SubCopy Text NOT Matching."
        logger.info(': #####  Verification Complete  #####\n')














