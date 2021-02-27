import os
import sys
import logging
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
# os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
from Test_Campaign_2021.scripts.python.Page.BasePageClass import BasePage
from Test_Campaign_2021.scripts.python.Util_Data.ExcelReaderUtil import ExcelUtil
from Test_Campaign_2021.scripts.python.Util_Data.HTMLTestRunner import stdout_redirector
from Test_Campaign_2021.scripts.python.Util_Data import ReadConfig
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class TermsConditionPage(BasePage):

    def get_ConditionText1_validation(self,sheet_name,sheet_row1,sheet_row_NR, sheet_column1,sheet_column_NR,xpath_loc):
        logger.info(": ##### Started footer condition_text1 verification #####")
        self.tc1 = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row1), int(sheet_column1))
        self.tc1_NR = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row_NR), int(sheet_column_NR))
        subjectlineTxt = self.driver.find_element_by_xpath(ReadConfig.readFilePathData('FilePaths', 'subject_line')).text
        footerTxt1 = self.driver.find_element_by_xpath(xpath_loc).text
        try:
            if "Non" not in subjectlineTxt:
                assert self.tc1.encode('utf-8') in footerTxt1.encode('utf-8'), "Condition_Text1 Not Matching"
            elif "Non" in subjectlineTxt:
                assert self.tc1_NR.encode('utf-8') in footerTxt1.encode('utf-8'), "Condition_Text1 Not Matching"
        except:
            assert self.tc1.encode('utf-8') in footerTxt1.encode('utf-8'), "Condition_Text1 Not Matching"
        logger.info(": Validate footer condition_text1:: " + str(footerTxt1.encode('utf-8')))
        logger.info(': #####  Verification Complete  #####\n')

    def get_ConditionText2_validation(self,sheet_name,sheet_row1,sheet_row_NR, sheet_column1,sheet_column_NR,xpath_loc):
        logger.info(": ##### Started footer condition_text2 verification #####")
        self.tc2 = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row1), int(sheet_column1))
        self.tc2_NR = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row_NR), int(sheet_column_NR))
        subjectlineTxt = self.driver.find_element_by_xpath(ReadConfig.readFilePathData('FilePaths', 'subject_line')).text
        footerTxt2 = self.driver.find_element_by_xpath(xpath_loc).text
        try:
            if "Non" not in subjectlineTxt:
                assert self.tc2.encode('utf-8') in footerTxt2.encode('utf-8'), "Condition_Text2 Not Matching"
            elif "Non" in subjectlineTxt:
                assert self.tc2_NR.encode('utf-8') in footerTxt2.encode('utf-8'), "Condition_Text2 Not Matching"
        except:
            assert self.tc2.encode('utf-8') in footerTxt2.encode('utf-8'), "Condition_Text2 Not Matching"
        logger.info(": Validate footer condition_text2:: " + str(footerTxt2.encode('utf-8')))
        logger.info(': #####  Verification Complete  #####\n')

    def get_ConditionText3_validation(self,sheet_name,sheet_row1,sheet_row_NR, sheet_column1,sheet_column_NR,xpath_loc):
        logger.info(": ##### Started footer condition_text3 verification #####")
        self.tc3 = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row1), int(sheet_column1))
        self.tc3_NR = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row_NR), int(sheet_column_NR))
        subjectlineTxt = self.driver.find_element_by_xpath(ReadConfig.readFilePathData('FilePaths', 'subject_line')).text
        footerTxt3 = self.driver.find_element_by_xpath(xpath_loc).text
        try:
            if "Non" not in subjectlineTxt:
                assert self.tc3.encode('utf-8') in footerTxt3.encode('utf-8'), "Condition_Text3 Not Matching"
            elif "Non" in subjectlineTxt:
                assert self.tc3_NR.encode('utf-8') in footerTxt3.encode('utf-8'), "Condition_Text3 Not Matching"
        except:
            assert self.tc3.encode('utf-8') in footerTxt3.encode('utf-8'), "Condition_Text3 Not Matching"
        logger.info(": Validate footer condition_text3:: " + str(footerTxt3.encode('utf-8')))
        logger.info(': #####  Verification Complete  #####\n')

    def get_ConditionText4_validation(self,sheet_name,sheet_row1,sheet_row_NR, sheet_column1,sheet_column_NR,xpath_loc):
        logger.info(": ##### Started footer condition_text4 verification #####")
        self.tc4 = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row1), int(sheet_column1))
        self.tc4_NR = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row_NR), int(sheet_column_NR))
        subjectlineTxt = self.driver.find_element_by_xpath(ReadConfig.readFilePathData('FilePaths', 'subject_line')).text
        footerTxt4 = self.driver.find_element_by_xpath(xpath_loc).text
        try:
            if "Non" not in subjectlineTxt:
                assert self.tc4.encode('utf-8') in footerTxt4.encode('utf-8'), "Condition_Text4 Not Matching"
            elif "Non" in subjectlineTxt:
                assert self.tc4_NR.encode('utf-8') in footerTxt4.encode('utf-8'), "Condition_Text4 Not Matching"
        except:
            assert self.tc4.encode('utf-8') in footerTxt4.encode('utf-8'), "Condition_Text4 Not Matching"
        logger.info(": Validate footer condition_text4:: " + str(footerTxt4.encode('utf-8')))
        logger.info(': #####  Verification Complete  #####\n')
