import time
import unittest
import sys
import os
import logging
import glob
import warnings
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from lxml import html
import urllib.request
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Test_w_44_TV_SoundBar_Automation_T2.Page.url_segment import url_segment, segment_validation
from Utility_Files import ReadConfig
from Utility_Files.HTMLTestRunner import stdout_redirector
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class HTMLPage_W_45_HolidayDeals_Test(unittest.TestCase):
    driver = None
    unique_list = []

    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver1'), options=option)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        # with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
        #     urls = f.read().splitlines()
        #     for url in urls:
        #         if "Non_Reservers" and "CC" in url:
        #             self.driver.get(url)

    def test_write_CC_Category_URL(self):
        path = 'C:/Users/a.ferdous.CORP/Desktop/creativev2/smartphone/*.htm'
        with open('../TextFolder_Unique_URL/UniqueList_2.txt',"w")as f:
            files = glob.glob(path)
            for x in files:
                if "CC" in x:
                    self.unique_list.append(x)
                    someline = x + '\n'
                    f.writelines(someline)
                    print(someline)

    def test_write_DD_Category_URL(self):
        path = 'C:/Users/a.ferdous.CORP/Desktop/creativev2/smartphone/*.htm'
        with open('../TextFolder_Unique_URL/UniqueList_2.txt',"w")as f:
            files = glob.glob(path)
            for x in files:
                if "DD" in x:
                    self.unique_list.append(x)
                    someline = x + '\n'
                    f.writelines(someline)
                    print(someline)

    def test_count_url_write(self):
        count=0
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            for x in f:
                count+=1
        print("Total Number of URL: " , count)


    def test_get_url(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "HA_LAUNDRY" in subjectlineTxt:
            # self.driver.find_element_by_xpath("//*[@alt='Home Appliances - Shop ALL']").click()
            parent_window = self.driver.current_window_handle
            linkT = self.driver.find_element_by_xpath("//*[@alt='SMARTPHONES_Shop ALL']")
            linkT.click()
            # time.sleep(2)
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            time.sleep(5)
            ShopNow_URL = self.driver.current_url
            print("HA_LAUNDRY current url: " + ShopNow_URL)
            self.driver.switch_to.window(parent_window)
            time.sleep(5)

        if "MB_GALAXY" in subjectlineTxt:
            parent_window1 = self.driver.current_window_handle
            linkT = self.driver.find_element_by_xpath("//*[@alt='Home Appliances - Shop ALL']")
            linkT.click()
            time.sleep(5)
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window1][0]
            self.driver.switch_to.window(child_window)
            time.sleep(5)
            MB_GALAXY_URL = self.driver.current_url
            print("MB_GALAXY current url: " + MB_GALAXY_URL)
            # self.driver.switch_to.window(parent_window1)
            time.sleep(5)

        else:
            print("Nothoing Print")





    # def test_verifyEPPtext(self):
    #     logger.info(': ' + self.test_verifyEPPtext.__name__ + "\n #####  Starting TEST  ##### ")
    #     EPP_Txt = self.driver.find_element_by_xpath("//*[contains(text(),'Save up to an additional 20% with your member')]").text
    #     self.assertEqual(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'epp_text'), EPP_Txt, msg="Epp Text Not Matching")
    #     logger.info(": Expected EPP Text: " + EPP_Txt)
    #     logger.info('\n #####  TEST Complete  #####')
    #
    # def test_verifyGiveWonderEarlyaccess(self):
    #     logger.info(': ' + self.test_verifyGiveWonderEarlyaccess.__name__ + "\n #####  Starting TEST  ##### ")
    #     GWEA_Txt = self.driver.find_element_by_xpath("//*[contains(text(),'The gift that keeps on giving ')]").text
    #     self.assertEqual(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'givewonder_text'), GWEA_Txt, msg="Give Wonder Text Not Matching")
    #     logger.info(": Expected GIve wonder Text: " + GWEA_Txt)
    #     logger.info('\n #####  TEST Complete  #####')
    #
    # def test_a1_subjectLine_text_validation(self):
    #     logger.info(': '+self.test_a1_subjectLine_text_validation.__name__ + "\n #####  Starting TEST  ##### ")
    #     subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
    #     self.assertIn(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'subject_line'), subjectlineTxt, msg="Subject Line Text Not Matching")
    #     logger.info(": Subject Line text assert with : " + subjectlineTxt)
    #     logger.info('\n #####  TEST Complete  #####')
    #
    # def test_a2_pre_header_text_validation(self):
    #     logger.info(': '+self.test_a2_pre_header_text_validation.__name__ + "\n #####  Starting TEST  ##### ")
    #     pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
    #     self.assertEqual(ReadConfig.read_w45_HolidayDealsT1_configData('DATA', 'pre_headertext'), pheaderTxt, msg="Pre Header Text Not Matching")
    #     logger.info(": Pre-Header text assert with : " + pheaderTxt)
    #     logger.info('\n #####  TEST Complete  #####')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()