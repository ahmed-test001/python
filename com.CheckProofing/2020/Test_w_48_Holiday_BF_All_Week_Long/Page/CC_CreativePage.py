import os
import sys
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Utility_Files.ExcelReaderUtil import ExcelUtil
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


class CC_CreativePage(BasePage):

    def get_EPP_or_NonEPP_verification(self):
        logger.info(": ##### Started EPP version verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
            EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/1d3e0fa7a0ebb224c043e8d8a33533a5.jpg']")))
            EPP_WElement.is_displayed()
            assert EPP_WElement.is_displayed(), "Web Element not Displayed."
            logger.info(": successfully verified EPP version is present.")
        else:
            logger.info(': successfully verified EPP version NOT present.')
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_subjectLine_text_validation(self):
        logger.info(": ##### Started subjectLine_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH','SL') in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Subject Line text assert with : " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        if "Non" in subjectlineTxt:
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH','PH_Non_Reserve') in pheaderTxt, "Pre Header Text Not Matching"
        else:
            assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH','PH_Reserve') in pheaderTxt, "Pre Header Text Not Matching"
        logger.info(": Pre-Header text assert with : " + pheaderTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_link_validation(self):
        logger.info(": ##### Started pre_header_link_validation verification #####")
        self.PH_URL = ExcelUtil(tc_name="").read_from_excel("FINAL_MODULE_All_Versions", 2, 7)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@target='_blank'])[1]"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        self.url_list.append(URL)
        assert self.PH_URL in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n"+URL+'\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f:f.writelines(URL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_giveWonder_link_validation(self):
        logger.info(": ##### Started GiveWonder Module URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FINAL_MODULE_All_Versions", 3, 7)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/964160ea34117060e7eb9df0f08d4100.jpg']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        givewonderURL = self.driver.current_url
        assert self.url_path in givewonderURL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Web Landing page URL:\n" + givewonderURL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(givewonderURL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Top_Hero_link_validation(self):
        logger.info(": ##### Started Top_Hero Module URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FINAL_MODULE_All_Versions", 2, 7)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/a6f1b5509ab5137ea157700e97fbfe52.png']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        TopHeroURL = self.driver.current_url
        assert self.url_path in TopHeroURL, "Web Landing Page URL is not Matching by Buy_Now_URL"
        logger.info(": successfully verified Web Landing page URL:\n" + TopHeroURL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(TopHeroURL)
        URLSegemntPage.get_segment()
        URLSegemntPage.get_segment_validation()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Module1_SubHeadLineText(self):
        logger.info(": ##### Started Text verification #####")
        self.Reserve = ExcelUtil(tc_name="").read_from_excel("SL_PH", 2, 13).strip()
        self.Non_Reserve = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 13).strip()

        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        SubHeadLine_Txt = self.driver.find_element_by_xpath("//*[@_label='Hero_Text']").text.encode('utf-8')

        if "CC" in subjectlineTxt:
            if "Non" in subjectlineTxt:
                assert self.Non_Reserve.encode('utf-8') in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
            else:
                assert self.Reserve.encode('utf-8') in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."

        logger.info(': #####  Verification Complete  #####\n')

    def get_Text(self):
        logger.info(": ##### Started Text verification #####")
        self.Reserve = ExcelUtil(tc_name="").read_from_excel("SL_PH", 2, 13).strip()
        self.Non_Reserve = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 13).strip()

        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        SubHeadLine_Txt = self.driver.find_element_by_xpath("//*[@href='https://protect2.fireeye.com/v1/url?k=c7c22403-98591d8c-c7c3af4c-0cc47a31307c-08644406e1f4deb8&q=1&e=6222dfc2-cdae-49df-8f76-990fd3136843&u=http%3A%2F%2Ft.info.samsungusa.com%2Fr%2F%3Fid%3Dh345623d7%252C2d15bf6f%252C1fedb3d4%26p1%3D0245437519%26p2%3DFCP_756399983_PDM170661%26p3%3Deml-brd-mul-1120-3100-%26p4%3DEPP_NonReservers%26p5%3D0245437519%26p6%3D0245437519%26p7%3DFCP_756399983_PDM170661%26p8%3Deml-brd-mul-1120-3100-%26p9%3DEPP_NonReservers%26p10%3D0245437519%26p11%3D0245437519%26p12%3DFCP_756399983_PDM170661%26p13%3Deml-brd-mul-1120-3100-%26p14%3DEPP_NonReservers%26p15%3D0245437519%26p16%3D0245437519%26p17%3DFCP_756399983_PDM170661%26p18%3Deml-brd-mul-1120-3100-%26p19%3DEPP_NonReservers%26p20%3D0245437519%26s%3Dh2JLSA8pKxjtx378kBhymN9PJoq0-0aR8Knux07dglo%3D']").text.encode('utf-8')
        print(SubHeadLine_Txt)
        # if "CC" in subjectlineTxt:
        #     if "Non" in subjectlineTxt:
        #         assert self.Non_Reserve.encode('utf-8') in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."
        #     else:
        #         assert self.Reserve.encode('utf-8') in SubHeadLine_Txt, "SubHeadLine Text NOT Matching."

        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_Dynamic_Module_HeadLineText(self):
        logger.info(": ##### Started Text verification #####")

        self.HL_MB = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 4).strip()
        self.HL_TV = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 4, 4).strip()
        self.HL_WEAR = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 5, 4).strip()
        self.HL_COM = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 4).strip()
        self.HL_HA = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 7, 4).strip()

        Prod_Family1_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline_1'])[1]").text.encode('utf-8')
        Prod_Family2_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline_1'])[2]").text.encode('utf-8')
        Prod_Family3_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline_1'])[3]").text.encode('utf-8')
        Prod_Family4_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline_1'])[4]").text.encode('utf-8')
        Prod_Family5_Txt = self.driver.find_element_by_xpath("(//*[@_label='Mod_Headline_1'])[5]").text.encode('utf-8')
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text

        if "CC" in subjectlineTxt:
            if "TV" in subjectlineTxt:
                assert self.HL_TV.encode('utf-8') in Prod_Family1_Txt, "HeadLine Text NOT Matching."
                assert self.HL_MB.encode('utf-8') in Prod_Family2_Txt, "HeadLine Text NOT Matching."
                assert self.HL_WEAR.encode('utf-8') in Prod_Family3_Txt, "HeadLine Text NOT Matching."
                assert self.HL_COM.encode('utf-8') in Prod_Family4_Txt, "HeadLine Text NOT Matching."
                assert self.HL_HA.encode('utf-8') in Prod_Family5_Txt, "HeadLine Text NOT Matching."

            elif "MB" in subjectlineTxt:
                if "WEAR" in subjectlineTxt:
                    assert self.HL_WEAR.encode('utf-8') in Prod_Family1_Txt, "HeadLine Text NOT Matching."
                    assert self.HL_MB.encode('utf-8') in Prod_Family2_Txt, "HeadLine Text NOT Matching."
                    assert self.HL_TV.encode('utf-8') in Prod_Family3_Txt, "HeadLine Text NOT Matching."
                    assert self.HL_COM.encode('utf-8') in Prod_Family4_Txt, "HeadLine Text NOT Matching."
                    assert self.HL_HA.encode('utf-8') in Prod_Family5_Txt, "HeadLine Text NOT Matching."

                else:
                    assert self.HL_MB.encode('utf-8') in Prod_Family1_Txt, "HeadLine Text NOT Matching."
                    assert self.HL_TV.encode('utf-8') in Prod_Family2_Txt, "HeadLine Text NOT Matching."
                    assert self.HL_WEAR.encode('utf-8') in Prod_Family3_Txt, "HeadLine Text NOT Matching."
                    assert self.HL_COM.encode('utf-8') in Prod_Family4_Txt, "HeadLine Text NOT Matching."
                    assert self.HL_HA.encode('utf-8') in Prod_Family5_Txt, "HeadLine Text NOT Matching."

            elif "COMPUTER" in subjectlineTxt:
                assert self.HL_COM.encode('utf-8') in Prod_Family1_Txt, "HeadLine Text NOT Matching."
                assert self.HL_MB.encode('utf-8') in Prod_Family2_Txt, "HeadLine Text NOT Matching."
                assert self.HL_TV.encode('utf-8') in Prod_Family3_Txt, "HeadLine Text NOT Matching."
                assert self.HL_WEAR.encode('utf-8') in Prod_Family4_Txt, "HeadLine Text NOT Matching."
                assert self.HL_HA.encode('utf-8') in Prod_Family5_Txt, "HeadLine Text NOT Matching."

            elif "HA" in subjectlineTxt:
                assert self.HL_HA.encode('utf-8') in Prod_Family1_Txt, "HeadLine Text NOT Matching."
                assert self.HL_MB.encode('utf-8') in Prod_Family2_Txt, "HeadLine Text NOT Matching."
                assert self.HL_TV.encode('utf-8') in Prod_Family3_Txt, "HeadLine Text NOT Matching."
                assert self.HL_WEAR.encode('utf-8') in Prod_Family4_Txt, "HeadLine Text NOT Matching."
                assert self.HL_COM.encode('utf-8') in Prod_Family5_Txt, "HeadLine Text NOT Matching."

        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_Dynamic_Module_SubCopyText(self):
        logger.info(": ##### Started Text verification #####")

        self.SC_MB = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 3, 5).strip()
        self.SC_TV = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 4, 5).strip()
        self.SC_WEAR = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 5, 5).strip()
        self.SC_COM = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 6, 5).strip()
        self.SC_HA = ExcelUtil(tc_name="").read_from_excel("CC_Versions", 7, 5).strip()

        Prod_Family1_Txt = self.driver.find_element_by_xpath("(//*[@_label='Module_Text'])[1]").text.encode('utf-8')
        Prod_Family2_Txt = self.driver.find_element_by_xpath("(//*[@_label='Module_Text'])[2]").text.encode('utf-8')
        Prod_Family3_Txt = self.driver.find_element_by_xpath("(//*[@_label='Module_Text'])[3]").text.encode('utf-8')
        Prod_Family4_Txt = self.driver.find_element_by_xpath("(//*[@_label='Module_Text'])[4]").text.encode('utf-8')
        Prod_Family5_Txt = self.driver.find_element_by_xpath("(//*[@_label='Module_Text'])[5]").text.encode('utf-8')
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text

        if "CC" in subjectlineTxt:
            if "TV" in subjectlineTxt:
                assert self.SC_TV.encode('utf-8') in Prod_Family1_Txt, "SubCopy Text NOT Matching."
                assert self.SC_MB.encode('utf-8') in Prod_Family2_Txt, "SubCopy Text NOT Matching."
                assert self.SC_WEAR.encode('utf-8') in Prod_Family3_Txt, "SubCopy Text NOT Matching."
                assert self.SC_COM.encode('utf-8') in Prod_Family4_Txt, "SubCopy Text NOT Matching."
                assert self.SC_HA.encode('utf-8') in Prod_Family5_Txt, "SubCopy Text NOT Matching."

            elif "MB" in subjectlineTxt:
                if "WEAR" in subjectlineTxt:
                    print(self.SC_MB.encode('utf-8'))
                    print(Prod_Family2_Txt)
                    assert self.SC_WEAR.encode('utf-8') in Prod_Family1_Txt, "SubCopy Text NOT Matching."
                    assert self.SC_MB in Prod_Family2_Txt, "SubCopy Text NOT Matching."
                    assert self.SC_TV.encode('utf-8') in Prod_Family3_Txt, "SubCopy Text NOT Matching."
                    assert self.SC_COM.encode('utf-8') in Prod_Family4_Txt, "SubCopy Text NOT Matching."
                    assert self.SC_HA.encode('utf-8') in Prod_Family5_Txt, "SubCopy Text NOT Matching."

                else:
                    print(self.SC_COM.encode('utf-8'))
                    print(Prod_Family1_Txt)
                    assert self.SC_MB.encode('utf-8') in Prod_Family1_Txt, "SubCopy Text NOT Matching."
                    assert self.SC_TV.encode('utf-8') in Prod_Family2_Txt, "SubCopy Text NOT Matching."
                    assert self.SC_WEAR.encode('utf-8') in Prod_Family3_Txt, "SubCopy Text NOT Matching."
                    assert self.SC_COM.encode('utf-8') in Prod_Family4_Txt, "SubCopy Text NOT Matching."
                    assert self.SC_HA.encode('utf-8') in Prod_Family5_Txt, "SubCopy Text NOT Matching."


            elif "COMPUTER" in subjectlineTxt:
                assert self.SC_COM.encode('utf-8') in Prod_Family1_Txt, "SubCopy Text NOT Matching."
                assert self.SC_MB.encode('utf-8') in Prod_Family2_Txt, "SubCopy Text NOT Matching."
                assert self.SC_TV.encode('utf-8') in Prod_Family3_Txt, "SubCopy Text NOT Matching."
                assert self.SC_WEAR.encode('utf-8') in Prod_Family4_Txt, "SubCopy Text NOT Matching."
                assert self.SC_HA.encode('utf-8') in Prod_Family5_Txt, "SubCopy Text NOT Matching."

            elif "HA" in subjectlineTxt:
                assert self.SC_HA.encode('utf-8') in Prod_Family1_Txt, "SubCopy Text NOT Matching."
                assert self.SC_MB.encode('utf-8') in Prod_Family2_Txt, "SubCopy Text NOT Matching."
                assert self.SC_TV.encode('utf-8') in Prod_Family3_Txt, "SubCopy Text NOT Matching."
                assert self.SC_WEAR.encode('utf-8') in Prod_Family4_Txt, "SubCopy Text NOT Matching."
                assert self.SC_COM.encode('utf-8') in Prod_Family5_Txt, "SubCopy Text NOT Matching."

        logger.info(': #####  Verification Complete  #####\n')














