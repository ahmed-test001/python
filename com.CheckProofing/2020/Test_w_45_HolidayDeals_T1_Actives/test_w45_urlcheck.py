import time
import unittest
import sys
import os
import logging
import warnings
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from PageClass.UrlSegmentPage import URLSegemntPage

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from Utility_Files import ReadConfig
from Utility_Files.HTMLTestRunner import stdout_redirector
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class HTMLPage_W_45Test(unittest.TestCase):
    method1=""
    driver = None
    url_list = []
    method_list_in_Url = []

    @classmethod
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver1'), options=option)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        self.wait = WebDriverWait(self.driver, 10)
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            urls = f.read().splitlines()
            for url in urls:
                if "DD" in url:
                    self.driver.get(url)


    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_a1_family1_validation(self):

            if  self.method1:
                logger.info(': ' + self.test_a1_family1_validation.__name__ + "\n #####  Starting TEST  ##### ")
                parent_window = self.driver.current_window_handle
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='UHD 4K TV']"))).click()
                all_windows = self.driver.window_handles
                child_window = [window for window in all_windows if window != parent_window][0]
                self.driver.switch_to.window(child_window)
                Pre_Header_URL = self.driver.current_url
                self.url_list.append(Pre_Header_URL)
                # self.method_list_in_Url.append(self.test_a1_8ktv_link_validation.__name__)
                self.assertIn(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'tv_url'), Pre_Header_URL,msg="Web Landing Page URL is not Matching by Buy_Now_URL")
                logger.info("\nsuccessfully verified Web Landing page URL:" + Pre_Header_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:
                    f.writelines(Pre_Header_URL)
                URLSegemntPage.get_segment()
                # segment_validation()
                self.driver.close()
                self.driver.switch_to.window(parent_window)
                logger.info('\n ####  TEST Complete  ####')

            elif self.method1:
                logger.info(': ' + self.test_a1_family1_validation.__name__ + "\n #####  Starting TEST  ##### ")
                parent_window = self.driver.current_window_handle
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='HA washers and dryers']"))).click()
                all_windows = self.driver.window_handles
                child_window = [window for window in all_windows if window != parent_window][0]
                self.driver.switch_to.window(child_window)
                Pre_Header_URL = self.driver.current_url
                self.url_list.append(Pre_Header_URL)
                # self.method_list_in_Url.append(self.test_h1_dryer_link_validation.__name__)
                self.assertIn(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'ha_url'), Pre_Header_URL,msg="Web Landing Page URL is not Matching by Buy_Now_URL")
                logger.info("\nsuccessfully verified Web Landing page URL:" + Pre_Header_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(Pre_Header_URL)
                URLSegemntPage.get_segment()
                # segment_validation()
                self.driver.close()
                self.driver.switch_to.window(parent_window)
                logger.info('\n ####  TEST Complete  ####')
            else:
                logger.info(': ' + self.test_a1_family1_validation.__name__ + "\n #####  Starting TEST  ##### ")
                parent_window = self.driver.current_window_handle
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='Galaxy Note20 5G / Note 20 Ultra 5G']"))).click()
                all_windows = self.driver.window_handles
                child_window = [window for window in all_windows if window != parent_window][0]
                self.driver.switch_to.window(child_window)
                Pre_Header_URL = self.driver.current_url
                self.url_list.append(Pre_Header_URL)
                # self.method_list_in_Url.append(self.test_h1_dryer_link_validation.__name__)
                self.assertIn(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'mb_galaxy'), Pre_Header_URL,msg="Web Landing Page URL is not Matching by Buy_Now_URL")
                logger.info("\nsuccessfully verified Web Landing page URL:" + Pre_Header_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(Pre_Header_URL)
                URLSegemntPage.get_segment()
                # segment_validation()
                self.driver.close()
                self.driver.switch_to.window(parent_window)
                logger.info('\n ####  TEST Complete  ####')

    def test_a2_family2_validation(self):

            if self.method1:
                logger.info(': ' + self.test_a2_family2_validation.__name__ + "\n #####  Starting TEST  ##### ")
                parent_window = self.driver.current_window_handle
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='4K TV']"))).click()
                all_windows = self.driver.window_handles
                child_window = [window for window in all_windows if window != parent_window][0]
                self.driver.switch_to.window(child_window)
                Pre_Header_URL = self.driver.current_url
                self.url_list.append(Pre_Header_URL)
                # self.method_list_in_Url.append(self.test_a1_8ktv_link_validation.__name__)
                self.assertIn(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'tv_url'), Pre_Header_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
                logger.info("\nsuccessfully verified Web Landing page URL:" + Pre_Header_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Pre_Header_URL)
                URLSegemntPage.get_segment()
                # segment_validation()
                self.driver.close()
                self.driver.switch_to.window(parent_window)
                logger.info('\n ####  TEST Complete  ####')
            elif self.method1:
                logger.info(': ' + self.test_a2_family2_validation.__name__ + "\n #####  Starting TEST  ##### ")
                parent_window = self.driver.current_window_handle
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='HA Jet Stick']"))).click()
                all_windows = self.driver.window_handles
                child_window = [window for window in all_windows if window != parent_window][0]
                self.driver.switch_to.window(child_window)
                Pre_Header_URL = self.driver.current_url
                self.url_list.append(Pre_Header_URL)
                # self.method_list_in_Url.append(self.test_h1_dryer_link_validation.__name__)
                self.assertIn(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'ha_url'), Pre_Header_URL,msg="Web Landing Page URL is not Matching by Buy_Now_URL")
                logger.info("\nsuccessfully verified Web Landing page URL:" + Pre_Header_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(Pre_Header_URL)
                URLSegemntPage.get_segment()
                # segment_validation()
                self.driver.close()
                self.driver.switch_to.window(parent_window)
                logger.info('\n ####  TEST Complete  ####')
            else:
                logger.info(': ' + self.test_a2_family2_validation.__name__ + "\n #####  Starting TEST  ##### ")
                parent_window = self.driver.current_window_handle
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='Galaxy S20 FE 5G']"))).click()
                all_windows = self.driver.window_handles
                child_window = [window for window in all_windows if window != parent_window][0]
                self.driver.switch_to.window(child_window)
                Pre_Header_URL = self.driver.current_url
                time.sleep(5)
                self.url_list.append(Pre_Header_URL)
                # self.method_list_in_Url.append(self.test_h1_dryer_link_validation.__name__)
                self.assertIn(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'mb_galaxy1'), Pre_Header_URL,msg="Web Landing Page URL is not Matching by Buy_Now_URL")
                logger.info("\nsuccessfully verified Web Landing page URL:" + Pre_Header_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(Pre_Header_URL)
                URLSegemntPage.get_segment()
                # segment_validation()
                self.driver.close()
                self.driver.switch_to.window(parent_window)
                logger.info('\n ####  TEST Complete  ####')

    def test_a3_family3_validation(self):
            if self.method1:
                logger.info(': ' + self.test_a3_family3_validation.__name__ + "\n #####  Starting TEST  ##### ")
                parent_window = self.driver.current_window_handle
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='Frame TV']"))).click()
                all_windows = self.driver.window_handles
                child_window = [window for window in all_windows if window != parent_window][0]
                self.driver.switch_to.window(child_window)
                Pre_Header_URL = self.driver.current_url
                self.url_list.append(Pre_Header_URL)
                # self.method_list_in_Url.append(self.test_a1_8ktv_link_validation.__name__)
                self.assertIn(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'tv_url'), Pre_Header_URL,msg="Web Landing Page URL is not Matching by Buy_Now_URL")
                logger.info("\nsuccessfully verified Web Landing page URL:" + Pre_Header_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:
                    f.writelines(Pre_Header_URL)
                URLSegemntPage.get_segment()
                # segment_validation()
                self.driver.close()
                self.driver.switch_to.window(parent_window)
                logger.info('\n ####  TEST Complete  ####')
            elif self.method1:
                logger.info(': ' + self.test_a3_family3_validation.__name__ + "\n #####  Starting TEST  ##### ")
                parent_window = self.driver.current_window_handle
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='HA Robot Vacuums']"))).click()
                all_windows = self.driver.window_handles
                child_window = [window for window in all_windows if window != parent_window][0]
                self.driver.switch_to.window(child_window)
                Pre_Header_URL = self.driver.current_url
                self.url_list.append(Pre_Header_URL)
                # self.method_list_in_Url.append(self.test_h1_dryer_link_validation.__name__)
                self.assertIn(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'ha_url'), Pre_Header_URL,msg="Web Landing Page URL is not Matching by Buy_Now_URL")
                logger.info("\nsuccessfully verified Web Landing page URL:" + Pre_Header_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(Pre_Header_URL)
                URLSegemntPage.get_segment()
                # segment_validation()
                self.driver.close()
                self.driver.switch_to.window(parent_window)
                logger.info('\n ####  TEST Complete  ####')
            else:
                logger.info(': ' + self.test_a3_family3_validation.__name__ + "\n #####  Starting TEST  ##### ")
                parent_window = self.driver.current_window_handle
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='Galaxy Z Fold2 5G']"))).click()
                all_windows = self.driver.window_handles
                child_window = [window for window in all_windows if window != parent_window][0]
                self.driver.switch_to.window(child_window)
                Pre_Header_URL = self.driver.current_url
                self.url_list.append(Pre_Header_URL)
                # self.method_list_in_Url.append(self.test_h1_dryer_link_validation.__name__)
                self.assertIn(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'mb_galaxy'), Pre_Header_URL,msg="Web Landing Page URL is not Matching by Buy_Now_URL")
                logger.info("\nsuccessfully verified Web Landing page URL:" + Pre_Header_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(Pre_Header_URL)
                URLSegemntPage.get_segment()
                # segment_validation()
                self.driver.close()
                self.driver.switch_to.window(parent_window)
                logger.info('\n ####  TEST Complete  ####')

    def test_a4_family4_validation(self):
            if self.method1:
                logger.info(': ' + self.test_a4_family4_validation.__name__ + "\n #####  Starting TEST  ##### ")
                parent_window = self.driver.current_window_handle
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='Q Series Soundbars']"))).click()
                all_windows = self.driver.window_handles
                child_window = [window for window in all_windows if window != parent_window][0]
                self.driver.switch_to.window(child_window)
                Pre_Header_URL = self.driver.current_url
                self.url_list.append(Pre_Header_URL)
                # self.method_list_in_Url.append(self.test_a1_8ktv_link_validation.__name__)
                self.assertIn(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'tv_url'), Pre_Header_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
                logger.info("\nsuccessfully verified Web Landing page URL:" + Pre_Header_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:
                    f.writelines(Pre_Header_URL)
                URLSegemntPage.get_segment()
                # segment_validation()
                self.driver.close()
                self.driver.switch_to.window(parent_window)
                logger.info('\n ####  TEST Complete  ####')
            elif self.method1:
                logger.info(': ' + self.test_a4_family4_validation.__name__ + "\n #####  Starting TEST  ##### ")
                parent_window = self.driver.current_window_handle
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='HA Clean Station, Air Dresser and Jet 90 Stick Vacuum']"))).click()
                all_windows = self.driver.window_handles
                child_window = [window for window in all_windows if window != parent_window][0]
                self.driver.switch_to.window(child_window)
                Pre_Header_URL = self.driver.current_url
                self.url_list.append(Pre_Header_URL)
                # self.method_list_in_Url.append(self.test_h1_dryer_link_validation.__name__)
                self.assertIn(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'ha_url'), Pre_Header_URL,msg="Web Landing Page URL is not Matching by Buy_Now_URL")
                logger.info("\nsuccessfully verified Web Landing page URL:" + Pre_Header_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(Pre_Header_URL)
                URLSegemntPage.get_segment()
                # segment_validation()
                self.driver.close()
                self.driver.switch_to.window(parent_window)
                logger.info('\n ####  TEST Complete  ####')
            else:
                logger.info(': ' + self.test_a4_family4_validation.__name__ + "\n #####  Starting TEST  ##### ")
                parent_window = self.driver.current_window_handle
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='Galaxy S20+ 5G']"))).click()
                all_windows = self.driver.window_handles
                child_window = [window for window in all_windows if window != parent_window][0]
                self.driver.switch_to.window(child_window)
                Pre_Header_URL = self.driver.current_url
                self.url_list.append(Pre_Header_URL)
                # self.method_list_in_Url.append(self.test_h1_dryer_link_validation.__name__)
                self.assertIn(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'mb_galaxy1'), Pre_Header_URL,msg="Web Landing Page URL is not Matching by Buy_Now_URL")
                logger.info("\nsuccessfully verified Web Landing page URL:" + Pre_Header_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(Pre_Header_URL)
                URLSegemntPage.get_segment()
                # segment_validation()
                self.driver.close()
                self.driver.switch_to.window(parent_window)
                logger.info('\n ####  TEST Complete  ####')

    def test_a5_family5_validation(self):
            if self.method1:
                logger.info(': ' + self.test_a5_family5_validation.__name__ + "\n #####  Starting TEST  ##### ")
                parent_window = self.driver.current_window_handle
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='UHD 4K TV']"))).click()
                all_windows = self.driver.window_handles
                child_window = [window for window in all_windows if window != parent_window][0]
                self.driver.switch_to.window(child_window)
                Pre_Header_URL = self.driver.current_url
                self.url_list.append(Pre_Header_URL)
                # self.method_list_in_Url.append(self.test_a1_8ktv_link_validation.__name__)
                self.assertIn(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'tv_url'), Pre_Header_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
                logger.info("\nsuccessfully verified Web Landing page URL:" + Pre_Header_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:
                    f.writelines(Pre_Header_URL)
                URLSegemntPage.get_segment()
                # segment_validation()
                self.driver.close()
                self.driver.switch_to.window(parent_window)
                logger.info('\n ####  TEST Complete  ####')
            elif self.method1:
                logger.info(': ' + self.test_a5_family5_validation.__name__ + "\n #####  Starting TEST  ##### ")
                parent_window = self.driver.current_window_handle
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='HA Clean Station, Air Dresser and Jet 75 Stick Vacuum']"))).click()
                all_windows = self.driver.window_handles
                child_window = [window for window in all_windows if window != parent_window][0]
                self.driver.switch_to.window(child_window)
                Pre_Header_URL = self.driver.current_url
                self.url_list.append(Pre_Header_URL)
                # self.method_list_in_Url.append(self.test_h1_dryer_link_validation.__name__)
                self.assertIn(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'ha_url'), Pre_Header_URL,msg="Web Landing Page URL is not Matching by Buy_Now_URL")
                logger.info("\nsuccessfully verified Web Landing page URL:" + Pre_Header_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(Pre_Header_URL)
                URLSegemntPage.get_segment()
                # segment_validation()
                self.driver.close()
                self.driver.switch_to.window(parent_window)
                logger.info('\n ####  TEST Complete  ####')
            else:
                logger.info(': ' + self.test_a5_family5_validation.__name__ + "\n #####  Starting TEST  ##### ")
                parent_window = self.driver.current_window_handle
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='Galaxy A71 5G or A51 5G']"))).click()
                all_windows = self.driver.window_handles
                child_window = [window for window in all_windows if window != parent_window][0]
                self.driver.switch_to.window(child_window)
                Pre_Header_URL = self.driver.current_url
                self.url_list.append(Pre_Header_URL)
                # self.method_list_in_Url.append(self.test_h1_dryer_link_validation.__name__)
                self.assertIn(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'mb_galaxy1'), Pre_Header_URL,msg="Web Landing Page URL is not Matching by Buy_Now_URL")
                logger.info("\nsuccessfully verified Web Landing page URL:" + Pre_Header_URL + '\n')
                with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(Pre_Header_URL)
                URLSegemntPage.get_segment()
                # segment_validation()
                self.driver.close()
                self.driver.switch_to.window(parent_window)
                logger.info('\n ####  TEST Complete  ####')


if __name__ == '__main__':
    unittest.main()