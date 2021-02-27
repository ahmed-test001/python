import os
import sys
import logging
from urllib.request import urlopen
from bs4 import BeautifulSoup
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


class ImageTextExtract(BasePage):

    def get_Text(self):
        logger.info(": ##### Started text_extraction verification #####")
        self.SL = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 18).strip()
        url = "file:///C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/Test_w_53_NewYears_Holiday_Offers_Email/creative/Proof_R1-N1_eComm_Week53_New_Years_Holiday_Offers_201230-Generic-Catch_All-S1-G.htm"
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out

        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        print(self.SL)
        print(text)

        assert self.SL in text, "Subject Line Text Not Matching"
        logger.info(": Validated Subject Line Text:: " + text)
        logger.info(': #####  Verification Complete  #####\n')

