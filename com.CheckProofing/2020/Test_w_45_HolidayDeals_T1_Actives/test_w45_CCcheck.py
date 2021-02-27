import time
import unittest
import sys
import os
import logging
import warnings
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



from PageClass.UrlSegmentPage import URLSegemntPage

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from PageClass.ComputingPage import ComputingPage
from PageClass.MobileAccessoriesPage import MobileAccessoriesPage
from PageClass.TVHomeTheaterPage import TVHomeTheaterPage
from PageClass.SmartPhonePage import SmartPhonePage
from PageClass.HomeAppliancePage import HomeAppliancePage
from PageClass.TabletPage import TabletPage
from Utility_Files import ReadConfig
from Utility_Files.HTMLTestRunner import stdout_redirector
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class HTMLPage_W_45_CCTest(unittest.TestCase):
    method1=""
    driver = None
    url_list = []
    method_list_in_Url = []

    @classmethod
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver1'), options=option)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        self.wait = WebDriverWait(self.driver, 10)


    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_Proofs(self):
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            urls = f.read().splitlines()
            for url in urls:
                if url != 0:
                    if "DD" in url:
                        print("Select DD")
                        self.driver.get(url)
                        MB_smartphone=SmartPhonePage(self.driver)
                        MB_smartphone.get_SMARTPHONE_ShopAll()
                        # MB_smartphone.get_Module1_link()
                    elif "CC" in url:
                        self.driver.get(url)
                        if "MB" in url:
                            print("Select CC")
                            MB_smartphone=SmartPhonePage(self.driver)
                            MB_smartphone.get_SMARTPHONE_ShopAll()
                            MB_smartphone.get_Module4_link()
                        if "HA" in url:
                            print("Select HA")
                            HA_homeappliance=HomeAppliancePage(self.driver)
                            HA_homeappliance.get_HomeAppliance_ShopAll()
                            HA_homeappliance.get_Module4_link()
                        if "MB_TABLET" in url:
                            print("Select MB_TABLET")
                            MB_tablet = TabletPage(self.driver)
                            MB_tablet.get_Tablet_ShopAll()
                            MB_tablet.get_Module1_link()
                        if "TV" in url:
                            print("Select TV")
                            TV_HomeTheater=TVHomeTheaterPage(self.driver)
                            TV_HomeTheater.get_TVHomeTheater_ShopAll()
                            TV_HomeTheater.get_Module4_link()
                        if "MB_WEAR" in url:
                            print("Select MB_WEAR")
                            MB_Wear=MobileAccessoriesPage(self.driver)
                            MB_Wear.get_MobileAccessories_ShopAll()
                            MB_Wear.get_Module4_link()
                        if "CE_COMPUTER" in url:
                            print("Select CE_COMPUTER")
                            CE_Computer=ComputingPage(self.driver)
                            CE_Computer.get_Computing_ShopAll()
                            CE_Computer.get_Module4_link()
                        else:
                            print("Not able to RUN")

    # def test_computing(self):
    #     with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
    #         urls = f.read().splitlines()
    #         for url in urls:
    #             if url != 0:
    #                 if "CC" in url:
    #                     self.driver.get(url)
    #                     if "CE_COMPUTER" in url:
    #                         print("Select CE_COMPUTER")
    #                         # self.driver.get(url)
    #                         CE_Computer=ComputingPage(self.driver)
    #                         CE_Computer.get_Computing_ShopAll()
    #                         CE_Computer.get_Module4_link()


if __name__ == '__main__':
    unittest.main()