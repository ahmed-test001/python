import os
import sys
import logging

from selenium.common.exceptions import NoSuchElementException
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


class TabletPage(BasePage):

    def get_Tablet_Mod(self):
        logger.info(": ##### Started TABLET S7 & S7 Plus URL verification #####\n")
        self.url_path3 = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 9, 8)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/ba391ea8db66fa42d68c3bcd900cf9aa.jpg']"))).click()
        parent_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Module_1_URL = self.driver.current_url
        assert self.url_path3 in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified S7 & S7 Plus Landing page URL:" + Module_1_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')


    def get_Tablet_ShopAll(self):
        logger.info(": ##### Started TABLET_ShopAll Banner URL verification #####\n")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/97b0f57ab9d6e6fa423840e52cbd7175.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        self.url_list.append(ShopAll_URL)
        assert ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'Deals_tablet') in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Tablet_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_MB_TABLET_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "MB_TABLET" in subjectlineTxt:
            logger.info(": ##### Started MB_TABLET Module_1 URL verification #####\n")
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/0b2d29f05a32ff1aa348a0f4febacc28.jpg']"))).click()
            parent_window = self.driver.current_window_handle
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            # assert ReadConfig.read_w45_HolidayDealsT1_configData('DATA','MB_S20FE') in Pre_Header_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_TABLET Landing page URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

    def get_TABLET_Module1(self):
        logger.info(": ##### Started TABLET Module_1 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CCModuleCopy", 15, 7)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1037']"))).click()
        URL = self.driver.current_url
        assert self.url_path in URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MOBILE_ACCESSORIES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.back()
        logger.info(': #####  Verification Complete  #####\n')

    def get_TABLET_Module2(self):
        logger.info(": ##### Started TABLET Module_2 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CCModuleCopy", 15, 7)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1038']"))).click()
        URL = self.driver.current_url
        assert self.url_path in URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MOBILE_ACCESSORIES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.back()
        logger.info(': #####  Verification Complete  #####\n')

    def get_TABLET_Module3(self):
        logger.info(": ##### Started TABLET Module_3 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CCModuleCopy", 15, 7)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1039']"))).click()
        URL = self.driver.current_url
        assert self.url_path in URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MOBILE_ACCESSORIES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.back()
        logger.info(': #####  Verification Complete  #####\n')

    def get_TABLET_Module4(self):
        logger.info(": ##### Started TABLET Module_4 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CCModuleCopy", 15, 7)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1040']"))).click()
        URL = self.driver.current_url
        print(self.url_path)
        assert self.url_path in URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MOBILE_ACCESSORIES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.back()
        logger.info(': #####  Verification Complete  #####\n')

    def get_TABLET_Module5(self):
        logger.info(": ##### Started TABLET Module_5 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CCModuleCopy", 15, 7)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1041']"))).click()
        URL = self.driver.current_url
        assert self.url_path in URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MOBILE_ACCESSORIES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.back()
        logger.info(': #####  Verification Complete  #####\n')

    def get_TABLET_Module6(self):
        logger.info(": ##### Started TABLET Module_6 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CCModuleCopy", 15, 7)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1041']"))).click()
        URL = self.driver.current_url
        assert self.url_path in URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MOBILE_ACCESSORIES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.back()
        logger.info(': #####  Verification Complete  #####\n')



