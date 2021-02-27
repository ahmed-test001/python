import json
import os
import sys
import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
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





class TVHomeTheaterPage(BasePage):

    subjectlineTxt2=""

    """
    Below codes are for DD=Deep-Dive Modules validation.
    """

    def get_segment_validation1(self):
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            urls = f.read().splitlines()
            url = urls[0]

        if "Non" in url:
                print("Reservers NOT Present.")
                if "EPP" in url:
                    print("EPP NON Reserver")
                else:
                    print("NO EPP.")
        elif "Non" not in url:
                print("Reservers Present.")
                if "EPP" in url:
                    print("EPP Reserver")
                else:
                    print("NO EPP")


    def get_TV_QLED_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "TV_QLED" in subjectlineTxt:
            logger.info(": ##### Started TV_QLED_4K Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/fe79c2ecb709888c0de46b4b934e7b55.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'TV_4kQLED_url') in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified TV_QLED_4K Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.get_segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            # logger.info(": ##### Started TV_QLED_8K Module URL verification #####")
            # parent_window = self.driver.current_window_handle
            # self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/143fc21d555631a43dd1e79b1ac57b70.jpg']"))).click()
            # all_windows = self.driver.window_handles
            # child_window = [window for window in all_windows if window != parent_window][0]
            # self.driver.switch_to.window(child_window)
            # Module_2_URL = self.driver.current_url
            # # self.url_list.append(Module_1_URL)
            # assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'TV_8kQLED_url') in  Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            # logger.info(": successfully verified TV_QLED_8K Module URL:" + Module_2_URL + '\n')
            # with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            # URLSegemntPage.get_segment()
            # URLSegemntPage.get_segment_validation()
            # self.driver.close()
            # self.driver.switch_to.window(parent_window)
            # logger.info(': #####  Verification Complete  #####\n')
            # logger.info(": ##### Started 75inc_TV Module URL verification #####")
            # parent_window = self.driver.current_window_handle
            # self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/b235b40a6583d6a6238a0644caa19dee.jpg']"))).click()
            # all_windows = self.driver.window_handles
            # child_window = [window for window in all_windows if window != parent_window][0]
            # self.driver.switch_to.window(child_window)
            # Module_3_URL = self.driver.current_url
            # self.url_list.append(Module_3_URL)
            # assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', '75inc_TV_url') in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            # logger.info(": successfully verified 75inc_TV Module URL:" + Module_3_URL + '\n')
            # with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            # URLSegemntPage.get_segment()
            # URLSegemntPage.get_segment_validation()
            # self.driver.close()
            # self.driver.switch_to.window(parent_window)
            # logger.info(': #####  Verification Complete  #####\n')
            # logger.info(": ##### Started Terrace_TV Module URL verification #####")
            # parent_window = self.driver.current_window_handle
            # self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/a6728cf161412d6ba3213dbb3b3c94a5.jpg']"))).click()
            # all_windows = self.driver.window_handles
            # child_window = [window for window in all_windows if window != parent_window][0]
            # self.driver.switch_to.window(child_window)
            # Module_4_URL = self.driver.current_url
            # self.url_list.append(Module_4_URL)
            # assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'Terrace_TV_url') in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            # logger.info(": successfully verified Terrace_TV Module URL:" + Module_4_URL + '\n')
            # with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            # URLSegemntPage.get_segment()
            # URLSegemntPage.get_segment_validation()
            # self.driver.close()
            # self.driver.switch_to.window(parent_window)
            # logger.info(': #####  Verification Complete  #####\n')
            # logger.info(": ##### Started Soundbars Module URL verification #####")
            # parent_window = self.driver.current_window_handle
            # self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/3fc42505bf9fceb216f99b94bfb515bc.jpg']"))).click()
            # all_windows = self.driver.window_handles
            # child_window = [window for window in all_windows if window != parent_window][0]
            # self.driver.switch_to.window(child_window)
            # Module_5_URL = self.driver.current_url
            # self.url_list.append(Module_5_URL)
            # assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'Soundbars_url') in Module_5_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            # logger.info(": successfully verified Soundbars Module URL:" + Module_5_URL + '\n')
            # with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_5_URL)
            # URLSegemntPage.get_segment()
            # URLSegemntPage.get_segment_validation()
            # self.driver.close()
            # self.driver.switch_to.window(parent_window)
            # logger.info(': #####  Verification Complete  #####\n')

    def get_TV_ACCESSORY_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "TV_ACCESSORY" in subjectlineTxt:
            logger.info(": ##### Started Soundbars Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/3fc42505bf9fceb216f99b94bfb515bc.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'Soundbars_url') in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Soundbars Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            # URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started TV_QLED_4K Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/fe79c2ecb709888c0de46b4b934e7b55.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_2_URL = self.driver.current_url
            self.url_list.append(Module_2_URL)
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'TV_4kQLED_url') in Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified TV_QLED_4K Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            # URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started TV_QLED_8K Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/143fc21d555631a43dd1e79b1ac57b70.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_3_URL = self.driver.current_url
            # self.url_list.append(Module_3_URL)
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'TV_8kQLED_url') in  Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified TV_QLED_8K Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            # URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started 75inc_TV Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/b235b40a6583d6a6238a0644caa19dee.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_4_URL = self.driver.current_url
            self.url_list.append(Module_4_URL)
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', '75inc_TV_url') in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified 75inc_TV Module URL:" + Module_4_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            URLSegemntPage.get_segment()
            # URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started Terrace_TV Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/a6728cf161412d6ba3213dbb3b3c94a5.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_5_URL = self.driver.current_url
            self.url_list.append(Module_5_URL)
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'Terrace_TV_url') in Module_5_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Terrace_TV Module URL:" + Module_5_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_5_URL)
            URLSegemntPage.get_segment()
            # URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')



    """
    Below codes are for CC-Cross category Modules validation.
    """

    def get_TVHomeTheater_ShopAll(self):
        logger.info(": ##### Started TV_HOMETHEATER_ShopAll Banner URL verification #####\n")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/69bee55d0224d6feb564f88ea38da655.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        self.url_list.append(ShopAll_URL)
        assert ReadConfig.read_w46_HolidayDeals_T2_configData('CC_Module', 'Deals_tv_theater') in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified TVHomeTheater_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_TV_HomeTheaterModule(self):
        logger.info(": ##### Started TV_HOME_THEATER Module URL verification #####\n")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/612bce063f34bc13116528e8255ffb96.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        self.url_list.append(URL)
        assert ReadConfig.read_w46_HolidayDeals_T2_configData('CC_Module', 'tv_theater_url') in URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified TV_HOME_THEATER_ModuleL Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')