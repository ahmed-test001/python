import json
import os
import sys
import logging
import time
from urllib.parse import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Utility_Files.ExcelReaderUtil import ExcelUtil
from PageClass.UrlSegmentPage import URLSegmentPage
from PageClass.BasePageClass import BasePage
from Utility_Files.HTMLTestRunner import stdout_redirector
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class CC_CreativePage(BasePage):
    subjectlineTxt =""

    def get_CC_subjectLine_text_validation(self):
        logger.info(": ##### Started subjectLine_text verification #####")
        self.SL = ExcelUtil(tc_name="").read_from_excel("Copy", 7, 3).strip()
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        print(self.SL)
        print(subjectlineTxt)
        assert self.SL in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Validated Subject Line Text:: " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        self.PH = ExcelUtil(tc_name="").read_from_excel("Copy", 8, 3).strip()
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        assert self.PH in pheaderTxt, "Pre Header Text Not Matching"
        logger.info(": Validated Pre-Header Text:: " + pheaderTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_link_validation(self):
        logger.info(": ##### Started pre_header_link_validation verification #####")
        self.PH = ExcelUtil(tc_name="").read_from_excel("Generic", 6, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@target='_blank'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.PH in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegmentPage.get_segment()
        CC_CreativePage.get_URL_Segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Top_Hero_link_validation(self):
        logger.info(": ##### Started Hero_link_validation #####")
        time.sleep(4)
        # self.subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.url = ExcelUtil(tc_name="").read_from_excel("Generic", 6, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='Hero_Image']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegmentPage.get_segment()
        CC_CreativePage.get_URL_Segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_m1_Conditiontext1_validation(self):
        logger.info(": ##### Started footer condition_text1 verification #####")
        self.SL = ExcelUtil(tc_name="").read_from_excel("TERM_CONDITION", 2, 1)
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        footerTxt1 = self.driver.find_element_by_xpath("//*[@id='footer_text1']/span").text
        assert self.SL in footerTxt1, "Condition_Text1 Not Matching"
        logger.info(": Validate footer condition_text1:: " + self.SL)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Hero_Text_validation(self):
        logger.info(": ##### Started Hero_Text_validation #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        ProofTxt = self.driver.find_element_by_xpath("(//span)[35]").text
        self.PH_URL_N20 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 9, 11)
        self.PH_URL_N20U = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 10, 11)
        self.PH_URL_S20 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 12, 11)
        self.PH_URL_S20P = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 13, 11)
        self.PH_URL_S20U = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 14, 11)
        self.PH_URL_ZFlip = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 17, 11)
        self.PH_URL_ZFold2 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 18, 11)
        self.PH_URL_S10E = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 19, 11)
        self.PH_URL_S10 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 20, 11)
        self.PH_URL_S10P = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 21, 11)
        self.PH_URL_N10 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 23, 11)
        self.PH_URL_N10P = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 24, 11)
        self.PH_URL_A51 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 26, 11)
        if "N20" in subjectlineTxt:
            assert self.PH_URL_N20 in ProofTxt, "Web Landing Page URL is not Matching."
        elif "N20U" in subjectlineTxt:
            assert self.PH_URL_N20U in ProofTxt, "Web Landing Page URL is not Matching."
        elif "S20" in subjectlineTxt:
            assert self.PH_URL_S20 in ProofTxt, "Web Landing Page URL is not Matching."
        elif "S20P" in subjectlineTxt:
            assert self.PH_URL_S20P in ProofTxt, "Web Landing Page URL is not Matching."
        elif "S20U" in subjectlineTxt:
            assert self.PH_URL_S20U in ProofTxt, "Web Landing Page URL is not Matching."
        elif "ZFLIP" in subjectlineTxt:
            assert self.PH_URL_ZFlip in ProofTxt, "Web Landing Page URL is not Matching."
        elif "ZFOLD2" in subjectlineTxt:
            assert self.PH_URL_ZFold2 in ProofTxt, "Web Landing Page URL is not Matching."
        elif "S10E" in subjectlineTxt:
            assert self.PH_URL_S10E in ProofTxt, "Web Landing Page URL is not Matching."
        elif "S10" in subjectlineTxt:
            assert self.PH_URL_S10 in ProofTxt, "Web Landing Page URL is not Matching."
        elif "S10P" in subjectlineTxt:
            assert self.PH_URL_S10P in ProofTxt, "Web Landing Page URL is not Matching."
        elif "N10" in subjectlineTxt:
            assert self.PH_URL_N10 in ProofTxt, "Web Landing Page URL is not Matching."
        elif "N10P" in subjectlineTxt:
            assert self.PH_URL_N10P in ProofTxt, "Web Landing Page URL is not Matching."
        elif "A51" in subjectlineTxt:
            assert self.PH_URL_A51 in ProofTxt, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Text:\n" + ProofTxt + '\n')
        # self.driver.back()
        logger.info(': #####  Verification Complete  #####\n')

    def get_URL_Segment_validation(self):
        logger.info(": ##### Started URL Segment_validation #####")
        with open('../OutputT/OutResult.json', 'r')as jsonfile:
            readdata = json.load(jsonfile)
            if "utm_source" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("urlsegment", 3, 2) in readdata['check_list'][0]['utm_source']:
                    assert ExcelUtil(tc_name="").read_from_excel("urlsegment", 3, 2) in readdata['check_list'][0]['utm_source'], "utm_source Not Matching."
                    logger.info(": utm_source==" + ExcelUtil(tc_name="").read_from_excel("urlsegment", 3, 2) )
                else:
                    logger.info(": FAIL:: utm_source NOT matched.")
            else:
                logger.info(": utm_source segment NOT present.")
            if "utm_medium" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("urlsegment", 4, 2) in readdata['check_list'][0]['utm_medium']:
                    assert ExcelUtil(tc_name="").read_from_excel("urlsegment", 4, 2) in readdata['check_list'][0]['utm_medium'], "utm_medium Not Matching."
                    logger.info(": utm_medium==" + ExcelUtil(tc_name="").read_from_excel("urlsegment", 4, 2))
                else:
                    logger.info(": FAIL:: utm_medium NOT matched.")
            else:
                logger.info(": utm_medium segment NOT present.")
            if "utm_campaign" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("urlsegment", 5, 2) in readdata['check_list'][0]['utm_campaign']:
                    assert ExcelUtil(tc_name="").read_from_excel("urlsegment", 5, 2) in readdata['check_list'][0]['utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": utm_campaign==" + ExcelUtil(tc_name="").read_from_excel("urlsegment", 5, 2))
                else:
                    logger.info(": FAIL:: utm_campaign NOT matched.")
            else:
                logger.info(": utm_campaign segment NOT present.")

            if "marsLinkCategory" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("urlsegment", 7, 3) in readdata['check_list'][0]['marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("urlsegment", 7, 3) in readdata['check_list'][0]['marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("urlsegment", 7, 3))
                else:
                    logger.info(": FAIL:: marsLinkCategory NOT matched.")
            else:
                logger.info(": marsLinkCategory segment NOT present.")
            if "cid" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("urlsegment", 2, 4) in readdata['check_list'][0]['cid']:
                    assert ExcelUtil(tc_name="").read_from_excel("urlsegment", 2, 4) in readdata['check_list'][0]['cid'], "cid Not Matching."
                    logger.info(": cid==" + ExcelUtil(tc_name="").read_from_excel("urlsegment", 2, 4))
                else:
                    logger.info(": FAIL:: cid NOT matched.")
            else:
                logger.info(": cid segment NOT present.")




















