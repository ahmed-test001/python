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

    # def get_CC_device_text_validation(self):
    #     logger.info(": ##### Started subjectLine_text verification #####")
    #     # self.SL = ExcelUtil(tc_name="").read_from_excel("Copy", 9, 3).strip()
    #     # self.SL_non = ExcelUtil(tc_name="").read_from_excel("Copy", 9, 4).strip()
    #     subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='name'])[1]").text
    #     # if "Non" not in subjectlineTxt:
    #     #     assert self.SL in subjectlineTxt, "Subject line text NOT matched."
    #     # elif "Non" in subjectlineTxt:
    #     #     assert self.SL_non in subjectlineTxt, "Subject line text NOT matched."
    #     logger.info(": Validated Subject Line Text:: " + str(subjectlineTxt.encode('utf-8')))
    #     logger.info(': #####  Verification Complete  #####\n')

    def get_CC_subjectLine_text_validation(self):
        logger.info(": ##### Started subjectLine_text verification #####")
        self.SL = ExcelUtil(tc_name="").read_from_excel("Copy", 9, 3).strip()
        self.SL_non = ExcelUtil(tc_name="").read_from_excel("Copy", 9, 4).strip()
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "Non" not in subjectlineTxt:
            assert self.SL in subjectlineTxt, "Subject line text NOT matched."
        elif "Non" in subjectlineTxt:
            assert self.SL_non in subjectlineTxt, "Subject line text NOT matched."
        logger.info(": Validated Subject Line Text:: " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        self.PH = ExcelUtil(tc_name="").read_from_excel("Copy", 10, 3).strip()
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        assert self.PH in pheaderTxt, "Pre Header Text Not Matching"
        logger.info(": Validated Pre-Header Text:: " + pheaderTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_link_validation(self):
        logger.info(": ##### Started pre_header_link_validation verification #####")
        self.PH = ExcelUtil(tc_name="").read_from_excel("Module", 6, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@target='_blank'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        # print("Excel::"+self.PH)
        # print(URL)
        assert self.PH in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegmentPage.get_segment()
        # CC_CreativePage.get_URL_Segment_validation(self)
        CC_CreativePage.get_tradein_DeviceName_validation(self)
        # CC_CreativePage.get_modelColor_validation(self)
        # CC_CreativePage.get_modelprocessor_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Top_Hero_link_validation(self):
        logger.info(": ##### Started Hero_link_validation #####")
        # self.subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.url = ExcelUtil(tc_name="").read_from_excel("Module", 6, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='kv_cta']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegmentPage.get_segment()
        CC_CreativePage.get_URL_Segment_validation(self)
        # CC_CreativePage.get_tradein_DeviceName_validation(self)
        # CC_CreativePage.get_modelColor_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module1_link_validation(self):
        logger.info(": ##### Started Module1_link_validation #####")
        # self.subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.url = ExcelUtil(tc_name="").read_from_excel("Module", 6, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ecosystem_hl_cta_table']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegmentPage.get_segment()
        CC_CreativePage.get_URL_Segment_validation(self)
        # CC_CreativePage.get_tradein_DeviceName_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module2_link_validation(self):
        logger.info(": ##### Started Module2_link_validation #####")
        # self.subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.url = ExcelUtil(tc_name="").read_from_excel("Module", 6, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='value_prop_hl_sh_cta']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegmentPage.get_segment()
        CC_CreativePage.get_URL_Segment_validation(self)
        # CC_CreativePage.get_tradein_DeviceName_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_m1_Conditiontext1_validation(self):
        logger.info(": ##### Started footer condition_text1 verification #####")
        # self.SL = ExcelUtil(tc_name="").read_from_excel("TERM_CONDITION", 2, 1)
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        footerTxt1 = self.driver.find_element_by_xpath("//*[@id='footer_text1']/p/span").text
        # assert self.SL in footerTxt1, "Condition_Text1 Not Matching"
        logger.info(": Validate footer condition_text1:: " + footerTxt1)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_m2_Conditiontext2_validation(self):
        logger.info(": ##### Started footer condition_text2 verification #####")
        # self.SL = ExcelUtil(tc_name="").read_from_excel("TERM_CONDITION", 2, 1)
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        footerTxt1 = self.driver.find_element_by_xpath("//*[@id='footer_text2']/p/span").text
        # assert self.SL in footerTxt1, "Condition_Text1 Not Matching"
        logger.info(": Validate footer condition_text1:: " + footerTxt1)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_m3_Conditiontext3_validation(self):
        logger.info(": ##### Started footer condition_text3 verification #####")
        # self.SL = ExcelUtil(tc_name="").read_from_excel("TERM_CONDITION", 2, 1)
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        footerTxt1 = self.driver.find_element_by_xpath("//*[@id='footer_text3']/p/span").text
        # assert self.SL in footerTxt1, "Condition_Text1 Not Matching"
        logger.info(": Validate footer condition_text1:: " + footerTxt1)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_m4_Conditiontext4_validation(self):
        logger.info(": ##### Started footer condition_text4 verification #####")
        # self.SL = ExcelUtil(tc_name="").read_from_excel("TERM_CONDITION", 2, 1)
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        footerTxt1 = self.driver.find_element_by_xpath("//*[@id='footer_text4']/p/span").text
        # assert self.SL in footerTxt1, "Condition_Text1 Not Matching"
        logger.info(": Validate footer condition_text1:: " + footerTxt1)
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

    def get_CC_kv_sc_text_validation(self):
        logger.info(": ##### Started kv_sc_text verification #####")
        self.sc = ExcelUtil(tc_name="").read_from_excel("Copy", 22, 7).strip()
        self.sc_epp = ExcelUtil(tc_name="").read_from_excel("Copy", 22, 8).strip()
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        subcopyTxt = self.driver.find_element_by_xpath("//*[@id='kv_sc']").text
        if "EPP" not in subjectlineTxt:

            assert self.sc in subcopyTxt, "subcopy text NOT matched."
        elif "EPP" in subjectlineTxt:

            assert self.sc_epp.encode('utf-8') in subcopyTxt.encode('utf-8'), "subcopy text NOT matched."
            # assert self.sc_epp in subcopyTxt, "subcopy text NOT matched."
        logger.info(": Validated Subject Line Text:: " + str(subcopyTxt.encode('utf-8')))
        logger.info(': #####  Verification Complete  #####\n')

    def get_Hero_HL_Text_validation(self):
        logger.info(": ##### Started Hero_HL_Text_validation #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        Hero_SL = self.driver.find_element_by_xpath("//*[@id='hero_hl1']").get_attribute("alt")
        if "EPP" in subjectlineTxt:
            if "NonReservers" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/cf127116fe58da2d23468c6fd22a093d.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "Reservers" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/13f136bb495067f0c96da0bdb1fa4cfb.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
        elif "EPP" not in subjectlineTxt:
            if "NonReservers" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/55d03e219218fd9221aa851887ad01aa.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "Reservers" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/19e551e92620b6b4d4f920e15de46459.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
        # logger.info(": Validated Subject Line Text:: " + str(Hero_SL))
        logger.info(': #####  Verification Complete  #####\n')

    def get_URL_Segment_validation(self):
        logger.info(": ##### Started URL Segment_validation #####")
        with open('../OutputT/OutResult.json', 'r')as jsonfile:
            readdata = json.load(jsonfile)
            if "utm_source" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 3, 2) in readdata['check_list'][0]['utm_source']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 3, 2) in readdata['check_list'][0]['utm_source'], "utm_source Not Matching."
                    logger.info(": utm_source==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 3, 2) )
                else:
                    logger.info(": FAIL:: utm_source NOT matched.")
            else:
                logger.info(": utm_source segment NOT present.")
            if "utm_medium" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 4, 2) in readdata['check_list'][0]['utm_medium']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 4, 2) in readdata['check_list'][0]['utm_medium'], "utm_medium Not Matching."
                    logger.info(": utm_medium==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 4, 2))
                else:
                    logger.info(": FAIL:: utm_medium NOT matched.")
            else:
                logger.info(": utm_medium segment NOT present.")
            if "utm_campaign" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 2) in readdata['check_list'][0]['utm_campaign']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 2) in readdata['check_list'][0]['utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": utm_campaign==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 2))
                else:
                    logger.info(": FAIL:: utm_campaign NOT matched.")
            else:
                logger.info(": utm_campaign segment NOT present.")

            if "marsLinkCategory" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 2) in readdata['check_list'][0]['marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 2) in readdata['check_list'][0]['marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 2))
                else:
                    logger.info(": FAIL:: marsLinkCategory NOT matched.")
            else:
                logger.info(": marsLinkCategory segment NOT present.")
            if "cid" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 2) in readdata['check_list'][0]['cid']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 2) in readdata['check_list'][0]['cid'], "cid Not Matching."
                    logger.info(": cid==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 2))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 3) in readdata['check_list'][0]['cid']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 3) in readdata['check_list'][0]['cid'], "cid Not Matching."
                    logger.info(": cid==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 3))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 4) in readdata['check_list'][0]['cid']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 4) in readdata['check_list'][0]['cid'], "cid Not Matching."
                    logger.info(": cid==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 4))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 5) in readdata['check_list'][0]['cid']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 5) in readdata['check_list'][0]['cid'], "cid Not Matching."
                    logger.info(": cid==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 5))
                else:
                    logger.info(": FAIL:: cid NOT matched.")
            else:
                logger.info(": cid segment NOT present.")

    def get_tradein_DeviceName_validation(self):
        # logger.info(": ##### Started tradein_DeviceName validation  #####")
        with open('../OutputT/OutResult.json', 'r')as jsonfile:
            readdata = json.load(jsonfile)
            try:
                deviceName = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[3]"))).text
                if "tradeIn" in readdata['check_list'][0]:
                    if ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 4, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 4, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 4, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 5, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 5, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 5, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 6, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 6, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 6, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 7, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 7, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 7, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 8, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 8, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 8, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 9, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 9, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 9, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 10, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 10, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 10, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 11, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 11, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 11, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 12, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 12, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 12, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 13, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 13, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 13, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 14, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 14, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 14, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 15, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 15, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 15, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 16, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 16, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 16, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 17, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 17, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 17, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 18, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 18, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 18, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 19, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 19, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 19, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 20, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 20, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 20, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 21, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 21, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 21, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 22, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 22, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 22, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 23, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 23, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 23, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 24, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 24, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 24, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 25, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 25, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 25, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 26, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 26, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 26, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 27, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 27, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 27, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 28, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 28, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 28, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 29, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 29, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 29, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 30, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 30, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 30, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 31, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 31, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 31, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 32, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 32, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 32, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 33, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 33, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 33, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 34, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 34, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 34, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 35, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 35, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 35, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 36, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 36, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 36, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 37, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 37, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 37, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 38, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 38, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 38, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 39, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 39, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 39, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 40, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 40, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 40, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 41, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 41, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 41, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 42, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 42, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 42, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 43, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 43, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 43, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 44, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 44, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 44, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 45, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 45, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 45, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 46, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 46, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 46, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 47, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 47, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 47, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 48, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 48, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 48, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 49, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 49, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 49, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 50, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 50, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 50, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 51, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 51, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 51, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 52, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 52, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 52, 1))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 53, 2) in readdata['check_list'][0]['tradeIn']:
                        assert deviceName in ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 53, 1)
                        logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 53, 1))
                    else:
                        logger.info(": DeviceName NOT Matched.")
            except:
                    logger.info(": Trade-In_Device segment NOT present.")

    def get_modelprocessor_validation(self):
        # logger.info(": ##### Started skipCarrier validation From Landing Page #####")
        with open('../OutputT/OutResult.json', 'r')as jsonfile:
            readdata = json.load(jsonfile)
            if "modelCode" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 4, 3) in readdata['check_list'][0]['modelCode']:
                    # i3_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='intel®-core™-i3-processor' and @aria-checked='true']")))
                    # assert i3_WElement.is_displayed(), "Processor Option not Selected."
                    logger.info(": modelCode Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 4, 5))

                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 5, 3) in readdata['check_list'][0]['modelCode']:
                    celeron_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tile7 selected type-device row-list-item four-row-item' and @aria-checked='true']")))
                    assert celeron_WElement.is_displayed(), "Processor Option not Selected."
                    logger.info(": modelCode Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 5, 5))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 6, 3) in readdata['check_list'][0]['modelCode']:
                    i3_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tile7 type-device row-list-item four-row-item' and @aria-checked='true']")))
                    assert i3_WElement.is_displayed(), "Processor Option not Selected."
                    logger.info(": modelCode Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 6, 4))

                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 9, 3) in readdata['check_list'][0]['modelCode']:
                    celeron_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tile7 selected type-device row-list-item four-row-item' and @aria-checked='true']")))
                    assert celeron_WElement.is_displayed(), "Processor Option not Selected."
                    logger.info(": modelCode Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 9, 5))
                else:
                    logger.info(": Processor Not matched.")
            else:
                logger.info(": Processor_modelCode Not Present.")

    def get_modelColor_validation(self):
        # logger.info(": ##### Started skipCarrier validation From Landing Page #####")
        with open('../OutputT/OutResult.json', 'r')as jsonfile:
            readdata = json.load(jsonfile)
            if "modelCode" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 4, 3) in readdata['check_list'][0]['modelCode']:
                    redcolor_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='fiesta-red' and @aria-checked='true']")))
                    assert redcolor_WElement.is_displayed(), "color Option not Selected."
                    logger.info(": model color ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 4, 4))

                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 5, 3) in readdata['check_list'][0]['modelCode']:
                    greycolor_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='mercury-gray' and @aria-checked='true']")))
                    assert greycolor_WElement.is_displayed(), "color Option not Selected."
                    logger.info(": modelCode Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 5, 4))

                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 6, 3) in readdata['check_list'][0]['modelCode']:
                    redcolor_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='fiesta-red' and @aria-checked='true']")))
                    assert redcolor_WElement.is_displayed(), "color Option not Selected."
                    logger.info(": model color ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 6, 4))

                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 9, 3) in readdata['check_list'][0]['modelCode']:
                    greycolor_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='mercury-gray' and @aria-checked='true']")))
                    assert greycolor_WElement.is_displayed(), "color Option not Selected."
                    logger.info(": modelCode Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 9, 4))
            else:
                logger.info(": model_Color Not Present.")



















