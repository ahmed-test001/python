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


class W_45_DD_Module_Verify_Test(unittest.TestCase):

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
        logger.info(': \n#####  Test Complete  #####')

    def test_CC_ModuleVerification_URL1(self):
        logger.info(': ' + self.test_CC_ModuleVerification_URL1.__name__ + "\n #####  Starting TEST  ##### ")
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            urls = f.read().splitlines()
            url=urls[0]
            self.driver.get(url)
            try:
                        if "CC" in url:
                            # self.driver.get(url)
                            if "MB" in url:
                                try:
                                    if "MB_FOLD" in url:
                                        MB_smartphone=SmartPhonePage(self.driver)
                                        MB_smartphone.get_SMARTPHONE_ShopAll()
                                        MB_smartphone.get_MB_FOLD_Module()
                                    if "MB_NOTE" in url:
                                        MB_smartphone=SmartPhonePage(self.driver)
                                        MB_smartphone.get_SMARTPHONE_ShopAll()
                                        MB_smartphone.get_MB_NOTE_Module()
                                    if "MB_GALAXY" in url:
                                        MB_smartphone=SmartPhonePage(self.driver)
                                        MB_smartphone.get_SMARTPHONE_ShopAll()
                                        MB_smartphone.get_MB_GALAXY_Module()
                                    if "MB_WEAR" in url:
                                        MB_Wear=MobileAccessoriesPage(self.driver)
                                        MB_Wear.get_MobileAccessories_ShopAll()
                                        MB_Wear.get_MB_WEAR_Module()
                                    if "MB_TABLET" in url:
                                        MB_tablet = TabletPage(self.driver)
                                        MB_tablet.get_Tablet_ShopAll()
                                        MB_tablet.get_MB_TABLET_Module()
                                except:
                                    print("MB option is NOT selected.")

                            if "HA" in url:
                                try:
                                    if "HA_LAUNDRY" in url:
                                        HA_homeappliance=HomeAppliancePage(self.driver)
                                        HA_homeappliance.get_HomeAppliance_ShopAll()
                                        HA_homeappliance.get_HA_LAUNDRY_Module()
                                    if "HA_KITCHEN" in url:
                                        HA_homeappliance=HomeAppliancePage(self.driver)
                                        HA_homeappliance.get_HomeAppliance_ShopAll()
                                        HA_homeappliance.get_HA_KITCHEN_Module()
                                    if "HA_CLEANER" in url:
                                        HA_homeappliance=HomeAppliancePage(self.driver)
                                        HA_homeappliance.get_HomeAppliance_ShopAll()
                                        HA_homeappliance.get_HA_CLEANER_Module()
                                except:
                                    print("HA option is NOT selected.")

                            if "TV" in url:
                                try:
                                    if "TV_UHD" in url:
                                        TV_HomeTheater=TVHomeTheaterPage(self.driver)
                                        TV_HomeTheater.get_TVHomeTheater_ShopAll()
                                        TV_HomeTheater.get_TV_UHD_Module()
                                    if "TV_QLED" in url:
                                        TV_HomeTheater=TVHomeTheaterPage(self.driver)
                                        TV_HomeTheater.get_TVHomeTheater_ShopAll()
                                        TV_HomeTheater.get_TV_QLED_Module()
                                    if "TV_ACCESSORY" in url:
                                        TV_HomeTheater=TVHomeTheaterPage(self.driver)
                                        TV_HomeTheater.get_TVHomeTheater_ShopAll()
                                        TV_HomeTheater.get_TV_ACCESSORY_Module()
                                    if "TV_FRAME" in url:
                                        TV_HomeTheater=TVHomeTheaterPage(self.driver)
                                        TV_HomeTheater.get_TVHomeTheater_ShopAll()
                                        TV_HomeTheater.get_TV_FRAME_Module()
                                except:
                                    print("TV option is NOT selected.")

                            if "CE_COMPUTER" in url:
                                try:
                                    if "CE_COMPUTER" in url:
                                        CE_Computer=ComputingPage(self.driver)
                                        CE_Computer.get_Computing_ShopAll()
                                        CE_Computer.get_CE_COMPUTER_Module()
                                except:
                                    print("CE option is NOT selected.")
            except:
                    raise ("CC Category NOT selected.")

    def test_CC_ModuleVerification_URL2(self):
        logger.info(': ' + self.test_CC_ModuleVerification_URL2.__name__ + "\n #####  Starting TEST  ##### ")
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            urls = f.read().splitlines()
            url=urls[1]
            self.driver.get(url)
            try:
                if "CC" in url:
                    if "MB" in url:
                        try:
                            if "MB_FOLD" in url:
                                MB_smartphone=SmartPhonePage(self.driver)
                                MB_smartphone.get_SMARTPHONE_ShopAll()
                                MB_smartphone.get_MB_FOLD_Module()
                            if "MB_NOTE" in url:
                                MB_smartphone=SmartPhonePage(self.driver)
                                MB_smartphone.get_SMARTPHONE_ShopAll()
                                MB_smartphone.get_MB_NOTE_Module()
                            if "MB_GALAXY" in url:
                                MB_smartphone=SmartPhonePage(self.driver)
                                MB_smartphone.get_SMARTPHONE_ShopAll()
                                MB_smartphone.get_MB_GALAXY_Module()
                            if "MB_WEAR" in url:
                                MB_Wear=MobileAccessoriesPage(self.driver)
                                MB_Wear.get_MobileAccessories_ShopAll()
                                MB_Wear.get_MB_WEAR_Module()
                            if "MB_TABLET" in url:
                                MB_tablet = TabletPage(self.driver)
                                MB_tablet.get_Tablet_ShopAll()
                                MB_tablet.get_MB_TABLET_Module()
                        except:
                                print("MB option is NOT selected.")

                    if "HA" in url:
                        try:
                            if "HA_LAUNDRY" in url:
                                HA_homeappliance=HomeAppliancePage(self.driver)
                                HA_homeappliance.get_HomeAppliance_ShopAll()
                                HA_homeappliance.get_HA_LAUNDRY_Module()
                            if "HA_KITCHEN" in url:
                                HA_homeappliance=HomeAppliancePage(self.driver)
                                HA_homeappliance.get_HomeAppliance_ShopAll()
                                HA_homeappliance.get_HA_KITCHEN_Module()
                            if "HA_CLEANER" in url:
                                HA_homeappliance=HomeAppliancePage(self.driver)
                                HA_homeappliance.get_HomeAppliance_ShopAll()
                                HA_homeappliance.get_HA_CLEANER_Module()
                        except:
                                print("HA option is NOT selected.")

                    if "TV" in url:
                        try:
                            if "TV_UHD" in url:
                                TV_HomeTheater=TVHomeTheaterPage(self.driver)
                                TV_HomeTheater.get_TVHomeTheater_ShopAll()
                                TV_HomeTheater.get_TV_UHD_Module()
                            if "TV_QLED" in url:
                                TV_HomeTheater=TVHomeTheaterPage(self.driver)
                                TV_HomeTheater.get_TVHomeTheater_ShopAll()
                                TV_HomeTheater.get_TV_QLED_Module()
                            if "TV_ACCESSORY" in url:
                                TV_HomeTheater=TVHomeTheaterPage(self.driver)
                                TV_HomeTheater.get_TVHomeTheater_ShopAll()
                                TV_HomeTheater.get_TV_ACCESSORY_Module()
                            if "TV_FRAME" in url:
                                TV_HomeTheater=TVHomeTheaterPage(self.driver)
                                TV_HomeTheater.get_TVHomeTheater_ShopAll()
                                TV_HomeTheater.get_TV_FRAME_Module()
                        except:
                                print("TV option is NOT selected.")

                    if "CE_COMPUTER" in url:
                        try:
                            if "CE_COMPUTER" in url:
                                CE_Computer=ComputingPage(self.driver)
                                CE_Computer.get_Computing_ShopAll()
                                CE_Computer.get_CE_COMPUTER_Module()
                        except:
                            print("CE option is NOT selected.")
            except:
                    raise ("CC Category NOT selected.")

    def test_CC_ModuleVerification_URL3(self):
        logger.info(': ' + self.test_CC_ModuleVerification_URL3.__name__ + "\n #####  Starting TEST  ##### ")
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            urls = f.read().splitlines()
            url=urls[1]
            self.driver.get(url)
            try:
                if "CC" in url:
                    if "MB" in url:
                        try:
                            if "MB_FOLD" in url:
                                MB_smartphone=SmartPhonePage(self.driver)
                                MB_smartphone.get_SMARTPHONE_ShopAll()
                                MB_smartphone.get_MB_FOLD_Module()
                            if "MB_NOTE" in url:
                                MB_smartphone=SmartPhonePage(self.driver)
                                MB_smartphone.get_SMARTPHONE_ShopAll()
                                MB_smartphone.get_MB_NOTE_Module()
                            if "MB_GALAXY" in url:
                                MB_smartphone=SmartPhonePage(self.driver)
                                MB_smartphone.get_SMARTPHONE_ShopAll()
                                MB_smartphone.get_MB_GALAXY_Module()
                            if "MB_WEAR" in url:
                                MB_Wear=MobileAccessoriesPage(self.driver)
                                MB_Wear.get_MobileAccessories_ShopAll()
                                MB_Wear.get_MB_WEAR_Module()
                            if "MB_TABLET" in url:
                                MB_tablet = TabletPage(self.driver)
                                MB_tablet.get_Tablet_ShopAll()
                                MB_tablet.get_MB_TABLET_Module()
                        except:
                                print("MB option is NOT selected.")

                    if "HA" in url:
                        try:
                            if "HA_LAUNDRY" in url:
                                HA_homeappliance=HomeAppliancePage(self.driver)
                                HA_homeappliance.get_HomeAppliance_ShopAll()
                                HA_homeappliance.get_HA_LAUNDRY_Module()
                            if "HA_KITCHEN" in url:
                                HA_homeappliance=HomeAppliancePage(self.driver)
                                HA_homeappliance.get_HomeAppliance_ShopAll()
                                HA_homeappliance.get_HA_KITCHEN_Module()
                            if "HA_CLEANER" in url:
                                HA_homeappliance=HomeAppliancePage(self.driver)
                                HA_homeappliance.get_HomeAppliance_ShopAll()
                                HA_homeappliance.get_HA_CLEANER_Module()
                        except:
                                print("HA option is NOT selected.")

                    if "TV" in url:
                        try:
                            if "TV_UHD" in url:
                                TV_HomeTheater=TVHomeTheaterPage(self.driver)
                                TV_HomeTheater.get_TVHomeTheater_ShopAll()
                                TV_HomeTheater.get_TV_UHD_Module()
                            if "TV_QLED" in url:
                                TV_HomeTheater=TVHomeTheaterPage(self.driver)
                                TV_HomeTheater.get_TVHomeTheater_ShopAll()
                                TV_HomeTheater.get_TV_QLED_Module()
                            if "TV_ACCESSORY" in url:
                                TV_HomeTheater=TVHomeTheaterPage(self.driver)
                                TV_HomeTheater.get_TVHomeTheater_ShopAll()
                                TV_HomeTheater.get_TV_ACCESSORY_Module()
                            if "TV_FRAME" in url:
                                TV_HomeTheater=TVHomeTheaterPage(self.driver)
                                TV_HomeTheater.get_TVHomeTheater_ShopAll()
                                TV_HomeTheater.get_TV_FRAME_Module()
                        except:
                                print("TV option is NOT selected.")

                    if "CE_COMPUTER" in url:
                        try:
                            if "CE_COMPUTER" in url:
                                CE_Computer=ComputingPage(self.driver)
                                CE_Computer.get_Computing_ShopAll()
                                CE_Computer.get_CE_COMPUTER_Module()
                        except:
                            print("CE option is NOT selected.")
            except:
                    raise ("CC Category NOT selected.")


if __name__ == '__main__':
    unittest.main()