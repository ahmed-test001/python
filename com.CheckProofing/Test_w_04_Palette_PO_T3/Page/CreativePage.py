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

    def get_DeviceOption_verification(self):
        logger.info(": ##### Started Device Option verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "N-1" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c39d932b959f69d8e9ab7c5ca9f220b6.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), " N-1 Web Element not Displayed."
            logger.info(": successfully verified [N-1] Device Option is present.")
        elif "N-2" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/521d4058606a427d275404ac7f98a60d.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), " N-2 Web Element not Displayed."
            logger.info(": successfully verified [N-2] Device Option is present.")
        elif "N-3" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c8366baeb008af8739608f52ee6769d7.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), " N-3 Web Element not Displayed."
            logger.info(": successfully verified [N-3] Device Option is present.")
        elif "N-4" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/65c9f0e3caa299f87bb0e59719f2d550.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), " N-4 Web Element not Displayed."
            logger.info(": successfully verified [N-4] Device Option is present.")
        elif "S10+" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/f0b9990cd504c058451ce8d69fd9f3e9.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), " S10+ Web Element not Displayed."
            logger.info(": successfully verified [S10+] Device Option is present.")
        elif "S10" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/112d83f87be0045636e79abe5c64a474.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), " S10 Web Element not Displayed."
            logger.info(": successfully verified [S10] Device Option is present.")
        elif "S9+" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/32e5b02ffd6e40d894e618d9e1f5da66.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), " S9+ Web Element not Displayed."
            logger.info(": successfully verified [S9+] Device Option is present.")
        elif "N10+" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/f9838f5312b658668b6a57f968754679.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), " N10+ Web Element not Displayed."
            logger.info(": successfully verified [N10+] Device Option is present.")
        elif "S20+" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/2888f545a3228dce17f7627848f1d133.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), " s20+ Web Element not Displayed."
            logger.info(": successfully verified [S20+] Device Option is present.")
        elif "S20" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/723b4f20683e21a28592dcb1cbb168b7.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), " S20 Web Element not Displayed."
            logger.info(": successfully verified [S20] Device Option is present.")
        elif "LO" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/5e34fe7b89fe4e557f4788a42e4c6d1f.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), " LO Web Element not Displayed."
            logger.info(": successfully verified [LO] Device Option is present.")
        elif "Reserver_Generic" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/5e34fe7b89fe4e557f4788a42e4c6d1f.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), " Reserver_Generic Web Element not Displayed."
            logger.info(": successfully verified [Reserver_Generic] Device Option is present.")
        elif "Non-Reserves" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/5e34fe7b89fe4e557f4788a42e4c6d1f.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), " Reserver_Generic Web Element not Displayed."
            logger.info(": successfully verified [Reserver_Generic] Device Option is present.")
        else:
            logger.info(': Device Option NOT selected.')
        logger.info(': #####  Verification Complete  #####\n')

    def get_EPP_or_NonEPP_verification(self):
        logger.info(": ##### Started EPP version verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/7feb8ddbd30649ff0ed9e1771052d5d6.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), "Web Element not Displayed."
            logger.info(": successfully verified EPP version is present.")
        else:
            logger.info(': successfully verified EPP version NOT present.')
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_subjectLine_text_validation(self):
        logger.info(": ##### Started subjectLine_text verification #####")
        self.SL = ExcelUtil(tc_name="").read_from_excel("Generic", 10, 3).strip()
        self.SL_2 = ExcelUtil(tc_name="").read_from_excel("Generic", 10, 25).strip()
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "Non" in subjectlineTxt:
            assert self.SL_2 in subjectlineTxt, "Subject Line Text Not Matching"
        else:
            assert self.SL in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Validated Subject Line Text:: " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.SL_700 = ExcelUtil(tc_name="").read_from_excel("Generic", 11, 3).strip()
        self.SL_550 = ExcelUtil(tc_name="").read_from_excel("Generic", 11, 4).strip()
        self.SL_350 = ExcelUtil(tc_name="").read_from_excel("Generic", 11, 5).strip()
        self.SL_250 = ExcelUtil(tc_name="").read_from_excel("Generic", 11, 6).strip()
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        if "250_T1" in subjectlineTxt:
            # print(self.SL_250)
            # print(subjectlineTxt)
            assert self.SL_250 in pheaderTxt, "pheader Text Not Matching"
        elif "350_TI" in subjectlineTxt:
            # print(self.SL_350)
            # print(subjectlineTxt)
            assert self.SL_350 in pheaderTxt, "pheader Text Not Matching"
        elif "700_TI" in subjectlineTxt:
            # print(self.SL_700)
            # print(subjectlineTxt)
            assert self.SL_700 in pheaderTxt, "pheader Text Not Matching"
        elif "550_TI" in subjectlineTxt:
            # print(self.SL_550)
            # print(subjectlineTxt)
            assert self.SL_550 in pheaderTxt, "pheader Text Not Matching"
        elif "N10+" in subjectlineTxt:
            # print(self.SL_250)
            # print(subjectlineTxt)
            assert self.SL_250 in pheaderTxt, "pheader Text Not Matching"
        elif "N10" in subjectlineTxt:
            # print(self.SL_550)
            # print(subjectlineTxt)
            assert self.SL_550 in pheaderTxt, "pheader Text Not Matching"
        elif "S10+" in subjectlineTxt:
            # print(self.SL_550)
            # print(subjectlineTxt)
            assert self.SL_550 in pheaderTxt, "pheader Text Not Matching"
        elif "S20+" in subjectlineTxt:
            # print(self.SL_700)
            # print(subjectlineTxt)
            assert self.SL_700 in pheaderTxt, "pheader Text Not Matching"
        elif "S20" in subjectlineTxt:
            # print(self.SL_700)
            # print(subjectlineTxt)
            assert self.SL_700 in pheaderTxt, "pheader Text Not Matching"
        elif "S10" in subjectlineTxt:
            # print(self.SL_550)
            # print(subjectlineTxt)
            assert self.SL_550 in pheaderTxt, "pheader Text Not Matching"
        elif "N-3_$350" in subjectlineTxt:
            # print(self.SL_350)
            # print(subjectlineTxt)
            assert self.SL_350 in pheaderTxt, "pheader Text Not Matching"
        elif "S9+" in subjectlineTxt:
            # print(self.SL_250)
            # print(subjectlineTxt)
            assert self.SL_250 in pheaderTxt, "pheader Text Not Matching"
        elif "LO" in subjectlineTxt:
            # print(self.SL_250)
            # print(subjectlineTxt)
            assert self.SL_700 in pheaderTxt, "pheader Text Not Matching"
        elif "Reserver_Generic" in subjectlineTxt:
            # print(self.SL_700)
            # print(subjectlineTxt)
            assert self.SL_700 in pheaderTxt, "pheader Text Not Matching"
        elif "EPP_Enrollees_Non_Res" in subjectlineTxt:
            # print(self.SL_700)
            # print(subjectlineTxt)
            assert self.SL_700 in pheaderTxt, "pheader Text Not Matching"
        else:
            assert self.SL_700 in pheaderTxt, "pheader Text Not Matching"
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
        assert self.PH_URL_generic in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        CC_CreativePage.get_pre_order_title_price_validation(self)
        URLSegemntPage.get_skipCarrier_validation()
        CC_CreativePage.get_DeviceName_validation(self)
        URLSegemntPage.get_tradeinDevice_validation()
        CC_CreativePage.verify_tradein_price_validation(self)
        # CC_CreativePage.get_carrier_instant_credit_validation(self)
        CC_CreativePage.get_Hero_Pre_OrderNow_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        # logger.info(': #####  Verification Complete  #####\n')

        # select_box=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='price'])[6]"))).text
        # tradein = select_box[:12]
        # print(tradein)

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
        URLSegemntPage.get_skipCarrier_validation()
        CC_CreativePage.get_DeviceName_validation(self)
        URLSegemntPage.get_tradeinDevice_validation()
        CC_CreativePage.verify_tradein_price_validation(self)
        # CC_CreativePage.get_carrier_instant_credit_validation(self)
        CC_CreativePage.get_Hero_Pre_OrderNow_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        # logger.info(': #####  Verification Complete  #####\n')

    def get_Module1_link_verification(self):
        logger.info(": ##### Started Module1 link_validation verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("Generic1", 9, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/9d391411ba22f6410af21c785010a092.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url_path in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        CC_CreativePage.get_pre_order_title_price_validation(self)
        URLSegemntPage.get_skipCarrier_validation()
        CC_CreativePage.get_DeviceName_validation(self)
        URLSegemntPage.get_tradeinDevice_validation()
        CC_CreativePage.verify_tradein_price_validation(self)
        # CC_CreativePage.get_carrier_instant_credit_validation(self)
        CC_CreativePage.get_Hero_Pre_OrderNow_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        # logger.info(': #####  Verification Complete  #####\n')

    def get_Module2_link_verification(self):
        logger.info(": ##### Started Module2 link_validation verification #####")
        time.sleep(5)
        self.url_path = ExcelUtil(tc_name="").read_from_excel("Generic1", 9, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/9d63d803d6dfe193226cd822867c0ffc.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url_path in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        CC_CreativePage.get_pre_order_title_price_validation(self)
        URLSegemntPage.get_skipCarrier_validation()
        CC_CreativePage.get_DeviceName_validation(self)
        URLSegemntPage.get_tradeinDevice_validation()
        CC_CreativePage.verify_tradein_price_validation(self)
        # CC_CreativePage.get_carrier_instant_credit_validation(self)
        CC_CreativePage.get_Hero_Pre_OrderNow_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        # logger.info(': #####  Verification Complete  #####\n')

    def get_Module3_link_verification(self):
        logger.info(": ##### Started Module3 link_validation verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("Generic1", 9, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/ba6fe6a990065d4582738866711835e6.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.url_path in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        CC_CreativePage.get_pre_order_title_price_validation(self)
        URLSegemntPage.get_skipCarrier_validation()
        CC_CreativePage.get_DeviceName_validation(self)
        URLSegemntPage.get_tradeinDevice_validation()
        CC_CreativePage.verify_tradein_price_validation(self)
        # CC_CreativePage.get_carrier_instant_credit_validation(self)
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
        CC_CreativePage.get_DeviceName_validation(self)
        URLSegemntPage.get_tradeinDevice_validation()
        CC_CreativePage.verify_tradein_price_validation(self)
        # CC_CreativePage.get_carrier_instant_credit_validation(self)
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
        CC_CreativePage.get_DeviceName_validation(self)
        URLSegemntPage.get_tradeinDevice_validation()
        CC_CreativePage.verify_tradein_price_validation(self)
        # CC_CreativePage.get_carrier_instant_credit_validation(self)
        CC_CreativePage.get_Hero_Pre_OrderNow_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        # logger.info(': #####  Verification Complete  #####\n')

    def verify_tradein_price_validation(self):
        logger.info(": ##### Started Eligible Trade-in price validation verification #####")
        # time.sleep(5)
        # tradein1=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='tradeinPrice'])[1]"))).text
        try:
            tradein1=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='price-info']/span/strong)[3]"))).text
            tradein = tradein1[:7]
            logger.info(': assertion Trade-in price with: ' + tradein)
        except:
            logger.info(': assertion Trade-in price with: N/A-NON_RESERVE')
        # logger.info(': #####  Verification Complete  #####\n')

    def get_pre_order_title_price_validation(self):
        logger.info(": ##### Started pre order title price verification #####")
        time.sleep(5)
        abc="Pre-order the next Galaxy to get up to $250 instant credit for watches, earbuds, tablets and more. Includes your reservation credit."
        abc2="Pre-order the next Galaxy to get up to $200 instant credit for watches, earbuds, tablets and more."
        # tradein1=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class ='tradeinPrice'])[1]"))).text
        tradein=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='title'])[2]"))).text
        # tradein1 = tradein1[:7]
        # logger.info(': assertion pre_order_title_ with: ' + abc)
        # print(abc)
        # print(tradein)
        try:
            assert abc in tradein, "pre order title price NOT Matching."
            logger.info(': assertion pre_order_title_ with: ' + abc)
        except:
            assert abc2 in tradein, "pre order title price NOT Matching."
            logger.info(': assertion pre_order_title_ with: ' + abc2)
        # logger.info(': #####  Verification Complete  #####\n')

    def get_carrier_instant_credit_validation(self):
        logger.info(": ##### Started carrier instant credit verification #####")
        try:
            tradein=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='title' and @role='heading'])[3]"))).text
            # tradein1 = tradein1[:7]
            logger.info(': assertion Trade-in price with: ' + tradein)
        except:
            logger.info(': assertion Trade-in price with: N/A-NON_RESERVE')

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

    def get_DeviceName_validation(self):
        logger.info(": ##### Started DeviceName validation  #####")
        device1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='oos-title2'])"))).text
        try:
            assert "Galaxy S21 5G" in device1, "Device Name Not Matching."
            logger.info(': Successfully matched Targeted Device Name:' + device1)
        except:
            assert "Galaxy S21 Ultra 5G" in device1, "Device Name Not Matching."
            logger.info(': Successfully matched Targeted Device Name:' + device1)

    def get_Hero_Pre_OrderNow_validation(self):
        logger.info(": ##### Started  Pre Order Now validation  #####")
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
        # self.SL = ExcelUtil(tc_name="").read_from_excel("Generic1", 6, 9).strip()
        footerTxt1 = self.driver.find_element_by_xpath("(//span)[182]").text
        # assert self.SL in footerTxt1, "Condition_Text1 Not Matching"
        logger.info(": Validate footer condition_text1:: " + footerTxt1)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_m2_Conditiontext2_validation(self):
        logger.info(": ##### Started footer condition_text2 verification #####")
        # self.SL = ExcelUtil(tc_name="").read_from_excel("Generic1", 7, 9).strip()
        footerTxt2 = self.driver.find_element_by_xpath("(//span)[184]").text
        # print(self.SL)
        # assert self.SL in footerTxt2, "Condition_Text2 Not Matching"
        # logger.info(": Validate footer condition_text2:: " + str(footerTxt2))
        logger.info(": Validate footer condition_text2:: " + footerTxt2)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_m3_Conditiontext3_validation(self):
        logger.info(": ##### Started footer condition_text3 verification #####")
        self.SL = ExcelUtil(tc_name="").read_from_excel("Generic1", 8, 9).strip()
        footerTxt2 = self.driver.find_element_by_xpath("(//span)[222]").text
        # print(self.SL)
        # assert self.SL in footerTxt2, "Condition_Text3 Not Matching"
        logger.info(": Validate footer condition_text3:: " + footerTxt2)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_m4_Conditiontext4_validation(self):
        logger.info(": ##### Started footer condition_text4 verification #####")
        # self.SL = ExcelUtil(tc_name="").read_from_excel("Generic1", 13, 9).strip()
        footerTxt2 = self.driver.find_element_by_xpath("(//span)[224]").text
        # print(self.SL)
        # print(self.SL)
        # assert self.SL in footerTxt2, "Condition_Text4 Not Matching"
        logger.info(": Validate footer condition_text4:: " + footerTxt2)
        logger.info(': #####  Verification Complete  #####\n')














