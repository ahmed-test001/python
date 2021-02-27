import logging
import os
import sys
import time
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

    def get_EPP_or_NonEPP_verification(self):
        logger.info(": ##### Started EPP version verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/39e6e2bb3929e664996a7bd380e40cd5.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), "Web Element not Displayed."
            logger.info(": successfully verified EPP version is present.")
        else:
            logger.info(': successfully verified EPP version NOT present.')
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_subjectLine_text_validation(self):
        logger.info(": ##### Started subjectLine_text verification #####")
        self.SL_700 = ExcelUtil(tc_name="").read_from_excel("Generic", 9, 3).strip()
        self.SL_550 = ExcelUtil(tc_name="").read_from_excel("Generic", 9, 4).strip()
        self.SL_350 = ExcelUtil(tc_name="").read_from_excel("Generic", 9, 5).strip()
        self.SL_250 = ExcelUtil(tc_name="").read_from_excel("Generic", 9, 6).strip()
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "N-4_$250" in subjectlineTxt:
            print(self.SL_250)
            print(subjectlineTxt)
            assert self.SL_250 in subjectlineTxt, "Subject Line Text Not Matching"
        elif "N-1_$700" in subjectlineTxt:
            print(self.SL_700)
            print(subjectlineTxt)
            assert self.SL_700 in subjectlineTxt, "Subject Line Text Not Matching"
        elif "N-2_$550" or "N10+" or "N10" or "S10+" or "S10" in subjectlineTxt:
            print(self.SL_550)
            print(subjectlineTxt)
            assert self.SL_550 in subjectlineTxt, "Subject Line Text Not Matching"
        elif "N-3_$350" or "S9+" in subjectlineTxt:
            print(self.SL_350)
            print(subjectlineTxt)
            assert self.SL_350 in subjectlineTxt, "Subject Line Text Not Matching"
        else:
            assert self.SL_700 in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Validated Subject Line Text:: " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH_1 = ExcelUtil(tc_name="").read_from_excel("Generic", 10, 25).strip()
        self.PH_2 = ExcelUtil(tc_name="").read_from_excel("Generic", 10, 3).strip()
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        # pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text.encode('utf-8')
        if "Non" in subjectlineTxt:
            assert self.PH_1 in pheaderTxt, "pre_header Text Not Matching"
        else:
            assert self.PH_2 in pheaderTxt, "pre_header Text Not Matching"
        logger.info(": Validated Pre-Header Text:: " + pheaderTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_link_validation(self):
        logger.info(": ##### Started pre_header_link_validation verification #####")
        self.PH_URL_generic = ExcelUtil(tc_name="").read_from_excel("Generic1", 6, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@target='_blank'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        # print("From Excel :"+self.PH_URL_generic)
        # print("From Web :"+URL)
        # assert self.PH_URL_generic in URL, "Web Landing Page URL is not Matching."



        # logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        # with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        # URLSegemntPage.get_segment()
        # CC_CreativePage.get_pre_order_title_price_validation(self)
        # CC_CreativePage.get_Hero_DeviceName_validation(self)
        # URLSegemntPage.get_tradeinDevice_validation()
        # CC_CreativePage.verify_tradein_price_validation(self)
        # CC_CreativePage.get_carrier_instant_credit_validation(self)
        # CC_CreativePage.get_Hero_Pre_OrderNow_validation(self)
        # self.driver.close()
        # self.driver.switch_to.window(parent_window)


        # logger.info(': #####  Verification Complete  #####\n')

        select_box=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='price'])[6]"))).text
        tradein = select_box[:12]
        print(tradein)





    def get_Top_Hero_link_validation(self):
        logger.info(": ##### Started Hero link_validation verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("Generic1", 6, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='Module1']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url_path in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        CC_CreativePage.get_pre_order_title_price_validation(self)
        CC_CreativePage.get_Hero_DeviceName_validation(self)
        URLSegemntPage.get_tradeinDevice_validation()
        CC_CreativePage.verify_tradein_price_validation(self)
        CC_CreativePage.get_carrier_instant_credit_validation(self)
        CC_CreativePage.get_Hero_Pre_OrderNow_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        # logger.info(': #####  Verification Complete  #####\n')

    # def get_Module1_SubCopyText(self):
    #     logger.info(": ##### Started Module_1 SubCopy_text verification #####")
    #     subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
    #     SubCopy = self.driver.find_element_by_xpath("(//*[@_label='Hero_Text'])[2]").text
    #     self.SC = ExcelUtil(tc_name="").read_from_excel("Generic", 6, 6).strip()
    #     assert self.SC in SubCopy, "SubCopy Text Not Matching"
    #     logger.info(": Validated Module_1 Subcopy Text:: " + self.SC)
    #     logger.info(': #####  Verification Complete  #####\n')
    #
    # def get_Module1_SubCopyText2(self):
    #     logger.info(": ##### Started Module_1 SubCopy_text2 verification #####")
    #     subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
    #     SubCopy = self.driver.find_element_by_xpath("(//span)[41]").text
    #     self.SC = ExcelUtil(tc_name="").read_from_excel("Generic", 6, 5).strip()
    #     assert self.SC in SubCopy, "SubCopy Text Not Matching"
    #     logger.info(": Validated Module_1 Subcopy Text2:: " + self.SC)
    #     logger.info(': #####  Verification Complete  #####\n')
    #
    # def get_Module2_SubCopyText(self):
    #     logger.info(": ##### Started Module_2 SubCopy_text verification #####")
    #     subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
    #     SubCopy = self.driver.find_element_by_xpath("//*[@_label='Text']").text
    #     self.SC = ExcelUtil(tc_name="").read_from_excel("Generic", 7, 7).strip()
    #     assert self.SC in SubCopy, "SubCopy Text Not Matching"
    #     logger.info(": Validated Module_1 Subcopy Text:: " + self.SC)
    #     logger.info(': #####  Verification Complete  #####\n')
    #
    # def get_CC_a4_SubHead_text_validation(self):
    #     logger.info(": ##### Started Sub_Head text verification #####")
    #     self.SL = ExcelUtil(tc_name="").read_from_excel("Generic", 6, 7).strip()
    #     footerTxt1 = self.driver.find_element_by_xpath("(//*[@_label='Hero_Text'])[1]").text
    #     assert self.SL in footerTxt1, "SubHead Text Not Matching"
    #     logger.info(": Validate footer condition text:: " + footerTxt1)
    #     logger.info(': #####  Verification Complete  #####\n')
    #
    # def get_CC_Condition_text_validation(self):
    #     logger.info(": ##### Started footer condition text verification #####")
    #     self.SL = ExcelUtil(tc_name="").read_from_excel("Generic", 6, 10).strip()
    #     # footerTxt1 = self.driver.find_element_by_xpath("(//span)[104]").text.encode('utf-8')
    #     footerTxt1 = self.driver.find_element_by_xpath("(//span)[104]").text
    #     assert self.SL in footerTxt1, "Footer Condition Text Not Matching"
    #     logger.info(": Validate footer condition text:: " + footerTxt1)
    #     logger.info(': #####  Verification Complete  #####\n')
    #
    # def get_CC_a2_text_validation(self):
    #     logger.info(": ##### Started footer condition text verification #####")
    #     # self.SL = ExcelUtil(tc_name="").read_from_excel("Generic", 7, 8).strip()
    #     footerTxt2 = self.driver.find_element_by_xpath("(//span)[103]").text.encode('utf-8')
    #     # assert self.SL.encode('utf-8') in footerTxt2, "Subject Line Text Not Matching"
    #     logger.info(": Validate footer condition text:: " + str(footerTxt2))
    #     logger.info(': #####  Verification Complete  #####\n')
    #
    # def get_CC_a3_text_validation(self):
    #     logger.info(": ##### Started footer condition text verification #####")
    #     # self.SL = ExcelUtil(tc_name="").read_from_excel("Generic", 7, 8).strip()
    #     footerTxt3 = self.driver.find_element_by_xpath("(//span)[110]").text.encode('utf-8')
    #     # assert self.SL.encode('utf-8') in footerTxt3, "Subject Line Text Not Matching"
    #     logger.info(": Validate footer condition text:: " + str(footerTxt3))
    #     logger.info(': #####  Verification Complete  #####\n')
    #
    # def get_CC_a4_text_validation(self):
    #     logger.info(": ##### Started footer condition text verification #####")
    #     # self.SL = ExcelUtil(tc_name="").read_from_excel("Generic", 7, 8).strip()
    #     footerTxt4 = self.driver.find_element_by_xpath("(//span)[113]").text.encode('utf-8')
    #     # assert self.SL.encode('utf-8') in footerTxt4, "Subject Line Text Not Matching"
    #     logger.info(": Validate footer condition text:: " + str(footerTxt4))
    #     logger.info(': #####  Verification Complete  #####\n')
    #
    # def get_CC_m1_Conditiontext1_validation(self):
    #     logger.info(": ##### Started footer condition_text1 verification #####")
    #     self.SL = ExcelUtil(tc_name="").read_from_excel("Generic", 6, 9).strip()
    #     footerTxt1 = self.driver.find_element_by_xpath("(//span)[125]").text
    #     # print(self.SL)
    #     # print(footerTxt1)
    #     assert self.SL in footerTxt1, "Condition_Text1 Not Matching"
    #     logger.info(": Validate footer condition_text1:: " + str(footerTxt1))
    #     logger.info(': #####  Verification Complete  #####\n')
    #
    # def get_CC_m2_Conditiontext2_validation(self):
    #     logger.info(": ##### Started footer condition_text2 verification #####")
    #     self.SL = ExcelUtil(tc_name="").read_from_excel("Generic", 7, 9).strip()
    #     footerTxt2 = self.driver.find_element_by_xpath("(//span)[127]").text
    #     assert self.SL in footerTxt2, "Condition_Text2 Not Matching"
    #     logger.info(": Validate footer condition_text2:: " + str(footerTxt2))
    #     logger.info(': #####  Verification Complete  #####\n')
    #
    # def get_CC_m3_Conditiontext3_validation(self):
    #     logger.info(": ##### Started footer condition_text3 verification #####")
    #     self.SL = ExcelUtil(tc_name="").read_from_excel("Generic", 11, 9).strip()
    #     footerTxt2 = self.driver.find_element_by_xpath("(//span)[129]").text
    #     assert self.SL in footerTxt2, "Condition_Text3 Not Matching"
    #     logger.info(": Validate footer condition_text3:: " + str(footerTxt2))
    #     logger.info(': #####  Verification Complete  #####\n')
    #
    # def get_CC_m4_Conditiontext4_validation(self):
    #     logger.info(": ##### Started footer condition_text4 verification #####")
    #     self.SL = ExcelUtil(tc_name="").read_from_excel("Generic", 12, 9).strip()
    #     footerTxt2 = self.driver.find_element_by_xpath("(//span)[131]").text
    #     assert self.SL in footerTxt2, "Condition_Text4 Not Matching"
    #     logger.info(": Validate footer condition_text4:: " + str(footerTxt2))
    #     logger.info(': #####  Verification Complete  #####\n')
    #
    # def get_Module2_RemindME_link_verification(self):
    #     logger.info(": ##### Started Module2_RemindME_link_validation verification #####")
    #     self.url_path = ExcelUtil(tc_name="").read_from_excel("Generic", 7, 8)
    #     parent_window = self.driver.current_window_handle
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/fb40aeab9f353faea1a21c295d85f37e.jpg']"))).click()
    #     all_windows = self.driver.window_handles
    #     child_window = [window for window in all_windows if window != parent_window][0]
    #     self.driver.switch_to.window(child_window)
    #     URL = self.driver.current_url
    #     assert self.url_path in URL, "Web Landing Page URL is not Matching."
    #     logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
    #     with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
    #     URLSegemntPage.get_segment()
    #     URLSegemntPage.get_segment_validation()
    #     self.driver.close()
    #     self.driver.switch_to.window(parent_window)
    #     logger.info(': #####  Verification Complete  #####\n')

    def get_Module1_link_verification(self):
        logger.info(": ##### Started Module1 link_validation verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("Generic1", 9, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@_label='Hero_Text'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        # assert self.url_path in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        CC_CreativePage.get_pre_order_title_price_validation(self)
        CC_CreativePage.get_Hero_DeviceName_validation(self)
        URLSegemntPage.get_tradeinDevice_validation()
        CC_CreativePage.verify_tradein_price_validation(self)
        CC_CreativePage.get_carrier_instant_credit_validation(self)
        CC_CreativePage.get_Hero_Pre_OrderNow_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        # logger.info(': #####  Verification Complete  #####\n')

    def get_Module2_link_verification(self):
        logger.info(": ##### Started Module2 link_validation verification #####")
        time.sleep(5)
        self.url_path = ExcelUtil(tc_name="").read_from_excel("Generic1", 9, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@_label='Hero_Text'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        # assert self.url_path in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        CC_CreativePage.get_pre_order_title_price_validation(self)
        CC_CreativePage.get_Hero_DeviceName_validation(self)
        URLSegemntPage.get_tradeinDevice_validation()
        CC_CreativePage.verify_tradein_price_validation(self)
        CC_CreativePage.get_carrier_instant_credit_validation(self)
        CC_CreativePage.get_Hero_Pre_OrderNow_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        # logger.info(': #####  Verification Complete  #####\n')

    def get_Module3_link_verification(self):
        logger.info(": ##### Started Module3 link_validation verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("Generic1", 9, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@_label='Hero_Text'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        # assert self.url_path in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        CC_CreativePage.get_pre_order_title_price_validation(self)
        CC_CreativePage.get_Hero_DeviceName_validation(self)
        URLSegemntPage.get_tradeinDevice_validation()
        CC_CreativePage.verify_tradein_price_validation(self)
        CC_CreativePage.get_carrier_instant_credit_validation(self)
        CC_CreativePage.get_Hero_Pre_OrderNow_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        # logger.info(': #####  Verification Complete  #####\n')

    def get_Module4_link_verification(self):
        logger.info(": ##### Started Module4 ink_validation verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("Generic1", 9, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@_label='Hero_Text'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        # assert self.url_path in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        CC_CreativePage.get_pre_order_title_price_validation(self)
        CC_CreativePage.get_Hero_DeviceName_validation(self)
        URLSegemntPage.get_tradeinDevice_validation()
        CC_CreativePage.verify_tradein_price_validation(self)
        CC_CreativePage.get_carrier_instant_credit_validation(self)
        CC_CreativePage.get_Hero_Pre_OrderNow_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        # logger.info(': #####  Verification Complete  #####\n')

    def get_Module5_link_verification(self):
        logger.info(": ##### Started Module5 link_validation verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("Generic1", 9, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@_label='Hero_Text'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        # assert self.url_path in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        CC_CreativePage.get_pre_order_title_price_validation(self)
        CC_CreativePage.get_Hero_DeviceName_validation(self)
        URLSegemntPage.get_tradeinDevice_validation()
        CC_CreativePage.verify_tradein_price_validation(self)
        CC_CreativePage.get_carrier_instant_credit_validation(self)
        CC_CreativePage.get_Hero_Pre_OrderNow_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        # logger.info(': #####  Verification Complete  #####\n')

    def verify_tradein_price_validation(self):
        logger.info(": ##### Started Eligible Trade-in price validation verification #####")
        time.sleep(5)
        # tradein1=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='tradeinPrice'])[1]"))).text
        tradein1=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='price-info']/span/strong)[3]"))).text
        tradein = tradein1[:7]
        logger.info(': assertion Trade-in price with: ' + tradein)
        # logger.info(': #####  Verification Complete  #####\n')

    def get_pre_order_title_price_validation(self):
        logger.info(": ##### Started pre order title price verification #####")
        time.sleep(5)
        # tradein1=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='tradeinPrice'])[1]"))).text
        tradein=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='title'])[2]"))).text
        # tradein1 = tradein1[:7]
        logger.info(': assertion pre_order_title_ with: ' + tradein)
        # logger.info(': #####  Verification Complete  #####\n')

    def get_carrier_instant_credit_validation(self):
        logger.info(": ##### Started carrier instant credit verification #####")
        tradein=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='title' and @role='heading'])[3]"))).text
        # tradein1 = tradein1[:7]
        logger.info(': assertion Trade-in price with: ' + tradein)

    def get_Hero_carrier_validation(self):
        logger.info(": ##### Started carrier validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='Module1']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        # time.sleep(5)
        if "unlocked" in subjectlineTxt:
            unlocked_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[1]")))
            unlocked_WElement.is_displayed()
            assert unlocked_WElement.is_displayed(), "unlocked carrier Option not Selected."
            logger.info(": successfully verified carrier option : unlocked ")
        elif "att" in subjectlineTxt:
            att_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[3]")))
            att_WElement.is_displayed()
            assert att_WElement.is_displayed(), "AT&T carrier Option not Selected."
            logger.info(": successfully verified carrier option : AT&T  ")
        elif "verizon" in subjectlineTxt:
            verizon_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[2]")))
            verizon_WElement.is_displayed()
            assert verizon_WElement.is_displayed(), "verizon carrier Option not Selected."
            logger.info(": successfully verified carrier option :verizon")
        elif "tmobile" in subjectlineTxt:
            tmobile_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[4]")))
            tmobile_WElement.is_displayed()
            assert tmobile_WElement.is_displayed(), "tmobile carrier Option not Selected."
            logger.info(": successfully verified carrier option: Tmobile")
        # elif "Reserver_Generic" in subjectlineTxt:
        #     unlocked_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[1]")))
        #     unlocked_WElement.is_displayed()
        #     assert unlocked_WElement.is_displayed(), "unlocked carrier Option not Selected."
        #     logger.info(": successfully verifiedcarrier option : unlocked ")
        # elif "Reserver_Generic" in subjectlineTxt:
        #     unlocked_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[1]")))
        #     unlocked_WElement.is_displayed()
        #     assert unlocked_WElement.is_displayed(), "unlocked carrier Option not Selected."
        #     logger.info(": successfully verifiedcarrier option : unlocked ")
        # elif "Non-Reserves" in subjectlineTxt:
        #     unlocked_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[1]")))
        #     unlocked_WElement.is_displayed()
        #     assert unlocked_WElement.is_displayed(), "unlocked carrier Option not Selected."
        #     logger.info(": successfully verifiedcarrier option : unlocked ")
        # elif "EPP_Generic" in subjectlineTxt:
        #     unlocked_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[1]")))
        #     unlocked_WElement.is_displayed()
        #     assert unlocked_WElement.is_displayed(), "unlocked carrier Option not Selected."
        #     logger.info(": successfully verifiedcarrier option : unlocked ")
        else:
            logger.info(": successfully verified carrier option : unlocked ")
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_M1_carrier_validation(self):
        logger.info(": ##### Started Module1 carrier validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@_label='Hero_Text'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        if "unlocked" in subjectlineTxt:
            unlocked_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[1]")))
            unlocked_WElement.is_displayed()
            assert unlocked_WElement.is_displayed(), "unlocked carrier Option not Selected."
            logger.info(": successfully verifiedcarrier option : unlocked ")
        elif "att" in subjectlineTxt:
            att_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[3]")))
            att_WElement.is_displayed()
            assert att_WElement.is_displayed(), "AT&T carrier Option not Selected."
            logger.info(": successfully verifiedcarrier option : AT&T  ")
        elif "verizon" in subjectlineTxt:
            verizon_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[2]")))
            verizon_WElement.is_displayed()
            assert verizon_WElement.is_displayed(), "verizon carrier Option not Selected."
            logger.info(": successfully verified carrier option :verizon")
        elif "tmobile" in subjectlineTxt:
            tmobile_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[4]")))
            tmobile_WElement.is_displayed()
            assert tmobile_WElement.is_displayed(), "tmobile carrier Option not Selected."
            logger.info(": successfully verified carrier option: Tmobile")
        else:
            logger.info(': Carrier Option NOT present.')
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_M2_carrier_validation(self):
        logger.info(": ##### Started Module 2 carrier validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@_label='Hero_Text'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        if "unlocked" in subjectlineTxt:
            unlocked_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[1]")))
            unlocked_WElement.is_displayed()
            assert unlocked_WElement.is_displayed(), "unlocked carrier Option not Selected."
            logger.info(": successfully verifiedcarrier option : unlocked ")
        elif "att" in subjectlineTxt:
            att_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[3]")))
            att_WElement.is_displayed()
            assert att_WElement.is_displayed(), "AT&T carrier Option not Selected."
            logger.info(": successfully verifiedcarrier option : AT&T  ")
        elif "verizon" in subjectlineTxt:
            verizon_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[2]")))
            verizon_WElement.is_displayed()
            assert verizon_WElement.is_displayed(), "verizon carrier Option not Selected."
            logger.info(": successfully verified carrier option :verizon")
        elif "tmobile" in subjectlineTxt:
            tmobile_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[4]")))
            tmobile_WElement.is_displayed()
            assert tmobile_WElement.is_displayed(), "tmobile carrier Option not Selected."
            logger.info(": successfully verified carrier option: Tmobile")
        else:
            logger.info(': Carrier Option NOT present.')
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_M3_carrier_validation(self):
        logger.info(": ##### Started Module3 carrier validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@_label='Hero_Text'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        if "unlocked" in subjectlineTxt:
            unlocked_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[1]")))
            unlocked_WElement.is_displayed()
            assert unlocked_WElement.is_displayed(), "unlocked carrier Option not Selected."
            logger.info(": successfully verifiedcarrier option : unlocked ")
        elif "att" in subjectlineTxt:
            att_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[3]")))
            att_WElement.is_displayed()
            assert att_WElement.is_displayed(), "AT&T carrier Option not Selected."
            logger.info(": successfully verifiedcarrier option : AT&T  ")
        elif "verizon" in subjectlineTxt:
            verizon_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[2]")))
            verizon_WElement.is_displayed()
            assert verizon_WElement.is_displayed(), "verizon carrier Option not Selected."
            logger.info(": successfully verified carrier option :verizon")
        elif "tmobile" in subjectlineTxt:
            tmobile_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[4]")))
            tmobile_WElement.is_displayed()
            assert tmobile_WElement.is_displayed(), "tmobile carrier Option not Selected."
            logger.info(": successfully verified carrier option: Tmobile")
        else:
            logger.info(': Carrier Option NOT present.')
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_M4_carrier_validation(self):
        logger.info(": ##### Started Module4 carrier validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@_label='Hero_Text'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        if "unlocked" in subjectlineTxt:
            unlocked_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[1]")))
            unlocked_WElement.is_displayed()
            assert unlocked_WElement.is_displayed(), "unlocked carrier Option not Selected."
            logger.info(": successfully verifiedcarrier option : unlocked ")
        elif "att" in subjectlineTxt:
            att_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[3]")))
            att_WElement.is_displayed()
            assert att_WElement.is_displayed(), "AT&T carrier Option not Selected."
            logger.info(": successfully verifiedcarrier option : AT&T  ")
        elif "verizon" in subjectlineTxt:
            verizon_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[2]")))
            verizon_WElement.is_displayed()
            assert verizon_WElement.is_displayed(), "verizon carrier Option not Selected."
            logger.info(": successfully verified carrier option :verizon")
        elif "tmobile" in subjectlineTxt:
            tmobile_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[4]")))
            tmobile_WElement.is_displayed()
            assert tmobile_WElement.is_displayed(), "tmobile carrier Option not Selected."
            logger.info(": successfully verified carrier option: Tmobile")
        else:
            logger.info(': Carrier Option NOT present.')
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_M5_carrier_validation(self):
        logger.info(": ##### Started Module5 carrier validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@_label='Hero_Text'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        if "unlocked" in subjectlineTxt:
            unlocked_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[1]")))
            unlocked_WElement.is_displayed()
            assert unlocked_WElement.is_displayed(), "unlocked carrier Option not Selected."
            logger.info(": successfully verifiedcarrier option : unlocked ")
        elif "att" in subjectlineTxt:
            att_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[3]")))
            att_WElement.is_displayed()
            assert att_WElement.is_displayed(), "AT&T carrier Option not Selected."
            logger.info(": successfully verifiedcarrier option : AT&T  ")
        elif "verizon" in subjectlineTxt:
            verizon_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[2]")))
            verizon_WElement.is_displayed()
            assert verizon_WElement.is_displayed(), "verizon carrier Option not Selected."
            logger.info(": successfully verified carrier option :verizon")
        elif "tmobile" in subjectlineTxt:
            tmobile_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='item-img'])[4]")))
            tmobile_WElement.is_displayed()
            assert tmobile_WElement.is_displayed(), "tmobile carrier Option not Selected."
            logger.info(": successfully verified carrier option: Tmobile")
        else:
            logger.info(': Carrier Option NOT present.')
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Hero_DeviceName_validation(self):
        logger.info(": ##### Started Hero DeviceName validation  #####")
        device1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='oos-title2'])"))).text
        try:
            assert "Galaxy S21 5G" in device1, "Device Name Not Matching."
            logger.info(': Successfully matched Targeted Device Name:' + device1)
        except:
            assert "Galaxy S21 Ultra 5G" in device1, "Device Name Not Matching."
            logger.info(': Successfully matched Targeted Device Name:' + device1)
        # CC_CreativePage.get_Pre_OrderNow_validation(self)
        # self.driver.close()
        # self.driver.switch_to.window(parent_window)
        # logger.info(': #####  Verification Complete  #####\n')

    def get_Hero_Pre_OrderNow_validation(self):
        logger.info(": ##### Started  Pre Order Now validation  #####")
        # subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        # parent_window = self.driver.current_window_handle
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='Module1']"))).click()
        # all_windows = self.driver.window_handles
        # child_window = [window for window in all_windows if window != parent_window][0]
        # self.driver.switch_to.window(child_window)
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='button  PRE-ORDER NOW'])[1]"))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='confirmationBtnLeft'])[1]"))).click()
            preorderdevice=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='tile2 selected tradein-tile'])[1]"))).text
            logger.info(': Successfully matched pre order information :' + preorderdevice)
        except:
            logger.info(': Need to select Device Manually.')
        # self.driver.close()
        # self.driver.switch_to.window(parent_window)
        # logger.info(': #####  Verification Complete  #####\n')

    def get_M1_Pre_OrderNow_validation(self):
        logger.info(": ##### Started M1 Pre Order Now validation  #####")
        # subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@_label='Hero_Text'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='button  PRE-ORDER NOW'])[1]"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='confirmationBtnLeft'])[1]"))).click()
        preorderdevice=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='tile2 selected tradein-tile'])[1]"))).text
        logger.info(': Successfully matched pre order information :' + preorderdevice)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_M2_Pre_OrderNow_validation(self):
        logger.info(": ##### Started M2 Pre Order Now validation  #####")
        # subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1044']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='button  PRE-ORDER NOW'])[1]"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='confirmationBtnLeft'])[1]"))).click()
        preorderdevice=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='tile2 selected tradein-tile'])[1]"))).text
        logger.info(': Successfully matched pre order information :' + preorderdevice)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_M3_Pre_OrderNow_validation(self):
        logger.info(": ##### Started M3 Pre Order Now validation  #####")
        # subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1049']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='button  PRE-ORDER NOW'])[1]"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='confirmationBtnLeft'])[1]"))).click()
        preorderdevice=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='tile2 selected tradein-tile'])[1]"))).text
        logger.info(': Successfully matched pre order information :' + preorderdevice)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_M4_Pre_OrderNow_validation(self):
        logger.info(": ##### Started M4 Pre Order Now validation  #####")
        # subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1051']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='button  PRE-ORDER NOW'])[1]"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='confirmationBtnLeft'])[1]"))).click()
        preorderdevice=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='tile2 selected tradein-tile'])[1]"))).text
        logger.info(': Successfully matched pre order information :' + preorderdevice)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_M5_Pre_OrderNow_validation(self):
        logger.info(": ##### Started M5 Pre Order Now validation  #####")
        # subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_x0000_i1059']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='button  PRE-ORDER NOW'])[1]"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='confirmationBtnLeft'])[1]"))).click()
        preorderdevice=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='tile2 selected tradein-tile'])[1]"))).text
        logger.info(': Successfully matched pre order information :' + preorderdevice)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')


    def get_M1_DeviceName_validation(self):
        logger.info(": ##### Started Module1 DeviceName validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@_label='Hero_Text'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        device1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='oos-title2'])"))).text
        # device2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='name'])[1]"))).text
        # if "947de220-7ad3-455c-a8fd-dae88cefe0b8" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 10 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "82ac4f16-9db5-4660-8178-6300d0bb3ac3" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 10" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "420693fa-aa43-4c2a-b2ea-1544e33f5a22" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S20 Ultra" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "7ac0c3df-e6eb-435a-8489-23f4644fe880" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S20 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "Galaxy_Note20_5G_Ultra" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note205G Ultra" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "c5560643-90f8-411e-a620-b32d2b2a6252" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S10 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "52f4db23-29ba-4b5c-897f-fd5c7c2cc226" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S10" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "21d2ee82-2f3b-45e6-b7ab-2d82a13c9d64" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S10e" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "a611576d-a872-4965-bda9-109acd864a75" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S8" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "eb7347a7-5441-4331-86aa-5493feabbdca" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 8" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "2e15b32a-6706-4193-ad1b-bc8ec2c0441c" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S9" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "777bb915-f317-43ef-bd9d-1ad902463a18" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S9 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # # elif "2e15b32a-6706-4193-ad1b-bc8ec2c0441c" in subjectlineTxt:
        # #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        # #     assert "Galaxy S9" in devicename_WElement, "Device Name Not Matching."
        # #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "d1f1e943-3a9f-402a-97e3-ee67f956faab" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 9" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "8275de7b-e61a-4769-8cee-6665875a9573" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note205G Ultra" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "2e15b32a-6706-4193-ad1b-bc8ec2c0441c" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S9" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "dbf9d8e5-abb5-4da9-bb67-1641b7927ab4" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Pixel 3a XL" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "1d21fcf8-d5c0-41a0-b455-6738f78cac9d" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Pixel 3 XL" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # else:
        #     logger.info(': Device Name NOT present in Box.')
        try:
            assert "Galaxy S21 5G" in device1, "Device Name Not Matching."
            logger.info(': Successfully matched Device Name:' + device1)
        except:
            assert "Galaxy S21 Ultra 5G" in device1, "Device Name Not Matching."
            logger.info(': Successfully matched Device Name:' + device1)
        # CC_CreativePage.get_Pre_OrderNow_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_M2_DeviceName_validation(self):
        logger.info(": ##### Started Module 2 DeviceName validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@_label='Hero_Text'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        device1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='oos-title2'])"))).text
        # device2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='name'])[1]"))).text
        # if "947de220-7ad3-455c-a8fd-dae88cefe0b8" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 10 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "82ac4f16-9db5-4660-8178-6300d0bb3ac3" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 10" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "420693fa-aa43-4c2a-b2ea-1544e33f5a22" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S20 Ultra" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "7ac0c3df-e6eb-435a-8489-23f4644fe880" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S20 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "Galaxy_Note20_5G_Ultra" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note205G Ultra" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "c5560643-90f8-411e-a620-b32d2b2a6252" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S10 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "52f4db23-29ba-4b5c-897f-fd5c7c2cc226" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S10" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "21d2ee82-2f3b-45e6-b7ab-2d82a13c9d64" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S10e" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "a611576d-a872-4965-bda9-109acd864a75" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S8" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "eb7347a7-5441-4331-86aa-5493feabbdca" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 8" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "2e15b32a-6706-4193-ad1b-bc8ec2c0441c" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S9" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "777bb915-f317-43ef-bd9d-1ad902463a18" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S9 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # # elif "2e15b32a-6706-4193-ad1b-bc8ec2c0441c" in subjectlineTxt:
        # #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        # #     assert "Galaxy S9" in devicename_WElement, "Device Name Not Matching."
        # #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "d1f1e943-3a9f-402a-97e3-ee67f956faab" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 9" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "8275de7b-e61a-4769-8cee-6665875a9573" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note205G Ultra" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "2e15b32a-6706-4193-ad1b-bc8ec2c0441c" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S9" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "dbf9d8e5-abb5-4da9-bb67-1641b7927ab4" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Pixel 3a XL" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "1d21fcf8-d5c0-41a0-b455-6738f78cac9d" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Pixel 3 XL" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # else:
        #     logger.info(': Device Name NOT present in Box.')
        try:
            assert "Galaxy S21 5G" in device1, "Device Name Not Matching."
            logger.info(': Successfully matched Device Name:' + device1)
        except:
            assert "Galaxy S21 Ultra 5G" in device1, "Device Name Not Matching."
            logger.info(': Successfully matched Device Name:' + device1)
        # CC_CreativePage.get_Pre_OrderNow_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_M3_DeviceName_validation(self):
        logger.info(": ##### Started Module3 DeviceName validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@_label='Hero_Text'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        device1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='oos-title2'])"))).text
        # device2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='name'])[1]"))).text
        # if "947de220-7ad3-455c-a8fd-dae88cefe0b8" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 10 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "82ac4f16-9db5-4660-8178-6300d0bb3ac3" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 10" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "420693fa-aa43-4c2a-b2ea-1544e33f5a22" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S20 Ultra" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "7ac0c3df-e6eb-435a-8489-23f4644fe880" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S20 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "Galaxy_Note20_5G_Ultra" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note205G Ultra" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "c5560643-90f8-411e-a620-b32d2b2a6252" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S10 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "52f4db23-29ba-4b5c-897f-fd5c7c2cc226" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S10" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "21d2ee82-2f3b-45e6-b7ab-2d82a13c9d64" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S10e" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "a611576d-a872-4965-bda9-109acd864a75" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S8" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "eb7347a7-5441-4331-86aa-5493feabbdca" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 8" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "2e15b32a-6706-4193-ad1b-bc8ec2c0441c" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S9" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "777bb915-f317-43ef-bd9d-1ad902463a18" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S9 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # # elif "2e15b32a-6706-4193-ad1b-bc8ec2c0441c" in subjectlineTxt:
        # #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        # #     assert "Galaxy S9" in devicename_WElement, "Device Name Not Matching."
        # #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "d1f1e943-3a9f-402a-97e3-ee67f956faab" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 9" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "8275de7b-e61a-4769-8cee-6665875a9573" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note205G Ultra" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "2e15b32a-6706-4193-ad1b-bc8ec2c0441c" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S9" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "dbf9d8e5-abb5-4da9-bb67-1641b7927ab4" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Pixel 3a XL" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "1d21fcf8-d5c0-41a0-b455-6738f78cac9d" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Pixel 3 XL" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # else:
        #     logger.info(': Device Name NOT present in Box.')
        try:
            assert "Galaxy S21 5G" in device1, "Device Name Not Matching."
            logger.info(': Successfully matched Device Name:' + device1)
        except:
            assert "Galaxy S21 Ultra 5G" in device1, "Device Name Not Matching."
            logger.info(': Successfully matched Device Name:' + device1)
        # CC_CreativePage.get_Pre_OrderNow_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_M4_DeviceName_validation(self):
        logger.info(": ##### Started Module4 DeviceName validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@_label='Hero_Text'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        device1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='oos-title2'])"))).text
        # device2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='name'])[1]"))).text
        # if "947de220-7ad3-455c-a8fd-dae88cefe0b8" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 10 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "82ac4f16-9db5-4660-8178-6300d0bb3ac3" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 10" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "420693fa-aa43-4c2a-b2ea-1544e33f5a22" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S20 Ultra" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "7ac0c3df-e6eb-435a-8489-23f4644fe880" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S20 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "Galaxy_Note20_5G_Ultra" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note205G Ultra" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "c5560643-90f8-411e-a620-b32d2b2a6252" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S10 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "52f4db23-29ba-4b5c-897f-fd5c7c2cc226" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S10" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "21d2ee82-2f3b-45e6-b7ab-2d82a13c9d64" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S10e" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "a611576d-a872-4965-bda9-109acd864a75" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S8" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "eb7347a7-5441-4331-86aa-5493feabbdca" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 8" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "2e15b32a-6706-4193-ad1b-bc8ec2c0441c" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S9" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "777bb915-f317-43ef-bd9d-1ad902463a18" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S9 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # # elif "2e15b32a-6706-4193-ad1b-bc8ec2c0441c" in subjectlineTxt:
        # #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        # #     assert "Galaxy S9" in devicename_WElement, "Device Name Not Matching."
        # #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "d1f1e943-3a9f-402a-97e3-ee67f956faab" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 9" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "8275de7b-e61a-4769-8cee-6665875a9573" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note205G Ultra" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "2e15b32a-6706-4193-ad1b-bc8ec2c0441c" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S9" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "dbf9d8e5-abb5-4da9-bb67-1641b7927ab4" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Pixel 3a XL" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "1d21fcf8-d5c0-41a0-b455-6738f78cac9d" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Pixel 3 XL" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # else:
        #     logger.info(': Device Name NOT present in Box.')
        try:
            assert "Galaxy S21 5G" in device1, "Device Name Not Matching."
            logger.info(': Successfully matched Device Name:' + device1)
        except:
            assert "Galaxy S21 Ultra 5G" in device1, "Device Name Not Matching."
            logger.info(': Successfully matched Device Name:' + device1)
        # CC_CreativePage.get_Pre_OrderNow_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_M5_DeviceName_validation(self):
        logger.info(": ##### Started Module5 DeviceName validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@_label='Hero_Text'])[2]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        device1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='oos-title2'])"))).text
        # device2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='name'])[1]"))).text
        # if "947de220-7ad3-455c-a8fd-dae88cefe0b8" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 10 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "82ac4f16-9db5-4660-8178-6300d0bb3ac3" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 10" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "420693fa-aa43-4c2a-b2ea-1544e33f5a22" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S20 Ultra" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "7ac0c3df-e6eb-435a-8489-23f4644fe880" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S20 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "Galaxy_Note20_5G_Ultra" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note205G Ultra" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "c5560643-90f8-411e-a620-b32d2b2a6252" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S10 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "52f4db23-29ba-4b5c-897f-fd5c7c2cc226" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S10" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "21d2ee82-2f3b-45e6-b7ab-2d82a13c9d64" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S10e" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "a611576d-a872-4965-bda9-109acd864a75" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S8" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "eb7347a7-5441-4331-86aa-5493feabbdca" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 8" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "2e15b32a-6706-4193-ad1b-bc8ec2c0441c" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S9" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "777bb915-f317-43ef-bd9d-1ad902463a18" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S9 Plus" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # # elif "2e15b32a-6706-4193-ad1b-bc8ec2c0441c" in subjectlineTxt:
        # #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        # #     assert "Galaxy S9" in devicename_WElement, "Device Name Not Matching."
        # #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "d1f1e943-3a9f-402a-97e3-ee67f956faab" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note 9" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        #
        # elif "8275de7b-e61a-4769-8cee-6665875a9573" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy Note205G Ultra" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "2e15b32a-6706-4193-ad1b-bc8ec2c0441c" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Galaxy S9" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "dbf9d8e5-abb5-4da9-bb67-1641b7927ab4" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Pixel 3a XL" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # elif "1d21fcf8-d5c0-41a0-b455-6738f78cac9d" in subjectlineTxt:
        #     devicename_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
        #     assert "Pixel 3 XL" in devicename_WElement, "Device Name Not Matching."
        #     logger.info(': assertion Device Name with: ' + devicename_WElement)
        # else:
        #     logger.info(': Device Name NOT present in Box.')
        try:
            assert "Galaxy S21 5G" in device1, "Device Name Not Matching."
            logger.info(': Successfully matched Device Name:' + device1)
        except:
            assert "Galaxy S21 Ultra 5G" in device1, "Device Name Not Matching."
            logger.info(': Successfully matched Device Name:' + device1)
        # CC_CreativePage.get_Pre_OrderNow_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_CC_m1_Conditiontext1_validation(self):
        logger.info(": ##### Started footer condition_text1 verification #####")
        self.SL = ExcelUtil(tc_name="").read_from_excel("Generic1", 6, 9).strip()
        footerTxt1 = self.driver.find_element_by_xpath("(//span)[165]").text
        # assert self.SL in footerTxt1, "Condition_Text1 Not Matching"
        logger.info(": Validate footer condition_text1:: " + str(footerTxt1))
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_m2_Conditiontext2_validation(self):
        logger.info(": ##### Started footer condition_text2 verification #####")
        self.SL = ExcelUtil(tc_name="").read_from_excel("Generic1", 7, 9).strip()
        footerTxt2 = self.driver.find_element_by_xpath("(//span)[168]").text
        # print(self.SL)
        # assert self.SL in footerTxt2, "Condition_Text2 Not Matching"
        # logger.info(": Validate footer condition_text2:: " + str(footerTxt2))
        logger.info(": Validate footer condition_text2:: " + self.SL)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_m3_Conditiontext3_validation(self):
        logger.info(": ##### Started footer condition_text3 verification #####")
        self.SL = ExcelUtil(tc_name="").read_from_excel("Generic1", 8, 9).strip()
        footerTxt2 = self.driver.find_element_by_xpath("(//span)[170]").text
        # print(self.SL)
        # assert self.SL in footerTxt2, "Condition_Text3 Not Matching"
        logger.info(": Validate footer condition_text3:: " + self.SL)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_m4_Conditiontext4_validation(self):
        logger.info(": ##### Started footer condition_text4 verification #####")
        self.SL = ExcelUtil(tc_name="").read_from_excel("Generic1", 13, 9).strip()
        footerTxt2 = self.driver.find_element_by_xpath("(//span)[172]").text
        # print(self.SL)
        # print(self.SL)
        # assert self.SL in footerTxt2, "Condition_Text4 Not Matching"
        logger.info(": Validate footer condition_text4:: " + self.SL)
        logger.info(': #####  Verification Complete  #####\n')














