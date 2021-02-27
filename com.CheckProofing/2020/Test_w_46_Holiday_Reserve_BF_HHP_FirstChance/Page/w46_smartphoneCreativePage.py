import os
import sys
import logging
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


class w46_SmartphoneCreativePage(BasePage):

    def get_W46_MB_NOTE_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "MB_NOTE" in subjectlineTxt:
            logger.info(": ##### Started MB_NOTE20 Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/389f648ac09cceb0e6b7b12217661711.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('WEBLink', 'note20') in  Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_NOTE20 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started MB_GALAXY_S20 Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/e6fb0eab63354e6b1118ea3c6570e39e.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_2_URL = self.driver.current_url
            self.url_list.append(Module_2_URL)
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('WEBLink', 's20') in Module_2_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_GALAXY_S20 Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started MB_FOLD2 Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/3f8cfcb7a553c4dc3e4fcc6cc5c3a10a.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_3_URL = self.driver.current_url
            self.url_list.append(Module_3_URL)
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('WEBLink', 'foldZ') in Module_3_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_FOLD2 Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started MB_GALAXY_A71_5G Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/b97616f5f07089ccaf023fa946ae3fa4.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_4_URL = self.driver.current_url
            self.url_list.append(Module_4_URL)
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('WEBLink', 'A71') in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_GALAXY_A71_5G Module URL:" + Module_4_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

    def get_W46_MB_GALAXY_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "MB_GALAXY" in subjectlineTxt:
            logger.info(": ##### Started MB_GALAXY_S20 Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/e6fb0eab63354e6b1118ea3c6570e39e.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_2_URL = self.driver.current_url
            self.url_list.append(Module_2_URL)
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('WEBLink', 's20') in Module_2_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_GALAXY_S20 Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started MB_NOTE20 Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/389f648ac09cceb0e6b7b12217661711.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_2_URL = self.driver.current_url
            self.url_list.append(Module_2_URL)
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('WEBLink', 'note20') in Module_2_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_NOTE20 Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started MB_FOLD2 Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/3f8cfcb7a553c4dc3e4fcc6cc5c3a10a.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_3_URL = self.driver.current_url
            self.url_list.append(Module_3_URL)
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('WEBLink', 'foldZ') in Module_3_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_FOLD2 Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started MB_GALAXY_A71_5G Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/b97616f5f07089ccaf023fa946ae3fa4.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_4_URL = self.driver.current_url
            self.url_list.append(Module_4_URL)
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('WEBLink', 'A71') in Module_4_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_GALAXY_A71_5G Module URL:" + Module_4_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

    def get_W46_MB_FOLD_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "MB_FOLD" in subjectlineTxt:
            logger.info(": ##### Started MB_FOLD2 Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/3f8cfcb7a553c4dc3e4fcc6cc5c3a10a.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('WEBLink', 'foldZ') in Module_1_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_FOLD2 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started MB_NOTE20 Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/389f648ac09cceb0e6b7b12217661711.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_2_URL = self.driver.current_url
            self.url_list.append(Module_2_URL)
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('WEBLink', 'note20') in Module_2_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_NOTE20 Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started MB_GALAXY_S20 Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/e6fb0eab63354e6b1118ea3c6570e39e.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_3_URL = self.driver.current_url
            self.url_list.append(Module_3_URL)
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('WEBLink', 's20') in Module_3_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_GALAXY_S20 Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started MB_GALAXY_A71_5G Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/b97616f5f07089ccaf023fa946ae3fa4.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_4_URL = self.driver.current_url
            self.url_list.append(Module_4_URL)
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('WEBLink', 'A71') in Module_4_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_GALAXY_A71_5G Module URL:" + Module_4_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

    def get_W46_MB_MIDTIER_Module(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "MB_MIDTIER" in subjectlineTxt:
            logger.info(": ##### Started MB_GALAXY_A71_5G Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/b97616f5f07089ccaf023fa946ae3fa4.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_4_URL = self.driver.current_url
            self.url_list.append(Module_4_URL)
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('WEBLink', 'A71') in Module_4_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_GALAXY_A71_5G Module URL:" + Module_4_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_4_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started MB_NOTE20 Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/389f648ac09cceb0e6b7b12217661711.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_2_URL = self.driver.current_url
            self.url_list.append(Module_2_URL)
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('WEBLink', 'note20') in Module_2_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_NOTE20 Module URL:" + Module_2_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_2_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started MB_GALAXY_S20 Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/e6fb0eab63354e6b1118ea3c6570e39e.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_3_URL = self.driver.current_url
            self.url_list.append(Module_3_URL)
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('WEBLink', 's20') in Module_3_URL,"Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_GALAXY_S20 Module URL:" + Module_3_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_3_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')
            logger.info(": ##### Started MB_FOLD2 Module URL verification #####")
            parent_window = self.driver.current_window_handle
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/3f8cfcb7a553c4dc3e4fcc6cc5c3a10a.jpg']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            Module_1_URL = self.driver.current_url
            self.url_list.append(Module_1_URL)
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('WEBLink', 'foldZ') in Module_1_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
            logger.info(": successfully verified MB_FOLD2 Module URL:" + Module_1_URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(Module_1_URL)
            URLSegemntPage.get_segment()
            URLSegemntPage.segment_validation()
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            logger.info(': #####  Verification Complete  #####\n')

    def get_EPP_or_NonEPP_verification(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
            logger.info(": ##### Started EPP version verification #####")
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/38850d7759d209a2df3f90bd22dcd56d.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), "Web Element not Displayed."
            logger.info(": successfully verified EPP Web Element is present.")
        else:
            logger.info(": ##### Started EPP version verification #####")
            logger.info(': successfully verified EPP Element NOT present.')
        logger.info(': #####  Verification Complete  #####\n')

    def get_subjectLine_text_validation(self):
        logger.info(": ##### Started subjectLine_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        try:
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('DataEPP', 'subject_line') in subjectlineTxt, "Subject Line Text Not Matching"
        except:
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('DataGEN','subject_line') in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Subject Line text assert with : " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        try:
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('DataEPP', 'pre_headertext') in pheaderTxt, "Pre Header Text Not Matching"
        except:
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('DataGEN', 'pre_headertext') in pheaderTxt, "Pre Header Text Not Matching"
        logger.info(": Pre-Header text assert with : " + pheaderTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_pre_header_link_validation(self):
        logger.info(": ##### Started pre_header_link_validation verification #####")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@target='_blank'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Pre_Header_URL = self.driver.current_url
        self.url_list.append(Pre_Header_URL)
        try:
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('DataEPP', 'url') in Pre_Header_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        except:
            assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('DataGEN', 'url') in Pre_Header_URL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Web Landing page URL:\n"+Pre_Header_URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(Pre_Header_URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_giveWonder_link_validation(self):
        logger.info(": ##### Started GiveWonder Module URL verification #####")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/e01a02e8574a31662178fcc3a9165e12.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        givewonderURL = self.driver.current_url
        self.url_list.append(givewonderURL)
        assert ReadConfig.read_w46_HolidayReserve_BF_HHP_configData('WEBLink', 'givewonderURL') in givewonderURL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Web Landing page URL:\n" + givewonderURL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(givewonderURL)
        URLSegemntPage.get_segment()
        URLSegemntPage.segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')











