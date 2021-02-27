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
        self.SL = ExcelUtil(tc_name="").read_from_excel("Generic", 1, 8).strip()
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        assert self.SL in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Validated Subject Line Text:: " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        # subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH = ExcelUtil(tc_name="").read_from_excel("Generic", 2, 8).strip()
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        assert self.PH in pheaderTxt, "Pre Header Text Not Matching"
        logger.info(": Validated Pre-Header Text:: " + pheaderTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_link_validation(self):
        logger.info(": ##### Started pre_header_link_validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH_URL_generic = ExcelUtil(tc_name="").read_from_excel("Generic", 6, 8)
        self.PH_URL_T700 = ExcelUtil(tc_name="").read_from_excel("Test-700", 6, 8)
        self.PH_URL_T550 = ExcelUtil(tc_name="").read_from_excel("Test-550", 6, 8)
        self.PH_URL_T350 = ExcelUtil(tc_name="").read_from_excel("Test-350", 6, 8)
        self.PH_URL_T250 = ExcelUtil(tc_name="").read_from_excel("Test-250", 6, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@target='_blank'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.PH_URL_generic in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Top_Hero_link_validation(self):
        logger.info(": ##### Started TOp Hero_link_validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH = ExcelUtil(tc_name="").read_from_excel("Generic", 6, 8)
        self.PH_URL_generic = ExcelUtil(tc_name="").read_from_excel("Generic", 6, 8)
        self.PH_URL_T700 = ExcelUtil(tc_name="").read_from_excel("Test-700", 6, 8)
        self.PH_URL_T550 = ExcelUtil(tc_name="").read_from_excel("Test-550", 6, 8)
        self.PH_URL_T350 = ExcelUtil(tc_name="").read_from_excel("Test-350", 6, 8)
        self.PH_URL_T250 = ExcelUtil(tc_name="").read_from_excel("Test-250", 6, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@target='_blank'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.PH in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module1_SubCopyText(self):
        logger.info(": ##### Started Module_1 SubCopy_text verification #####")
        SubCopy = self.driver.find_element_by_xpath("//*[@_label='Hero_Text']").text.encode('utf-8')
        self.SC = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 16).strip()
        assert self.SC.encode('utf-8') in SubCopy, "SubCopy Text Not Matching"
        logger.info(": Validated Module_1 Subcopy Text:: " + self.SC)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_a_text_validation(self):
        logger.info(": ##### Started footer condition text verification #####")
        self.SL = ExcelUtil(tc_name="").read_from_excel("Generic", 7, 8).strip()
        # footerTxt1 = self.driver.find_element_by_xpath("(//span)[22]").text.encode('utf-8')
        footerTxt1 = self.driver.find_element_by_xpath("(//span)[22]").text
        print(self.SL)
        print(footerTxt1)
        assert self.SL in footerTxt1, "Subject Line Text Not Matching"
        logger.info(": Validate footer condition text:: " + footerTxt1)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_a1_text_validation(self):
        logger.info(": ##### Started footer condition text verification #####")
        self.SL = ExcelUtil(tc_name="").read_from_excel("Generic", 6, 10).strip()
        footerTxt1 = self.driver.find_element_by_xpath("(//span)[101]").text.encode('utf-8')
        print("from excel::" + str(self.SL.encode('utf-8')))
        print("from html::" + str(footerTxt1))
        assert self.SL.encode('utf-8') in footerTxt1, "Subject Line Text Not Matching"
        logger.info(": Validate footer condition text:: " + str(footerTxt1))
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_a2_text_validation(self):
        logger.info(": ##### Started footer condition text verification #####")
        # self.SL = ExcelUtil(tc_name="").read_from_excel("Generic", 7, 8).strip()
        footerTxt2 = self.driver.find_element_by_xpath("(//span)[103]").text.encode('utf-8')
        # assert self.SL.encode('utf-8') in footerTxt2, "Subject Line Text Not Matching"
        logger.info(": Validate footer condition text:: " + str(footerTxt2))
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_a3_text_validation(self):
        logger.info(": ##### Started footer condition text verification #####")
        # self.SL = ExcelUtil(tc_name="").read_from_excel("Generic", 7, 8).strip()
        footerTxt3 = self.driver.find_element_by_xpath("(//span)[110]").text.encode('utf-8')
        # assert self.SL.encode('utf-8') in footerTxt3, "Subject Line Text Not Matching"
        logger.info(": Validate footer condition text:: " + str(footerTxt3))
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_a4_text_validation(self):
        logger.info(": ##### Started footer condition text verification #####")
        # self.SL = ExcelUtil(tc_name="").read_from_excel("Generic", 7, 8).strip()
        footerTxt4 = self.driver.find_element_by_xpath("(//span)[113]").text.encode('utf-8')
        # assert self.SL.encode('utf-8') in footerTxt4, "Subject Line Text Not Matching"
        logger.info(": Validate footer condition text:: " + str(footerTxt4))
        logger.info(': #####  Verification Complete  #####\n')
















