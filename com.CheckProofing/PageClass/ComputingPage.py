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


class ComputingPage(BasePage):

    def get_SSD_Mod(self):
        logger.info(": ##### Started Memory_Card Module URL verification #####")
        self.url_path3 = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 10, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/5a7f02235791ccb5f3bfcc2156b95b8b.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path3 in ShopAll_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified HomeAppliance_Shop jet Stick Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_CE_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
            logger.info(": ##### Started TAB S7 Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 12, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1040']"))).click()
            Module_1_URL = self.driver.current_url
            assert self.url_path in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified TAB S7 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started TAB S6 Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 14, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1041']"))).click()
            Module_1_URL = self.driver.current_url
            assert self.url_path in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified TAB S6 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Monitor Module URL verification #####")
            self.url_path2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 15, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1042']"))).click()
            Module_2_URL = self.driver.current_url
            assert self.url_path2 in Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Monitor Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Memory_Card Module URL verification #####")
            self.url_path3 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 16, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1043']"))).click()
            Module_3_URL = self.driver.current_url
            print(self.url_path3)
            print(Module_3_URL)
            assert self.url_path3 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Memory_Card Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')
        else:
            logger.info(": ##### Started TAB S7 Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 12, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1039']"))).click()
            Module_1_URL = self.driver.current_url
            assert self.url_path in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified TAB S7 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started TAB S6 Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 14, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1040']"))).click()
            Module_1_URL = self.driver.current_url
            assert self.url_path in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified TAB S6 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Monitor Module URL verification #####")
            self.url_path2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 15, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1041']"))).click()
            Module_2_URL = self.driver.current_url
            assert self.url_path2 in Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Monitor Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Memory_Card Module URL verification #####")
            self.url_path3 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 16, 12)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='_x0000_i1042']"))).click()
            Module_3_URL = self.driver.current_url
            assert self.url_path3 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Memory_Card Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.back()
            logger.info(': #####  Verification Complete  #####\n')

    def get_CC_COM_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
            if "TABCOM" in subjectlineTxt:
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
            if "TABCOM" in subjectlineTxt:
                logger.info(": ##### Started COMPUTER Module URL verification #####")
                self.url_MB = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 8, 7)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1039']"))).click()
                Mod_URL = self.driver.current_url
                assert self.url_MB in Mod_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
                logger.info(": successfully verified COMPUTER Module URL:" + Mod_URL + '\n')
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

    def get_CC_COM_Module3(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
            if "TABCOM" in subjectlineTxt:
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
        else:
            if "TABCOM" in subjectlineTxt:
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

    """
        W_49 CyberWeek_T3.
    """

    def get_Computing_Shop_Monitors(self):
        logger.info(": ##### Started COMPUTING_Shop Monitors Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/664bdb2d53d7bfa3cce13a2362d5207d.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        self.url_list.append(ShopAll_URL)
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Computing_Shop Monitors Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    """************************************************************************************************************"""
    """
       Below codes are for W_49 CyberWeek_T2 DD= Deep-Dive Modules validation.
    """

    def get_CE_COMPUTER_Mod(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "CE_COMPUTER" in subjectlineTxt:
            logger.info(": ##### Started Gaming_Monitor Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 40, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c23fdfd9db801c1d20960d55e1420740.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert self.url_path in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Gaming_Monitor Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Odyssey Gaming_Monitor Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 40, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c23fdfd9db801c1d20960d55e1420740.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            time.sleep(5)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert self.url_path in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Odyssey Gaming_Monitor Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started SSD Module URL verification #####")
            self.url_path2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 42, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/13f6a83c629b8326df9b3cb585ab6778.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_2_URL = self.driver.current_url
            self.url_list.append(Module_2_URL)
            assert self.url_path2 in Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified SSD Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Memory_Card Module URL verification #####")
            self.url_path3 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 43, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/fd6f16ab098bb998ffed15b657ae33dc.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_3_URL = self.driver.current_url
            self.url_list.append(Module_3_URL)
            assert self.url_path3 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Memory_Card Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started USB Module URL verification #####")
            self.url_path4 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 44, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/1f55784c9fa5dd7f6999019c795767e8.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_4_URL = self.driver.current_url
            self.url_list.append(Module_4_URL)
            assert self.url_path4 in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified USB Module URL:" + Module_4_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

    """
    Below codes are for W_49 CyberWeek_T2 CC-Cross category Modules validation.
    """

    def get_Computing_Shop_Odyssey(self):
        logger.info(": ##### Started COMPUTING_Shop Odyssey Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/664bdb2d53d7bfa3cce13a2362d5207d.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        self.url_list.append(ShopAll_URL)
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Computing_Shop Odyssey Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    """**********************************************************************************************************"""

    """
    Below codes are for DD= Deep-Dive Modules validation.
    """
    def get_CE_COMPUTER_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "CE_COMPUTER" in subjectlineTxt:
            logger.info(": ##### Started Gaming_Monitor Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 40, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c23fdfd9db801c1d20960d55e1420740.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert self.url_path in  Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Gaming_Monitor Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Odyssey Gaming_Monitor Module URL verification #####")
            self.url_path = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 40, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c23fdfd9db801c1d20960d55e1420740.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            time.sleep(5)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert self.url_path in  Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Odyssey Gaming_Monitor Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started SSD Module URL verification #####")
            self.url_path2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 42, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/13f6a83c629b8326df9b3cb585ab6778.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_2_URL = self.driver.current_url
            self.url_list.append(Module_2_URL)
            assert self.url_path2 in Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified SSD Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Memory_Card Module URL verification #####")
            self.url_path3 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 43, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/fd6f16ab098bb998ffed15b657ae33dc.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_3_URL = self.driver.current_url
            self.url_list.append(Module_3_URL)
            assert self.url_path3 in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Memory_Card Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started USB Module URL verification #####")
            self.url_path4 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 44, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/1f55784c9fa5dd7f6999019c795767e8.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_4_URL = self.driver.current_url
            self.url_list.append(Module_4_URL)
            assert self.url_path4 in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified USB Module URL:" + Module_4_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

    """
    Below codes are for CC-Cross category Modules validation.
    """

    def get_Shop_Monitors(self):
        logger.info(": ##### Started COMPUTING_Shop Monitors Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/0d8a73091a52e02f26170dac85b53111.jpg'])[4]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        self.url_list.append(ShopAll_URL)
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Computing_Shop Monitors Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Computing_ShopAll1(self):
        logger.info(": ##### Started COMPUTING_ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 8)
        # self.url_path = ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH', 'com')
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/c7677f96e448182ab94f7da76a8f951a.jpg'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Computing_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Computing_ShopAll2(self):
        logger.info(": ##### Started COMPUTING_ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 8)
        # self.url_path = ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH', 'com')
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/c7677f96e448182ab94f7da76a8f951a.jpg'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Computing_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Computing_ShopAll3(self):
        logger.info(": ##### Started COMPUTING_ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 8)
        # self.url_path = ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH', 'com')
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/c7677f96e448182ab94f7da76a8f951a.jpg'])[3]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Computing_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Computing_ShopAll4(self):
        logger.info(": ##### Started COMPUTING_ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 8)
        # self.url_path = ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH', 'com')
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/c7677f96e448182ab94f7da76a8f951a.jpg'])[4]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Computing_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Computing_ShopAll5(self):
        logger.info(": ##### Started COMPUTING_ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 8)
        # self.url_path = ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH', 'com')
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@src='http://t.info.samsungusa.com/res/samsung/c7677f96e448182ab94f7da76a8f951a.jpg'])[5]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Computing_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Computing_ShopAll(self):
        logger.info(": ##### Started COMPUTING_ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 10)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/c7677f96e448182ab94f7da76a8f951a.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Computing_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Computing_Module1(self):
        logger.info(": ##### Started COMPUTING Module_1 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@alt='Shop Offer of the Day'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        self.url_list.append(URL)
        assert self.url_path in URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified COMPUTING_ModuleL Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Computing_Module2(self):
        logger.info(": ##### Started COMPUTING Module_2 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@alt='Shop Offer of the Day'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        self.url_list.append(URL)
        assert self.url_path in URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified COMPUTING_ModuleL Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Computing_Module3(self):
        logger.info(": ##### Started COMPUTING Module_3 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@alt='Shop Offer of the Day'])[3]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        self.url_list.append(URL)
        assert self.url_path in URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified COMPUTING_ModuleL Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Computing_Module4(self):
        logger.info(": ##### Started COMPUTING Module_4 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@alt='Shop Offer of the Day'])[4]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        self.url_list.append(URL)
        assert self.url_path in URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified COMPUTING_ModuleL Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Computing_Module5(self):
        logger.info(": ##### Started COMPUTING Module_5 URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 14)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@alt='Shop Offer of the Day'])[5]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        self.url_list.append(URL)
        assert self.url_path in URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified COMPUTING_ModuleL Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Computing_Module6(self):
        logger.info(": ##### Started COMPUTING Module_6 URL verification #####\n")
        parent_window = self.driver.current_window_handle
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 8)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1042']"))).click()
        URL = self.driver.current_url
        self.url_list.append(URL)
        assert self.url_path in URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified COMPUTING_ModuleL Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')