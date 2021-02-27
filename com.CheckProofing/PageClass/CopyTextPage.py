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


class CopyTextPage(BasePage):

    def get_subjectLine_text_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started subjectLine_text verification #####")
        self.SL = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        self.SL_non = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        subjectlineTxt = self.driver.find_element_by_xpath(xpath_loc).text
        # subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "Non" not in subjectlineTxt:
            assert self.SL in subjectlineTxt, "Subject line text NOT matched."
        elif "Non" in subjectlineTxt:
            assert self.SL_non in subjectlineTxt, "Subject line text NOT matched."
        logger.info(": Validated Subject Line Text:: " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_subjectLine_text_validation(self):
        logger.info(": ##### Started subjectLine_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.SL = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 9).strip()
        self.SL_B = ExcelUtil(tc_name="").read_from_excel("SL_PH", 5, 9).strip()
        self.SL_TV_NR = ExcelUtil(tc_name="").read_from_excel("SL_PH", 6, 9).strip()
        self.SL_TV_DD = ExcelUtil(tc_name="").read_from_excel("SL_PH", 27, 9).strip()
        if "CC" in subjectlineTxt:
            if "TV" in subjectlineTxt:
                if "EPP" in subjectlineTxt:
                    assert self.SL in subjectlineTxt, "Subject Line Text Not Matching"
                elif "EPP" not in subjectlineTxt:
                    if "Non" in subjectlineTxt:
                        assert self.SL_TV_NR in subjectlineTxt, "Subject Line Text Not Matching"
                    else:
                        assert self.SL_B in subjectlineTxt, "Subject Line Text Not Matching"
            elif "TABCOM" in subjectlineTxt:
                assert self.SL in subjectlineTxt, "Subject Line Text Not Matching"
            elif "WEAR" in subjectlineTxt:
                assert self.SL in subjectlineTxt, "Subject Line Text Not Matching"
            elif "OTHER" in subjectlineTxt:
                assert self.SL in subjectlineTxt, "Subject Line Text Not Matching"
            elif "HA" in subjectlineTxt:
                if "EPP" in subjectlineTxt:
                    assert self.SL in subjectlineTxt, "Subject Line Text Not Matching"
                else:
                    assert self.SL_B in subjectlineTxt, "Subject Line Text Not Matching"
            elif "MB" in subjectlineTxt:
                assert self.SL in subjectlineTxt, "Subject Line Text Not Matching"

        elif "DD" in subjectlineTxt:
            if "MB" in subjectlineTxt:
                assert self.SL in subjectlineTxt, "Subject Line Text Not Matching"
            elif "TV" in subjectlineTxt:
                print(self.SL_TV_DD)
                print(subjectlineTxt)
                assert self.SL_TV_DD in subjectlineTxt, "Subject Line Text Not Matching"

        elif "Gift" in subjectlineTxt:
            assert self.SL in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Validated Subject Line Text:: " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_subjectLine_text_validation(self):
        logger.info(": ##### Started subjectLine_text verification #####")
        self.SL_1 = ExcelUtil(tc_name="").read_from_excel("Generic", 8, 3).strip()
        self.SL_2 = ExcelUtil(tc_name="").read_from_excel("Generic", 8, 11).strip()
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "EPP" in subjectlineTxt:
            if "Non" in subjectlineTxt:
                assert self.SL_2 in subjectlineTxt, "Subject Line Text Not Matching"
            else:
                assert self.SL_1 in subjectlineTxt, "Subject Line Text Not Matching"
        else:
            assert self.SL_1 in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Validated Subject Line Text:: " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_subjectLine_text_validation(self):
        logger.info(": ##### Started subjectLine_text verification #####")
        self.SL_700 = ExcelUtil(tc_name="").read_from_excel("Generic", 9, 3).strip()
        self.SL_550 = ExcelUtil(tc_name="").read_from_excel("Generic", 9, 4).strip()
        self.SL_350 = ExcelUtil(tc_name="").read_from_excel("Generic", 9, 5).strip()
        self.SL_250 = ExcelUtil(tc_name="").read_from_excel("Generic", 9, 6).strip()
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "N-4_$250" in subjectlineTxt:
            assert self.SL_250 in subjectlineTxt, "Subject Line Text Not Matching"
        elif "N-1_$700" in subjectlineTxt:
            assert self.SL_700 in subjectlineTxt, "Subject Line Text Not Matching"
        elif "N-2_$550" or "N10+" or "N10" or "S10+" or "S10" in subjectlineTxt:
            assert self.SL_550 in subjectlineTxt, "Subject Line Text Not Matching"
        elif "N-3_$350" or "S9+" in subjectlineTxt:
            assert self.SL_350 in subjectlineTxt, "Subject Line Text Not Matching"
        else:
            assert self.SL_700 in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Validated Subject Line Text:: " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_subjectLine_text_validation(self):
        logger.info(": ##### Started subjectLine_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.SL_Fold = ExcelUtil(tc_name="").read_from_excel("SL_PH", 2, 8).strip()
        self.SL_S = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 8).strip()
        self.SL_A71 = ExcelUtil(tc_name="").read_from_excel("SL_PH", 4, 8).strip()
        self.SL_CE = ExcelUtil(tc_name="").read_from_excel("SL_PH", 5, 8).strip()
        self.SL_WEAR = ExcelUtil(tc_name="").read_from_excel("SL_PH", 6, 8).strip()
        self.SL_CC_MB = ExcelUtil(tc_name="").read_from_excel("SL_PH_CC", 2, 8).strip()
        self.SL_CC_WEAR = ExcelUtil(tc_name="").read_from_excel("SL_PH_CC", 4, 8).strip()
        self.SL_CC_TABCOM = ExcelUtil(tc_name="").read_from_excel("SL_PH_CC", 6, 8).strip()

        if "CC" in subjectlineTxt:
            if "MB" in subjectlineTxt:
                assert self.SL_CC_MB in subjectlineTxt, "Subject Line Text Not Matching"
            elif "TABCOM" in subjectlineTxt:
                assert self.SL_CC_TABCOM in subjectlineTxt, "Subject Line Text Not Matching"
            elif "WEAR" in subjectlineTxt:
                assert self.SL_CC_WEAR in subjectlineTxt, "Subject Line Text Not Matching"
            elif "CATCH" in subjectlineTxt:
                assert self.SL_CC_MB in subjectlineTxt, "Subject Line Text Not Matching"
            elif "Wear" in subjectlineTxt:
                assert self.SL_CC_WEAR in subjectlineTxt, "Subject Line Text Not Matching"
            elif "Catch" in subjectlineTxt:
                assert self.SL_CC_MB in subjectlineTxt, "Subject Line Text Not Matching"

        elif "DD" in subjectlineTxt:
            if "CE" in subjectlineTxt:
                assert self.SL_CE in subjectlineTxt, "Subject Line Text Not Matching"
            elif "FOLD" in subjectlineTxt:
                assert self.SL_Fold in subjectlineTxt, "Subject Line Text Not Matching"
            elif "Fold" in subjectlineTxt:
                assert self.SL_Fold in subjectlineTxt, "Subject Line Text Not Matching"
            elif "A71" in subjectlineTxt:
                assert self.SL_A71 in subjectlineTxt, "Subject Line Text Not Matching"
            elif "CE" in subjectlineTxt:
                assert self.SL_CE in subjectlineTxt, "Subject Line Text Not Matching"
            elif "WEAR" in subjectlineTxt:
                assert self.SL_WEAR in subjectlineTxt, "Subject Line Text Not Matching"
            elif "Wear" in subjectlineTxt:
                assert self.SL_WEAR in subjectlineTxt, "Subject Line Text Not Matching"
            elif "S" in subjectlineTxt:
                assert self.SL_S in subjectlineTxt, "Subject Line Text Not Matching"

        logger.info(": Validated Subject Line Text:: " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_pre_header_text_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started pre_header_text verification #####")
        self.PH = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column)).strip()
        pheaderTxt = self.driver.find_element_by_xpath(xpath_loc).text
        # pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        assert self.PH in pheaderTxt, "Pre Header Text Not Matching"
        logger.info(": Validated Pre-Header Text:: " + pheaderTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        self.PH_700 = ExcelUtil(tc_name="").read_from_excel("Generic1", 10, 3).strip()
        self.PH_350 = ExcelUtil(tc_name="").read_from_excel("Generic1", 10, 3).strip()
        self.PH_550 = ExcelUtil(tc_name="").read_from_excel("Generic1", 10, 5).strip()
        self.PH_250 = ExcelUtil(tc_name="").read_from_excel("Generic1", 10, 7).strip()
        self.PH_N20 = ExcelUtil(tc_name="").read_from_excel("Generic1", 10, 12).strip()
        self.PH_NR = ExcelUtil(tc_name="").read_from_excel("Generic1", 10, 4).strip()
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "700_TI" in subjectlineTxt:
            assert self.PH_700 in pheaderTxt, "pheader Text Not Matching"
        elif "550_TI" in subjectlineTxt:
            assert self.PH_550 in pheaderTxt, "pheader Text Not Matching"
        elif "350_TI" in subjectlineTxt:
            assert self.PH_350 in pheaderTxt, "pheader Text Not Matching"
        elif "250_T1" in subjectlineTxt:
            assert self.PH_250 in pheaderTxt, "pheader Text Not Matching"
        elif "LO" in subjectlineTxt:
            assert self.PH_700 in pheaderTxt, "pheader Text Not Matching"
        elif "S10+" in subjectlineTxt:
            assert self.PH_550 in pheaderTxt, "pheader Text Not Matching"
        elif "S10" in subjectlineTxt:
            assert self.PH_550 in pheaderTxt, "pheader Text Not Matching"
        elif "S9+" in subjectlineTxt:
            assert self.PH_350 in pheaderTxt, "pheader Text Not Matching"
        elif "N10+" in subjectlineTxt:
            assert self.PH_550 in pheaderTxt, "pheader Text Not Matching"
        elif "N10" in subjectlineTxt:
            assert self.PH_550 in pheaderTxt, "pheader Text Not Matching"
        elif "S20+" in subjectlineTxt:
            assert self.PH_N20 in pheaderTxt, "pheader Text Not Matching"
        elif "S20" in subjectlineTxt:
            assert self.PH_N20 in pheaderTxt, "pheader Text Not Matching"
        elif "Reserver_Generic_No_JetStick" in subjectlineTxt:
            assert self.PH_NR in pheaderTxt, "pheader Text Not Matching"
        elif "EPP_Enrollees_Non_Res" in subjectlineTxt:
            assert self.PH_NR in pheaderTxt, "pheader Text Not Matching"
        else:
            assert self.PH_700 in pheaderTxt, "pheader Text Not Matching"
        logger.info(": Validated Pre-Header Text:: " + pheaderTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        self.PH_MB_DD = ExcelUtil(tc_name="").read_from_excel("SL_PH", 25, 10).strip()
        self.PH_MB_DD_NR = ExcelUtil(tc_name="").read_from_excel("SL_PH", 26, 10).strip()
        self.PH_MB = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 10).strip()
        self.PH_MB_WEAR = ExcelUtil(tc_name="").read_from_excel("SL_PH", 10, 10).strip()
        self.PH_TV = ExcelUtil(tc_name="").read_from_excel("SL_PH", 5, 10).strip()
        self.PH_TV_EPP = ExcelUtil(tc_name="").read_from_excel("SL_PH", 15, 10).strip()
        self.PH_DD_TV = ExcelUtil(tc_name="").read_from_excel("SL_PH", 27, 10).strip()
        self.PH_CE = ExcelUtil(tc_name="").read_from_excel("SL_PH", 7, 10).strip()
        self.PH_HA = ExcelUtil(tc_name="").read_from_excel("SL_PH", 11, 10).strip()
        self.PH_HA_EPP = ExcelUtil(tc_name="").read_from_excel("SL_PH", 22, 10).strip()

        if "CC" in subjectlineTxt:
            if "TABCOM" in subjectlineTxt:
                assert self.PH_CE in pheaderTxt, "Pre Header Text Not Matching"
            elif "TV" in subjectlineTxt:
                if "EPP" in subjectlineTxt:
                    assert self.PH_TV_EPP in pheaderTxt, "Pre Header Text Not Matching"
                else:
                    assert self.PH_TV in pheaderTxt, "Pre Header Text Not Matching"
            elif "MB" in subjectlineTxt:
                if "WEAR" in subjectlineTxt:
                    assert self.PH_MB_WEAR in pheaderTxt, "Pre Header Text Not Matching"
                else:
                    assert self.PH_MB in pheaderTxt, "Pre Header Text Not Matching"
            elif "HA_KITCHEN" in subjectlineTxt:
                if "EPP" in subjectlineTxt:
                    print(self.PH_HA_EPP)
                    print(pheaderTxt)
                    assert self.PH_HA_EPP in pheaderTxt, "Pre Header Text Not Matching"
                else:
                    print(self.PH_HA)
                    print(pheaderTxt)
                    assert self.PH_HA in pheaderTxt, "Pre Header Text Not Matching"
            elif "HA_CLEANER" in subjectlineTxt:
                if "EPP" in subjectlineTxt:
                    print(self.PH_HA_EPP)
                    print(pheaderTxt)
                    assert self.PH_HA_EPP in pheaderTxt, "Pre Header Text Not Matching"
                else:
                    assert self.PH_HA in pheaderTxt, "Pre Header Text Not Matching"

        elif "DD" in subjectlineTxt:
            if "MB" in subjectlineTxt:
                if "Non" in subjectlineTxt:
                    assert self.PH_MB_DD_NR in pheaderTxt, "Pre Header Text Not Matching"
                else:
                    assert self.PH_MB_DD in pheaderTxt, "Pre Header Text Not Matching"
            elif "TV" in subjectlineTxt:
                assert self.PH_DD_TV in pheaderTxt, "Pre Header Text Not Matching"
        logger.info(": Validated Pre-Header Text:: " + pheaderTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        self.PH_R = ExcelUtil(tc_name="").read_from_excel("SL_PH", 2, 9).strip()
        self.PH_NR = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 9).strip()
        if "MB" in subjectlineTxt:
            if "Non" in subjectlineTxt:
                assert self.PH_NR in pheaderTxt, "Pre Header Text Not Matching"
            else:
                assert self.PH_R in pheaderTxt, "Pre Header Text Not Matching"
        else:
            assert self.PH_NR in pheaderTxt, "Pre Header Text Not Matching"
        logger.info(": Validated Pre-Header Text:: " + pheaderTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_CC_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text.encode('utf-8')
        self.PH_R = ExcelUtil(tc_name="").read_from_excel("SL_PH", 2, 9).strip()
        self.PH_DD_NR = ExcelUtil(tc_name="").read_from_excel("SL_PH", 7, 9).strip()
        self.PH_CC_NR = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 9).strip()
        if "DD" in subjectlineTxt:
            if "MB" in subjectlineTxt:
                if "Non" in subjectlineTxt:
                    assert self.PH_DD_NR.encode('utf-8') in pheaderTxt, "Pre Header Text Not Matching"
                else:
                    assert self.PH_R.encode('utf-8') in pheaderTxt, "Pre Header Text Not Matching"
        elif "Default" in subjectlineTxt:
            if "Non" in subjectlineTxt:
                assert self.PH_CC_NR.encode('utf-8') in pheaderTxt, "Pre Header Text Not Matching"
            else:
                assert self.PH_R.encode('utf-8') in pheaderTxt, "Pre Header Text Not Matching"

        logger.info(": Validated Pre-Header Text:: " + str(pheaderTxt,'utf-8'))
        logger.info(': #####  Verification Complete  #####\n')

    def get_DD_pre_header_text_validation(self):
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        logger.info(": ##### Started pre_header_text verification #####")
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        if "MB" in subjectlineTxt:
            if "NOTE" in subjectlineTxt:
                if "Non_Reservers" in subjectlineTxt:
                    self.PH_Note_NR = ExcelUtil(tc_name="").read_from_excel("SL_PH", 8, 5)
                    assert self.PH_Note_NR in pheaderTxt, "Pre Header Text Not Matching"
                elif "Reservers" in subjectlineTxt:
                    self.PH_Note_R = ExcelUtil(tc_name="").read_from_excel("SL_PH", 7, 5)
                    assert self.PH_Note_R in pheaderTxt, "Pre Header Text Not Matching"
            elif "GALAXY" in subjectlineTxt:
                self.PH_Galaxy_R = ExcelUtil(tc_name="").read_from_excel("SL_PH", 6, 5)
                assert self.PH_Galaxy_R in pheaderTxt, "Pre Header Text Not Matching"
            elif "WEAR" in subjectlineTxt:
                self.PH_ME = ExcelUtil(tc_name="").read_from_excel("SL_PH", 12, 5)
                assert self.PH_ME in pheaderTxt, "Pre Header Text Not Matching"
            elif "ACCESSORY" in subjectlineTxt:
                self.PH_ME = ExcelUtil(tc_name="").read_from_excel("SL_PH", 12, 5)
                assert self.PH_ME in pheaderTxt, "Pre Header Text Not Matching"

        elif "TV" in subjectlineTxt:
            if "QLED" in subjectlineTxt:
                self.PH_TV_QLED = ExcelUtil(tc_name="").read_from_excel("SL_PH", 17, 5)
                # assert self.PH_TV_QLED in pheaderTxt, "Pre Header Text Not Matching"
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH', 'tv') in pheaderTxt, "Pre Header Text Not Matching"
            elif "ACCESSORY" in subjectlineTxt:
                self.PH_TV_ACCESSORY = ExcelUtil(tc_name="").read_from_excel("SL_PH", 10, 5)
                # assert self.PH_TV_ACCESSORY in pheaderTxt, "Pre Header Text Not Matching"
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH', 'tv_accessory') in pheaderTxt, "Pre Header Text Not Matching"

        elif "CE" in subjectlineTxt:
            if "COMPUTER" in subjectlineTxt:
                self.PH_TV_CE = ExcelUtil(tc_name="").read_from_excel("SL_PH", 11, 5)
                # assert self.PH_TV_CE in pheaderTxt, "Pre Header Text Not Matching"
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH','COMPUTER') in pheaderTxt, "Pre Header Text Not Matching"

        elif "HA" in subjectlineTxt:
            if "LAUNDRY" in subjectlineTxt:
                self.PH_HA_LAUNDRY = ExcelUtil(tc_name="").read_from_excel("SL_PH", 14, 5)
                # assert self.PH_HA_LAUNDRY in pheaderTxt, "Pre Header Text Not Matching"
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH','LAUNDRY') in pheaderTxt, "Pre Header Text Not Matching"
            elif "KITCHEN" in subjectlineTxt:
                self.PH_HA_KITCHEN = ExcelUtil(tc_name="").read_from_excel("SL_PH", 21, 5)
                # assert self.PH_HA_KITCHEN in pheaderTxt, "Pre Header Text Not Matching"
                assert ReadConfig.read_w46_HolidayDeals_T2_configData('proof_PH', 'KITCHEN') in pheaderTxt, "Pre Header Text Not Matching"

        logger.info(": Pre-Header text assert with : " + pheaderTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Hero_Banner1_Text_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Hero_Banner1_Text_validation #####")
        self.Banner1 = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column)).strip()
        Hero_Banner1_txt = self.driver.find_element_by_xpath("//a[@id='hero_banner1']").text
        Hero_Banner1_alt = self.driver.find_element_by_xpath("//a[@id='hero_banner1").get_attribute("alt")
        try:
            assert Hero_Banner1_txt in self.Banner1, "Text Not Matching"
        except:
            assert Hero_Banner1_alt in self.Banner1, "Text Not Matching"
        logger.info(": Validated Hero Banner1 Text:: " + self.Banner1)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Hero_Headline1_Text_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Hero_Headline1_Text_validation #####")
        self.HL1 = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column)).strip()
        Hero_HL1_txt = self.driver.find_element_by_xpath("//a[@id='hero_headline1']").text
        Hero_HL1_alt = self.driver.find_element_by_xpath("//a[@id='hero_headline1").get_attribute("alt")
        try:
            assert Hero_HL1_txt in self.Banner1, "Text Not Matching"
        except:
            assert Hero_HL1_alt in self.Banner1, "Text Not Matching"
        logger.info(": Validated Headline1 Text:: " + self.HL1)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Hero_Headline2_Text_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Hero_Headline2_Text_validation #####")
        self.HL2 = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column)).strip()
        Hero_HL2_txt = self.driver.find_element_by_xpath("//a[@id='hero_headline2']").text
        Hero_HL2_alt = self.driver.find_element_by_xpath("//a[@id='hero_headline2").get_attribute("alt")
        try:
            assert Hero_HL2_txt in self.Banner1, "Text Not Matching"
        except:
            assert Hero_HL2_alt in self.Banner1, "Text Not Matching"
        logger.info(": Validated Headline2 Text:: " + self.HL2)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Hero_Sub_Headline1_Text_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Hero_sub_Headline1_Text_validation #####")
        self.subHL1 = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column)).strip()
        Hero_subHL1_txt = self.driver.find_element_by_xpath("//a[@id='hero_subheadline1']").text
        Hero_subHL1_alt = self.driver.find_element_by_xpath("//a[@id='hero_subheadline1").get_attribute("alt")
        try:
            assert Hero_subHL1_txt in self.Banner1, "Text Not Matching"
        except:
            assert Hero_subHL1_alt in self.Banner1, "Text Not Matching"
        logger.info(": Validated Sub_Headline1 Text:: " + self.subHL1)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Hero_Sub_Copy1_Text_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Hero_Sub_Copy1_Text_validation #####")
        self.subHL1 = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column)).strip()
        Hero_subHL1_txt = self.driver.find_element_by_xpath("//a[@id='hero_subheadline1']").text
        Hero_subHL1_alt = self.driver.find_element_by_xpath("//a[@id='hero_subheadline1").get_attribute("alt")
        try:
            assert Hero_subHL1_txt in self.Banner1, "Text Not Matching"
        except:
            assert Hero_subHL1_alt in self.Banner1, "Text Not Matching"
        logger.info(": Validated Sub_Copy1_Text Text:: " + self.subHL1)
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
        self.sc = ExcelUtil(tc_name="").read_from_excel("Copy", 19, 7).strip()
        self.sc_epp = ExcelUtil(tc_name="").read_from_excel("Copy", 19, 8).strip()
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        subcopyTxt = self.driver.find_element_by_xpath("//*[@id='kv_sc']").text
        if "EPP" not in subjectlineTxt:
            assert self.sc in subcopyTxt, "subcopy text NOT matched."
        elif "EPP" in subjectlineTxt:
            assert self.sc_epp.encode('utf-8') in subcopyTxt.encode('utf-8'), "subcopy text NOT matched."
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
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/082be9e3dc6ee0498dea3cad3850a922.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "Reservers" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/19e551e92620b6b4d4f920e15de46459.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
        logger.info(": Validated Subject Line Text:: " + Hero_SL)
        logger.info(': #####  Verification Complete  #####\n')



















