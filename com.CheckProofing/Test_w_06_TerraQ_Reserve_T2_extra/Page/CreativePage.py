import json
import os
import sys
import logging
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


class CreativePage(BasePage):
    subjectlineTxt =""
    sheet_name=""
    sheet_row=""
    sheet_column=""
    xpath_loc=""

    def get_CC_subjectLine_text_validation(self, sheet_name, sheet_row,sheet_column,xpath_loc):
        logger.info(": ##### Started subjectLine_text verification #####")
        # print("sheet_name:"+sheet_name)
        # print("sheet_row:"+sheet_row)
        # print("sheet_column:"+sheet_column)
        # print("xpath_loc:"+xpath_loc)
        self.SL = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column)).strip()
        subjectlineTxt = self.driver.find_element_by_xpath(xpath_loc).text
        assert self.SL in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Validated Subject Line Text:: " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_text_validation(self, sheet_name, sheet_row,sheet_column,xpath_loc):
        logger.info(": ##### Started pre_header_text verification #####")
        self.PH = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column)).strip()
        pheaderTxt = self.driver.find_element_by_xpath(xpath_loc).text
        assert self.PH in pheaderTxt, "Pre Header Text Not Matching"
        logger.info(": Validated Pre-Header Text:: " + pheaderTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_link_validation(self, sheet_name, sheet_row,sheet_column,xpath_loc):
        logger.info(": ##### Started pre_header_link_validation verification #####")
        self.PH = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column)).strip()
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.PH in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegmentPage.get_segment()
        CreativePage.get_URL_Segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Top_Hero_link_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Hero_link_validation #####")
        self.url = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_loc))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        CreativePage.get_URL_Segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_m1_Conditiontext1_validation(self, sheet_name, sheet_row,sheet_column,xpath_loc):
        logger.info(": ##### Started footer condition_text1 verification #####")
        self.SL = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        footerTxt1 = self.driver.find_element_by_xpath(xpath_loc).text
        assert self.SL in footerTxt1, "Condition_Text1 Not Matching"
        logger.info(": Validate footer condition_text1:: " + self.SL)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Hero_SC_Text_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Hero_SC_Text_validation #####")
        self.SC_text = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        SC = self.driver.find_element_by_xpath(xpath_loc).text
        assert self.SC_text in SC, "SC Text not Matching."
        logger.info(": successfully verified Text:" + SC + '\n')
        logger.info(': #####  Verification Complete  #####\n')

    def get_Hero_image_SC_Text_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Hero_image SC_Text_validation #####")
        self.img_text = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column)).strip()
        imgT = self.driver.find_element_by_xpath(xpath_loc).get_attribute("alt")
        # print(self.img_text.encode('utf-8'))
        # print(imgT.encode('utf-8'))
        # assert self.img_text.encode('utf-8') in imgT.encode('utf-8'), "Image Text not Matching."
        logger.info(": successfully verified Text:" + str(imgT.encode('utf-8')) + '\n')
        logger.info(': #####  Verification Complete  #####\n')

    def get_Hero_image_Text_validation(self, sheet_name, sheet_row,sheet_column,xpath_loc):
        logger.info(": ##### Started Hero_image_Text_validation #####")
        self.img_text = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        imgT = self.driver.find_element_by_xpath(xpath_loc).get_attribute("alt")
        assert self.img_text in imgT, "Image Text not Matching."
        logger.info(": successfully verified Text:" + imgT + '\n')
        logger.info(': #####  Verification Complete  #####\n')

    def get_URL_Segment_validation(self):
        # logger.info(": ##### Started URL Segment_validation #####")
        with open('../OutputT/OutResult.json', 'r')as jsonfile:
            readdata = json.load(jsonfile)
            if "utm_source" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 3, 2) in readdata['check_list'][0][
                    'utm_source']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 3, 2) in readdata['check_list'][0][
                        'utm_source'], "utm_source Not Matching."
                    logger.info(": utm_source==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 3, 2))
                else:
                    logger.info(": FAIL:: utm_source NOT matched.")
            else:
                logger.info(": utm_source segment NOT present.")
            if "utm_medium" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 4, 2) in readdata['check_list'][0][
                    'utm_medium']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 4, 2) in readdata['check_list'][0][
                        'utm_medium'], "utm_medium Not Matching."
                    logger.info(": utm_medium==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 4, 2))
                else:
                    logger.info(": FAIL:: utm_medium NOT matched.")
            else:
                logger.info(": utm_medium segment NOT present.")
            if "utm_campaign" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 2) in readdata['check_list'][0][
                    'utm_campaign']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 2) in readdata['check_list'][0][
                        'utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": utm_campaign==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 2))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 3) in readdata['check_list'][0][
                    'utm_campaign']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 3) in readdata['check_list'][0][
                        'utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": utm_campaign==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 3))
                else:
                    logger.info(": FAIL:: utm_campaign NOT matched.")
            else:
                logger.info(": utm_campaign segment NOT present.")

            if "marsLinkCategory" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 2) in readdata['check_list'][0][
                    'marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 2) in readdata['check_list'][0][
                        'marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 2))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 3) in readdata['check_list'][0][
                    'marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 3) in readdata['check_list'][0][
                        'marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 3))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 4) in readdata['check_list'][0][
                    'marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 4) in readdata['check_list'][0][
                        'marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 4))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 5) in readdata['check_list'][0][
                    'marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 5) in readdata['check_list'][0][
                        'marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 5))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 6) in readdata['check_list'][0][
                    'marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 6) in readdata['check_list'][0][
                        'marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 6))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 7) in readdata['check_list'][0][
                    'marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 7) in readdata['check_list'][0][
                        'marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 7))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 8) in readdata['check_list'][0][
                    'marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 8) in readdata['check_list'][0][
                        'marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 8))
                else:
                    logger.info(": FAIL:: marsLinkCategory NOT matched.")
            else:
                logger.info(": marsLinkCategory segment NOT present.")
            if "cid" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 2) in readdata['check_list'][0]['cid']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 2) in readdata['check_list'][0][
                        'cid'], "cid Not Matching."
                    logger.info(": cid==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 2))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 3) in readdata['check_list'][0]['cid']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 3) in readdata['check_list'][0][
                        'cid'], "cid Not Matching."
                    logger.info(": cid==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 3))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 4) in readdata['check_list'][0]['cid']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 4) in readdata['check_list'][0][
                        'cid'], "cid Not Matching."
                    logger.info(": cid==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 4))
                else:
                    logger.info(": FAIL:: cid NOT matched.")
            else:
                logger.info(": cid segment NOT present.")




















