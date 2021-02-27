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

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Test_w_42_PrimeDay_Disrupt.Page.url_segment import url_segment, segment_validation
from Utility_Files import ReadConfig
from Utility_Files.HTMLTestRunner import stdout_redirector
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class HTMLPage_W_42_PrimeDay_GEN_Test(unittest.TestCase):
    driver = None
    url_list = []
    method_list_in_Url = []

    @classmethod
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver1'), options=option)
        warnings.filterwarnings(action="ignore",message="unclosed",category=ResourceWarning)
        self.driver.get(ReadConfig.read_w42_PrimeDay_configData('PrimeDataGEN','html_path'))
        self.wait = WebDriverWait(self.driver, 10)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_a1_subjectLine_text_validation(self):
        logger.info(': '+self.test_a1_subjectLine_text_validation.__name__ + "\n #####  Starting TEST  ##### ")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.assertEqual(ReadConfig.read_w42_PrimeDay_configData('PrimeDataGEN', 'subject_line'), subjectlineTxt,
                      msg="Subject Line Text Not Matching")
        logger.info(": Subject Line text assert with : " + ReadConfig.read_w42_PrimeDay_configData('PrimeDataGEN', 'subject_line'))
        logger.info('\n ####  TEST Complete  ####')

    def test_a2_pre_header_text_validation(self):
        logger.info(': '+self.test_a2_pre_header_text_validation.__name__ + "\n #####  Starting TEST  ##### ")
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        self.assertEqual(ReadConfig.read_w42_PrimeDay_configData('PrimeDataGEN', 'pre_headertext'), pheaderTxt, msg="Pre Header Text Not Matching")
        logger.info(": Pre-Header text assert with : " + pheaderTxt)
        logger.info('\n ####  TEST Complete  ####')

    def test_a3_pre_header_link_validation(self):
        logger.info(': '+self.test_a3_pre_header_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@target='_blank'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Pre_Header_URL = self.driver.current_url
        self.url_list.append(Pre_Header_URL)
        self.method_list_in_Url.append(self.test_a3_pre_header_link_validation.__name__)
        self.assertEqual(ReadConfig.read_w42_PrimeDay_configData('PrimeDataGEN', 'url'), Pre_Header_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Pre_Header_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f:f.writelines(Pre_Header_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_b1_OctoberSale_link_validation(self):
        logger.info(': '+self.test_b1_OctoberSale_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1032']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_b1_OctoberSale_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'oct_deals'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_c1_Tablets_link_validation(self):
        logger.info(': '+self.test_c1_Tablets_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1033']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_c1_Tablets_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'cellphone_acc'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_c2_galaxyS7_BuyNow_link_validation(self):
        logger.info(': '+self.test_c2_galaxyS7_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1035']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_c2_galaxyS7_BuyNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 's7'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_c3_galaxyTabS6_BuyNow_link_validation(self):
        logger.info(': '+self.test_c3_galaxyTabS6_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1036']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_c3_galaxyTabS6_BuyNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'tabs6'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f:f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_c4_galaxyTabA_BuyNow_link_validation(self):
        logger.info(': '+self.test_c4_galaxyTabA_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1037']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_c4_galaxyTabA_BuyNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'tabA'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f:f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_d1_AudioWatch_link_validation(self):
        logger.info(': '+self.test_d1_AudioWatch_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1038']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_d1_AudioWatch_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'cellphone_acc'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_d2_galaxyBuds_BuyNow_link_validation(self):
        logger.info(': '+self.test_d2_galaxyBuds_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1040']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_d2_galaxyBuds_BuyNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'buds'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_d3_galaxyWatch_Active2_BuyNow_link_validation(self):
        logger.info(': '+self.test_d3_galaxyWatch_Active2_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1041']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_d3_galaxyWatch_Active2_BuyNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'active2'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_d4_galaxyWatch_Active_BuyNow_link_validation(self):
        logger.info(': '+self.test_d4_galaxyWatch_Active_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1042']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_d4_galaxyWatch_Active_BuyNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'active'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_e1_SmartPhones_link_validation(self):
        logger.info(': '+self.test_e1_SmartPhones_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1043']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_e1_SmartPhones_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'smartphone'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_e2_galaxyA71_BuyNow_link_validation(self):
        logger.info(': '+self.test_e2_galaxyA71_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1045']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_e2_galaxyA71_BuyNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'a71'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_e3_CellPhoneDeals_link_validation(self):
        logger.info(': '+self.test_e3_CellPhoneDeals_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1046']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        # self.wait.until(EC.url_contains(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'smartphone')))
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_e3_CellPhoneDeals_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'smartphone'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_e4_galaxyS20plus_BuyNow_link_validation(self):
        logger.info(': '+self.test_e4_galaxyS20plus_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1047']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        self.wait.until(EC.url_changes(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 's205g')))
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_e4_galaxyS20plus_BuyNow_link_validation.__name__)
        self.assertNotIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 's205g'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_e5_galaxyS20ultra_BuyNow_link_validation(self):
        logger.info(': '+self.test_e5_galaxyS20ultra_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1048']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_e5_galaxyS20ultra_BuyNow_link_validation.__name__)
        self.assertNotIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 's20ultra'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_e6_galaxyNote20_BuyNow_link_validation(self):
        logger.info(': '+self.test_e6_galaxyNote20_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1049']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_e6_galaxyNote20_BuyNow_link_validation.__name__)
        self.assertNotIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'note20'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_f1_TVSoundBar_link_validation(self):
        logger.info(': '+self.test_f1_TVSoundBar_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1050']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_f1_TVSoundBar_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'TvSoundBar'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_f2_QLED8kTV_ShopNow_link_validation(self):
        logger.info(': '+self.test_f2_QLED8kTV_ShopNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1052']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Shop_Now_URL = self.driver.current_url
        self.url_list.append(Shop_Now_URL)
        self.method_list_in_Url.append(self.test_f2_QLED8kTV_ShopNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'Qled8k'), Shop_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Shop_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Shop_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_f3_QLED4kTV_ShopNow_link_validation(self):
        logger.info(': '+self.test_f3_QLED4kTV_ShopNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1053']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Shop_Now_URL = self.driver.current_url
        self.url_list.append(Shop_Now_URL)
        self.method_list_in_Url.append(self.test_f3_QLED4kTV_ShopNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'Qled4k'), Shop_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Shop_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Shop_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_f4_Frame32TV_BuyNow_link_validation(self):
        logger.info(': '+self.test_f4_Frame32TV_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1054']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_f4_Frame32TV_BuyNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'frame32'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f:f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_f5_Terrace55TV_BuyNow_link_validation(self):
        logger.info(': '+self.test_f5_Terrace55TV_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1055']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_f5_Terrace55TV_BuyNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'terrace55'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f:f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_f6_Sero43TV_BuyNow_link_validation(self):
        logger.info(': '+self.test_f6_Sero43TV_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1056']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_f6_Sero43TV_BuyNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'sero43'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_f7_Serif43TV_BuyNow_link_validation(self):
        logger.info(': '+self.test_f7_Serif43TV_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1057']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_f7_Serif43TV_BuyNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'serif43'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_g1_HomeAppliance_link_validation(self):
        logger.info(': '+self.test_g1_HomeAppliance_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1058']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_g1_HomeAppliance_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'homeappliance'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_g2_ShopWasher_link_validation(self):
        logger.info(': '+self.test_g2_ShopWasher_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='Shop washers']"))).click()
        Shop_Now_URL = self.driver.current_url
        self.url_list.append(Shop_Now_URL)
        self.method_list_in_Url.append(self.test_g2_ShopWasher_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'washers'), Shop_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Shop_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Shop_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        logger.info('\n ####  TEST Complete  ####')

    def test_g3_ShopDryer_link_validation(self):
        logger.info(': '+self.test_g3_ShopDryer_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='Shop dryers']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Shop_Now_URL = self.driver.current_url
        self.url_list.append(Shop_Now_URL)
        self.method_list_in_Url.append(self.test_g3_ShopDryer_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'dryers'), Shop_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Shop_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Shop_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_g4_Ranges_ShopNow_link_validation(self):
        logger.info(': '+self.test_g4_Ranges_ShopNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1060']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Shop_Now_URL = self.driver.current_url
        self.url_list.append(Shop_Now_URL)
        self.method_list_in_Url.append(self.test_g4_Ranges_ShopNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'ranges'), Shop_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Shop_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Shop_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_g5_AirDresser_BuyNow_link_validation(self):
        logger.info(': '+self.test_g5_AirDresser_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1061']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_g5_AirDresser_BuyNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'airdresser'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_g6_Vacuums_BuyNow_link_validation(self):
        logger.info(': '+self.test_g6_Vacuums_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1062']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_g6_Vacuums_BuyNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'vacuums'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_g7_CubeAirPurifier_BuyNow_link_validation(self):
        logger.info(': '+self.test_g7_CubeAirPurifier_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1063']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_g7_CubeAirPurifier_BuyNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'cubeAirpurifier'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f: f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_g8_CleaneStation_BuyNow_link_validation(self):
        logger.info(': '+self.test_g8_CleaneStation_BuyNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1064']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_g8_CleaneStation_BuyNow_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'cleanstation'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f:f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_h1_SignUpSavings_link_validation(self):
        logger.info(': '+self.test_h1_SignUpSavings_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1066']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Buy_Now_URL = self.driver.current_url
        self.url_list.append(Buy_Now_URL)
        self.method_list_in_Url.append(self.test_h1_SignUpSavings_link_validation.__name__)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('WEBLink', 'signupsavings'), Buy_Now_URL, msg="Web Landing Page URL is not Matching by Buy_Now_URL")
        logger.info("\nsuccessfully verified Web Landing page URL:"+Buy_Now_URL+'\n')
        with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt', 'w')as f:f.writelines(Buy_Now_URL)
        url_segment()
        segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_i1_pay_later_icon_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_i1_pay_later_icon_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        payover = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@_label='Pay_Over_Time_Title'])[1]")))
        self.driver.execute_script("arguments[0].scrollIntoView();", payover)
        self.driver.execute_script("arguments[0].click();", payover)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        # self.wait.until(EC.number_of_windows_to_be(child_window))
        self.driver.switch_to.window(child_window)
        paylater_url = self.driver.current_url
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('EMAILPage', 'pay_later_url'), paylater_url, msg="Pay Later Landing Page URL is not Matched.")
        logger.info(': Assertion Pay Later with: ' + paylater_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_i2_free_shipping_icon_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_i2_free_shipping_icon_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        freeShipping = self.driver.find_element_by_xpath("//a[@_label='Free_Shipping_Title']")
        self.driver.execute_script("arguments[0].scrollIntoView();", freeShipping)
        self.driver.execute_script("arguments[0].click();", freeShipping)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        freeShipping_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('EMAILPage', 'free_shipping_url'), freeShipping_url, msg="Free Shipping Landing Page URL is not Matched.")
        logger.info(': Assertion Free SHipping with: ' + freeShipping_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_j1_google_play_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_j1_google_play_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        googleApp = self.driver.find_element_by_xpath("//a[@_label='Download_App_Google']")
        self.driver.execute_script("arguments[0].scrollIntoView();", googleApp)
        self.driver.execute_script("arguments[0].click();", googleApp)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        googleApp_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('EMAILPage', 'google_play_url'), googleApp_url, msg="Google Play store Page URL Not Matched.")
        logger.info(': Assertion Free Google Play App with: ' + googleApp_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_j2_apple_store_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_j2_apple_store_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        appleApp = self.driver.find_element_by_xpath("//a[@_label='Download_App_Apple']")
        self.driver.execute_script("arguments[0].scrollIntoView();", appleApp)
        self.driver.execute_script("arguments[0].click();", appleApp)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        appleApp_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('EMAILPage', 'apple_url'), appleApp_url, msg="Apple App Page URL Not Matched.")
        logger.info(': Assertion Free Apple App with: ' + appleApp_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_k1_free_shipping_details_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k1_free_shipping_details_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        freeShip_button = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[2]")
        self.driver.execute_script("arguments[0].scrollIntoView();", freeShip_button)
        self.driver.execute_script("arguments[0].click();", freeShip_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        freeShip_button_url = self.driver.current_url
        time.sleep(5)
        self.assertEqual(ReadConfig.read_w42_PrimeDay_configData('EMAILPage', 'free_shipping_url'), freeShip_button_url, msg="Free Shipping Page URL Not Matched.")
        logger.info(': Assertion Free Ship Button URL with: ' + freeShip_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_k2_Mobile_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k2_Mobile_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        freeShip_button = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[3]")
        self.driver.execute_script("arguments[0].scrollIntoView();", freeShip_button)
        self.driver.execute_script("arguments[0].click();", freeShip_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        mobile_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('EMAILPage', 'mobile_button_url'), mobile_button_url, msg="Mobile Page URL Not Matched.")
        logger.info(': Assertion Mobile Button URL with: ' + mobile_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_k3_TV_Audio_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k3_TV_Audio_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        Audio_button = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[4]")
        self.driver.execute_script("arguments[0].scrollIntoView();", Audio_button)
        self.driver.execute_script("arguments[0].click();", Audio_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        Tv_Audio_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('EMAILPage', 'tv_audio_button_url'), Tv_Audio_button_url, msg="TV & Audio Page URL Not Matched.")
        logger.info(': Assertion TV & Audio Button URL with: ' + Tv_Audio_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_k4_computing_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k4_computing_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        Computing_button = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[5]")
        self.driver.execute_script("arguments[0].scrollIntoView();", Computing_button)
        self.driver.execute_script("arguments[0].click();", Computing_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        Computing_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('EMAILPage', 'computing_button_url'), Computing_button_url, msg="Computing Page URL Not Matched.")
        logger.info(': Assertion Computing Button URL with: ' + Computing_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_k5_appliances_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k5_appliances_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        Appliance_button = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[6]")
        self.driver.execute_script("arguments[0].scrollIntoView();", Appliance_button)
        self.driver.execute_script("arguments[0].click();", Appliance_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        Appliance_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('EMAILPage', 'appliances_button_url'), Appliance_button_url, msg="Appliance Page URL Not Matched.")
        logger.info(': Assertion Appliance Button URL with: ' + Appliance_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_k6_weekly_offer_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_k6_weekly_offer_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        WeeklyOffer_button = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[7]")
        self.driver.execute_script("arguments[0].scrollIntoView();", WeeklyOffer_button)
        self.driver.execute_script("arguments[0].click();", WeeklyOffer_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        WeeklyOffer_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('EMAILPage', 'weekly_offer_button_url'), WeeklyOffer_button_url, msg="Weekly Offer Page URL Not Matched.")
        logger.info(': Assertion Weekly Offer Button URL with: ' + WeeklyOffer_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_l1_facebook_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_l1_facebook_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        Facebook_button = self.driver.find_element_by_xpath("//a[@_label='Facebook']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Facebook_button)
        self.driver.execute_script("arguments[0].click();", Facebook_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        Facebook_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('EMAILPage', 'facebook_url'), Facebook_button_url, msg="Facebook Page URL Not Matched.")
        logger.info(': Assertion Facebook Button URL with: ' + Facebook_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_l2_instagram_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_l2_instagram_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        Instagram_button = self.driver.find_element_by_xpath("//a[@_label='Instagram']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Instagram_button)
        self.driver.execute_script("arguments[0].click();", Instagram_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        Instagram_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('EMAILPage', 'instagram_url'), Instagram_button_url, msg="Instagram Page URL Not Matched.")
        logger.info(': Assertion Instagram Button URL with: ' + Instagram_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_l3_twitter_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_l3_twitter_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        Twitter_button = self.driver.find_element_by_xpath("//a[@_label='Twitter']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Twitter_button)
        self.driver.execute_script("arguments[0].click();", Twitter_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        Twitter_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('EMAILPage', 'twitter_url'), Twitter_button_url, msg="Twitter Page URL Not Matched.")
        logger.info(': Assertion Twitter Button URL with: ' + Twitter_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    def test_l4_youtube_button_LandingPage_URL_validation(self):
        logger.info(': ' + self.test_l4_youtube_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        Youtube_button = self.driver.find_element_by_xpath("// a[@_label='Youtube']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Youtube_button)
        self.driver.execute_script("arguments[0].click();", Youtube_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        Youtube_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w42_PrimeDay_configData('EMAILPage', 'youtube_url'), Youtube_button_url, msg="Youtube Page URL Not Matched.")
        logger.info(': Assertion YouTube Button URL with: ' + Youtube_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('\n ####  TEST Complete  ####')

    # def test_m1_collect_unique_URL_with_method_Name(self):
    #     logger.info(' ##### ' + self.test_m1_collect_unique_URL_with_method_Name.__name__ + "\n #####  Starting TEST  ##### ")
    #     with open('../TextFolder/TestOut_UniqueURL_DictList.txt', 'w')as f:
    #         res_dct = dict(zip(self.method_list_in_Url,self.url_list))
    #         temp = []
    #         res = dict()
    #         for key, val in res_dct.items():
    #             if val not in temp:
    #                 temp.append(val)
    #                 res[key] = val
    #         # print(res)
    #         f.writelines(str(res))
    #         logger.info("### Collected Unique URL with Method Name: " + str(res) + "\n")
    #     logger.info('\n ####  TEST Complete  ####')
    #
    # def test_m2_get_unique_URL_list(self):
    #     logger.info(' ##### ' + self.test_m2_get_unique_URL_list.__name__ + "\n #####  Starting TEST  ##### ")
    #     with open('../TextFolder/TestIn_UniqueURL_List.txt', 'w')as f:
    #         unique_list = []
    #         for x in self.url_list:
    #             # check unique_list or not
    #             if x not in unique_list:
    #                 unique_list.append(x)
    #
    #         for x in unique_list:
    #             someline = x+'\n'
    #             f.writelines(someline)
    #             logger.info("##### Get unique URL List:  "+x)
    #     logger.info('\n ####  TEST Complete  ####')


if __name__ == '__main__':
    unittest.main()