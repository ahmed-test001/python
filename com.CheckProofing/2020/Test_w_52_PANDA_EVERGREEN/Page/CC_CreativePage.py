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
        self.SL_3 = ExcelUtil(tc_name="").read_from_excel("3rd", 1, 8).strip()
        self.SL_5 = ExcelUtil(tc_name="").read_from_excel("5th", 1, 8).strip()
        self.SL_10 = ExcelUtil(tc_name="").read_from_excel("10th", 1, 8).strip()
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "3M" in subjectlineTxt:
            assert self.SL_3 in subjectlineTxt, "Subject Line Text Not Matching"
        elif "5M" in subjectlineTxt:
            assert self.SL_5 in subjectlineTxt, "Subject Line Text Not Matching"
        elif "10M" in subjectlineTxt:
            assert self.SL_10 in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Validated Subject Line Text:: " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH_3 = ExcelUtil(tc_name="").read_from_excel("3rd", 2, 8).strip()
        self.PH_5 = ExcelUtil(tc_name="").read_from_excel("5th", 2, 8).strip()
        self.PH_10 = ExcelUtil(tc_name="").read_from_excel("10th", 2, 8).strip()
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        if "3M" in subjectlineTxt:
            assert self.PH_3 in pheaderTxt, "Pre Header Text Not Matching"
        elif "5M" in subjectlineTxt:
            assert self.PH_5 in pheaderTxt, "Pre Header Text Not Matching"
        elif "10M" in subjectlineTxt:
            assert self.PH_10 in pheaderTxt, "Pre Header Text Not Matching"
        logger.info(": Validated Pre-Header Text:: " + pheaderTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_link_validation(self):
        logger.info(": ##### Started pre_header_link_validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH_URL_N20 = ExcelUtil(tc_name="").read_from_excel("URL", 30, 5)
        self.PH_URL_N20U = ExcelUtil(tc_name="").read_from_excel("URL", 31, 5)
        self.PH_URL_S20 = ExcelUtil(tc_name="").read_from_excel("URL", 33, 5)
        self.PH_URL_S20P = ExcelUtil(tc_name="").read_from_excel("URL", 34, 5)
        self.PH_URL_S20U = ExcelUtil(tc_name="").read_from_excel("URL", 35, 5)
        self.PH_URL_ZFlip = ExcelUtil(tc_name="").read_from_excel("URL", 37, 5)
        self.PH_URL_ZFold2 = ExcelUtil(tc_name="").read_from_excel("URL", 38, 5)
        self.PH_URL_S10E = ExcelUtil(tc_name="").read_from_excel("URL", 39, 5)
        self.PH_URL_S10 = ExcelUtil(tc_name="").read_from_excel("URL", 40, 5)
        self.PH_URL_S10P = ExcelUtil(tc_name="").read_from_excel("URL", 41, 5)
        self.PH_URL_N10 = ExcelUtil(tc_name="").read_from_excel("URL", 43, 5)
        self.PH_URL_N10P = ExcelUtil(tc_name="").read_from_excel("URL", 44, 5)
        self.PH_URL_A51 = ExcelUtil(tc_name="").read_from_excel("URL", 46, 5)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@target='_blank'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        if "N20" in subjectlineTxt:
            assert self.PH_URL_N20 in URL, "Web Landing Page URL is not Matching."
        elif "N20 Ultra" in subjectlineTxt:
            assert self.PH_URL_N20U in URL, "Web Landing Page URL is not Matching."
        elif "S20" in subjectlineTxt:
            assert self.PH_URL_S20 in URL, "Web Landing Page URL is not Matching."
        elif "S20+" in subjectlineTxt:
            assert self.PH_URL_S20P in URL, "Web Landing Page URL is not Matching."
        elif "S20 Ultra" in subjectlineTxt:
            assert self.PH_URL_S20U in URL, "Web Landing Page URL is not Matching."
        elif "Z Flip" in subjectlineTxt:
            assert self.PH_URL_ZFlip in URL, "Web Landing Page URL is not Matching."
        elif "Z Fold2" in subjectlineTxt:
            assert self.PH_URL_ZFold2 in URL, "Web Landing Page URL is not Matching."
        elif "S10e" in subjectlineTxt:
            assert self.PH_URL_S10E in URL, "Web Landing Page URL is not Matching."
        elif "S10" in subjectlineTxt:
            assert self.PH_URL_S10 in URL, "Web Landing Page URL is not Matching."
        elif "S10+" in subjectlineTxt:
            assert self.PH_URL_S10P in URL, "Web Landing Page URL is not Matching."
        elif "Note10" in subjectlineTxt:
            assert self.PH_URL_N10 in URL, "Web Landing Page URL is not Matching."
        elif "Note10+" in subjectlineTxt:
            assert self.PH_URL_N10P in URL, "Web Landing Page URL is not Matching."
        elif "A51" in subjectlineTxt:
            assert self.PH_URL_A51 in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_giveWonder_link_validation(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
            logger.info(": ##### Started GiveWonder Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("MiscModules", 2, 14)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1042']"))).click()
            Module_1_URL = self.driver.current_url
            assert self.url_path in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy Watch3 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')
        else:
            logger.info(": ##### Started GiveWonder Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("MiscModules", 2, 14)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1042']"))).click()
            Module_1_URL = self.driver.current_url
            assert self.url_path in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy Watch3 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

    def get_Top_Hero_link_validation(self):
        logger.info(": ##### Started pre_header_link_validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH_URL_N20 = ExcelUtil(tc_name="").read_from_excel("URL", 30, 5)
        self.PH_URL_N20U = ExcelUtil(tc_name="").read_from_excel("URL", 31, 5)
        self.PH_URL_S20 = ExcelUtil(tc_name="").read_from_excel("URL", 33, 5)
        self.PH_URL_S20P = ExcelUtil(tc_name="").read_from_excel("URL", 34, 5)
        self.PH_URL_S20U = ExcelUtil(tc_name="").read_from_excel("URL", 35, 5)
        self.PH_URL_ZFlip = ExcelUtil(tc_name="").read_from_excel("URL", 37, 5)
        self.PH_URL_ZFold2 = ExcelUtil(tc_name="").read_from_excel("URL", 38, 5)
        self.PH_URL_S10E = ExcelUtil(tc_name="").read_from_excel("URL", 39, 5)
        self.PH_URL_S10 = ExcelUtil(tc_name="").read_from_excel("URL", 40, 5)
        self.PH_URL_S10P = ExcelUtil(tc_name="").read_from_excel("URL", 41, 5)
        self.PH_URL_N10 = ExcelUtil(tc_name="").read_from_excel("URL", 43, 5)
        self.PH_URL_N10P = ExcelUtil(tc_name="").read_from_excel("URL", 44, 5)
        self.PH_URL_A51 = ExcelUtil(tc_name="").read_from_excel("URL", 46, 5)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@target='_blank'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        if "N20" in subjectlineTxt:
            assert self.PH_URL_N20 in URL, "Web Landing Page URL is not Matching."
        elif "N20 Ultra" in subjectlineTxt:
            assert self.PH_URL_N20U in URL, "Web Landing Page URL is not Matching."
        elif "S20" in subjectlineTxt:
            assert self.PH_URL_S20 in URL, "Web Landing Page URL is not Matching."
        elif "S20+" in subjectlineTxt:
            assert self.PH_URL_S20P in URL, "Web Landing Page URL is not Matching."
        elif "S20 Ultra" in subjectlineTxt:
            assert self.PH_URL_S20U in URL, "Web Landing Page URL is not Matching."
        elif "Z Flip" in subjectlineTxt:
            assert self.PH_URL_ZFlip in URL, "Web Landing Page URL is not Matching."
        elif "Z Fold2" in subjectlineTxt:
            assert self.PH_URL_ZFold2 in URL, "Web Landing Page URL is not Matching."
        elif "S10e" in subjectlineTxt:
            assert self.PH_URL_S10E in URL, "Web Landing Page URL is not Matching."
        elif "S10" in subjectlineTxt:
            assert self.PH_URL_S10 in URL, "Web Landing Page URL is not Matching."
        elif "S10+" in subjectlineTxt:
            assert self.PH_URL_S10P in URL, "Web Landing Page URL is not Matching."
        elif "Note10" in subjectlineTxt:
            assert self.PH_URL_N10 in URL, "Web Landing Page URL is not Matching."
        elif "Note10+" in subjectlineTxt:
            assert self.PH_URL_N10P in URL, "Web Landing Page URL is not Matching."
        elif "A51" in subjectlineTxt:
            assert self.PH_URL_A51 in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
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
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.SH_R = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 15).strip()
        self.SH_MB_EPPNR = ExcelUtil(tc_name="").read_from_excel("SL_PH", 14, 15).strip()
        self.SH_MB_DD_NR = ExcelUtil(tc_name="").read_from_excel("SL_PH", 26, 15).strip()
        self.SH_TV = ExcelUtil(tc_name="").read_from_excel("SL_PH", 5, 15).strip()
        self.SH_TV_EPP = ExcelUtil(tc_name="").read_from_excel("SL_PH", 15, 15).strip()
        self.SH_TV_DD = ExcelUtil(tc_name="").read_from_excel("SL_PH", 27, 15).strip()
        self.SH_MB_WEAR = ExcelUtil(tc_name="").read_from_excel("SL_PH", 10, 15).strip()
        self.SH_HA = ExcelUtil(tc_name="").read_from_excel("SL_PH", 11, 15).strip()
        self.SH_HA_EPP = ExcelUtil(tc_name="").read_from_excel("SL_PH", 21, 15).strip()
        self.SH_CE = ExcelUtil(tc_name="").read_from_excel("SL_PH", 7, 15).strip()
        self.SH_CE_EPPNR = ExcelUtil(tc_name="").read_from_excel("SL_PH", 20, 15).strip()
        SubHeadLine_Txt = self.driver.find_element_by_xpath("//*[@_label='Hero_Text']").text
        if "CC" in subjectlineTxt:
            if "TABCOM" in subjectlineTxt:
                if "EPP" in subjectlineTxt:
                    if "Non" in subjectlineTxt:
                        assert self.SH_CE_EPPNR in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                        logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_CE_EPPNR)
                else:
                    assert self.SH_CE in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                    logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_CE)
            elif "HA_KITCHEN" in subjectlineTxt:
                if "EPP" in subjectlineTxt:
                    assert self.SH_HA_EPP in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                    logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_HA_EPP)
                else:
                    assert self.SH_HA in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                    logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_HA)
            elif "HA_CLEANER" in subjectlineTxt:
                if "EPP" in subjectlineTxt:
                    assert self.SH_HA_EPP in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                    logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_HA_EPP)
                else:
                    assert self.SH_HA in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                    logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_HA)
            elif "MB" in subjectlineTxt:
                if "EPP" in subjectlineTxt:
                    if "Non" in subjectlineTxt:
                        # print("From Excel: "+self.SH_MB_EPPNR)
                        # print("From UI: "+SubHeadLine_Txt)
                        assert self.SH_MB_EPPNR in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                        logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_MB_EPPNR)
                    else:
                        assert self.SH_R in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                        logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_R)
                elif "WEAR" in subjectlineTxt:
                    assert self.SH_R in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                    logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_R)
            elif "TV" in subjectlineTxt:
                if "EPP" in subjectlineTxt:
                    assert self.SH_TV_EPP in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                    logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_TV_EPP)
                else:
                    assert self.SH_TV in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                    logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_TV)
        elif "DD" in subjectlineTxt:
            if "MB" in subjectlineTxt:
                if "Non" in subjectlineTxt:
                    assert self.SH_MB_DD_NR in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                    logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_MB_DD_NR)
                else:
                    assert self.SH_R in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                    logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_R)
            elif "TV" in subjectlineTxt:

                assert self.SH_TV_DD in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
                logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_TV_DD)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module1_SubCopyText(self):
        logger.info(": ##### Started Module_1 SubCopy_text verification #####")
        SubCopy = self.driver.find_element_by_xpath("//*[@_label='Hero_Text']").text.encode('utf-8')
        self.SC = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 16).strip()
        assert self.SC.encode('utf-8') in SubCopy, "SubCopy Text Not Matching"
        logger.info(": Validated Module_1 Subcopy Text:: " + self.SC)
        logger.info(': #####  Verification Complete  #####\n')
















