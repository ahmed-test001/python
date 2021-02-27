import json
import os
import sys
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Test_w_46_HolidayDeals_T2.Page.UrlSegmentPage import URLSegemntPage
from PageClass.BasePageClass import BasePage
from Utility_Files import ReadConfig
from Utility_Files.HTMLTestRunner import stdout_redirector
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class W46_DD_CreativePage(BasePage):

    def get_EPP_or_NonEPP_verification(self):
            logger.info(": ##### Started EPP version verification #####")
            subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
            if "EPP" in subjectlineTxt:
                EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/cd194720564918c9cfbd0803fff96ee3.jpg']")))
                EPP_WElement.is_displayed()
                assert EPP_WElement.is_displayed(), "Web Element not Displayed."
                logger.info(": successfully verified EPP version is present.")
            else:
                logger.info(': successfully verified EPP version NOT present.')
            logger.info(': #####  Verification Complete  #####\n')

    def get_DD_subjectLine_text_validation(self):
        logger.info(": ##### Started subjectLine_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        try:
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'DD_Note_reservers_Nonreserver_subject_line') in subjectlineTxt, "Subject Line Text Not Matching"
        except:
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module','DD_SL') in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Subject Line text assert with : " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_DD_pre_header_text_validation(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        logger.info(": ##### Started pre_header_text verification #####")
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        if "MB" in subjectlineTxt:
            if "NOTE" in subjectlineTxt:
                if "Non_Reservers" in subjectlineTxt:
                    assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'dd_note_nonReserve_pre_headertext') in pheaderTxt, "Pre Header Text Not Matching"
                elif "Reservers" in subjectlineTxt:
                    assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'dd_note_pre_headertext') in pheaderTxt, "Pre Header Text Not Matching"
            elif "GALAXY" in subjectlineTxt:
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'dd_note_pre_headertext') in pheaderTxt, "Pre Header Text Not Matching"
            elif "WEAR" in subjectlineTxt:
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module','dd_ware_pre_headertext') in pheaderTxt, "Pre Header Text Not Matching"
            elif "ACCESSORY" in subjectlineTxt:
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module','dd_ware_pre_headertext') in pheaderTxt, "Pre Header Text Not Matching"

        elif "TV" in subjectlineTxt:
            if "QLED" in subjectlineTxt:
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module','dd_qled_pre_headertext') in pheaderTxt, "Pre Header Text Not Matching"
            elif "ACCESSORY" in subjectlineTxt:
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module','dd_accessory_pre_headertext') in pheaderTxt, "Pre Header Text Not Matching"

        elif "CE" in subjectlineTxt:
            if "COMPUTER" in subjectlineTxt:
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module','dd_computer_pre_headertext') in pheaderTxt, "Pre Header Text Not Matching"

        elif "HA" in subjectlineTxt:
            if "LAUNDRY" in subjectlineTxt:
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module','dd_HA_laundry') in pheaderTxt, "Pre Header Text Not Matching"
            elif "KITCHEN" in subjectlineTxt:
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'dd_HA_KITCHEN') in pheaderTxt, "Pre Header Text Not Matching"

        logger.info(": Pre-Header text assert with : " + pheaderTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_DD_pre_header_link_validation(self):
        logger.info(": ##### Started pre_header_link_validation verification #####")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@target='_blank'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        self.url_list.append(URL)
        assert ReadConfig.read_w46_HolidayDeals_T2_configData('DD_Module', 'DD_pre_header_url') in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        # W46_DD_CreativePage.segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_giveWonder_link_validation(self):
        logger.info(": ##### Started GiveWonder Module URL verification #####")
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/964160ea34117060e7eb9df0f08d4100.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        givewonderURL = self.driver.current_url
        assert ReadConfig.read_w46_HolidayDeals_T2_configData('WEBLink', 'givewonderURL') in givewonderURL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Web Landing page URL:\n" + givewonderURL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(givewonderURL)
        URLSegemntPage.get_segment()
        # URLSegemntPage.segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')












