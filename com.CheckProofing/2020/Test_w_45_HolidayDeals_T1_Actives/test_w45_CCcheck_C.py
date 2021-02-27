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


class HTMLPage_W_45_CC_C_Test(unittest.TestCase):
    urls=""
    driver = None
    url_list = []
    method_list_in_Url = []


    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver1'), options=option)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        self.wait = WebDriverWait(self.driver, 10)
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            self.urls = f.read().splitlines()


    def tearDown(self):
        self.driver.quit()

    # def test_ShopAllProofs(self):
    #     with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
    #         urls = f.read().splitlines()
    #         for url in urls:
    #             if url != 0:
    #                 if "DD" in url:
    #                     print("Select DD")
    #                     # self.driver.get(url)
    #                     # MB_smartphone=SmartPhonePage(self.driver)
    #                     # MB_smartphone.get_SMARTPHONE_ShopAll()
    #                     # # MB_smartphone.get_Module1_link()
    #                 elif "CC" in url:
    #                     self.driver.get(url)
    #                     if "MB" in url:
    #                         print("Select CC URL:" + url)
    #                         MB_smartphone=SmartPhonePage(self.driver)
    #                         MB_smartphone.get_SMARTPHONE_ShopAll()
    #                         # MB_smartphone.get_Module4_link()
    #                     if "HA" in url:
    #                         print("Select HA URL:" + url)
    #                         HA_homeappliance=HomeAppliancePage(self.driver)
    #                         HA_homeappliance.get_HomeAppliance_ShopAll()
    #                         # HA_homeappliance.get_Module4_link()
    #                     if "MB_TABLET" in url:
    #                         print("Select MB_TABLET URL:" + url)
    #                         MB_tablet = TabletPage(self.driver)
    #                         MB_tablet.get_Tablet_ShopAll()
    #                         # MB_tablet.get_Module1_link()
    #                     if "TV" in url:
    #                         print("Select TV URL:" + url)
    #                         TV_HomeTheater=TVHomeTheaterPage(self.driver)
    #                         TV_HomeTheater.get_TVHomeTheater_ShopAll()
    #                         # TV_HomeTheater.get_Module4_link()
    #                     if "MB_WEAR" in url:
    #                         print("Select MB_WEAR URL:" + url)
    #                         MB_Wear=MobileAccessoriesPage(self.driver)
    #                         MB_Wear.get_MobileAccessories_ShopAll()
    #                         # MB_Wear.get_Module4_link()
    #                     if "CE_COMPUTER" in url:
    #                         print("Select CE_COMPUTER URL:" + url)
    #                         CE_Computer=ComputingPage(self.driver)
    #                         CE_Computer.get_Computing_ShopAll()
    #                         # CE_Computer.get_Module4_link()
    #                     else:
    #                         print("Not able to RUN")


    # def test_Module1Proofs(self):
    #     with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
    #         urls = f.read().splitlines()
    #         for url in urls:
    #             if url != 0:
    #                 if "DD" in url:
    #                     print("Select DD")
    #                     # self.driver.get(url)
    #                     # MB_smartphone=SmartPhonePage(self.driver)
    #                     # # MB_smartphone.get_SMARTPHONE_ShopAll()
    #                     # MB_smartphone.get_Module1_link()
    #                 elif "CC" in url:
    #                     self.driver.get(url)
    #                     if "MB" in url:
    #                         print("Select URL:" + url)
    #                         MB_smartphone=SmartPhonePage(self.driver)
    #                         # MB_smartphone.get_SMARTPHONE_ShopAll()
    #                         MB_smartphone.get_Module4_link()
    #                     if "HA" in url:
    #                         print("Select HA")
    #                         HA_homeappliance=HomeAppliancePage(self.driver)
    #                         # HA_homeappliance.get_HomeAppliance_ShopAll()
    #                         HA_homeappliance.get_Module4_link()
    #                     if "MB_TABLET" in url:
    #                         print("Select MB_TABLET")
    #                         MB_tablet = TabletPage(self.driver)
    #                         MB_tablet.get_Tablet_ShopAll()
    #                         MB_tablet.get_Module1_link()
    #                     if "TV" in url:
    #                         print("Select TV")
    #                         TV_HomeTheater=TVHomeTheaterPage(self.driver)
    #                         # TV_HomeTheater.get_TVHomeTheater_ShopAll()
    #                         TV_HomeTheater.get_Module4_link()
    #                     if "MB_WEAR" in url:
    #                         print("Select MB_WEAR")
    #                         MB_Wear=MobileAccessoriesPage(self.driver)
    #                         # MB_Wear.get_MobileAccessories_ShopAll()
    #                         MB_Wear.get_Module4_link()
    #                     if "CE_COMPUTER" in url:
    #                         print("Select CE_COMPUTER")
    #                         CE_Computer=ComputingPage(self.driver)
    #                         # CE_Computer.get_Computing_ShopAll()
    #                         CE_Computer.get_Module4_link()
    #                     else:
    #                         print("Not able to RUN")

    # def test_Module1Proofs(self):
    #     with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
    #         urls = f.read().splitlines()
    #         for url in urls:
    #             if url != 0:
    #                 try:
    #                     if "CC" in url:
    #                         # self.driver.get(url)
    #                         if "MB" in url:
    #                             try:
    #                                 if "MB_FOLD" in url:
    #                                     self.driver.get(url)
    #                                     print("Select MB_FOLD URL:" + url)
    #                                     MB_smartphone=SmartPhonePage(self.driver)
    #                                     MB_smartphone.get_SMARTPHONE_ShopAll()
    #                                     MB_smartphone.get_MB_FOLD_Module()
    #                                 if "MB_NOTE" in url:
    #                                     self.driver.get(url)
    #                                     print("Select MB_NOTE URL:" + url)
    #                                     MB_smartphone=SmartPhonePage(self.driver)
    #                                     MB_smartphone.get_SMARTPHONE_ShopAll()
    #                                     MB_smartphone.get_MB_NOTE_Module()
    #                                 if "MB_GALAXY" in url:
    #                                     self.driver.get(url)
    #                                     print("Select MB_GALAXY URL:" + url)
    #                                     MB_smartphone=SmartPhonePage(self.driver)
    #                                     MB_smartphone.get_SMARTPHONE_ShopAll()
    #                                     MB_smartphone.get_MB_GALAXY_Module()
    #                                 if "MB_WEAR" in url:
    #                                     self.driver.get(url)
    #                                     print("Select MB_WEAR URL:" + url)
    #                                     MB_Wear=MobileAccessoriesPage(self.driver)
    #                                     MB_Wear.get_MobileAccessories_ShopAll()
    #                                     MB_Wear.get_MB_WEAR_Module()
    #                                 if "MB_TABLET" in url:
    #                                     self.driver.get(url)
    #                                     print("Select MB_TABLET URL:" + url)
    #                                     MB_tablet = TabletPage(self.driver)
    #                                     MB_tablet.get_Tablet_ShopAll()
    #                                     MB_tablet.get_MB_TABLET_Module()
    #                             except:
    #                                 print("MB option is NOT selected.")
    #
    #                         if "HA" in url:
    #                             try:
    #                                 if "HA_LAUNDRY" in url:
    #                                     self.driver.get(url)
    #                                     print("Select HA_LAUNDRY URL:" + url)
    #                                     HA_homeappliance=HomeAppliancePage(self.driver)
    #                                     HA_homeappliance.get_HomeAppliance_ShopAll()
    #                                     HA_homeappliance.get_HA_LAUNDRY_Module()
    #                                 if "HA_KITCHEN" in url:
    #                                     self.driver.get(url)
    #                                     print("Select HA_KITCHEN URL:" + url)
    #                                     HA_homeappliance=HomeAppliancePage(self.driver)
    #                                     HA_homeappliance.get_HomeAppliance_ShopAll()
    #                                     HA_homeappliance.get_HA_KITCHEN_Module()
    #                                 if "HA_CLEANER" in url:
    #                                     self.driver.get(url)
    #                                     print("Select HA_CLEANER URL:" + url)
    #                                     HA_homeappliance=HomeAppliancePage(self.driver)
    #                                     HA_homeappliance.get_HomeAppliance_ShopAll()
    #                                     HA_homeappliance.get_HA_CLEANER_Module()
    #                             except:
    #                                 print("HA option is NOT selected.")
    #
    #                         if "TV" in url:
    #                             try:
    #
    #                                 if "TV_UHD" in url:
    #                                     self.driver.get(url)
    #                                     print("Select TV_UHD URL:" + url)
    #                                     TV_HomeTheater=TVHomeTheaterPage(self.driver)
    #                                     TV_HomeTheater.get_TVHomeTheater_ShopAll()
    #                                     TV_HomeTheater.get_TV_UHD_Module()
    #                                 if "TV_QLED" in url:
    #                                     self.driver.get(url)
    #                                     print("Select TV_QLED URL:" + url)
    #                                     TV_HomeTheater=TVHomeTheaterPage(self.driver)
    #                                     TV_HomeTheater.get_TVHomeTheater_ShopAll()
    #                                     TV_HomeTheater.get_TV_QLED_Module()
    #                                 if "TV_ACCESSORY" in url:
    #                                     self.driver.get(url)
    #                                     print("Select TV_ACCESSORY URL:" + url)
    #                                     TV_HomeTheater=TVHomeTheaterPage(self.driver)
    #                                     TV_HomeTheater.get_TVHomeTheater_ShopAll()
    #                                     TV_HomeTheater.get_TV_ACCESSORY_Module()
    #                                 if "TV_FRAME" in url:
    #                                     self.driver.get(url)
    #                                     print("Select TV_FRAME URL:" + url)
    #                                     TV_HomeTheater=TVHomeTheaterPage(self.driver)
    #                                     TV_HomeTheater.get_TVHomeTheater_ShopAll()
    #                                     TV_HomeTheater.get_TV_FRAME_Module()
    #                             except:
    #                                 print("TV option is NOT selected.")
    #
    #                         if "CE_COMPUTER" in url:
    #                             try:
    #                                 if "CE_COMPUTER" in url:
    #                                     self.driver.get(url)
    #                                     print("Select CE_COMPUTER URL:" + url)
    #                                     CE_Computer=ComputingPage(self.driver)
    #                                     CE_Computer.get_Computing_ShopAll()
    #                                     CE_Computer.get_CE_COMPUTER_Module()
    #                             except:
    #                                 print("CE option is NOT selected.")
    #                 except:
    #                     raise ("CC option NOT selected.")

