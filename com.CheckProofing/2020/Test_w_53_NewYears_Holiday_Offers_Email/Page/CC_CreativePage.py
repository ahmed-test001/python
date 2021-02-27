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
        self.SL = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 9).strip()
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        assert self.SL in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Validated Subject Line Text:: " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 10).strip()
        self.PH_EPP = ExcelUtil(tc_name="").read_from_excel("SL_PH", 4, 10).strip()
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        if "EPP" in subjectlineTxt:
            assert self.PH_EPP in pheaderTxt, "Pre Header Text Not Matching"
        else:
            assert self.PH in pheaderTxt, "Pre Header Text Not Matching"
        logger.info(": Validated Pre-Header Text:: " + pheaderTxt)
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

    def get_Bottom_Hero_link_validation(self):
        logger.info(": ##### Started Bottom_Hero_link_validation verification #####")
        self.PH_URL = ExcelUtil(tc_name="").read_from_excel("MiscModules", 3, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/a30ba38211f9ecb750d04061b629ba6c.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.PH_URL in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Palette_Reserve_Banner_link_validation(self):
        logger.info(": ##### Started Bottom_Hero_link_validation verification #####")
        self.PH_URL = ExcelUtil(tc_name="").read_from_excel("MiscModules", 4, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/558af8872a925c32931d04196b41545a.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.PH_URL in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Top_Hero_link_validation(self):
        logger.info(": ##### Started TOp Hero_link_validation verification #####")
        self.PH_URL = ExcelUtil(tc_name="").read_from_excel("MiscModules", 2, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@target='_blank'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        self.url_list.append(URL)
        assert self.PH_URL in URL, "Web Landing Page URL is not Matching."
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

    # def get_Module1_SubHeadLineText(self):
    #     logger.info(": ##### Started Text verification #####")
    #     subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
    #     self.SH_R = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 15).strip()
    #     self.SH_MB_EPPNR = ExcelUtil(tc_name="").read_from_excel("SL_PH", 14, 15).strip()
    #     self.SH_MB_DD_NR = ExcelUtil(tc_name="").read_from_excel("SL_PH", 26, 15).strip()
    #     self.SH_TV = ExcelUtil(tc_name="").read_from_excel("SL_PH", 5, 15).strip()
    #     self.SH_TV_EPP = ExcelUtil(tc_name="").read_from_excel("SL_PH", 15, 15).strip()
    #     self.SH_TV_DD = ExcelUtil(tc_name="").read_from_excel("SL_PH", 27, 15).strip()
    #     self.SH_MB_WEAR = ExcelUtil(tc_name="").read_from_excel("SL_PH", 10, 15).strip()
    #     self.SH_HA = ExcelUtil(tc_name="").read_from_excel("SL_PH", 11, 15).strip()
    #     self.SH_HA_EPP = ExcelUtil(tc_name="").read_from_excel("SL_PH", 21, 15).strip()
    #     self.SH_CE = ExcelUtil(tc_name="").read_from_excel("SL_PH", 7, 15).strip()
    #     self.SH_CE_EPPNR = ExcelUtil(tc_name="").read_from_excel("SL_PH", 20, 15).strip()
    #     SubHeadLine_Txt = self.driver.find_element_by_xpath("//*[@_label='Hero_Text']").text
    #     if "CC" in subjectlineTxt:
    #         if "TABCOM" in subjectlineTxt:
    #             if "EPP" in subjectlineTxt:
    #                 if "Non" in subjectlineTxt:
    #                     assert self.SH_CE_EPPNR in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
    #                     logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_CE_EPPNR)
    #             else:
    #                 assert self.SH_CE in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
    #                 logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_CE)
    #         elif "HA_KITCHEN" in subjectlineTxt:
    #             if "EPP" in subjectlineTxt:
    #                 assert self.SH_HA_EPP in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
    #                 logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_HA_EPP)
    #             else:
    #                 assert self.SH_HA in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
    #                 logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_HA)
    #         elif "HA_CLEANER" in subjectlineTxt:
    #             if "EPP" in subjectlineTxt:
    #                 assert self.SH_HA_EPP in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
    #                 logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_HA_EPP)
    #             else:
    #                 assert self.SH_HA in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
    #                 logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_HA)
    #         elif "MB" in subjectlineTxt:
    #             if "EPP" in subjectlineTxt:
    #                 if "Non" in subjectlineTxt:
    #                     # print("From Excel: "+self.SH_MB_EPPNR)
    #                     # print("From UI: "+SubHeadLine_Txt)
    #                     assert self.SH_MB_EPPNR in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
    #                     logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_MB_EPPNR)
    #                 else:
    #                     assert self.SH_R in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
    #                     logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_R)
    #             elif "WEAR" in subjectlineTxt:
    #                 assert self.SH_R in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
    #                 logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_R)
    #         elif "TV" in subjectlineTxt:
    #             if "EPP" in subjectlineTxt:
    #                 assert self.SH_TV_EPP in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
    #                 logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_TV_EPP)
    #             else:
    #                 assert self.SH_TV in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
    #                 logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_TV)
    #     elif "DD" in subjectlineTxt:
    #         if "MB" in subjectlineTxt:
    #             if "Non" in subjectlineTxt:
    #                 assert self.SH_MB_DD_NR in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
    #                 logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_MB_DD_NR)
    #             else:
    #                 assert self.SH_R in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
    #                 logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_R)
    #         elif "TV" in subjectlineTxt:
    #
    #             assert self.SH_TV_DD in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
    #             logger.info(": Validated Module-1 SubHeadLine Text:: " + self.SH_TV_DD)
    #     logger.info(': #####  Verification Complete  #####\n')

    def get_Module1_SubCopyText(self):
        logger.info(": ##### Started Module_1 SubCopy_text verification #####")
        SubCopy = self.driver.find_element_by_xpath("//*[@_label='Hero_Text']").text.encode('utf-8')
        self.SC = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 16).strip()
        assert self.SC.encode('utf-8') in SubCopy, "SubCopy Text Not Matching"
        logger.info(": Validated Module_1 Subcopy Text:: " + self.SC)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module1_SubCopyText(self):
        logger.info(": ##### Started Module_1 SubCopy_text verification #####")
        SubCopy = self.driver.find_element_by_xpath("//*[@_label='Hero_Text']").text.encode('utf-8')
        self.SC = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 16).strip()
        assert self.SC.encode('utf-8') in SubCopy, "SubCopy Text Not Matching"
        logger.info(": Validated Module_1 Subcopy Text:: " + self.SC)
        logger.info(': #####  Verification Complete  #####\n')















