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


class HomeAppliancePage(BasePage):

    """
    Below codes are for DD-Deep Drive Modules validation.
    """

    def get_HA_LAUNDRY_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "HA_LAUNDRY" in subjectlineTxt:
            logger.info(": ##### Started Washer_Dryers Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/d831a5dbcaf1a8e1f3d70cddeaeebd66.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'Washer_Dryers_url') in  Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Washer_Dryers Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            # URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started Jet_Stick Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/4b2f287be144d1504a034e4c3959ed63.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_2_URL = self.driver.current_url
            self.url_list.append(Module_2_URL)
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'jet_stick_url') in Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Jet_Stick Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            # URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started Robot vacuums & Mops Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/494cd175b4c396c9fdb95a8a6a3eb9bd.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_3_URL = self.driver.current_url
            self.url_list.append(Module_3_URL)
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'robot_vacuum_url') in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Robot_vacuums_Mops Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            # URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started Air Dresser Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/9df1b7a1f27eb1ba73b9556535db0bb9.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_4_URL = self.driver.current_url
            self.url_list.append(Module_4_URL)
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'air_dresser_url') in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Air Dresser Module URL:" + Module_4_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            URLSegemntPage.get_segment()
            # URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started Air Purifier Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c6a247ba3ab0486934721f02083e6bab.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_5_URL = self.driver.current_url
            self.url_list.append(Module_5_URL)
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'air_purifier_url') in Module_5_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Air Purifier Module URL:" + Module_5_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_5_URL)
            URLSegemntPage.get_segment()
            # URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

    def get_HA_KITCHEN_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "HA_KITCHEN" in subjectlineTxt:
            logger.info(": ##### Started KITCHEN Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/39261065cf8b84263b9bd59986795046.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'kitchen_url') in  Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified KITCHEN Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            # URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started Dish_washer Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/15176f63d507743d288bef66d31d7515.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_2_URL = self.driver.current_url
            self.url_list.append(Module_2_URL)
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'dish_washer_url') in Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Dish_washer Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            # URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started Wall_Microwave Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/bcb89ed86c3006711ca180966f6e33ef.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_3_URL = self.driver.current_url
            self.url_list.append(Module_3_URL)
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'microwave_url') in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Wall_Microwave Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            # URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started Ranges Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/5bccadf947c0194bf96f94dcb63cf6e5.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_4_URL = self.driver.current_url
            self.url_list.append(Module_4_URL)
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'ranges_url') in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Ranges Module URL:" + Module_4_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            URLSegemntPage.get_segment()
            # URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started Refregerators Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/b1a4356bb6f99b481a4342aae89e9d27.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_5_URL = self.driver.current_url
            self.url_list.append(Module_5_URL)
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'refregerators_url') in Module_5_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified Refregerators Module URL:" + Module_5_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_5_URL)
            URLSegemntPage.get_segment()
            # URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')



    """
    Below codes are for CC-Cross category Modules validation.
    """

    def get_HomeAppliance_ShopAll(self):
        logger.info(": ##### Started HOME_APPLIANCE_ShopAll Banner URL verification #####\n")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/adfe0311d1373f0eb88108e2cc426f3f.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        ShopAll_URL = self.driver.current_url
        self.url_list.append(ShopAll_URL)
        assert ReadConfig.read_w46_HolidayDeals_T2_configData('CC_Module', 'Deals_home_appliance') in ShopAll_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified HomeAppliance_ShopAll Landing page URL:" + ShopAll_URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(ShopAll_URL)
        URLSegemntPage.get_segment()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_HomeAppliance_Module(self):
        logger.info(": ##### Started HOME_APPLIANCE Module URL verification #####\n")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/87ff1f6c64919397f2561e762a9e8f36.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        self.url_list.append(URL)
        assert ReadConfig.read_w46_HolidayDeals_T2_configData('CC_Module', 'home_appliance_url') in URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified HOME_APPLIANCE_Module Landing page URL:" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')