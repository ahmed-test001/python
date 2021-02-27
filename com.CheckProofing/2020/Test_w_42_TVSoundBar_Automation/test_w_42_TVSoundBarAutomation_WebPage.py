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

sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from Utility_Files.HTMLTestRunner import stdout_redirector
from Utility_Files import ReadConfig
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class WebPage_W_42_TVSoundBarAutomation_Test(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        with open('../TextFolder/TestIn_UniqueURL_List.txt')as f:
            urls = f.read().splitlines()
            for url in urls:
                if ReadConfig.read_w42_TVSoundBarAutomation_configData('TVSoundBarData', 'url') in url:
                    option = webdriver.ChromeOptions()
                    option.add_experimental_option('excludeSwitches', ['enable-logging'])
                    self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver1'), options=option)
                    warnings.filterwarnings(action="ignore", message="unclosed",category=ResourceWarning)
                    self.driver.get(url)
                    self.wait = WebDriverWait(self.driver, 10)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_a_TVSoundBar_WebLandingPage_URL_validation(self):
        logger.info(': '+self.test_a_TVSoundBar_WebLandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(3)
        WebPage_URL = self.driver.current_url
        self.assertEqual(ReadConfig.read_w42_TVSoundBarAutomation_configData('TVSoundBarData', 'url'), WebPage_URL, msg="Web Landing page URL not Matched.")
        logger.info(': assertion complete with: ' + WebPage_URL)
        logger.info('####  TEST Complete  ####')

    def test_b1_HW_T650_SoundBar_savings_validation(self):
        logger.info(': ' + self.test_b1_HW_T650_SoundBar_savings_validation.__name__ + "\n #####  Starting TEST  ##### ")
        savingTxt = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@class='Product-card__price-save'])[1]"))).text
        savingTxt = savingTxt[4:]
        self.assertIn(ReadConfig.read_w42_TVSoundBarAutomation_configData('WEBPage1', 'HW_T650'), savingTxt, msg="Saving Price Not Matching")
        logger.info(": Required Price : " + savingTxt)
        addToCart = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='cta-button'])[1]")))
        self.driver.execute_script("arguments[0].scrollIntoView();", addToCart)
        self.driver.execute_script("arguments[0].click();", addToCart)
        checkout = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='cta-button']")))
        self.driver.execute_script("arguments[0].click();", checkout)
        checkoutsavingTxt = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@class='os-price-value'])[5]"))).text
        self.assertIn(ReadConfig.read_w42_TVSoundBarAutomation_configData('WEBPage1', 'HW_T650'), checkoutsavingTxt,msg="Saving Price Not Matching")
        logger.info(": Required Price : " + checkoutsavingTxt)
        logger.info('\n ####  TEST Complete  ####')

    def test_b2_HW_Q60T_SoundBar_savings_validation(self):
        logger.info(': ' + self.test_b2_HW_Q60T_SoundBar_savings_validation.__name__ + "\n #####  Starting TEST  ##### ")
        savingTxt = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@class='Product-card__price-save'])[2]"))).text
        savingTxt = savingTxt[4:]
        self.assertIn(ReadConfig.read_w42_TVSoundBarAutomation_configData('WEBPage1', 'HW_Q60T'), savingTxt, msg="Saving Price Not Matching")
        logger.info(": Required Price : " + savingTxt)
        addToCart = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='cta-button'])[2]")))
        self.driver.execute_script("arguments[0].scrollIntoView();", addToCart)
        self.driver.execute_script("arguments[0].click();", addToCart)
        checkout = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='cta-button']")))
        self.driver.execute_script("arguments[0].click();", checkout)
        checkoutsavingTxt = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@class='os-price-value'])[5]"))).text
        self.assertIn(ReadConfig.read_w42_TVSoundBarAutomation_configData('WEBPage1', 'HW_Q60T'), checkoutsavingTxt,msg="Saving Price Not Matching")
        logger.info(": Required Price : " + checkoutsavingTxt)
        logger.info('\n ####  TEST Complete  ####')

    def test_b3_HW_Q70T_SoundBar_savings_validation(self):
        logger.info(': ' + self.test_b3_HW_Q70T_SoundBar_savings_validation.__name__ + "\n #####  Starting TEST  ##### ")
        savingTxt = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@class='Product-card__price-save'])[3]"))).text
        savingTxt = savingTxt[4:]
        self.assertIn(ReadConfig.read_w42_TVSoundBarAutomation_configData('WEBPage1', 'HW_Q70T'), savingTxt, msg="Saving Price Not Matching")
        logger.info(": Required Price : " + savingTxt)
        addToCart = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='cta-button'])[3]")))
        self.driver.execute_script("arguments[0].scrollIntoView();", addToCart)
        self.driver.execute_script("arguments[0].click();", addToCart)
        checkout = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='cta-button']")))
        self.driver.execute_script("arguments[0].click();", checkout)
        checkoutsavingTxt = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@class='os-price-value'])[5]"))).text
        self.assertIn(ReadConfig.read_w42_TVSoundBarAutomation_configData('WEBPage1', 'HW_Q70T'), checkoutsavingTxt,msg="Saving Price Not Matching")
        logger.info(": Required Price : " + checkoutsavingTxt)
        logger.info('\n ####  TEST Complete  ####')

    def test_b4_HW_Q800T_SoundBar_savings_validation(self):
        logger.info(': ' + self.test_b4_HW_Q800T_SoundBar_savings_validation.__name__ + "\n #####  Starting TEST  ##### ")
        savingTxt = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@class='Product-card__price-save'])[4]"))).text
        savingTxt = savingTxt[4:]
        self.assertIn(ReadConfig.read_w42_TVSoundBarAutomation_configData('WEBPage1', 'HW_Q800T'), savingTxt, msg="Saving Price Not Matching")
        logger.info(": Required Price : " + savingTxt)
        addToCart = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='cta-button'])[4]")))
        self.driver.execute_script("arguments[0].scrollIntoView();", addToCart)
        self.driver.execute_script("arguments[0].click();", addToCart)
        checkout = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='cta-button']")))
        self.driver.execute_script("arguments[0].click();", checkout)
        checkoutsavingTxt = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@class='os-price-value'])[5]"))).text
        self.assertIn(ReadConfig.read_w42_TVSoundBarAutomation_configData('WEBPage1', 'HW_Q800T'), checkoutsavingTxt,msg="Saving Price Not Matching")
        logger.info(": Required Price : " + checkoutsavingTxt)
        logger.info('\n ####  TEST Complete  ####')

    def test_b5_HW_Q900T_SoundBar_savings_validation(self):
        logger.info(': ' + self.test_b5_HW_Q900T_SoundBar_savings_validation.__name__ + "\n #####  Starting TEST  ##### ")
        savingTxt = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@class='Product-card__price-save'])[5]"))).text
        savingTxt = savingTxt[4:]
        self.assertIn(ReadConfig.read_w42_TVSoundBarAutomation_configData('WEBPage1', 'HW_Q900T'), savingTxt, msg="Saving Price Not Matching")
        logger.info(": Required Price : " + savingTxt)
        addToCart=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='cta-button'])[5]")))
        self.driver.execute_script("arguments[0].scrollIntoView();", addToCart)
        self.driver.execute_script("arguments[0].click();", addToCart)
        checkout = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='cta-button']")))
        self.driver.execute_script("arguments[0].click();", checkout)
        checkoutsavingTxt=self.wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@class='os-price-value'])[5]"))).text
        self.assertIn(ReadConfig.read_w42_TVSoundBarAutomation_configData('WEBPage1', 'HW_Q900T'), checkoutsavingTxt, msg="Saving Price Not Matching")
        logger.info(": Required Price : " + checkoutsavingTxt)
        logger.info('\n ####  TEST Complete  ####')

    def test_b6_HW_Q950T_SoundBar_savings_validation(self):
        logger.info(': ' + self.test_b6_HW_Q950T_SoundBar_savings_validation.__name__ + "\n #####  Starting TEST  ##### ")
        savingTxt = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@class='Product-card__price-save'])[6]"))).text
        savingTxt = savingTxt[4:]
        self.assertIn(ReadConfig.read_w42_TVSoundBarAutomation_configData('WEBPage1', 'HW_Q950T'), savingTxt, msg="Saving Price Not Matching")
        logger.info(": Required Price : " + savingTxt)
        addToCart=self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='cta-button'])[6]")))
        self.driver.execute_script("arguments[0].scrollIntoView();", addToCart)
        self.driver.execute_script("arguments[0].click();", addToCart)
        checkout = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='cta-button']")))
        self.driver.execute_script("arguments[0].click();", checkout)
        checkoutsavingTxt=self.wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@class='os-price-value'])[5]"))).text
        self.assertIn(ReadConfig.read_w42_TVSoundBarAutomation_configData('WEBPage1', 'HW_Q950T'), checkoutsavingTxt, msg="Saving Price Not Matching")
        logger.info(": Required Price : " + checkoutsavingTxt)
        logger.info('\n ####  TEST Complete  ####')

    def test_b7_HW_LST70T_SoundBar_savings_validation(self):
        logger.info(': ' + self.test_b7_HW_LST70T_SoundBar_savings_validation.__name__ + "\n #####  Starting TEST  ##### ")
        savingTxt = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//*[@class='Product-card__price-save'])[7]"))).text
        savingTxt = savingTxt[4:]
        self.assertIn(ReadConfig.read_w42_TVSoundBarAutomation_configData('WEBPage1', 'HW_LST70T'), savingTxt, msg="Saving Price Not Matching")
        logger.info(": Required Price : " + savingTxt)
        addToCart = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='cta-button'])[7]")))
        self.driver.execute_script("arguments[0].scrollIntoView();", addToCart)
        self.driver.execute_script("arguments[0].click();", addToCart)
        checkout = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='cta-button']")))
        self.driver.execute_script("arguments[0].click();", checkout)
        checkoutsavingTxt = self.wait.until( EC.presence_of_element_located((By.XPATH, "(//*[@class='os-price-value'])[5]"))).text
        self.assertIn(ReadConfig.read_w42_TVSoundBarAutomation_configData('WEBPage1', 'HW_LST70T'), checkoutsavingTxt, msg="Saving Price Not Matching")
        logger.info(": Required Price : " + checkoutsavingTxt)
        logger.info('\n ####  TEST Complete  ####')


if __name__ == '__main__':
    unittest.main()


