import json
import os
import sys
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Utility_Files.ExcelReaderUtil import ExcelUtil
from PageClass.UrlSegmentPage import URLSegmentPage
from PageClass.BasePageClass import BasePage
from Utility_Files.HTMLTestRunner import stdout_redirector
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class ModuleURLPage(BasePage):

    """Pre-Header Link below:"""
    def get_pre_header_link_validation(self, sheet_name, sheet_row,sheet_column,xpath_loc):
            logger.info(": ##### Started pre_header_link_validation verification #####")
            self.PH = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column)).strip()
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            URL = self.driver.current_url
            assert self.PH in URL, "Web Landing Page URL is not Matching."
            logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
            URLSegmentPage.get_segment()
            URLSegmentPage.get_URL_Segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

    # def get_pre_header_link_validation(self, sheet_name, sheet_row,sheet_column,xpath_loc):
    #     if sheet_row != "" or sheet_column != "":
    #         logger.info(": ##### Started pre_header_link_validation verification #####")
    #         self.PH = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column)).strip()
    #         parent_window = self.driver.current_window_handle
    #         self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
    #         all_windows = self.driver.window_handles
    #         child_window = [window for window in all_windows if window != parent_window][0]
    #         self.driver.switch_to.window(child_window)
    #         URL = self.driver.current_url
    #         assert self.PH in URL, "Web Landing Page URL is not Matching."
    #         logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
    #         with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
    #         URLSegmentPage.get_segment()
    #         URLSegmentPage.get_URL_Segment_validation()
    #         self.driver.close()
    #         self.driver.switch_to.window(parent_window)
    #         logger.info(': #####  Verification Complete  #####\n')
    #     else:
    #         logger.info(": Skip the Test Case.")

    """Hero TOP/BELOW Link below:"""

    def get_Top_Hero_CTA_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        if sheet_row != "" or sheet_column != "":
            logger.info(": ##### Started Hero_CTA_link_validation #####")
            self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            URL = self.driver.current_url
            assert self.url in URL, "Web Landing Page URL is not Matching."
            logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
            URLSegmentPage.get_segment()
            URLSegmentPage.get_URL_Segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
        else:
            logger.info(": Skip the Test Case.")

    def get_Footer_Hero_CTA_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        if sheet_row != "" or sheet_column != "":
            logger.info(": ##### Started Footer_Hero_CTA_link_validation #####")
            self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            URL = self.driver.current_url
            assert self.url in URL, "Web Landing Page URL is not Matching."
            logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
            URLSegmentPage.get_segment()
            URLSegmentPage.get_URL_Segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
        else:
            logger.info(": Skip the Test Case.")

    """Module_1 Link below:"""

    def get_Module1_Banner_link_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        if sheet_row != "" or sheet_column != "":
            logger.info(": ##### Started Module_1_Banner_link_validation #####")
            self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            URL = self.driver.current_url
            assert self.url in URL, "Web Landing Page URL is not Matching."
            logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
            URLSegmentPage.get_segment()
            URLSegmentPage.get_URL_Segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
        else:
            logger.info(": Skip the Test Case.")

    def get_Module1_CTA_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_1_CTA_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module1_mini_CTA1_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_1_mini_CTA_1_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module1_mini_CTA2_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_1_mini_CTA_2_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module1_mini_CTA3_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_1_mini_CTA_3_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    """Module_2 Link below:"""

    def get_Module2_Banner_link_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_2_Banner_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module2_CTA_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_2_CTA_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module2_mini_CTA1_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_2_mini_CTA_1_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module2_mini_CTA2_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_2_mini_CTA_2_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module2_mini_CTA3_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_2_mini_CTA_3_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    """Module_3 Link below:"""

    def get_Module3_Banner_link_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_3_Banner_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module3_CTA_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_3_CTA_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module3_mini_CTA1_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_3_mini_CTA_1_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module3_mini_CTA2_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_3_mini_CTA_2_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module3_mini_CTA3_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_3_mini_CTA_3_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    """Module_4 Link below:"""

    def get_Module4_Banner_link_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_4_Banner_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module4_CTA_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_4_CTA_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module4_mini_CTA1_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_4_mini_CTA_1_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module4_mini_CTA2_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_4_mini_CTA_2_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module4_mini_CTA3_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_4_mini_CTA_3_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    """Module_5 Link below:"""

    def get_Module5_Banner_link_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_5_Banner_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module5_CTA_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_5_CTA_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module5_mini_CTA1_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_5_mini_CTA_1_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module5_mini_CTA2_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_5_mini_CTA_2_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module5_mini_CTA3_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Module_5_mini_CTA_3_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegmentPage.get_segment()
        URLSegmentPage.get_URL_Segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')






















