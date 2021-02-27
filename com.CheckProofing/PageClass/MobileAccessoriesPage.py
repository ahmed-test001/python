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


class MobileAccessoriesPage(BasePage):
    def get_Buds_live(self):
        logger.info(": ##### Started Buds_Live Module URL verification #####")
        self.url_path3 = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 7, 8)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/f563bb84d759bbc6585b86a01a620b2d.jpg']"))).click()
        parent_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Module_1_URL = self.driver.current_url
        assert self.url_path3 in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Buds_Live Landing page URL:" + Module_1_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(Module_1_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Galaxy_watch3(self):
        logger.info(": ##### Started Galaxy Watch3 Module URL verification #####")
        self.url_path3 = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 8, 8)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/ac378dcdff8dd3eef4bea40f7833c3f6.jpg']"))).click()
        parent_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Module_1_URL = self.driver.current_url
        assert self.url_path3 in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Galaxy Watch3 Landing page URL:" + Module_1_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')


    def get_WEAR_Mod(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
            logger.info(": ##### Started Buds_Live Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 20, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1040']"))).click()
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert self.url_path in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Buds_Live Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Galaxy Watch3 Titanium Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 21, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1041']"))).click()
            Module_1_URL = self.driver.current_url
            assert self.url_path in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy Watch3 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Galaxy Watch3 Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 22, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1042']"))).click()
            Module_1_URL = self.driver.current_url
            assert self.url_path in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy Watch3 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Galaxy Watch Active 2 URL verification #####")
            self.url_path2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 23, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1043']"))).click()
            Module_2_URL = self.driver.current_url
            assert self.url_path2 in Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy Watch active 2 Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')
        else:
            logger.info(": ##### Started Buds_Live Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 20, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1039']"))).click()
            Module_1_URL = self.driver.current_url
            assert self.url_path in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Buds_Live Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Galaxy Watch3 Titanium Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 21, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1040']"))).click()
            Module_1_URL = self.driver.current_url
            assert self.url_path in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy Watch3 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Galaxy Watch3 Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 22, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1041']"))).click()
            Module_1_URL = self.driver.current_url
            assert self.url_path in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy Watch3 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Galaxy Watch Active 2 URL verification #####")
            self.url_path2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 23, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1042']"))).click()
            Module_2_URL = self.driver.current_url
            assert self.url_path2 in Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy Watch active 2 Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

    def get_CC_WEAR_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
                logger.info(": ##### Started WEAR Module URL verification #####")
                self.url_MB = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 7)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1040']"))).click()
                Mod_URL = self.driver.current_url
                assert self.url_MB in Mod_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified WEAR Module URL:" + Mod_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Mod_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started MB_GALAXY Module URL verification #####")
                self.url_MB = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 2, 7)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1041']"))).click()
                Mod_URL = self.driver.current_url
                assert self.url_MB in Mod_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified MB_GALAXY Module URL:" + Mod_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Mod_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started COMPUTER Module URL verification #####")
                self.url_MB = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 8, 7)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1042']"))).click()
                Mod_URL = self.driver.current_url
                assert self.url_MB in Mod_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified COMPUTER Module URL:" + Mod_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Mod_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started TV & HA Module URL verification #####")
                self.url_TV = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 4, 7)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1044']"))).click()
                TV_URL = self.driver.current_url
                assert self.url_TV in TV_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified TV & Audio Module URL:" + TV_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(TV_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                self.url_HA = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 4, 10)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1045']"))).click()
                HA_URL = self.driver.current_url
                assert self.url_HA in HA_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified HA Module URL:" + HA_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(HA_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')
        else:
                logger.info(": ##### Started WEAR Module URL verification #####")
                self.url_MB = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 7)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1039']"))).click()
                Mod_URL = self.driver.current_url
                assert self.url_MB in Mod_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified WEAR Module URL:" + Mod_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Mod_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started MB_GALAXY Module URL verification #####")
                self.url_MB = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 2, 7)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1040']"))).click()
                Mod_URL = self.driver.current_url
                assert self.url_MB in Mod_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified MB_GALAXY Module URL:" + Mod_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Mod_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started COMPUTER Module URL verification #####")
                self.url_MB = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 8, 7)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1041']"))).click()
                Mod_URL = self.driver.current_url
                assert self.url_MB in Mod_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified COMPUTER Module URL:" + Mod_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Mod_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started TV & HA Module URL verification #####")
                self.url_TV = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 4, 7)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1042']"))).click()
                TV_URL = self.driver.current_url
                assert self.url_TV in TV_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified TV & Audio Module URL:" + TV_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(TV_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                self.url_HA = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 4, 10)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1043']"))).click()
                HA_URL = self.driver.current_url
                assert self.url_HA in HA_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified HA Module URL:" + HA_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(HA_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

    def get_CC_WEAR_Module2(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
            if "WEAR" in subjectlineTxt:
                logger.info(": ##### Started WEAR Module URL verification #####")
                self.url_MB = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 7)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1041']"))).click()
                Mod_URL = self.driver.current_url
                assert self.url_MB in Mod_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified WEAR Module URL:" + Mod_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Mod_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')
        else:
            if "WEAR" in subjectlineTxt:
                logger.info(": ##### Started WEAR Module URL verification #####")
                self.url_MB = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 7)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1040']"))).click()
                Mod_URL = self.driver.current_url
                assert self.url_MB in Mod_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified WEAR Module URL:" + Mod_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Mod_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

    def get_CC_WEAR_Module3(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
            if "WEAR" in subjectlineTxt:
                logger.info(": ##### Started WEAR Module URL verification #####")
                self.url_MB = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 7)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1042']"))).click()
                Mod_URL = self.driver.current_url
                assert self.url_MB in Mod_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified WEAR Module URL:" + Mod_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Mod_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')
        else:
            if "WEAR" in subjectlineTxt:
                logger.info(": ##### Started WEAR Module URL verification #####")
                self.url_MB = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 7)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1041']"))).click()
                Mod_URL = self.driver.current_url
                assert self.url_MB in Mod_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified WEAR Module URL:" + Mod_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Mod_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')


    """
           Below codes are for W_49 CyberWeek_T2 DD= Deep-Dive Modules validation.
    """

    def get_ME_WEAR_Mod(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "WEAR" in subjectlineTxt:
            logger.info(": ##### Started Buds_Plus Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 40, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c23fdfd9db801c1d20960d55e1420740.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert self.url_path in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Buds_Plus Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Buds_Live Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 40, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c23fdfd9db801c1d20960d55e1420740.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert self.url_path in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Buds_Live Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Galaxy Watch3 Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 40, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c23fdfd9db801c1d20960d55e1420740.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert self.url_path in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy Watch3 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Galaxy Watch Active 2 URL verification #####")
            self.url_path2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 42, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/13f6a83c629b8326df9b3cb585ab6778.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_2_URL = self.driver.current_url
            self.url_list.append(Module_2_URL)
            assert self.url_path2 in Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy Watch active 2 Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Galaxy watch LTE Module URL verification #####")
            self.url_path3 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 43, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/fd6f16ab098bb998ffed15b657ae33dc.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_3_URL = self.driver.current_url
            self.url_list.append(Module_3_URL)
            assert self.url_path3 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy watch LTE Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')


    """
    Below codes are for W_49 CyberWeek_T2 CC-Cross category Modules validation.
    """

    def get_Shop_GalaxyBuds_Live(self):
        logger.info(": ##### Started MOBILE_ACCESSORIES Shop Buds_Live Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 5, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/0d8a73091a52e02f26170dac85b53111.jpg'])[3]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        self.url_list.append(ShopAll_URL)
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MobileAccessories_Shop Buds_Live Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    """*************************************************************************************************************"""

    def get_MobileAccessories_Buds_Plus(self):
        logger.info(": ##### Started MOBILE_ACCESSORIES Shop Buds_Plus Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 5, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/407fcd5dc3310853dbdfc5f30c286a80.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        self.url_list.append(ShopAll_URL)
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MobileAccessories_Shop Buds_Plus Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_MobileAccessories_ShopAll1(self):
        logger.info(": ##### Started MOBILE_ACCESSORIES ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 5, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/5e118028c12d024cb26baf55b8a25eb8.jpg'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MobileAccessories_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_MobileAccessories_ShopAll2(self):
        logger.info(": ##### Started MOBILE_ACCESSORIES ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 5, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/5e118028c12d024cb26baf55b8a25eb8.jpg'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MobileAccessories_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_MobileAccessories_ShopAll3(self):
        logger.info(": ##### Started MOBILE_ACCESSORIES ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 5, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/5e118028c12d024cb26baf55b8a25eb8.jpg'])[3]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MobileAccessories_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_MobileAccessories_ShopAll4(self):
        logger.info(": ##### Started MOBILE_ACCESSORIES ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 5, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/5e118028c12d024cb26baf55b8a25eb8.jpg'])[4]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MobileAccessories_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_MobileAccessories_ShopAll5(self):
        logger.info(": ##### Started MOBILE_ACCESSORIES ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 5, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/5e118028c12d024cb26baf55b8a25eb8.jpg'])[5]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MobileAccessories_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_MobileAccessories_ShopAll(self):
        logger.info(": ##### Started MOBILE_ACCESSORIES ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 5, 10)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/5e118028c12d024cb26baf55b8a25eb8.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MobileAccessories_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_MobileAccessories_Module1(self):
        logger.info(": ##### Started MOBILE_ACCESSORIES Module_1 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 5, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@alt='Shop Offer of the Day'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        # print(self.url_path)
        # print(URL)
        assert self.url_path in URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MOBILE_ACCESSORIES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_MobileAccessories_Module2(self):
        logger.info(": ##### Started MOBILE_ACCESSORIES Module_2 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 5, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@alt='Shop Offer of the Day'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url_path in URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MOBILE_ACCESSORIES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_MobileAccessories_Module3(self):
        logger.info(": ##### Started MOBILE_ACCESSORIES Module_3 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 5, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@alt='Shop Offer of the Day'])[3]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        # print(self.url_path)
        # print(URL)
        assert self.url_path in URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MOBILE_ACCESSORIES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_MobileAccessories_Module4(self):
        logger.info(": ##### Started MOBILE_ACCESSORIES Module_4 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 5, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@alt='Shop Offer of the Day'])[4]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        # print(self.url_path)
        # print(URL)
        assert self.url_path in URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MOBILE_ACCESSORIES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_MobileAccessories_Module5(self):
        logger.info(": ##### Started MOBILE_ACCESSORIES Module_5 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 5, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@alt='Shop Offer of the Day'])[5]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url_path in URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MOBILE_ACCESSORIES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_MobileAccessories_Module6(self):
        logger.info(": ##### Started MOBILE_ACCESSORIES Module_6 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 5, 8)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1042']"))).click()
        URL = self.driver.current_url
        assert self.url_path in URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified MOBILE_ACCESSORIES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window()
        logger.info(': #####  Verification Complete  #####\n')