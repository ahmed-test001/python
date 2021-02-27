import json
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


class CreativePage(BasePage):

    def get_Hero_Text_verification(self):
        logger.info(": ##### Started Hero SH Text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        Hero_text = self.driver.find_element_by_xpath("//*[@id='kdp_hl']").get_attribute("alt")
        self.kdp_sc1 = ExcelUtil(tc_name="").read_from_excel("Copy", 15, 7).strip()
        self.kdp_sc2 = ExcelUtil(tc_name="").read_from_excel("Copy", 15, 5).strip()
        self.kdp_sc3 = ExcelUtil(tc_name="").read_from_excel("Copy", 15, 6).strip()
        Hero_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='kdp_sc']"))).text
        if "V1" in subjectlineTxt:
            assert Hero_WE in self.kdp_sc1, "Hero SC Text not Matched."
        elif "V2" in subjectlineTxt:
            assert Hero_WE in self.kdp_sc2, "Hero SC Text not Matched."
        elif "V3" in subjectlineTxt:
            assert Hero_WE in self.kdp_sc3, "Hero SC Text not Matched."
        elif "V4" in subjectlineTxt:
            assert Hero_WE in self.kdp_sc1, "Hero SC Text not Matched."
        elif "V5" in subjectlineTxt:
            assert Hero_WE in self.kdp_sc2, "Hero SC Text not Matched."
        elif "V6" in subjectlineTxt:
            assert Hero_WE in self.kdp_sc3, "Hero SC Text not Matched."
        logger.info(": successfully verified Hero Text::" + Hero_text +"\n "+ Hero_WE)
        logger.info(': #####  Verification Complete  #####\n')

    def get_EPP_or_NonEPP_verification(self):
        logger.info(": ##### Started EPP version verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c7a58e26c304c5abfc889a7224bbcf91.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), "Web Element not Displayed."
            logger.info(": successfully verified EPP version is present.")
        else:
            logger.info(': successfully verified EPP version NOT present.')
        logger.info(': #####  Verification Complete  #####\n')

    def get_subjectLine_text_validation(self):
        logger.info(": ##### Started subjectLine_text verification #####")
        self.SL = ExcelUtil(tc_name="").read_from_excel("Copy", 6, 4).strip()
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        assert self.SL in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Validated Subject Line Text:: " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH_HA = ExcelUtil(tc_name="").read_from_excel("Copy", 7, 4).strip()
        self.PH_HE = ExcelUtil(tc_name="").read_from_excel("Copy", 7, 5).strip()
        self.PH_Mobile = ExcelUtil(tc_name="").read_from_excel("Copy", 7, 6).strip()
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        if "EPP" not in subjectlineTxt:
            if "V1" in subjectlineTxt:
                assert self.PH_HA in pheaderTxt, "pheader Text Not Matching"
            elif "V2" in subjectlineTxt:
                assert self.PH_HE in pheaderTxt, "pheader Text Not Matching"
            elif "V3" in subjectlineTxt:
                assert self.PH_Mobile in pheaderTxt, "pheader Text Not Matching"
        elif "EPP" in subjectlineTxt:
            if "V4" in subjectlineTxt:
                assert self.PH_HA in pheaderTxt, "pheader Text Not Matching"
            elif "V5" in subjectlineTxt:
                assert self.PH_HE in pheaderTxt, "pheader Text Not Matching"
            elif "V6" in subjectlineTxt:
                assert self.PH_Mobile in pheaderTxt, "pheader Text Not Matching"
        logger.info(": Validated Pre-Header Text:: " + pheaderTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_pre_header_link_validation(self):
        logger.info(": ##### Started pre_header_link_validation verification #####")
        self.PH_URL_generic = ExcelUtil(tc_name="").read_from_excel("Module", 6, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@target='_blank'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.PH_URL_generic in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        CreativePage.get_URL_Segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_Hero_link_validation(self):
        logger.info(": ##### Started Hero_link_validation verification #####")
        self.PH_URL_generic = ExcelUtil(tc_name="").read_from_excel("Module", 6, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='kdp_cta']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.PH_URL_generic in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        CreativePage.get_URL_Segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_Module1_top_link_verification(self):
        logger.info(": ##### Started Module1 top link_validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH_URL_HA = ExcelUtil(tc_name="").read_from_excel("Module", 11, 9)
        self.PH_URL_HE = ExcelUtil(tc_name="").read_from_excel("Module", 15, 9)
        self.PH_URL_Mobile = ExcelUtil(tc_name="").read_from_excel("Module", 7, 9)
        parent_window = self.driver.current_window_handle
        if "V1" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_non_top']"))).click()
        elif "V2" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_non_top']"))).click()
        elif "V3" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_non_top']"))).click()
        elif "V4" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_non_top']"))).click()
        elif "V5" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_non_top']"))).click()
        elif "V6" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_non_top']"))).click()

        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url

        if "V1" in subjectlineTxt:
            assert self.PH_URL_HA in URL, "Web Landing Page URL is not Matching."
        elif "V2" in subjectlineTxt:
            assert self.PH_URL_HE in URL, "Web Landing Page URL is not Matching."
        elif "V3" in subjectlineTxt:
            assert self.PH_URL_Mobile in URL, "Web Landing Page URL is not Matching."
        elif "V4" in subjectlineTxt:
            assert self.PH_URL_HA in URL, "Web Landing Page URL is not Matching."
        elif "V5" in subjectlineTxt:
            assert self.PH_URL_HE in URL, "Web Landing Page URL is not Matching."
        elif "V6" in subjectlineTxt:
            assert self.PH_URL_Mobile in URL, "Web Landing Page URL is not Matching."

        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        CreativePage.get_URL_Segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_Module1_link_verification(self):
        logger.info(": ##### Started Module1 link_validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH_URL_HA = ExcelUtil(tc_name="").read_from_excel("Module", 11, 8)
        self.PH_URL_HE = ExcelUtil(tc_name="").read_from_excel("Module", 15, 8)
        self.PH_URL_Mobile = ExcelUtil(tc_name="").read_from_excel("Module", 7, 8)
        parent_window = self.driver.current_window_handle
        if "V1" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_non_cta']"))).click()
        elif "V2" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_non_cta']"))).click()
        elif "V3" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_non_cta']"))).click()
        elif "V4" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_epp_cta']"))).click()
        elif "V5" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_epp_cta']"))).click()
        elif "V6" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_epp_cta']"))).click()

        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url

        if "V1" in subjectlineTxt:
            assert self.PH_URL_HA in URL, "Web Landing Page URL is not Matching."
        elif "V2" in subjectlineTxt:
            assert self.PH_URL_HE in URL, "Web Landing Page URL is not Matching."
        elif "V3" in subjectlineTxt:
            assert self.PH_URL_Mobile in URL, "Web Landing Page URL is not Matching."
        elif "V4" in subjectlineTxt:
            assert self.PH_URL_HA in URL, "Web Landing Page URL is not Matching."
        elif "V5" in subjectlineTxt:
            assert self.PH_URL_HE in URL, "Web Landing Page URL is not Matching."
        elif "V6" in subjectlineTxt:
            assert self.PH_URL_Mobile in URL, "Web Landing Page URL is not Matching."

        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        CreativePage.get_URL_Segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_Module1_minilink1_verification(self):
        logger.info(": ##### Started Module1 minilink1 verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.URL_refrigerator = ExcelUtil(tc_name="").read_from_excel("Module", 12, 8)
        self.URL_tv = ExcelUtil(tc_name="").read_from_excel("Module", 16, 8)
        self.URL_zfold2 = ExcelUtil(tc_name="").read_from_excel("Module", 8, 8)

        parent_window = self.driver.current_window_handle
        if "V1" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_non_inner1']"))).click()
        elif "V2" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_non_inner1']"))).click()
        elif "V3" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_non_inner1']"))).click()
        elif "V4" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_epp_inner1']"))).click()
        elif "V5" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_epp_inner1']"))).click()
        elif "V6" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_epp_inner1']"))).click()

        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url

        if "V1" in subjectlineTxt:
            assert self.URL_refrigerator in URL, "Web Landing Page URL is not Matching."
        elif "V2" in subjectlineTxt:
            assert self.URL_tv in URL, "Web Landing Page URL is not Matching."
        elif "V3" in subjectlineTxt:
            assert self.URL_zfold2 in URL, "Web Landing Page URL is not Matching."
        elif "V4" in subjectlineTxt:
            assert self.URL_refrigerator in URL, "Web Landing Page URL is not Matching."
        elif "V5" in subjectlineTxt:
            assert self.URL_tv in URL, "Web Landing Page URL is not Matching."
        elif "V6" in subjectlineTxt:
            assert self.URL_zfold2 in URL, "Web Landing Page URL is not Matching."

        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        CreativePage.get_URL_Segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_Module1_minilink2_verification(self):
        logger.info(": ##### Started Module1 minilink2 verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text

        self.URL_washer = ExcelUtil(tc_name="").read_from_excel("Module", 13, 9)
        self.URL_soundbar = ExcelUtil(tc_name="").read_from_excel("Module", 17, 8)
        self.URL_zflip = ExcelUtil(tc_name="").read_from_excel("Module", 9, 8)

        parent_window = self.driver.current_window_handle
        if "V1" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_non_inner2_dryer']"))).click()
        elif "V2" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_non_inner2']"))).click()
        elif "V3" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_non_inner2']"))).click()
        elif "V4" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_epp_inner2_dryer']"))).click()
        elif "V5" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_epp_inner2']"))).click()
        elif "V6" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_epp_inner2']"))).click()

        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url

        if "V1" in subjectlineTxt:
            assert self.URL_washer in URL, "Web Landing Page URL is not Matching."
        elif "V2" in subjectlineTxt:
            assert self.URL_soundbar in URL, "Web Landing Page URL is not Matching."
        elif "V3" in subjectlineTxt:
            assert self.URL_zflip in URL, "Web Landing Page URL is not Matching."
        elif "V4" in subjectlineTxt:
            assert self.URL_washer in URL, "Web Landing Page URL is not Matching."
        elif "V5" in subjectlineTxt:
            assert self.URL_soundbar in URL, "Web Landing Page URL is not Matching."
        elif "V6" in subjectlineTxt:
            assert self.URL_zflip in URL, "Web Landing Page URL is not Matching."

        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:
            f.writelines(URL)
        URLSegemntPage.get_segment()
        CreativePage.get_URL_Segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_Module1_minilink3_verification(self):
        logger.info(": ##### Started Module1 minilink3 verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "V2" in subjectlineTxt:
            logger.info(": 3rd Module Not Present.")
        elif "V5" in subjectlineTxt:
            logger.info(": 3rd Module Not Present.")
        if "V1" in subjectlineTxt:
            self.URL_jetstick = ExcelUtil(tc_name="").read_from_excel("Module", 14, 8)
            self.URL_n20 = ExcelUtil(tc_name="").read_from_excel("Module", 10, 8)
            parent_window = self.driver.current_window_handle
            if "V1" in subjectlineTxt:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_non_inner3']"))).click()
                self.driver.close()
            elif "V3" in subjectlineTxt:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_non_inner3']"))).click()
            elif "V4" in subjectlineTxt:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_epp_inner3']"))).click()
            elif "V5" in subjectlineTxt:
                logger.info(": 3rd Module Not Present.")
            elif "V6" in subjectlineTxt:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_epp_inner3']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            URL = self.driver.current_url
            if "V1" in subjectlineTxt:
                assert self.URL_jetstick in URL, "Web Landing Page URL is not Matching."
            elif "V3" in subjectlineTxt:
                assert self.URL_n20 in URL, "Web Landing Page URL is not Matching."
            elif "V4" in subjectlineTxt:
                assert self.URL_jetstick in URL, "Web Landing Page URL is not Matching."
            elif "V6" in subjectlineTxt:
                assert self.URL_n20 in URL, "Web Landing Page URL is not Matching."

            logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:
                f.writelines(URL)
            URLSegemntPage.get_segment()
            CreativePage.get_URL_Segment_validation(self)
            self.driver.close()
            self.driver.switch_to.window(parent_window)
        elif "V3" in subjectlineTxt:
            self.URL_jetstick = ExcelUtil(tc_name="").read_from_excel("Module", 14, 8)
            self.URL_n20 = ExcelUtil(tc_name="").read_from_excel("Module", 10, 8)
            parent_window = self.driver.current_window_handle
            if "V1" in subjectlineTxt:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_non_inner3']"))).click()
                self.driver.close()
            elif "V3" in subjectlineTxt:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_non_inner3']"))).click()
            elif "V4" in subjectlineTxt:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_epp_inner3']"))).click()
            elif "V5" in subjectlineTxt:
                logger.info(": 3rd Module Not Present.")
            elif "V6" in subjectlineTxt:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_epp_inner3']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            URL = self.driver.current_url
            if "V1" in subjectlineTxt:
                assert self.URL_jetstick in URL, "Web Landing Page URL is not Matching."
            elif "V3" in subjectlineTxt:
                assert self.URL_n20 in URL, "Web Landing Page URL is not Matching."
            elif "V4" in subjectlineTxt:
                assert self.URL_jetstick in URL, "Web Landing Page URL is not Matching."
            elif "V6" in subjectlineTxt:
                assert self.URL_n20 in URL, "Web Landing Page URL is not Matching."

            logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:
                f.writelines(URL)
            URLSegemntPage.get_segment()
            CreativePage.get_URL_Segment_validation(self)
            self.driver.close()
            self.driver.switch_to.window(parent_window)
        elif "V4" in subjectlineTxt:
            self.URL_jetstick = ExcelUtil(tc_name="").read_from_excel("Module", 14, 8)
            self.URL_n20 = ExcelUtil(tc_name="").read_from_excel("Module", 10, 8)
            parent_window = self.driver.current_window_handle
            if "V1" in subjectlineTxt:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_non_inner3']"))).click()
                self.driver.close()
            elif "V3" in subjectlineTxt:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_non_inner3']"))).click()
            elif "V4" in subjectlineTxt:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_epp_inner3']"))).click()
            elif "V5" in subjectlineTxt:
                logger.info(": 3rd Module Not Present.")
            elif "V6" in subjectlineTxt:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_epp_inner3']"))).click()
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            URL = self.driver.current_url
            if "V1" in subjectlineTxt:
                assert self.URL_jetstick in URL, "Web Landing Page URL is not Matching."
            elif "V3" in subjectlineTxt:
                assert self.URL_n20 in URL, "Web Landing Page URL is not Matching."
            elif "V4" in subjectlineTxt:
                assert self.URL_jetstick in URL, "Web Landing Page URL is not Matching."
            elif "V6" in subjectlineTxt:
                assert self.URL_n20 in URL, "Web Landing Page URL is not Matching."

            logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
            with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:
                f.writelines(URL)
            URLSegemntPage.get_segment()
            CreativePage.get_URL_Segment_validation(self)
            self.driver.close()
            self.driver.switch_to.window(parent_window)



    def get_Module2_link_verification(self):
        logger.info(": ##### Started Module2 link_validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH_URL_HA = ExcelUtil(tc_name="").read_from_excel("Module", 11, 8)
        self.PH_URL_HE = ExcelUtil(tc_name="").read_from_excel("Module", 15, 8)
        self.PH_URL_Mobile = ExcelUtil(tc_name="").read_from_excel("Module", 7, 8)
        parent_window = self.driver.current_window_handle
        if "V1" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_non_cta']"))).click()
        elif "V2" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_non_cta']"))).click()
        elif "V3" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_non_cta']"))).click()
        elif "V4" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_epp_cta']"))).click()
        elif "V5" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_epp_cta']"))).click()
        elif "V6" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_epp_cta']"))).click()

        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url

        if "V1" in subjectlineTxt:
            assert self.PH_URL_HA in URL, "Web Landing Page URL is not Matching."
        elif "V2" in subjectlineTxt:
            assert self.PH_URL_HE in URL, "Web Landing Page URL is not Matching."
        elif "V3" in subjectlineTxt:
            assert self.PH_URL_Mobile in URL, "Web Landing Page URL is not Matching."
        elif "V4" in subjectlineTxt:
            assert self.PH_URL_HA in URL, "Web Landing Page URL is not Matching."
        elif "V5" in subjectlineTxt:
            assert self.PH_URL_HE in URL, "Web Landing Page URL is not Matching."
        elif "V6" in subjectlineTxt:
            assert self.PH_URL_Mobile in URL, "Web Landing Page URL is not Matching."

        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:
            f.writelines(URL)
        URLSegemntPage.get_segment()
        CreativePage.get_URL_Segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_Module2_top_link_verification(self):
        logger.info(": ##### Started Module2 top link_validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH_URL_HA = ExcelUtil(tc_name="").read_from_excel("Module", 11, 9)
        self.PH_URL_HE = ExcelUtil(tc_name="").read_from_excel("Module", 15, 9)
        self.PH_URL_Mobile = ExcelUtil(tc_name="").read_from_excel("Module", 7, 9)
        parent_window = self.driver.current_window_handle
        if "V1" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_non_top']"))).click()
        elif "V2" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_non_top']"))).click()
        elif "V3" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_non_top']"))).click()
        elif "V4" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_non_top']"))).click()
        elif "V5" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_non_top']"))).click()
        elif "V6" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_non_top']"))).click()

        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url

        if "V1" in subjectlineTxt:
            assert self.PH_URL_HA in URL, "Web Landing Page URL is not Matching."
        elif "V2" in subjectlineTxt:
            assert self.PH_URL_HE in URL, "Web Landing Page URL is not Matching."
        elif "V3" in subjectlineTxt:
            assert self.PH_URL_Mobile in URL, "Web Landing Page URL is not Matching."
        elif "V4" in subjectlineTxt:
            assert self.PH_URL_HA in URL, "Web Landing Page URL is not Matching."
        elif "V5" in subjectlineTxt:
            assert self.PH_URL_HE in URL, "Web Landing Page URL is not Matching."
        elif "V6" in subjectlineTxt:
            assert self.PH_URL_Mobile in URL, "Web Landing Page URL is not Matching."

        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:
            f.writelines(URL)
        URLSegemntPage.get_segment()
        CreativePage.get_URL_Segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_Module3_link_verification(self):
        logger.info(": ##### Started Module3 link_validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH_URL_HA = ExcelUtil(tc_name="").read_from_excel("Module", 11, 8)
        self.PH_URL_HE = ExcelUtil(tc_name="").read_from_excel("Module", 15, 8)
        self.PH_URL_Mobile = ExcelUtil(tc_name="").read_from_excel("Module", 7, 8)
        parent_window = self.driver.current_window_handle
        if "V1" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_non_cta']"))).click()
        elif "V2" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_non_cta']"))).click()
        elif "V3" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_non_cta']"))).click()
        elif "V4" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_epp_cta']"))).click()
        elif "V5" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_epp_cta']"))).click()
        elif "V6" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_epp_cta']"))).click()

        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url

        if "V1" in subjectlineTxt:
            assert self.PH_URL_HA in URL, "Web Landing Page URL is not Matching."
        elif "V2" in subjectlineTxt:
            assert self.PH_URL_HE in URL, "Web Landing Page URL is not Matching."
        elif "V3" in subjectlineTxt:
            assert self.PH_URL_Mobile in URL, "Web Landing Page URL is not Matching."
        elif "V4" in subjectlineTxt:
            assert self.PH_URL_HA in URL, "Web Landing Page URL is not Matching."
        elif "V5" in subjectlineTxt:
            assert self.PH_URL_HE in URL, "Web Landing Page URL is not Matching."
        elif "V6" in subjectlineTxt:
            assert self.PH_URL_Mobile in URL, "Web Landing Page URL is not Matching."

        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:
            f.writelines(URL)
        URLSegemntPage.get_segment()
        CreativePage.get_URL_Segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_Module3_top_link_verification(self):
        logger.info(": ##### Started Module3 top link_validation verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH_URL_HA = ExcelUtil(tc_name="").read_from_excel("Module", 11, 9)
        self.PH_URL_HE = ExcelUtil(tc_name="").read_from_excel("Module", 15, 9)
        self.PH_URL_Mobile = ExcelUtil(tc_name="").read_from_excel("Module", 7, 9)
        parent_window = self.driver.current_window_handle
        if "V1" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_non_top']"))).click()
        elif "V2" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_non_top']"))).click()
        elif "V3" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_non_top']"))).click()
        elif "V4" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_non_top']"))).click()
        elif "V5" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_non_top']"))).click()
        elif "V6" in subjectlineTxt:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_non_top']"))).click()

        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url

        if "V1" in subjectlineTxt:
            assert self.PH_URL_HA in URL, "Web Landing Page URL is not Matching."
        elif "V2" in subjectlineTxt:
            assert self.PH_URL_HE in URL, "Web Landing Page URL is not Matching."
        elif "V3" in subjectlineTxt:
            assert self.PH_URL_Mobile in URL, "Web Landing Page URL is not Matching."
        elif "V4" in subjectlineTxt:
            assert self.PH_URL_HA in URL, "Web Landing Page URL is not Matching."
        elif "V5" in subjectlineTxt:
            assert self.PH_URL_HE in URL, "Web Landing Page URL is not Matching."
        elif "V6" in subjectlineTxt:
            assert self.PH_URL_Mobile in URL, "Web Landing Page URL is not Matching."

        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:
            f.writelines(URL)
        URLSegemntPage.get_segment()
        CreativePage.get_URL_Segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_Memory_Storage_Module_link_verification(self):
        logger.info(": ##### Started Memory & Storage Module link_validation verification #####")
        self.PH_URL_generic = ExcelUtil(tc_name="").read_from_excel("Module", 18, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='memory_cta']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.PH_URL_generic in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        CreativePage.get_URL_Segment_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_HA_validation(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "V1" in subjectlineTxt:
            self.HL = ExcelUtil(tc_name="").read_from_excel("Copy", 19, 4)
            self.SH = ExcelUtil(tc_name="").read_from_excel("Copy", 20, 4)
            self.SC = ExcelUtil(tc_name="").read_from_excel("Copy", 21, 4)
            HL_text = self.driver.find_element_by_xpath("//*[@id='module_ha_epp_hl']").get_attribute("alt")
            assert HL_text in self.HL, "HL text Not Matching."
            logger.info(": Head_Line Text:" + HL_text)
            SH_text = self.driver.find_element_by_xpath("//*[@id='module_ha_epp_sc1']/span").text
            assert SH_text in self.SH, "SH text Not Matching."
            logger.info(": Sub_Head Text:" + SH_text)
            SC_text = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_epp_sc2']"))).text
            assert SC_text in self.SC, " SC Text not Matched."
            logger.info(": Sub_Copy Text:" + SC_text)
        elif "V4" in subjectlineTxt:
            self.HL = ExcelUtil(tc_name="").read_from_excel("Copy", 19, 7)
            self.SH = ExcelUtil(tc_name="").read_from_excel("Copy", 20, 7)
            self.SC = ExcelUtil(tc_name="").read_from_excel("Copy", 21, 7)
            HL_text = self.driver.find_element_by_xpath("//*[@id='module_ha_non_hl']").get_attribute("alt")
            assert HL_text in self.HL, "HL text Not Matching."
            logger.info(": Head_Line Text:" + HL_text)
            SH_text = self.driver.find_element_by_xpath("//*[@id='module_ha_non_sc1']/span").text
            assert SH_text in self.SH, "SH text Not Matching."
            logger.info(": Sub_Head Text:" + SH_text)
            SC_text = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_ha_non_sc2']"))).text
            assert SC_text in self.SC, " SC Text not Matched."
            logger.info(": Sub_Copy Text:" + SC_text)

    def get_HE_validation(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "V2" in subjectlineTxt:
            self.HL = ExcelUtil(tc_name="").read_from_excel("Copy", 19, 5)
            self.SH = ExcelUtil(tc_name="").read_from_excel("Copy", 20, 5)
            self.SC = ExcelUtil(tc_name="").read_from_excel("Copy", 21, 5)
            HL_text = self.driver.find_element_by_xpath("//*[@id='module_he_non_hl']").get_attribute("alt")
            assert HL_text in self.HL, "HL text Not Matching."
            logger.info(": Head_Line Text:" + HL_text)
            SH_text = self.driver.find_element_by_xpath("//*[@id='module_he_non_sc1']/span").text
            assert SH_text in self.SH, "SH text Not Matching."
            logger.info(": Sub_Head Text:" + SH_text)
            SC_text = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_non_sc2']"))).text
            assert SC_text in self.SC, " SC Text not Matched."
            logger.info(": Sub_Copy Text:" + SC_text)
        elif "V5" in subjectlineTxt:
            self.HL = ExcelUtil(tc_name="").read_from_excel("Copy", 19, 8)
            self.SH = ExcelUtil(tc_name="").read_from_excel("Copy", 20, 8)
            self.SC = ExcelUtil(tc_name="").read_from_excel("Copy", 21, 8)
            HL_text = self.driver.find_element_by_xpath("//*[@id='module_he_epp_hl']").get_attribute("alt")
            assert HL_text in self.HL, "HL text Not Matching."
            logger.info(": Head_Line Text:" + HL_text)
            SH_text = self.driver.find_element_by_xpath("//*[@id='module_he_epp_sc1']/span").text
            assert SH_text in self.SH, "SH text Not Matching."
            logger.info(": Sub_Head Text:" + SH_text)
            SC_text = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_he_epp_sc2']"))).text
            assert SC_text in self.SC, " SC Text not Matched."
            logger.info(": Sub_Copy Text:" + SC_text)

    def get_Mobile_validation(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "V3" in subjectlineTxt:
            self.HL = ExcelUtil(tc_name="").read_from_excel("Copy", 19, 6)
            self.SH = ExcelUtil(tc_name="").read_from_excel("Copy", 20, 6)
            self.SC = ExcelUtil(tc_name="").read_from_excel("Copy", 21, 6)
            HL_text = self.driver.find_element_by_xpath("//*[@id='module_im_non_hl']").get_attribute("alt")
            assert HL_text in self.HL, "HL text Not Matching."
            logger.info(": Head_Line Text:" + HL_text)
            SH_text = self.driver.find_element_by_xpath("//*[@id='module_im_non_sc1']/span").text
            assert SH_text.encode('utf-8') in self.SH.encode('utf-8'), "SH text Not Matching."
            logger.info(": Sub_Head Text:" + str(SH_text.encode('utf-8')))
            SC_text = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_non_sc2']"))).text
            assert SC_text in self.SC, " SC Text not Matched."
            logger.info(": Sub_Copy Text:" + SC_text)
        elif "V6" in subjectlineTxt:
            self.HL = ExcelUtil(tc_name="").read_from_excel("Copy", 19, 9)
            self.SH = ExcelUtil(tc_name="").read_from_excel("Copy", 20, 9)
            self.SC = ExcelUtil(tc_name="").read_from_excel("Copy", 21, 9)
            HL_text = self.driver.find_element_by_xpath("//*[@id='module_im_epp_hl']").get_attribute("alt")
            assert HL_text in self.HL, "HL text Not Matching."
            logger.info(": Head_Line Text:" + HL_text)
            SH_text = self.driver.find_element_by_xpath("//*[@id='module_im_epp_sc1']/span").text
            assert SH_text.encode('utf-8') in self.SH.encode('utf-8'), "SH text Not Matching."
            logger.info(": Sub_Head Text:" + str(SH_text.encode('utf-8')))
            SC_text = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_epp_sc2']"))).text
            assert SC_text in self.SC, " SC Text not Matched."
            logger.info(": Sub_Copy Text:" + SC_text)

    def get_Module1_text_verification(self):
        logger.info(": ##### Started Module1 text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "V1" in subjectlineTxt:
            CreativePage.get_HA_validation(self)
        elif "V2" in subjectlineTxt:
            CreativePage.get_HE_validation(self)
        elif "V3" in subjectlineTxt:
            CreativePage.get_Mobile_validation(self)
        elif "V4" in subjectlineTxt:
            CreativePage.get_HA_validation(self)
        elif "V5" in subjectlineTxt:
            CreativePage.get_HE_validation(self)
        elif "V6" in subjectlineTxt:
            CreativePage.get_Mobile_validation(self)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module2_text_verification(self):
        logger.info(": ##### Started Module1 text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "V1" in subjectlineTxt:
            CreativePage.get_HE_validation(self)
        elif "V2" in subjectlineTxt:
            CreativePage.get_HA_validation(self)
        elif "V3" in subjectlineTxt:
            CreativePage.get_Mobile_validation(self)
        elif "V4" in subjectlineTxt:
            CreativePage.get_HE_validation(self)
        elif "V5" in subjectlineTxt:
            CreativePage.get_HA_validation(self)
        elif "V6" in subjectlineTxt:
            CreativePage.get_Mobile_validation(self)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module3_text_verification(self):
        logger.info(": ##### Started Module3 text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "V1" in subjectlineTxt:
            CreativePage.get_Mobile_validation(self)
        elif "V2" in subjectlineTxt:
            CreativePage.get_HA_validation(self)
        elif "V3" in subjectlineTxt:
            CreativePage.get_HE_validation(self)
        elif "V4" in subjectlineTxt:
            CreativePage.get_Mobile_validation(self)
        elif "V5" in subjectlineTxt:
            CreativePage.get_HA_validation(self)
        elif "V6" in subjectlineTxt:
            CreativePage.get_HE_validation(self)
        logger.info(': #####  Verification Complete  #####\n')

    def get_HA_subModule_Text_validation(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "V1" in subjectlineTxt:
            self.ref = ExcelUtil(tc_name="").read_from_excel("Copy", 24, 7)
            self.washer = ExcelUtil(tc_name="").read_from_excel("Copy", 28, 7)
            self.jetStick = ExcelUtil(tc_name="").read_from_excel("Copy", 32, 7)
            refrigerator_text = self.driver.find_element_by_xpath("//*[@id='module_ha_non_inner1']").get_attribute("alt")
            assert refrigerator_text in self.ref, "Refrigerator text Not Matching."
            logger.info(": Refrigerator Text:" + refrigerator_text)
            washer_text = self.driver.find_element_by_xpath("//*[@id='module_ha_non_inner2']").get_attribute("alt")
            assert washer_text in self.SH, "Washer & Dryer text Not Matching."
            logger.info(": Washer & Dryer Text:" + washer_text)
            jetstick_text = self.driver.find_element_by_xpath("//*[@id='module_ha_non_inner3']").get_attribute("alt")
            assert jetstick_text in self.jetStick, " JetStick Text not Matched."
            logger.info(": JetStick Text:" + jetstick_text)
        elif "V4" in subjectlineTxt:
            self.ref = ExcelUtil(tc_name="").read_from_excel("Copy", 24, 7)
            self.washer = ExcelUtil(tc_name="").read_from_excel("Copy", 28, 7)
            self.jetStick = ExcelUtil(tc_name="").read_from_excel("Copy", 32, 7)
            refrigerator_text = self.driver.find_element_by_xpath("//*[@id='module_ha_non_inner1']").get_attribute("alt")
            # assert refrigerator_text in self.ref, "Refrigerator text Not Matching."
            logger.info(": Refrigerator Text:" + refrigerator_text)
            washer_text = self.driver.find_element_by_xpath("//*[@id='module_ha_non_inner2_washer']").get_attribute("alt")
            assert washer_text in self.washer, "Washer & Dryer text Not Matching."
            logger.info(": Washer & Dryer Text:" + washer_text)
            jetstick_text = self.driver.find_element_by_xpath("//*[@id='module_ha_non_inner3']").get_attribute("alt")
            assert jetstick_text in self.jetStick, " JetStick Text not Matched."
            logger.info(": JetStick Text:" + jetstick_text)

    def get_HE_sunModule_Text_validation(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "V2" in subjectlineTxt:
            self.tv = ExcelUtil(tc_name="").read_from_excel("Copy", 24, 5)
            self.soundbar = ExcelUtil(tc_name="").read_from_excel("Copy", 28, 5)
            tv_text = self.driver.find_element_by_xpath("//*[@id='module_he_non_inner1']").get_attribute("alt")
            assert tv_text in self.tv, "TV text Not Matching."
            logger.info(": Head_Line Text:" + tv_text)
            soundBar_text = self.driver.find_element_by_xpath("//*[@id='module_he_non_inner2']").get_attribute("alt")
            assert soundBar_text in self.soundbar, "SoundBar text Not Matching."
            logger.info(": Sub_Head Text:" + soundBar_text)

        elif "V5" in subjectlineTxt:
            self.tv = ExcelUtil(tc_name="").read_from_excel("Copy", 24, 8)
            self.soundbar = ExcelUtil(tc_name="").read_from_excel("Copy", 28, 8)
            tv_text = self.driver.find_element_by_xpath("//*[@id='module_he_epp_inner1']").get_attribute("alt")
            assert tv_text in self.tv, "TV text Not Matching."
            logger.info(": Head_Line Text:" + tv_text)
            soundBar_text = self.driver.find_element_by_xpath("//*[@id='module_he_epp_inner2']").get_attribute("alt")
            assert soundBar_text in self.soundbar, "SoundBar text Not Matching."
            logger.info(": Sub_Head Text:" + soundBar_text)

    def get_Mobile_subModule_text_validation(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "V3" in subjectlineTxt:
            self.ZFold2 = ExcelUtil(tc_name="").read_from_excel("Copy", 24, 6)
            self.ZFlip = ExcelUtil(tc_name="").read_from_excel("Copy", 28, 6)
            self.N20 = ExcelUtil(tc_name="").read_from_excel("Copy", 21, 6)
            ZFold2_text = self.driver.find_element_by_xpath("//*[@id='module_im_non_inner1']").get_attribute("alt")
            assert ZFold2_text in self.HL, "ZFold2text Not Matching."
            logger.info(": Z_fold2 Text:" + ZFold2_text)
            ZFlip_text = self.driver.find_element_by_xpath("//*[@id='module_im_non_inner2']").get_attribute("alt")
            assert ZFlip_text in self.ZFlip, "ZFLip text Not Matching."
            logger.info(": Sub_Head Text:" + ZFlip_text)
            N20_text = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_non_inner3']"))).get_attribute("alt")
            assert N20_text in self.N20, " Note20 Text not Matched."
            logger.info(": Sub_Copy Text:" + N20_text)
        elif "V6" in subjectlineTxt:
            self.ZFold2 = ExcelUtil(tc_name="").read_from_excel("Copy", 24, 9)
            self.ZFlip = ExcelUtil(tc_name="").read_from_excel("Copy", 28, 9)
            self.N20 = ExcelUtil(tc_name="").read_from_excel("Copy", 21, 9)
            ZFold2_text = self.driver.find_element_by_xpath("//*[@id='module_im_epp_inner1']").get_attribute("alt")
            assert ZFold2_text in self.HL, "ZFold2text Not Matching."
            logger.info(": Z_fold2 Text:" + ZFold2_text)
            ZFlip_text = self.driver.find_element_by_xpath("//*[@id='module_im_epp_inner2']").get_attribute("alt")
            assert ZFlip_text in self.ZFlip, "ZFLip text Not Matching."
            logger.info(": Sub_Head Text:" + ZFlip_text)
            N20_text = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='module_im_epp_inner3']"))).get_attribute("alt")
            assert N20_text in self.N20, " Note20 Text not Matched."
            logger.info(": Sub_Copy Text:" + N20_text)

    def get_Module1_subModule_text_verification(self):
        logger.info(": ##### Started Module1 sub Module text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "V1" in subjectlineTxt:
            CreativePage.get_HA_subModule_Text_validation(self)
        elif "V2" in subjectlineTxt:
            CreativePage.get_HE_sunModule_Text_validation(self)
        elif "V3" in subjectlineTxt:
            CreativePage.get_Mobile_subModule_text_validation(self)
        elif "V4" in subjectlineTxt:
            CreativePage.get_HA_subModule_Text_validation(self)
        elif "V5" in subjectlineTxt:
            CreativePage.get_HE_sunModule_Text_validation(self)
        elif "V6" in subjectlineTxt:
            CreativePage.get_Mobile_subModule_text_validation(self)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module2_subModule_text_verification(self):
        logger.info(": ##### Started Module2 sub Module text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "V1" in subjectlineTxt:
            CreativePage.get_HE_sunModule_Text_validation(self)
        elif "V2" in subjectlineTxt:
            CreativePage.get_HA_subModule_Text_validation(self)
        elif "V3" in subjectlineTxt:
            CreativePage.get_Mobile_subModule_text_validation(self)
        elif "V4" in subjectlineTxt:
            CreativePage.get_HE_sunModule_Text_validation(self)
        elif "V5" in subjectlineTxt:
            CreativePage.get_HA_subModule_Text_validation(self)
        elif "V6" in subjectlineTxt:
            CreativePage.get_Mobile_subModule_text_validation(self)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module3_subModule_text_verification(self):
        logger.info(": ##### Started Module3 sub Module text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "V1" in subjectlineTxt:
            CreativePage.get_Mobile_subModule_text_validation(self)
        elif "V2" in subjectlineTxt:
            CreativePage.get_HA_subModule_Text_validation(self)
        elif "V3" in subjectlineTxt:
            CreativePage.get_HE_sunModule_Text_validation(self)
        elif "V4" in subjectlineTxt:
            CreativePage.get_Mobile_subModule_text_validation(self)
        elif "V5" in subjectlineTxt:
            CreativePage.get_HA_subModule_Text_validation(self)
        elif "V6" in subjectlineTxt:
            CreativePage.get_HE_sunModule_Text_validation(self)
        logger.info(': #####  Verification Complete  #####\n')

    def get_URL_Segment_validation(self):
        # logger.info(": ##### Started URL Segment_validation #####")
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
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 3) in readdata['check_list'][0]['utm_campaign']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 3) in readdata['check_list'][0]['utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": utm_campaign==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 3))
                else:
                    logger.info(": FAIL:: utm_campaign NOT matched.")
            else:
                logger.info(": utm_campaign segment NOT present.")

            if "marsLinkCategory" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 2) in readdata['check_list'][0]['marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 2) in readdata['check_list'][0]['marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 2))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 3) in readdata['check_list'][0]['marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 3) in readdata['check_list'][0]['marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 3))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 4) in readdata['check_list'][0]['marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 4) in readdata['check_list'][0]['marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 4))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 5) in readdata['check_list'][0]['marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 5) in readdata['check_list'][0]['marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 5))
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
                else:
                    logger.info(": FAIL:: cid NOT matched.")
            else:
                logger.info(": cid segment NOT present.")

    def get_m1_Conditiontext1_validation(self):
        logger.info(": ##### Started footer condition_text1 verification #####")
        self.tc = ExcelUtil(tc_name="").read_from_excel("TERMS_CONDITIONS", 4, 2)
        footerTxt1 = self.driver.find_element_by_xpath("//*[@id='footer_text1']/p/span").text
        assert self.tc in footerTxt1, "Condition_Text1 Not Matching"
        logger.info(": Validate footer condition_text1:: " + footerTxt1)
        logger.info(': #####  Verification Complete  #####\n')

    def get_m2_Conditiontext2_validation(self):
        logger.info(": ##### Started footer condition_text2 verification #####")
        self.tc2 = ExcelUtil(tc_name="").read_from_excel("TERMS_CONDITIONS", 5, 2)
        footerTxt1 = self.driver.find_element_by_xpath("//*[@id='footer_text2']/p/span").text
        # print(self.tc2.encode('utf-8'))
        # print(footerTxt1.encode('utf-8'))
        assert self.tc2 in footerTxt1, "Condition_Text2 Not Matching"
        logger.info(": Validate footer condition_text2:: " + footerTxt1)
        logger.info(': #####  Verification Complete  #####\n')

    def get_m3_Conditiontext3_validation(self):
        logger.info(": ##### Started footer condition_text3 verification #####")
        self.tc2 = ExcelUtil(tc_name="").read_from_excel("TERMS_CONDITIONS", 6, 2)
        footerTxt1 = self.driver.find_element_by_xpath("//*[@id='footer_text3']/p/span").text
        # print(self.tc2.encode('utf-8'))
        # print(footerTxt1.encode('utf-8'))
        assert self.tc2 in footerTxt1, "Condition_Text3 Not Matching"
        logger.info(": Validate footer condition_text3:: " + footerTxt1)
        logger.info(': #####  Verification Complete  #####\n')

    def get_m4_Conditiontext4_validation(self):
        logger.info(": ##### Started footer condition_text4 verification #####")
        self.tc2 = ExcelUtil(tc_name="").read_from_excel("TERMS_CONDITIONS", 7, 2)
        footerTxt1 = self.driver.find_element_by_xpath("//*[@id='footer_text4']/p/span").text
        # print(self.tc2.encode('utf-8'))
        # print(footerTxt1.encode('utf-8'))
        assert self.tc2 in footerTxt1, "Condition_Text4 Not Matching"
        logger.info(": Validate footer condition_text4:: " + footerTxt1)
        logger.info(': #####  Verification Complete  #####\n')

    def get_m5_Conditiontext5_validation(self):
        logger.info(": ##### Started footer condition_text5 verification #####")
        self.tc2 = ExcelUtil(tc_name="").read_from_excel("TERMS_CONDITIONS", 8, 2)
        footerTxt1 = self.driver.find_element_by_xpath("//*[@id='footer_text5']/p/span").text
        # print(self.tc2.encode('utf-8'))
        # print(footerTxt1.encode('utf-8'))
        assert self.tc2 in footerTxt1, "Condition_Text5 Not Matching"
        logger.info(": Validate footer condition_text5:: " + footerTxt1)
        logger.info(': #####  Verification Complete  #####\n')









