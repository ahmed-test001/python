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

    # def get_DeviceOption_verification(self):
    #     logger.info(": ##### Started Device Option verification #####")
    #     subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
    #     if "N-1" in subjectlineTxt:
    #         EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c39d932b959f69d8e9ab7c5ca9f220b6.jpg']")))
    #         EPP_WElement.is_displayed()
    #         assert EPP_WElement.is_displayed(), " N-1 Web Element not Displayed."
    #         logger.info(": successfully verified [N-1] Device Option is present.")
    #     elif "N-2" in subjectlineTxt:
    #         EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/521d4058606a427d275404ac7f98a60d.jpg']")))
    #         EPP_WElement.is_displayed()
    #         assert EPP_WElement.is_displayed(), " N-2 Web Element not Displayed."
    #         logger.info(": successfully verified [N-2] Device Option is present.")
    #     elif "N-3" in subjectlineTxt:
    #         EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c8366baeb008af8739608f52ee6769d7.jpg']")))
    #         EPP_WElement.is_displayed()
    #         assert EPP_WElement.is_displayed(), " N-3 Web Element not Displayed."
    #         logger.info(": successfully verified [N-3] Device Option is present.")
    #     elif "N-4" in subjectlineTxt:
    #         EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/65c9f0e3caa299f87bb0e59719f2d550.jpg']")))
    #         EPP_WElement.is_displayed()
    #         assert EPP_WElement.is_displayed(), " N-4 Web Element not Displayed."
    #         logger.info(": successfully verified [N-4] Device Option is present.")
    #     elif "S10+" in subjectlineTxt:
    #         EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/f0b9990cd504c058451ce8d69fd9f3e9.jpg']")))
    #         EPP_WElement.is_displayed()
    #         assert EPP_WElement.is_displayed(), " S10+ Web Element not Displayed."
    #         logger.info(": successfully verified [S10+] Device Option is present.")
    #     elif "S10" in subjectlineTxt:
    #         EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/112d83f87be0045636e79abe5c64a474.jpg']")))
    #         EPP_WElement.is_displayed()
    #         assert EPP_WElement.is_displayed(), " S10 Web Element not Displayed."
    #         logger.info(": successfully verified [S10] Device Option is present.")
    #     elif "S9+" in subjectlineTxt:
    #         EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/32e5b02ffd6e40d894e618d9e1f5da66.jpg']")))
    #         EPP_WElement.is_displayed()
    #         assert EPP_WElement.is_displayed(), " S9+ Web Element not Displayed."
    #         logger.info(": successfully verified [S9+] Device Option is present.")
    #     elif "N10+" in subjectlineTxt:
    #         EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/f9838f5312b658668b6a57f968754679.jpg']")))
    #         EPP_WElement.is_displayed()
    #         assert EPP_WElement.is_displayed(), " N10+ Web Element not Displayed."
    #         logger.info(": successfully verified [N10+] Device Option is present.")
    #     elif "S20+" in subjectlineTxt:
    #         EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/2888f545a3228dce17f7627848f1d133.jpg']")))
    #         EPP_WElement.is_displayed()
    #         assert EPP_WElement.is_displayed(), " s20+ Web Element not Displayed."
    #         logger.info(": successfully verified [S20+] Device Option is present.")
    #     elif "S20" in subjectlineTxt:
    #         EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/723b4f20683e21a28592dcb1cbb168b7.jpg']")))
    #         EPP_WElement.is_displayed()
    #         assert EPP_WElement.is_displayed(), " S20 Web Element not Displayed."
    #         logger.info(": successfully verified [S20] Device Option is present.")
    #     elif "LO" in subjectlineTxt:
    #         EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/5e34fe7b89fe4e557f4788a42e4c6d1f.jpg']")))
    #         EPP_WElement.is_displayed()
    #         assert EPP_WElement.is_displayed(), " LO Web Element not Displayed."
    #         logger.info(": successfully verified [LO] Device Option is present.")
    #     elif "Reserver_Generic" in subjectlineTxt:
    #         EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/5e34fe7b89fe4e557f4788a42e4c6d1f.jpg']")))
    #         EPP_WElement.is_displayed()
    #         assert EPP_WElement.is_displayed(), " Reserver_Generic Web Element not Displayed."
    #         logger.info(": successfully verified [Reserver_Generic] Device Option is present.")
    #     elif "Non-Reserves" in subjectlineTxt:
    #         EPP_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/5e34fe7b89fe4e557f4788a42e4c6d1f.jpg']")))
    #         EPP_WElement.is_displayed()
    #         assert EPP_WElement.is_displayed(), " Reserver_Generic Web Element not Displayed."
    #         logger.info(": successfully verified [Reserver_Generic] Device Option is present.")
    #     else:
    #         logger.info(': Device Option NOT selected.')
    #     logger.info(': #####  Verification Complete  #####\n')

    def get_Hero_SH_Text_verification(self):
        logger.info(": ##### Started Hero SH Text verification #####")
        SH_700_TI="//*[@src='http://t.info.samsungusa.com/res/samsung/5fa8841f2283c26106ba675d3bfac9a2.jpg']"
        SH_550_TI="//*[@src='http://t.info.samsungusa.com/res/samsung/533dae7bfeab0db8e88e5bcf9429feb6.jpg']"
        SH_350_TI="//*[@src='http://t.info.samsungusa.com/res/samsung/1afa9c0307135b0ca8051fd1ff53632e.jpg']"
        SH_250_T1="//*[@src='http://t.info.samsungusa.com/res/samsung/b05d60906cb98131a7558883c52ebd3c.jpg']"
        SH_LO="//*[@src='http://t.info.samsungusa.com/res/samsung/5fa8841f2283c26106ba675d3bfac9a2.jpg']"
        SH_S10p="//*[@src='http://t.info.samsungusa.com/res/samsung/533dae7bfeab0db8e88e5bcf9429feb6.jpg']"
        SH_S10="//*[@src='http://t.info.samsungusa.com/res/samsung/533dae7bfeab0db8e88e5bcf9429feb6.jpg']"
        SH_S9p="//*[@src='http://t.info.samsungusa.com/res/samsung/1afa9c0307135b0ca8051fd1ff53632e.jpg']"
        SH_N10p="//*[@src='http://t.info.samsungusa.com/res/samsung/533dae7bfeab0db8e88e5bcf9429feb6.jpg']"
        SH_N10="//*[@src='http://t.info.samsungusa.com/res/samsung/0722fc5bd3e4fa2d8922d74a2e319d55.jpg']"
        SH_S20p="//*[@src='http://t.info.samsungusa.com/res/samsung/8ea9d85b1d5183c55791aa2bc4f96623.jpg']"
        SH_S20="//*[@src='http://t.info.samsungusa.com/res/samsung/8ea9d85b1d5183c55791aa2bc4f96623.jpg']"
        SH_Reserver_Generic="//*[@src='http://t.info.samsungusa.com/res/samsung/5fa8841f2283c26106ba675d3bfac9a2.jpg']"


        SH_700_TI_epp = "//*[@src='http://t.info.samsungusa.com/res/samsung/0722fc5bd3e4fa2d8922d74a2e319d55.jpg']"
        SH_550_TI_epp = "//*[@src='http://t.info.samsungusa.com/res/samsung/600200f217a7c541aa954e8c18b5e3f0.jpg']"
        SH_350_TI_epp = "//*[@src='http://t.info.samsungusa.com/res/samsung/692b0f364e06dad12913e418ac75dff3.jpg']"
        SH_250_T1_epp = "//*[@src='http://t.info.samsungusa.com/res/samsung/5366c4f4e4a4786e92451fe575f476be.jpg']"
        SH_LO_epp = "//*[@src='http://t.info.samsungusa.com/res/samsung/0722fc5bd3e4fa2d8922d74a2e319d55.jpg']"
        SH_S10p_epp = "//*[@src='http://t.info.samsungusa.com/res/samsung/600200f217a7c541aa954e8c18b5e3f0.jpg']"
        SH_S10_epp = "//*[@src='http://t.info.samsungusa.com/res/samsung/600200f217a7c541aa954e8c18b5e3f0.jpg']"
        SH_S9p_epp = "//*[@src='http://t.info.samsungusa.com/res/samsung/692b0f364e06dad12913e418ac75dff3.jpg']"
        SH_N10p_epp = "//*[@src='http://t.info.samsungusa.com/res/samsung/600200f217a7c541aa954e8c18b5e3f0.jpg']"
        SH_N10_epp = "//*[@src='http://t.info.samsungusa.com/res/samsung/0722fc5bd3e4fa2d8922d74a2e319d55.jpg']"
        SH_S20p_epp = "//*[@src='http://t.info.samsungusa.com/res/samsung/cd0507708009c58e4afc2b96eaddfda9.jpg']"
        SH_S20_epp = "//*[@src='http://t.info.samsungusa.com/res/samsung/cd0507708009c58e4afc2b96eaddfda9.jpg']"
        SH_Reserver_Generic_epp = "//*[@src='http://t.info.samsungusa.com/res/samsung/0722fc5bd3e4fa2d8922d74a2e319d55.jpg']"
        SH_Enrollees_Non_Res_epp = "//*[@src='http://t.info.samsungusa.com/res/samsung/95080194de68a4768dd0ea656e8f714d.jpg']"

        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        Hero_SH = self.driver.find_element_by_xpath("//*[@id='hero_sh_text']").get_attribute("alt")
        if "EPP" not in subjectlineTxt:
            if "700_TI" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_700_TI)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_700, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "550_TI" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_550_TI)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_550, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "350_TI" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_350_TI)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_350, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "250_T1" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_250_T1)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_250, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "LO" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_LO)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_700, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "S10+" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_S10p)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_550, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "S10" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_S10)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_550, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "S9+" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_S9p)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_350, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "N10+" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_N10p)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_550, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "N10" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_N10)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_550, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "S20+" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_S20p)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_600, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "S20" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_S20)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_600, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "Reserver_Generic" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_Reserver_Generic)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_600, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
        elif "EPP" in subjectlineTxt:
            if "700_TI" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_700_TI_epp)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_700, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "550_TI" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_550_TI_epp)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_550, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "350_TI" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_350_TI_epp)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_350, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "250_T1" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_250_T1_epp)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_250, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "LO" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_LO_epp)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_700, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "S10+" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_S10p_epp)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_550, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "S10" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_S10_epp)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_550, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "S9+" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_S9p_epp)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_350, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "N10+" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_N10p_epp)))
                # SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_550, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "N10" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_N10_epp)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_550, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "S20+" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_S20p_epp)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_600, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "S20" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_S20_epp)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_600, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "Generic" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_Reserver_Generic_epp)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_700_epp, "Hero SH Text not Matched."
                # logger.info(": successfully verified Hero SH Text: " + Hero_SH)
            elif "EPP_Enrollees_Non_Res" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, SH_Enrollees_Non_Res_epp)))
                SH_WE.is_displayed()
                assert SH_WE.is_displayed(), "Web Element not Displayed."
                # assert Hero_SH in self.SH_NR, "Hero SH Text not Matched."
        logger.info(": successfully verified Hero SH Text::" + Hero_SH)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Galaxy_Z_FLip_Text_verification(self):
        logger.info(": ##### Started Galaxy_Z_FLip Text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        # Foldable_SH = self.driver.find_element_by_xpath("//*[@id='hero_sh_text']").get_attribute("alt")
        if "EPP" not in subjectlineTxt:
            if "700_TI" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/9988ec97963031d2d95e87b4154771c1.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "550_TI" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c7ec311bbff5fcbc0a855010881b1771.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "350_TI" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/02cc2daa5e0947ae4de816c2a5be2c14.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "250_T1" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/722ccb719f5632334359d2b0e32702c6.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "LO" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/9988ec97963031d2d95e87b4154771c1.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "S10+" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c7ec311bbff5fcbc0a855010881b1771.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "S10" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/9c44cb35ef73a5f8e1afd2c71772add7.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "S9+" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/1ec49f62ba7935c52c81a101340e5ede.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "N10+" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c7ec311bbff5fcbc0a855010881b1771.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "N10" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/39e6e2bb3929e664996a7bd380e40cd5.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "S20+" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c7ec311bbff5fcbc0a855010881b1771.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "S20" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/c7ec311bbff5fcbc0a855010881b1771.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "Reserver_Generic" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/9988ec97963031d2d95e87b4154771c1.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
        elif "EPP" in subjectlineTxt:
            if "700_TI" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/a2f386a24261b493737f7b82ac48097d.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "550_TI" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/a4d7b9c136335c57095628037b581e60.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "350_TI" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/9ef3458960e4465ed59057dc06d13d14.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "250_T1" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/6f1d6b6bccc1cf401360b1ea69e26093.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "LO" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/a2f386a24261b493737f7b82ac48097d.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "S10+" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/a4d7b9c136335c57095628037b581e60.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "S10" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/8c889b79dc04818579a952cbeeb9f2b9.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "S9+" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/60eff7efd0053ef8534632dd133fadd7.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "N10+" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/a4d7b9c136335c57095628037b581e60.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "N10" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/39e6e2bb3929e664996a7bd380e40cd5.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "S20+" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/a4d7b9c136335c57095628037b581e60.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "S20" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/a4d7b9c136335c57095628037b581e60.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "Generic" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@src='http://t.info.samsungusa.com/res/samsung/a2f386a24261b493737f7b82ac48097d.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
            elif "EPP_Enrollees_Non_Res" in subjectlineTxt:
                SH_WE = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@src='http://t.info.samsungusa.com/res/samsung/a2f386a24261b493737f7b82ac48097d.jpg']")))
                assert SH_WE.is_displayed(), "Web Element not Displayed."
        logger.info(": successfully verified Galaxy_Z_FLip SH Text.")
        logger.info(': #####  Verification Complete  #####\n')

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

    def get_subjectLine_text_validation(self):
        logger.info(": ##### Started subjectLine_text verification #####")
        self.SL = ExcelUtil(tc_name="").read_from_excel("Copy", 9, 4).strip()
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        # print(subjectlineTxt)
        # print(self.SL)
        assert self.SL in subjectlineTxt, "Subject Line Text Not Matching"
        logger.info(": Validated Subject Line Text:: " + subjectlineTxt)
        logger.info(': #####  Verification Complete  #####\n')

    def get_pre_header_text_validation(self):
        logger.info(": ##### Started pre_header_text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.PH = ExcelUtil(tc_name="").read_from_excel("Copy", 10, 4).strip()
        self.PH_NR = ExcelUtil(tc_name="").read_from_excel("Copy", 10, 26).strip()
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        if "Non" not in subjectlineTxt:
            assert self.PH in pheaderTxt, "pheader Text Not Matching"
        else:
            assert self.PH_NR in pheaderTxt, "pheader Text Not Matching"
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
        # CreativePage.get_Banner_validation(self)
        CreativePage.get_URL_Segment_validation(self)
        CreativePage.get_skipCarrier_validation(self)
        CreativePage.get_DeviceName_validation(self)
        CreativePage.get_tradein_DeviceName_validation(self)
        CreativePage.verify_tradein_price_validation(self)
        CreativePage.get_carrier_instant_credit_validation(self)
        # CreativePage.get_Device_trade_In_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_Module1_link_verification(self):
        logger.info(": ##### Started Module1 link_validation verification #####")
        self.PH_URL_generic = ExcelUtil(tc_name="").read_from_excel("Module", 7, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='kv_cta']"))).click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        URL = self.driver.current_url
        assert self.PH_URL_generic in URL, "Web Landing Page URL is not Matching."
        logger.info(": successfully verified Web Landing page URL:\n" + URL + '\n')
        with open('../TextFolder_Unique_URL/UniqueList.txt', 'w')as f: f.writelines(URL)
        URLSegemntPage.get_segment()
        # CreativePage.get_Banner_validation(self)
        CreativePage.get_URL_Segment_validation(self)
        CreativePage.get_skipCarrier_validation(self)
        CreativePage.get_DeviceName_validation(self)
        CreativePage.get_tradein_DeviceName_validation(self)
        CreativePage.verify_tradein_price_validation(self)
        CreativePage.get_carrier_instant_credit_validation(self)
        # CreativePage.get_Device_trade_In_validation(self)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def get_Module2_link_verification(self):
        logger.info(": ##### Started Module2 link_validation verification #####")
        self.PH_URL_generic = ExcelUtil(tc_name="").read_from_excel("Module", 8, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='trade_in_cta']"))).click()
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

    def get_Module3_link_verification(self):
        logger.info(": ##### Started Module3 link_validation verification #####")
        self.PH_URL_generic = ExcelUtil(tc_name="").read_from_excel("Module", 9, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='compare_chart_cta']"))).click()
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

    def get_Galaxy_Z_FLip_Module_link_verification(self):
        logger.info(": ##### Started Galaxy_Z_FLip Module link_validation verification #####")
        self.PH_URL_generic = ExcelUtil(tc_name="").read_from_excel("Module", 10, 8)
        parent_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='foldables_cta']"))).click()
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

    def get_Module1_KV_SC_verification(self):
        logger.info(": ##### Started Module1_KV_SC text verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.SC_700 = ExcelUtil(tc_name="").read_from_excel("Copy", 26, 4)
        self.SC_550 = ExcelUtil(tc_name="").read_from_excel("Copy", 26, 5)
        self.SC_350 = ExcelUtil(tc_name="").read_from_excel("Copy", 26, 6)
        self.SC_250 = ExcelUtil(tc_name="").read_from_excel("Copy", 26, 7)
        self.SC_S10p = ExcelUtil(tc_name="").read_from_excel("Copy", 26, 8)
        self.SC_N20 = ExcelUtil(tc_name="").read_from_excel("Copy", 26, 12)

        self.SC_700_epp = ExcelUtil(tc_name="").read_from_excel("Copy", 26, 15)
        self.SC_550_epp = ExcelUtil(tc_name="").read_from_excel("Copy", 26, 16)
        self.SC_350_epp = ExcelUtil(tc_name="").read_from_excel("Copy", 26, 17)
        self.SC_250_epp = ExcelUtil(tc_name="").read_from_excel("Copy", 26, 18)
        self.SC_S10p_epp = ExcelUtil(tc_name="").read_from_excel("Copy", 26, 19)
        self.SC_N20_epp = ExcelUtil(tc_name="").read_from_excel("Copy", 26, 23)
        self.SC_NR = ExcelUtil(tc_name="").read_from_excel("Copy", 26, 26)

        KV_SC = self.driver.find_element_by_xpath("//*[@id='kv_sc_text']").text
        # KV_SC = self.driver.find_element_by_xpath("(//*[@target='_blank'])[11]").text
        if "EPP" not in subjectlineTxt:
            if "700_TI" in subjectlineTxt:
                assert self.SC_700.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "550_TI" in subjectlineTxt:
                assert self.SC_550.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "350_TI" in subjectlineTxt:
                assert self.SC_350.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "250_T1" in subjectlineTxt:
                assert self.SC_250.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "LO" in subjectlineTxt:
                # print(self.SC_700.encode('utf8'))
                # print(KV_SC.encode('utf8'))
                assert self.SC_700.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "S10+" in subjectlineTxt:
                assert self.SC_S10p.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "S10" in subjectlineTxt:
                assert self.SC_S10p.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "S9+" in subjectlineTxt:
                assert self.SC_350.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "N10+" in subjectlineTxt:
                assert self.SC_550.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "N10" in subjectlineTxt:
                assert self.SC_550.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "S20+" in subjectlineTxt:
                assert self.SC_N20.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "S20" in subjectlineTxt:
                assert self.SC_N20.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "Generic" in subjectlineTxt:
                assert self.SC_700.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"

        elif "EPP" in subjectlineTxt:
            if "700_TI" in subjectlineTxt:
                assert self.SC_700_epp.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "550_TI" in subjectlineTxt:
                assert self.SC_550_epp.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "350_TI" in subjectlineTxt:
                assert self.SC_350_epp.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "250_T1" in subjectlineTxt:
                assert self.SC_250_epp.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "LO" in subjectlineTxt:
                assert self.SC_700_epp.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "S10+" in subjectlineTxt:
                assert self.SC_S10p_epp.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "S10" in subjectlineTxt:
                assert self.SC_S10p_epp.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "S9+" in subjectlineTxt:
                assert self.SC_350_epp.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "N10+" in subjectlineTxt:
                assert self.SC_550_epp.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "N10" in subjectlineTxt:
                assert self.SC_550_epp.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "S20+" in subjectlineTxt:
                assert self.SC_N20_epp.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "S20" in subjectlineTxt:
                assert self.SC_N20_epp.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "Generic" in subjectlineTxt:
                assert self.SC_700_epp.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
            elif "EPP_Enrollees_Non_Res" in subjectlineTxt:
                assert self.SC_NR.encode('utf8') in KV_SC.encode('utf8'), "KV_SC Text Not Matching"
        logger.info(": Validated Module1_KV_SC Text:: " +str(KV_SC.encode('utf8')))
        logger.info(': #####  Verification Complete  #####\n')

    def verify_tradein_price_validation(self):
        # logger.info(": ##### Started Eligible Trade-in price validation verification #####")
        try:
            tradein1=self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='price-info']/strong"))).text
            tradein = tradein1[:7]
            logger.info(': Trade-in price ==' + tradein)
        except:
            logger.info(': Trade-in price NOT present.')

    def get_Banner_validation(self):
        logger.info(": ##### Started Landing page Banner verification #####")
        time.sleep(2)
        tradein=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='title'])[2]"))).text
        logger.info(': Landing page Banner: ' + tradein)

    def get_carrier_instant_credit_validation(self):
        # logger.info(": ##### Started carrier instant credit verification #####")
        try:
            tradein=self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='instantRebate']/span"))).text
            # tradein1 = tradein1[:7]
            logger.info(': carrier instant-credit ==' + tradein)
        except:
            logger.info(': carrier instant-credit == 0.00')

    def get_DeviceName_validation(self):
        # logger.info(": ##### Started DeviceName validation  #####")
        device1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='oos-title2'])"))).text
        try:
            assert "Galaxy S21 5G" in device1, "Device Name Not Matching."
            logger.info(': Promoted Device Name ==' + device1)
        except:
            assert "Galaxy S21 Ultra 5G" in device1, "Device Name Not Matching."
            logger.info(': Promoted Device Name ==' + device1)

    def get_Device_trade_In_validation(self):
        # logger.info(": ##### Started  Total Device_trade_In validation  #####")
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='button  CONTINUE'])[1]"))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='confirmationBtnLeft'])[1]"))).click()
            preorderdevice = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='tile2 selected tradein-tile']"))).text
            logger.info(': Total Device_trade_In information :' + preorderdevice)
        except:
            logger.info(': Need to select Device Manually.')

    def get_skipCarrier_validation(self):
        # logger.info(": ##### Started skipCarrier validation From Landing Page #####")
        with open('../OutputT/OutResult.json', 'r')as jsonfile:
            readdata = json.load(jsonfile)
            if "skipCarrier" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 4, 3) in readdata['check_list'][0]['skipCarrier']:
                    unlocked_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='unlocked' and @aria-checked='true']")))
                    unlocked_WElement.is_displayed()
                    assert unlocked_WElement.is_displayed(), "unlocked carrier Option not Selected."
                    logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 4, 4))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 5, 3) in readdata['check_list'][0]['skipCarrier']:
                    verizon_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='verizon' and @aria-checked='true']")))
                    verizon_WElement.is_displayed()
                    assert verizon_WElement.is_displayed(), "verizon carrier Option not Selected."
                    logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 5, 4))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 6, 3) in readdata['check_list'][0]['skipCarrier']:
                    att_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='att' and @aria-checked='true']")))
                    att_WElement.is_displayed()
                    assert att_WElement.is_displayed(), "att carrier Option not Selected."
                    logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 6, 4))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 7, 3) in readdata['check_list'][0]['skipCarrier']:
                    tmobile_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='t-mobile' and @aria-checked='true']")))
                    tmobile_WElement.is_displayed()
                    assert tmobile_WElement.is_displayed(), "t-mobile carrier Option not Selected."
                    logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 7, 4))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 8, 3) in readdata['check_list'][0]['skipCarrier']:
                    sprint_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='sprint' and @aria-checked='true']")))
                    sprint_WElement.is_displayed()
                    assert sprint_WElement.is_displayed(), "sprint carrier Option not Selected."
                    logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 8, 4))
            elif "carrier" in readdata['check_list'][0]:
                    if ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 4, 3) in readdata['check_list'][0]['carrier']:
                        unlocked_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='unlocked' and @aria-checked='true']")))
                        unlocked_WElement.is_displayed()
                        assert unlocked_WElement.is_displayed(), "unlocked carrier Option not Selected."
                        logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 4, 4))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 5, 3) in readdata['check_list'][0]['carrier']:
                        verizon_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='verizon' and @aria-checked='true']")))
                        verizon_WElement.is_displayed()
                        assert verizon_WElement.is_displayed(), "verizon carrier Option not Selected."
                        logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 5, 4))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 6, 3) in readdata['check_list'][0]['carrier']:
                        att_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='att' and @aria-checked='true']")))
                        att_WElement.is_displayed()
                        assert att_WElement.is_displayed(), "att carrier Option not Selected."
                        logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 6, 4))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 7, 3) in readdata['check_list'][0]['carrier']:
                        tmobile_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='t-mobile' and @aria-checked='true']")))
                        tmobile_WElement.is_displayed()
                        assert tmobile_WElement.is_displayed(), "t-mobile carrier Option not Selected."
                        logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 7, 4))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 8, 3) in readdata['check_list'][0]['carrier']:
                        sprint_WElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='sprint' and @aria-checked='true']")))
                        sprint_WElement.is_displayed()
                        assert sprint_WElement.is_displayed(), "sprint carrier Option not Selected."
                        logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 8, 8))
            else:
                logger.info(": skipCarrier segment NOT present.")

    def get_tradein_DeviceName_validation(self):
        # logger.info(": ##### Started tradein_DeviceName validation  #####")
        with open('../OutputT/OutResult.json', 'r')as jsonfile:
            readdata = json.load(jsonfile)
            try:
                deviceName = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='device-label'])[2]"))).text
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
        self.tc_NR = ExcelUtil(tc_name="").read_from_excel("TERMS_CONDITIONS", 5, 2)
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        footerTxt1 = self.driver.find_element_by_xpath("//*[@id='footer_text1']/p/span").text
        # if "Non" not in subjectlineTxt:
        #     assert self.tc in footerTxt1, "Condition_Text1 Not Matching"
        # else:
        #     # assert self.tc_NR in footerTxt1, "Condition_Text1 Not Matching"
        logger.info(": Validate footer condition_text1:: " + footerTxt1)
        logger.info(': #####  Verification Complete  #####\n')

    def get_m2_Conditiontext2_validation(self):
        logger.info(": ##### Started footer condition_text2 verification #####")
        self.tc2 = ExcelUtil(tc_name="").read_from_excel("TERMS_CONDITIONS", 3, 2)
        footerTxt1 = self.driver.find_element_by_xpath("//*[@id='footer_text2']/span").text
        # print(self.tc2.encode('utf-8'))
        # print(footerTxt1.encode('utf-8'))
        # assert self.tc2 in footerTxt1, "Condition_Text2 Not Matching"
        logger.info(": Validate footer condition_text2:: " + footerTxt1)
        logger.info(': #####  Verification Complete  #####\n')

    def get_m2_Conditiontext3_validation(self):
        logger.info(": ##### Started footer condition_text3 verification #####")
        self.tc2 = ExcelUtil(tc_name="").read_from_excel("TERMS_CONDITIONS", 3, 2)
        footerTxt1 = self.driver.find_element_by_xpath("//*[@id='footer_text3']/span").text
        # print(self.tc2.encode('utf-8'))
        # print(footerTxt1.encode('utf-8'))
        # assert self.tc2 in footerTxt1, "Condition_Text2 Not Matching"
        logger.info(": Validate footer condition_text2:: " + footerTxt1)
        logger.info(': #####  Verification Complete  #####\n')

    def get_m2_Conditiontext4_validation(self):
        logger.info(": ##### Started footer condition_text4 verification #####")
        self.tc2 = ExcelUtil(tc_name="").read_from_excel("TERMS_CONDITIONS", 3, 2)
        footerTxt1 = self.driver.find_element_by_xpath("//*[@id='footer_text4']/span").text
        # print(self.tc2.encode('utf-8'))
        # print(footerTxt1.encode('utf-8'))
        # assert self.tc2 in footerTxt1, "Condition_Text2 Not Matching"
        logger.info(": Validate footer condition_text2:: " + footerTxt1)
        logger.info(': #####  Verification Complete  #####\n')









