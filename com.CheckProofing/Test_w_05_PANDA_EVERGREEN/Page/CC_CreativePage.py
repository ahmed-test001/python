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
from PageClass.UrlSegmentPage import URLSegemntPage
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
        self.SL_3 = ExcelUtil(tc_name="").read_from_excel("3rd", 1, 8).strip()
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        assert self.SL_3 in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Validated Subject Line Text:: " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        self.PH_3 = ExcelUtil(tc_name="").read_from_excel("3rd", 2, 8).strip()
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        assert self.PH_3 in pheaderTxt, "Pre Header Text Not Matching"
        logger.info(": Validated Pre-Header Text:: " + pheaderTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_link_validation(self):
        logger.info(": ##### Started pre_header_link_validation verification #####")
        self.subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH_URL_N20 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 9, 12)
        self.PH_URL_N20U = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 10, 12)
        self.PH_URL_S20 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 12, 12)
        self.PH_URL_S20P = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 13, 12)
        self.PH_URL_S20U = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 14, 12)
        self.PH_URL_ZFlip = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 17, 12)
        self.PH_URL_ZFold2 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 18, 12)
        self.PH_URL_S10E = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 19, 12)
        self.PH_URL_S10 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 20, 12)
        self.PH_URL_S10P = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 21, 12)
        self.PH_URL_N10 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 23, 12)
        self.PH_URL_N10P = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 24, 12)
        self.PH_URL_A51 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 26, 12)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@target='_blank'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        if "A51" in self.subjectlineTxt:
            assert self.PH_URL_A51 in URL, "Web Landing Page URL is not Matching."
        elif "N10P" in self.subjectlineTxt:
            assert self.PH_URL_N10P in URL, "Web Landing Page URL is not Matching."
        elif "N10" in self.subjectlineTxt:
            assert self.PH_URL_N10 in URL, "Web Landing Page URL is not Matching."
        elif "S10P" in self.subjectlineTxt:
            assert self.PH_URL_S10P in URL, "Web Landing Page URL is not Matching."
        elif "S10E" in self.subjectlineTxt:
            assert self.PH_URL_S10E in URL, "Web Landing Page URL is not Matching."
        elif "S10" in self.subjectlineTxt:
            assert self.PH_URL_S10 in URL, "Web Landing Page URL is not Matching."
        elif "ZFLIP" in self.subjectlineTxt:
            assert self.PH_URL_ZFlip in URL, "Web Landing Page URL is not Matching."
        elif "ZFOLD2" in self.subjectlineTxt:
            assert self.PH_URL_ZFold2 in URL, "Web Landing Page URL is not Matching."
        elif "S20U" in self.subjectlineTxt:
            assert self.PH_URL_S20U in URL, "Web Landing Page URL is not Matching."
        elif "S20P" in self.subjectlineTxt:
            assert self.PH_URL_S20P in URL, "Web Landing Page URL is not Matching."
        elif "S20" in self.subjectlineTxt:
            assert self.PH_URL_S20 in URL, "Web Landing Page URL is not Matching."
        elif "N20U" in self.subjectlineTxt:
            assert self.PH_URL_N20U in URL, "Web Landing Page URL is not Matching."
        elif "N20" in self.subjectlineTxt:
            assert self.PH_URL_N20 in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        CC_CreativePage.get_URL_Segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Top_Hero_link_validation(self):
        logger.info(": ##### Started Hero_link_validation #####")
        time.sleep(4)
        # self.subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH_URL_N20 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 9, 12)
        self.PH_URL_N20U = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 10, 12)
        self.PH_URL_S20 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 12, 12)
        self.PH_URL_S20P = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 13, 12)
        self.PH_URL_S20U = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 14, 12)
        self.PH_URL_ZFlip = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 17, 12)
        self.PH_URL_ZFold2 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 18, 12)
        self.PH_URL_S10E = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 19, 12)
        self.PH_URL_S10 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 20, 12)
        self.PH_URL_S10P = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 21, 12)
        self.PH_URL_N10 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 23, 12)
        self.PH_URL_N10P = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 24, 12)
        self.PH_URL_A51 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 26, 12)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@alt='Hero_Image']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        if "A51" in self.subjectlineTxt:
            assert self.PH_URL_A51 in URL, "Web Landing Page URL is not Matching."
        elif "N10P" in self.subjectlineTxt:
            assert self.PH_URL_N10P in URL, "Web Landing Page URL is not Matching."
        elif "N10" in self.subjectlineTxt:
            assert self.PH_URL_N10 in URL, "Web Landing Page URL is not Matching."
        elif "S10P" in self.subjectlineTxt:
            assert self.PH_URL_S10P in URL, "Web Landing Page URL is not Matching."
        elif "S10E" in self.subjectlineTxt:
            assert self.PH_URL_S10E in URL, "Web Landing Page URL is not Matching."
        elif "S10" in self.subjectlineTxt:
            assert self.PH_URL_S10 in URL, "Web Landing Page URL is not Matching."
        elif "ZFLIP" in self.subjectlineTxt:
            assert self.PH_URL_ZFlip in URL, "Web Landing Page URL is not Matching."
        elif "ZFOLD2" in self.subjectlineTxt:
            assert self.PH_URL_ZFold2 in URL, "Web Landing Page URL is not Matching."
        elif "S20U" in self.subjectlineTxt:
            assert self.PH_URL_S20U in URL, "Web Landing Page URL is not Matching."
        elif "S20P" in self.subjectlineTxt:
            assert self.PH_URL_S20P in URL, "Web Landing Page URL is not Matching."
        elif "S20" in self.subjectlineTxt:
            assert self.PH_URL_S20 in URL, "Web Landing Page URL is not Matching."
        elif "N20U" in self.subjectlineTxt:
            assert self.PH_URL_N20U in URL, "Web Landing Page URL is not Matching."
        elif "N20" in self.subjectlineTxt:
            assert self.PH_URL_N20 in URL, "Web Landing Page URL is not Matching."

        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        CC_CreativePage.get_URL_Segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
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
        # subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text

        self.PH_category_N20 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 9, 13)
        self.PH_category_N20U = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 10, 13)
        self.PH_category_S20 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 12, 13)
        self.PH_category_S20P = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 13, 13)
        self.PH_category_S20U = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 14, 13)
        self.PH_category_ZFlip = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 17, 13)
        self.PH_category_ZFold2 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 18, 13)
        self.PH_category_S10E = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 19, 13)
        self.PH_category_S10 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 20, 13)
        self.PH_category_S10P = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 21, 13)
        self.PH_category_N10 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 23, 13)
        self.PH_category_N10P = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 24, 13)
        self.PH_category_A51 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 26, 13)

        self.PH_campaign_N20 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 9, 14)
        self.PH_campaign_N20U = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 10, 14)
        self.PH_campaign_S20 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 12, 14)
        self.PH_campaign_S20P = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 13, 14)
        self.PH_campaign_S20U = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 14, 14)
        self.PH_campaign_ZFlip = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 17, 14)
        self.PH_campaign_ZFold2 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 18, 14)
        self.PH_campaign_S10E = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 19, 14)
        self.PH_campaign_S10 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 20, 14)
        self.PH_campaign_S10P = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 21, 14)
        self.PH_campaign_N10 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 23, 14)
        self.PH_campaign_N10P = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 24, 14)
        self.PH_campaign_A51 = ExcelUtil(tc_name="").read_from_excel("Versions_and_Deeplinks", 26, 14)

        # parent_window = self.driver.current_window_handle
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@target='_blank'])[1]"))).click()
        # all_windows = self.driver.window_handles
        # child_window = [window for window in all_windows if window != parent_window][0]
        # self.driver.switch_to.window(child_window)
        # URL = self.driver.current_url
        # with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        # URLSegemntPage.get_segment()
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

            if "promoCode" in readdata['check_list'][0]:
                logger.info(": promoCode==" + str(readdata['check_list'][0]['promoCode']))
                # if ExcelUtil(tc_name="").read_from_excel("urlsegment", 14, 2) in readdata['check_list'][0]['promoCode']:
                #     assert ExcelUtil(tc_name="").read_from_excel("urlsegment", 14, 2) in readdata['check_list'][0]['promoCode'], "promoCode Not Matching."
                #     logger.info(": promoCode==" + ExcelUtil(tc_name="").read_from_excel("urlsegment", 14, 2))
                #     logger.info(": promoCode==" + ExcelUtil(tc_name="").read_from_excel("urlsegment", 14, 2))
                # else:
                #     logger.info(": FAIL:: promoCode NOT matched.")
            else:
                logger.info(": promoCode segment NOT present.")

            if "marsLinkCategory" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("urlsegment", 3, 3) in readdata['check_list'][0]['marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("urlsegment", 3, 3) in readdata['check_list'][0]['marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("urlsegment", 3, 3))
                else:
                    logger.info(": FAIL:: marsLinkCategory NOT matched.")
            else:
                logger.info(": marsLinkCategory segment NOT present.")

            if "category" in readdata['check_list'][0]:
                if "A51" in self.subjectlineTxt:
                    assert self.PH_category_A51 in readdata['check_list'][0]['category'], "Category Not Matching."
                    logger.info(": category==" + self.PH_category_A51)
                elif "N10P" in self.subjectlineTxt:
                    assert self.PH_category_N10P in readdata['check_list'][0]['category'], "Category Not Matching."
                    logger.info(": category==" + self.PH_category_N10P)
                elif "N10" in self.subjectlineTxt:
                    assert self.PH_category_N10 in readdata['check_list'][0]['category'], "Category Not Matching."
                    logger.info(": category==" + self.PH_category_N20)
                elif "S10P" in self.subjectlineTxt:
                    assert self.PH_category_S10P in readdata['check_list'][0]['category'], "Category Not Matching."
                    logger.info(": category==" + self.PH_category_S10P)
                elif "S10E" in self.subjectlineTxt:
                    assert self.PH_category_S10E in readdata['check_list'][0]['category'], "Category Not Matching."
                    logger.info(": category==" + self.PH_category_S10E)
                elif "S10" in self.subjectlineTxt:
                    assert self.PH_category_S10 in readdata['check_list'][0]['category'], "Category Not Matching."
                    logger.info(": category==" + self.PH_category_S10)
                elif "ZFOLD2" in self.subjectlineTxt:
                    assert self.PH_category_ZFold2 in readdata['check_list'][0]['category'], "Category Not Matching."
                    logger.info(": category==" + self.PH_category_ZFold2)
                elif "ZFLIP" in self.subjectlineTxt:
                    assert self.PH_category_ZFlip in readdata['check_list'][0]['category'], "Category Not Matching."
                    logger.info(": category==" + self.PH_category_ZFlip)
                elif "S20U" in self.subjectlineTxt:
                    assert self.PH_category_S20U in readdata['check_list'][0]['category'], "Category Not Matching."
                    logger.info(": category==" + self.PH_category_S20U)
                elif "S20P" in self.subjectlineTxt:
                    assert self.PH_category_S20P in readdata['check_list'][0]['category'], "Category Not Matching."
                    logger.info(": category==" + self.PH_category_S20P)
                elif "S20" in self.subjectlineTxt:
                    assert self.PH_category_S20 in readdata['check_list'][0]['category'], "Category Not Matching."
                    logger.info(": category==" + self.PH_category_S20)
                elif "N20U" in self.subjectlineTxt:
                    assert self.PH_category_N20U in readdata['check_list'][0]['category'], "Category Not Matching."
                    logger.info(": category==" + self.PH_category_N20U)
                elif "N20" in self.subjectlineTxt:
                    assert self.PH_category_N20 in readdata['check_list'][0]['category'], "Category Not Matching."
                    logger.info(": category==" + self.PH_category_N20)
                else:
                    logger.info(": FAIL:: Category NOT matched.")
            else:
                logger.info(": Category segment NOT present.")

            if "utm_campaign" in readdata['check_list'][0]:
                if "A51" in self.subjectlineTxt:
                    # if self.PH_category_N20 in readdata['check_list'][0]['category']:
                    assert self.PH_campaign_A51 in readdata['check_list'][0]['utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": campaign==" + self.PH_campaign_A51)
                elif "N10P" in self.subjectlineTxt:
                    assert self.PH_campaign_N10P in readdata['check_list'][0]['utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": campaign==" + self.PH_campaign_N10P)
                elif "N10" in self.subjectlineTxt:
                    assert self.PH_campaign_N10 in readdata['check_list'][0]['utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": campaign==" + self.PH_campaign_N10)
                elif "S10P" in self.subjectlineTxt:
                    assert self.PH_campaign_S10P in readdata['check_list'][0]['utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": campaign==" + self.PH_campaign_S10P)
                elif "S10E" in self.subjectlineTxt:
                    assert self.PH_campaign_S10E in readdata['check_list'][0]['utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": campaign==" + self.PH_campaign_S10E)
                elif "S10" in self.subjectlineTxt:
                    assert self.PH_campaign_S10 in readdata['check_list'][0]['utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": campaign==" + self.PH_campaign_S10)
                elif "ZFOLD2" in self.subjectlineTxt:
                    assert self.PH_campaign_ZFold2 in readdata['check_list'][0]['utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": campaign==" + self.PH_campaign_ZFold2)
                elif "ZFLIP" in self.subjectlineTxt:
                    assert self.PH_campaign_ZFlip in readdata['check_list'][0]['utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": campaign==" + self.PH_campaign_ZFlip)
                elif "S20U" in self.subjectlineTxt:
                    assert self.PH_campaign_S20U in readdata['check_list'][0]['utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": campaign==" + self.PH_campaign_S20U)
                elif "S20P" in self.subjectlineTxt:
                    assert self.PH_campaign_S20P in readdata['check_list'][0]['utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": campaign==" + self.PH_campaign_S20P)
                elif "S20" in self.subjectlineTxt:
                    assert self.PH_campaign_S20 in readdata['check_list'][0]['utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": campaign==" + self.PH_campaign_S20)
                elif "N20U" in self.subjectlineTxt:
                    assert self.PH_campaign_N20U in readdata['check_list'][0]['utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": campaign==" + self.PH_campaign_N20U)
                elif "N20" in self.subjectlineTxt:
                    assert self.PH_campaign_N20 in readdata['check_list'][0]['utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": campaign==" + self.PH_campaign_N20)
                else:
                    logger.info(": FAIL:: utm_campaign NOT matched.")
            else:
                logger.info(": utm_campaign segment NOT present.")
        # self.driver.back()
        # self.driver.switch_to.window(parent_window)


