#     def test_Module2Proofs(self):
#
#             for url in self.urls:
#                 if url != 0:
#                     try:
#                         if "CC" in url:
#                             # self.driver.get(url)
#                             if "MB" in url:
#                                 try:
#                                     if "MB_FOLD" in url:
#                                         self.driver.get(url)
#                                         print("Select MB_FOLD URL:" + url)
#                                         MB_smartphone=SmartPhonePage(self.driver)
#                                         MB_smartphone.get_SMARTPHONE_ShopAll()
#                                         MB_smartphone.get_MB_FOLD_Module()
#                                     if "MB_NOTE" in url:
#                                         self.driver.get(url)
#                                         print("Select MB_NOTE URL:" + url)
#                                         MB_smartphone=SmartPhonePage(self.driver)
#                                         MB_smartphone.get_SMARTPHONE_ShopAll()
#                                         MB_smartphone.get_MB_NOTE_Module()
#                                     if "MB_GALAXY" in url:
#                                         self.driver.get(url)
#                                         print("Select MB_GALAXY URL:" + url)
#                                         MB_smartphone=SmartPhonePage(self.driver)
#                                         MB_smartphone.get_SMARTPHONE_ShopAll()
#                                         MB_smartphone.get_MB_GALAXY_Module()
#                                     if "MB_WEAR" in url:
#                                         self.driver.get(url)
#                                         print("Select MB_WEAR URL:" + url)
#                                         MB_Wear=MobileAccessoriesPage(self.driver)
#                                         MB_Wear.get_MobileAccessories_ShopAll()
#                                         MB_Wear.get_MB_WEAR_Module()
#                                     if "MB_TABLET" in url:
#                                         self.driver.get(url)
#                                         print("Select MB_TABLET URL:" + url)
#                                         MB_tablet = TabletPage(self.driver)
#                                         MB_tablet.get_Tablet_ShopAll()
#                                         MB_tablet.get_MB_TABLET_Module()
#                                 except:
#                                     print("MB option is NOT selected.")
#
#                             if "HA" in url:
#                                 try:
#                                     if "HA_LAUNDRY" in url:
#                                         self.driver.get(url)
#                                         print("Select HA_LAUNDRY URL:" + url)
#                                         HA_homeappliance=HomeAppliancePage(self.driver)
#                                         HA_homeappliance.get_HomeAppliance_ShopAll()
#                                         HA_homeappliance.get_HA_LAUNDRY_Module()
#                                     if "HA_KITCHEN" in url:
#                                         self.driver.get(url)
#                                         print("Select HA_KITCHEN URL:" + url)
#                                         HA_homeappliance=HomeAppliancePage(self.driver)
#                                         HA_homeappliance.get_HomeAppliance_ShopAll()
#                                         HA_homeappliance.get_HA_KITCHEN_Module()
#                                     if "HA_CLEANER" in url:
#                                         self.driver.get(url)
#                                         print("Select HA_CLEANER URL:" + url)
#                                         HA_homeappliance=HomeAppliancePage(self.driver)
#                                         HA_homeappliance.get_HomeAppliance_ShopAll()
#                                         HA_homeappliance.get_HA_CLEANER_Module()
#                                 except:
#                                     print("HA option is NOT selected.")
#
#                             if "TV" in url:
#                                 try:
#
#                                     if "TV_UHD" in url:
#                                         self.driver.get(url)
#                                         print("Select TV_UHD URL:" + url)
#                                         TV_HomeTheater=TVHomeTheaterPage(self.driver)
#                                         TV_HomeTheater.get_TVHomeTheater_ShopAll()
#                                         TV_HomeTheater.get_TV_UHD_Module()
#                                     if "TV_QLED" in url:
#                                         self.driver.get(url)
#                                         print("Select TV_QLED URL:" + url)
#                                         TV_HomeTheater=TVHomeTheaterPage(self.driver)
#                                         TV_HomeTheater.get_TVHomeTheater_ShopAll()
#                                         TV_HomeTheater.get_TV_QLED_Module()
#                                     if "TV_ACCESSORY" in url:
#                                         self.driver.get(url)
#                                         print("Select TV_ACCESSORY URL:" + url)
#                                         TV_HomeTheater=TVHomeTheaterPage(self.driver)
#                                         TV_HomeTheater.get_TVHomeTheater_ShopAll()
#                                         TV_HomeTheater.get_TV_ACCESSORY_Module()
#                                     if "TV_FRAME" in url:
#                                         self.driver.get(url)
#                                         print("Select TV_FRAME URL:" + url)
#                                         TV_HomeTheater=TVHomeTheaterPage(self.driver)
#                                         TV_HomeTheater.get_TVHomeTheater_ShopAll()
#                                         TV_HomeTheater.get_TV_FRAME_Module()
#                                 except:
#                                     print("TV option is NOT selected.")
#
#                             if "CE_COMPUTER" in url:
#                                 try:
#                                     if "CE_COMPUTER" in url:
#                                         self.driver.get(url)
#                                         print("Select CE_COMPUTER URL:" + url)
#                                         CE_Computer=ComputingPage(self.driver)
#                                         CE_Computer.get_Computing_ShopAll()
#                                         CE_Computer.get_CE_COMPUTER_Module()
#                                 except:
#                                     print("CE option is NOT selected.")
#                     except:
#                         raise ("CC option NOT selected.")
#
#
# if __name__ == '__main__':
#     unittest.main()