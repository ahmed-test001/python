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


class SmartPhonePage(BasePage):

    """
    Below codes are for DD=Deep-Dive Modules validation.
    """

    def get_MB_GALAXY_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "MB_GALAXY" in subjectlineTxt:
            logger.info(": ##### Started MB_GALAXY_S20FE Module URL verification #####")
            self.url_S20_FE = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 5, 9)
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
            logger.info(": ##### Started S20_plus Module URL verification #####")
            # self.url_S20_plus = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 5, 9)
            # parent_window = self.driver.current_window_handle
            # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/3871c26abb4680dfb456908d9172941c.jpg']"))).click()
            # all_windows = self.driver.window_handles
            # child_window = [window for window in all_windows if window != parent_window][0]
            # self.driver.switch_to.window(child_window)
            # Module_2_URL = self.driver.current_url
            # self.url_list.append(Module_2_URL)
            # assert self.url_S20_plus in Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            # logger.info(": successfully verified S20_plus Module URL:" + Module_2_URL + '\n')
            # with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            # URLSegemntPage.get_segment()
            # URLSegemntPage.get_segment_validation()
            # self.driver.close()
            # self.driver.switch_to.window(parent_window)
            # logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started Note20 Module URL verification #####")
            self.url_Note20 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 6, 9)
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
            self.url_Fold2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 7, 9)
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
            self.url_A71 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 8, 9)
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
            self.url_Note20 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 6, 9)
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
            logger.info(": ##### Started MB_GALAXY_S20FE Module URL verification #####")
            self.url_S20_FE = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 5, 9)
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
            self.url_Fold2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 7, 9)
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
            # logger.info(": ##### Started S20_plus Module URL verification #####")
            # self.url_S20_plus = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 5, 9)
            # parent_window = self.driver.current_window_handle
            # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/3871c26abb4680dfb456908d9172941c.jpg']"))).click()
            # all_windows = self.driver.window_handles
            # child_window = [window for window in all_windows if window != parent_window][0]
            # self.driver.switch_to.window(child_window)
            # Module_2_URL = self.driver.current_url
            # self.url_list.append(Module_2_URL)
            # assert self.url_S20_plus in Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            # logger.info(": successfully verified S20_plus Module URL:" + Module_2_URL + '\n')
            # with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            # URLSegemntPage.get_segment()
            # URLSegemntPage.get_segment_validation()
            # self.driver.close()
            # self.driver.switch_to.window(parent_window)
            # logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started Galaxy_A71 Module URL verification #####")
            self.url_A71 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 8, 9)
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

    def get_MB_WEAR_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "MB_WEAR" in subjectlineTxt:
            logger.info(": ##### Started MB_Tablet Module URL verification #####")
            self.url_tablet = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 43, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/0b2d29f05a32ff1aa348a0f4febacc28.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert self.url_tablet in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_Tablet Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Galaxy_Buds Module URL verification #####")
            self.url_Buds_plus = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 44, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/ae51e191677b5778ca46f93f93e1253f.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_2_URL = self.driver.current_url
            self.url_list.append(Module_2_URL)
            assert self.url_Buds_plus in Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Galaxy_Buds Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            logger.info(": ##### Started Watche3 Module URL verification #####")
            self.url_GW3 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 45, 9)
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/490a3c02e803160a2eadccd9d7e6f7ef.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_3_URL = self.driver.current_url
            # self.url_list.append(Module_2_URL)
            assert self.url_GW3 in  Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Watche3 Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

            # logger.info(": ##### Started Audio Trade_in Module URL verification #####")
            # parent_window = self.driver.current_window_handle
            # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/3ccd7b7010af438eb2be3a81900bcb71.jpg']"))).click()
            # all_windows = self.driver.window_handles
            # child_window = [window for window in all_windows if window != parent_window][0]
            # self.driver.switch_to.window(child_window)
            # Module_4_URL = self.driver.current_url
            # self.url_list.append(Module_4_URL)
            # assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'audio_trade_in_url') in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            # logger.info(": successfully verified Audio_Trade_in Module URL:" + Module_4_URL + '\n')
            # with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            # URLSegemntPage.get_segment()
            # URLSegemntPage.get_segment_validation()
            # self.driver.close()
            # self.driver.switch_to.window(parent_window)
            # logger.info(': #####  Verification Complete  #####\n')

    def get_MB_A71_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "A71" in subjectlineTxt:
            logger.info(": ##### Started Galaxy_A71 Module URL verification #####")
            self.url_A71 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 8, 9)
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

            logger.info(": ##### Started MB_GALAXY_S20FE Module URL verification #####")
            self.url_S20_FE = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 5, 9)
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

            logger.info(": ##### Started Note20 Module URL verification #####")
            self.url_Note20 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 6, 9)
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

            logger.info(": ##### Started FOld2 Module URL verification #####")
            self.url_Fold2 = ExcelUtil(tc_name="").read_from_excel("DD_Versions", 7, 9)
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


    """
    Below codes are for CC-Cross category Modules validation.
    """

    def get_SMARTPHONE_ShopAll(self):
        logger.info(": ##### Started SMARTPHONE_ShopAll Banner URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 7)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/90ca0c30cbb88a90c2573745c2f3498e.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        self.url_list.append(ShopAll_URL)
        assert self.url_path in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified SMARTPHONE_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_SmartPhoneModule(self):
        logger.info(": ##### Started SMARTPHONES Module URL verification #####\n")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 7)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/bd5d9dc6e1afe071e6913e58a104722d.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        self.url_list.append(URL)
        assert self.url_path in URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified SMARTPHONES_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')
