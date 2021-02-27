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


class SmartPhonePage(BasePage):

    def get_A71_Mod(self):
        logger.info(": ##### Started Galaxy_A71 Module URL verification #####")
        self.url_path3 = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 8)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/73997eca2251ad3c8d934627188c0494.jpg']"))).click()
        parent_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Module_1_URL = self.driver.current_url
        assert self.url_path3 in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Galaxy_A71 Landing page URL:" + Module_1_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(Module_1_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CPO_Mod(self):
        logger.info(": ##### Started Certified Pre-Owned Devices Module URL verification #####")
        self.url_path3 = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 4, 8)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/822d2c586773b79e3a0e09ae6e2cb04b.jpg']"))).click()
        parent_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Module_1_URL = self.driver.current_url
        assert self.url_path3 in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Pre-Owned Devices Landing page URL:" + Module_1_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(Module_1_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_A71_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
                logger.info(": ##### Started Galaxy_A71 Module URL verification #####")
                self.url_A71 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 10, 12)
                self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1040']"))).click()
                Module_5_URL = self.driver.current_url
                assert self.url_A71 in Module_5_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified Galaxy_A71 Module URL:" + Module_5_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_5_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started MB_GALAXY_S20 5G Module URL verification #####")
                self.url_S20_FE = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 8, 12)
                self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1041']"))).click()
                Module_1_URL = self.driver.current_url
                assert self.url_S20_FE in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified MB_GALAXY_S20 5G Module URL:" + Module_1_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started FOld2 Module URL verification #####")
                self.url_Fold2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 9, 12)
                self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1042']"))).click()
                Module_4_URL = self.driver.current_url
                assert self.url_Fold2 in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified Fold2 Module URL:" + Module_4_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started Certified Pre-Owned Devices Module URL verification #####")
                self.url_Note20 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 25, 12)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1043']"))).click()
                Module_3_URL = self.driver.current_url
                assert self.url_Note20 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified Certified Pre-Owned Devices Module URL:" + Module_3_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')
        else:
                logger.info(": ##### Started Galaxy_A71 Module URL verification #####")
                self.url_A71 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 10, 12)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1039']"))).click()
                Module_5_URL = self.driver.current_url
                assert self.url_A71 in Module_5_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified Galaxy_A71 Module URL:" + Module_5_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_5_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started MB_GALAXY_S20 5G Module URL verification #####")
                self.url_S20_FE = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 8, 12)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1040']"))).click()
                Module_1_URL = self.driver.current_url
                assert self.url_S20_FE in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified MB_GALAXY_S20 5G Module URL:" + Module_1_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started FOld2 Module URL verification #####")
                self.url_Fold2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 9, 12)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1041']"))).click()
                Module_4_URL = self.driver.current_url
                assert self.url_Fold2 in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified Fold2 Module URL:" + Module_4_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started Certified Pre-Owned Devices Module URL verification #####")
                self.url_Note20 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 25, 12)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1042']"))).click()
                Module_3_URL = self.driver.current_url
                assert self.url_Note20 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified Certified Pre-Owned Devices Module URL:" + Module_3_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

    def get_FOLD_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
            logger.info(": ##### Started FOld2 Module URL verification #####")
            self.url_Fold2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 9, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1040']"))).click()
            Module_4_URL = self.driver.current_url
            assert self.url_Fold2 in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Fold2 Module URL:" + Module_4_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started MB_GALAXY_S20 5G Module URL verification #####")
            self.url_S20_FE = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 8, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1041']"))).click()
            Module_1_URL = self.driver.current_url
            assert self.url_S20_FE in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_GALAXY_S20 5G Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Galaxy_A71 Module URL verification #####")
            self.url_A71 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 10, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1042']"))).click()
            Module_5_URL = self.driver.current_url
            assert self.url_A71 in Module_5_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy_A71 Module URL:" + Module_5_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_5_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Certified Pre-Owned Devices Module URL verification #####")
            self.url_Note20 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 25, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1043']"))).click()
            Module_3_URL = self.driver.current_url
            assert self.url_Note20 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Certified Pre-Owned Devices Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')
        else:
            logger.info(": ##### Started FOld2 Module URL verification #####")
            self.url_Fold2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 9, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1039']"))).click()
            Module_4_URL = self.driver.current_url
            assert self.url_Fold2 in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Fold2 Module URL:" + Module_4_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started MB_GALAXY_S20 5G Module URL verification #####")
            self.url_S20_FE = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 8, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1040']"))).click()
            Module_1_URL = self.driver.current_url
            assert self.url_S20_FE in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_GALAXY_S20 5G Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Galaxy_A71 Module URL verification #####")
            self.url_A71 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 10, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1041']"))).click()
            Module_5_URL = self.driver.current_url
            assert self.url_A71 in Module_5_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy_A71 Module URL:" + Module_5_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_5_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Certified Pre-Owned Devices Module URL verification #####")
            self.url_Note20 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 25, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1042']"))).click()
            Module_3_URL = self.driver.current_url
            assert self.url_Note20 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Certified Pre-Owned Devices Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

    def get_S_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
                logger.info(": ##### Started MB_GALAXY_S20 5G Module URL verification #####")
                self.url_S20_FE = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 8, 12)
                self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1040']"))).click()
                Module_1_URL = self.driver.current_url
                assert self.url_S20_FE in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified MB_GALAXY_S20 5G Module URL:" + Module_1_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started FOld2 Module URL verification #####")
                self.url_Fold2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 9, 12)
                self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1041']"))).click()
                Module_4_URL = self.driver.current_url
                assert self.url_Fold2 in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified Fold2 Module URL:" + Module_4_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started Galaxy_A71 Module URL verification #####")
                self.url_A71 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 10, 12)
                self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1042']"))).click()
                Module_5_URL = self.driver.current_url
                assert self.url_A71 in Module_5_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified Galaxy_A71 Module URL:" + Module_5_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_5_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started Certified Pre-Owned Devices Module URL verification #####")
                self.url_Note20 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 25, 12)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1043']"))).click()
                Module_3_URL = self.driver.current_url
                assert self.url_Note20 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified Certified Pre-Owned Devices Module URL:" + Module_3_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')
        else:
                logger.info(": ##### Started MB_GALAXY_S20 5G Module URL verification #####")
                self.url_S20_FE = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 8, 12)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1039']"))).click()
                Module_1_URL = self.driver.current_url
                assert self.url_S20_FE in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified MB_GALAXY_S20 5G Module URL:" + Module_1_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started FOld2 Module URL verification #####")
                self.url_Fold2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 9, 12)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1040']"))).click()
                Module_4_URL = self.driver.current_url
                assert self.url_Fold2 in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified Fold2 Module URL:" + Module_4_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started Galaxy_A71 Module URL verification #####")
                self.url_A71 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 10, 12)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1041']"))).click()
                Module_5_URL = self.driver.current_url
                assert self.url_A71 in Module_5_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified Galaxy_A71 Module URL:" + Module_5_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_5_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

                logger.info(": ##### Started Certified Pre-Owned Devices Module URL verification #####")
                self.url_Note20 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 25, 12)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1042']"))).click()
                Module_3_URL = self.driver.current_url
                assert self.url_Note20 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified Certified Pre-Owned Devices Module URL:" + Module_3_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

    def get_CC_MB_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
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
                logger.info(": ##### Started MB_GALAXY Module URL verification #####")
                self.url_MB = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 2, 7)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1038']"))).click()
                Mod_URL = self.driver.current_url
                assert self.url_MB in Mod_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified MB_GALAXY Module URL:" + Mod_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Mod_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

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

                logger.info(": ##### Started COMPUTER Module URL verification #####")
                self.url_MB = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 8, 7)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1040']"))).click()
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
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1041']"))).click()
                TV_URL = self.driver.current_url
                assert self.url_TV in TV_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified TV & Audio Module URL:" + TV_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(TV_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                self.url_HA = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 4, 10)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1042']"))).click()
                HA_URL = self.driver.current_url
                assert self.url_HA in HA_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified HA Module URL:" + HA_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(HA_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

    def get_CC_MB_Module2(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
            if "MB" in subjectlineTxt:
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
        else:
            if "MB" in subjectlineTxt:
                logger.info(": ##### Started MB_GALAXY Module URL verification #####")
                self.url_MB = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 2, 7)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1040']"))).click()
                Mod_URL = self.driver.current_url
                assert self.url_MB in Mod_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified MB_GALAXY Module URL:" + Mod_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Mod_URL)
                URLSegemntPage.get_segment()
                URLSegemntPage.get_segment_validation()
                self.driver.back()
                logger.info(': #####  Verification Complete  #####\n')

    """
    W_49 CyberWeek_T3.
    """

    def get_SMARTPHONE_Shop_Note20_5G(self):
        logger.info(": ##### Started SMARTPHONE_Shop Note20_5G Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/83aa29765a5589734f7af89220d7e10d.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        self.url_list.append(ShopAll_URL)
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified SMARTPHONE_Shop Note20_5G Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_SMARTPHONE_ShopAll1(self):
        logger.info(": ##### Started SMARTPHONE_ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/ebbc4a4272101826cc9f521c3540005b.jpg'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified SMARTPHONE_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_SMARTPHONE_ShopAll2(self):
        logger.info(": ##### Started SMARTPHONE_ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/ebbc4a4272101826cc9f521c3540005b.jpg'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified SMARTPHONE_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_SMARTPHONE_ShopAll3(self):
        logger.info(": ##### Started SMARTPHONE_ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/ebbc4a4272101826cc9f521c3540005b.jpg'])[3]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified SMARTPHONE_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_SMARTPHONE_ShopAll4(self):
        logger.info(": ##### Started SMARTPHONE_ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/ebbc4a4272101826cc9f521c3540005b.jpg'])[4]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified SMARTPHONE_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_SMARTPHONE_ShopAll5(self):
        logger.info(": ##### Started SMARTPHONE_ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/ebbc4a4272101826cc9f521c3540005b.jpg'])[5]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified SMARTPHONE_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_SMARTPHONE_ShopAll(self):
        logger.info(": ##### Started SMARTPHONE_ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/ebbc4a4272101826cc9f521c3540005b.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified SMARTPHONE_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    """*************************************************************************************************************"""

    """
    Below codes are for w-49 CyberWeek_T2 DD=Deep-Dive Modules validation.
    """

    def get_MB_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "MB" in subjectlineTxt:
            # logger.info(": ##### Started Note20 Module URL verification #####")
            # self.url_Note20 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 6, 8)
            # parent_window = self.driver.current_window_handle
            # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/389f648ac09cceb0e6b7b12217661711.jpg']"))).click()
            # all_windows = self.driver.window_handles
            # child_window = [window for window in all_windows if window != parent_window][0]
            # self.driver.switch_to.window(child_window)
            # Module_3_URL = self.driver.current_url
            # self.url_list.append(Module_3_URL)
            # assert self.url_Note20 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            # logger.info(": successfully verified Note20 Module URL:" + Module_3_URL + '\n')
            # with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            # URLSegemntPage.get_segment()
            # URLSegemntPage.get_segment_validation()
            # self.driver.close()
            # self.driver.switch_to.window(parent_window)
            # logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started MB_GALAXY_S20 Module URL verification #####")
            self.url_S20_FE = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 3, 8)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/1c3978331f18882e9cbe82751bece678.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            assert self.url_S20_FE in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_GALAXY_S20 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started FOld2 Module URL verification #####")
            self.url_Fold2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 4, 8)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/3f8cfcb7a553c4dc3e4fcc6cc5c3a10a.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_4_URL = self.driver.current_url
            self.url_list.append(Module_4_URL)
            assert self.url_Fold2 in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Fold2 Module URL:" + Module_4_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Galaxy_A71 Module URL verification #####")
            self.url_A71 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 5, 8)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/b97616f5f07089ccaf023fa946ae3fa4.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_5_URL = self.driver.current_url
            self.url_list.append(Module_5_URL)
            assert self.url_A71 in Module_5_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy_A71 Module URL:" + Module_5_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_5_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

    """
    Below codes are for w-49 CyberWeek_T2 CC-Cross category Modules validation.
    """

    def get_ShopGalaxy_S20_5G(self):
        logger.info(": ##### Started SMARTPHONE_Shop S20_5G Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/0d8a73091a52e02f26170dac85b53111.jpg'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        self.url_list.append(ShopAll_URL)
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified SMARTPHONE_Shop S20_5G Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    """**************************************************************************************************************"""

    """
    Below codes are for DD=Deep-Dive Modules validation.
    """

    def get_MB_GALAXY_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "MB_GALAXY" in subjectlineTxt:
            logger.info(": ##### Started MB_GALAXY_S20_plus Module URL verification #####")
            self.url_S20_FE = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 5, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/3871c26abb4680dfb456908d9172941c.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            # self.url_list.append(Module_1_URL)
            assert self.url_S20_FE in  Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_GALAXY_S20_plus Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started MB_GALAXY_S20FE Module URL verification #####")
            self.url_S20_FE = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 6, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/f92eef27e5ade30b3e92b26716f8d9aa.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            # self.url_list.append(Module_1_URL)
            assert self.url_S20_FE in  Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_GALAXY_S20FE Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Note20 Module URL verification #####")
            self.url_Note20 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 7, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/389f648ac09cceb0e6b7b12217661711.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_3_URL = self.driver.current_url
            self.url_list.append(Module_3_URL)
            assert self.url_Note20 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Note20 Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started FOld2 Module URL verification #####")
            self.url_Fold2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 8, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/3f8cfcb7a553c4dc3e4fcc6cc5c3a10a.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_4_URL = self.driver.current_url
            self.url_list.append(Module_4_URL)
            assert self.url_Fold2 in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Fold2 Module URL:" + Module_4_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Galaxy_A71 Module URL verification #####")
            self.url_A71 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 9, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/b97616f5f07089ccaf023fa946ae3fa4.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_5_URL = self.driver.current_url
            self.url_list.append(Module_5_URL)
            assert self.url_A71 in Module_5_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy_A71 Module URL:" + Module_5_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_5_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

    def get_MB_NOTE_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "MB_NOTE" in subjectlineTxt:
            logger.info(": ##### Started Note20 Module URL verification #####")
            self.url_Note20 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 12, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/389f648ac09cceb0e6b7b12217661711.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert self.url_Note20 in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Note20 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started MB_GALAXY_S20_plus Module URL verification #####")
            self.url_S20_FE = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 13, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/3871c26abb4680dfb456908d9172941c.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            # self.url_list.append(Module_1_URL)
            assert self.url_S20_FE in  Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_GALAXY_S20_plus Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started MB_GALAXY_S20FE Module URL verification #####")
            self.url_S20_FE = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 14, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/f92eef27e5ade30b3e92b26716f8d9aa.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_2_URL = self.driver.current_url
            # self.url_list.append(Module_1_URL)
            assert self.url_S20_FE in  Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_GALAXY_S20FE Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started FOld2 Module URL verification #####")
            self.url_Fold2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 15, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/3f8cfcb7a553c4dc3e4fcc6cc5c3a10a.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_3_URL = self.driver.current_url
            self.url_list.append(Module_3_URL)
            assert self.url_Fold2 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Fold2 Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Galaxy_A71 Module URL verification #####")
            self.url_A71 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 16, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/b97616f5f07089ccaf023fa946ae3fa4.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_4_URL = self.driver.current_url
            self.url_list.append(Module_4_URL)
            assert self.url_A71 in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy_A71 Module URL:" + Module_4_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

    def get_MB_NOTE1_Module_BlackFriday(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "MB_GALAXY" in subjectlineTxt:
            logger.info(": ##### Started Note20 Module URL verification #####")
            self.url_Note20 = ExcelUtil(tc_name="").read_from_excel("DDOfferCopy", 4, 10)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1037']"))).click()
            Module_1_URL = self.driver.current_url
            assert self.url_Note20 in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Note20 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

    def get_MB_NOTE2_Module_BlackFriday(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "MB_GALAXY" in subjectlineTxt:
            logger.info(": ##### Started MB_GALAXY_S20_5G Module URL verification #####")
            self.url_S20_FE = ExcelUtil(tc_name="").read_from_excel("DDOfferCopy", 5, 10)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1038']"))).click()
            Module_2_URL = self.driver.current_url
            assert self.url_S20_FE in  Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_GALAXY_S20FE Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

    def get_MB_NOTE3_Module_BlackFriday(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "MB_GALAXY" in subjectlineTxt:
            logger.info(": ##### Started FOld2 Module URL verification #####")
            self.url_Fold2 = ExcelUtil(tc_name="").read_from_excel("DDOfferCopy", 6, 10)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1039']"))).click()
            Module_3_URL = self.driver.current_url
            assert self.url_Fold2 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Fold2 Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

    def get_MB_NOTE4_Module_BlackFriday(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "MB_GALAXY" in subjectlineTxt:
            logger.info(": ##### Started Galaxy_A71 Module URL verification #####")
            self.url_A71 = ExcelUtil(tc_name="").read_from_excel("DDOfferCopy", 7, 10)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1040']"))).click()
            Module_4_URL = self.driver.current_url
            assert self.url_A71 in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy_A71 Module URL:" + Module_4_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

    def get_MB_WEAR_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "MB_WEAR" in subjectlineTxt:
            logger.info(": ##### Started Buds Plus Module URL verification #####")
            self.url_tablet = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 47, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/ae51e191677b5778ca46f93f93e1253f.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert self.url_tablet in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Buds Plus Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Watche3 Module URL verification #####")
            self.url_GW3 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 48, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/980affbbe67e79d812140068f0147dcc.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_3_URL = self.driver.current_url
            # self.url_list.append(Module_2_URL)
            assert self.url_GW3 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Watche3 Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Active2 Watche Module URL verification #####")
            self.url_GW3 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 49, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/490a3c02e803160a2eadccd9d7e6f7ef.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_3_URL = self.driver.current_url
            # self.url_list.append(Module_2_URL)
            assert self.url_GW3 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Active2 Watche Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Tablet S6 Module URL verification #####")
            self.url_tablet = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 50, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/00251909224afc561c08146448c6d9cb.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert self.url_tablet in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Tablet S6 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started S7/S7 PLUS Module URL verification #####")
            self.url_Buds_plus = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 51, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/a1875e29d5c468c4f09cf91798acf4fc.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_2_URL = self.driver.current_url
            self.url_list.append(Module_2_URL)
            assert self.url_Buds_plus in Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified S7/S7 Plus Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

    def get_MB_A71_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "A71" in subjectlineTxt:
            logger.info(": ##### Started Galaxy_A71 Module URL verification #####")
            self.url_A71 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 124, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/b97616f5f07089ccaf023fa946ae3fa4.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_4_URL = self.driver.current_url
            self.url_list.append(Module_4_URL)
            assert self.url_A71 in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy_A71 Module URL:" + Module_4_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started MB_GALAXY_Note20 Module URL verification #####")
            self.url_S20_FE = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 125, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/389f648ac09cceb0e6b7b12217661711.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_2_URL = self.driver.current_url
            # self.url_list.append(Module_1_URL)
            assert self.url_S20_FE in  Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_GALAXY_Note20 Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started S20 Plus Module URL verification #####")
            self.url_Note20 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 126, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/3871c26abb4680dfb456908d9172941c.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert self.url_Note20 in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified S20 Plus Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started S20FE Module URL verification #####")
            self.url_Fold2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 127, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/f92eef27e5ade30b3e92b26716f8d9aa.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_3_URL = self.driver.current_url
            self.url_list.append(Module_3_URL)
            assert self.url_Fold2 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified S20FE Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Fold z Module URL verification #####")
            self.url_Fold2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 128, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/3f8cfcb7a553c4dc3e4fcc6cc5c3a10a.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_3_URL = self.driver.current_url
            self.url_list.append(Module_3_URL)
            assert self.url_Fold2 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Fold z Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')


    """
    Below codes are for CC-Cross category Modules validation.
    """

    def get_SmartPhoneModule1(self):
        logger.info(": ##### Started SMARTPHONES Module_1 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@alt='Shop Offer of the Day'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url_path in URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified SMARTPHONES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_SmartPhoneModule2(self):
        logger.info(": ##### Started SMARTPHONES Module_2 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@alt='Shop Offer of the Day'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        logger.info(": successfully verified SMARTPHONES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_SmartPhoneModule3(self):
        logger.info(": ##### Started SMARTPHONES Module_3 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@alt='Shop Offer of the Day'])[3]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url_path in URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified SMARTPHONES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_SmartPhoneModule4(self):
        logger.info(": ##### Started SMARTPHONES Module_4 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@alt='Shop Offer of the Day'])[4]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url_path in URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified SMARTPHONES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_SmartPhoneModule5(self):
        logger.info(": ##### Started SMARTPHONES Module_5 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@alt='Shop Offer of the Day'])[5]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url_path in URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified SMARTPHONES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_SmartPhoneModule6(self):
        logger.info(": ##### Started SMARTPHONES Module_6 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 14)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1042']"))).click()
        URL = self.driver.current_url
        assert self.url_path in URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified SMARTPHONES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        # self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')
