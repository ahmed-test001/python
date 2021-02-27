import os
import sys
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from Utility_Files.ExcelReaderUtil import ExcelUtil
from PageClass.BasePageClass import BasePage
from Utility_Files.HTMLTestRunner import stdout_redirector
logger = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class W_47_FooterLinkPage(BasePage):

    def get_pay_later_icon_LandingPage_URL_validation(self):
        logger.info(": ##### Started pay_later URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("EMAILPage", 2, 2)
        parent_window = self.driver.current_window_handle
        payover = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@_label='Pay_Over_Time_Title'])[1]")))
        self.driver.execute_script("arguments[0].scrollIntoView();", payover)
        self.driver.execute_script("arguments[0].click();", payover)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        paylater_url = self.driver.current_url
        assert self.url_path in paylater_url,"Pay Later Landing Page URL is not Matched."
        logger.info(': Assertion Pay Later with: ' + paylater_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_free_shipping_icon_LandingPage_URL_validation(self):
        logger.info(": ##### Started free_shipping URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("EMAILPage", 3, 2)
        parent_window = self.driver.current_window_handle
        freeShipping = self.driver.find_element_by_xpath("//a[@_label='Free_Shipping_Title']")
        self.driver.execute_script("arguments[0].scrollIntoView();", freeShipping)
        self.driver.execute_script("arguments[0].click();", freeShipping)
        # time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        # time.sleep(5)
        freeShipping_url = self.driver.current_url
        # time.sleep(5)
        assert self.url_path in freeShipping_url, "Free Shipping Landing Page URL is not Matched."
        logger.info(': Assertion Free SHipping with: ' + freeShipping_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_google_play_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started google_play URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("EMAILPage", 4, 2)
        parent_window = self.driver.current_window_handle
        googleApp = self.driver.find_element_by_xpath("//a[@_label='Download_App_Google']")
        self.driver.execute_script("arguments[0].scrollIntoView();", googleApp)
        self.driver.execute_script("arguments[0].click();", googleApp)
        # time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        # time.sleep(5)
        googleApp_url = self.driver.current_url
        # time.sleep(5)
        assert self.url_path in googleApp_url, "Google Play store Page URL Not Matched."
        logger.info(': Assertion Free Google Play App with: ' + googleApp_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_apple_store_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started apple_store URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("EMAILPage", 5, 2)
        parent_window = self.driver.current_window_handle
        appleApp = self.driver.find_element_by_xpath("//a[@_label='Download_App_Apple']")
        self.driver.execute_script("arguments[0].scrollIntoView();", appleApp)
        self.driver.execute_script("arguments[0].click();", appleApp)
        # time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        # time.sleep(5)
        appleApp_url = self.driver.current_url
        # time.sleep(5)
        assert self.url_path in appleApp_url,"Apple App Page URL Not Matched."
        logger.info(': Assertion Free Apple App with: ' + appleApp_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_free_shipping_details_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started free_shipping URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("EMAILPage", 3, 2)
        parent_window = self.driver.current_window_handle
        freeShip_button = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[2]")
        self.driver.execute_script("arguments[0].scrollIntoView();", freeShip_button)
        self.driver.execute_script("arguments[0].click();", freeShip_button)
        # time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        # time.sleep(5)
        freeShip_button_url = self.driver.current_url
        # time.sleep(5)
        assert self.url_path in freeShip_button_url, "Free Shipping Page URL Not Matched."
        logger.info(': Assertion Free Ship Button URL with: ' + freeShip_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Mobile_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started Mobile_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("EMAILPage", 6, 2)
        parent_window = self.driver.current_window_handle
        freeShip_button = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[3]")
        self.driver.execute_script("arguments[0].scrollIntoView();", freeShip_button)
        self.driver.execute_script("arguments[0].click();", freeShip_button)
        # time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        # time.sleep(5)
        mobile_button_url = self.driver.current_url
        # time.sleep(5)
        assert self.url_path in mobile_button_url, "Mobile Page URL Not Matched."
        logger.info(': Assertion Mobile Button URL with: ' + mobile_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_TV_Audio_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started TV_Audio_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("EMAILPage", 7, 2)
        parent_window = self.driver.current_window_handle
        Audio_button = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[4]")
        self.driver.execute_script("arguments[0].scrollIntoView();", Audio_button)
        self.driver.execute_script("arguments[0].click();", Audio_button)
        # time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        # time.sleep(5)
        Tv_Audio_button_url = self.driver.current_url
        # time.sleep(5)
        assert self.url_path in Tv_Audio_button_url, "TV & Audio Page URL Not Matched."
        logger.info(': Assertion TV & Audio Button URL with: ' + Tv_Audio_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_computing_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started computing_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("EMAILPage", 8, 2)
        parent_window = self.driver.current_window_handle
        Computing_button = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[5]")
        self.driver.execute_script("arguments[0].scrollIntoView();", Computing_button)
        self.driver.execute_script("arguments[0].click();", Computing_button)
        # time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        # time.sleep(5)
        Computing_button_url = self.driver.current_url
        # time.sleep(5)
        assert self.url_path in Computing_button_url, "Computing Page URL Not Matched."
        logger.info(': Assertion Computing Button URL with: ' + Computing_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_appliances_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started appliances_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("EMAILPage", 9, 2)
        parent_window = self.driver.current_window_handle
        Appliance_button = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[6]")
        self.driver.execute_script("arguments[0].scrollIntoView();", Appliance_button)
        self.driver.execute_script("arguments[0].click();", Appliance_button)
        # time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        # time.sleep(5)
        Appliance_button_url = self.driver.current_url
        # time.sleep(5)
        assert self.url_path in Appliance_button_url, "Appliance Page URL Not Matched."
        logger.info(': Assertion Appliance Button URL with: ' + Appliance_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_weekly_offer_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started weekly_offer_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("EMAILPage", 10, 2)
        parent_window = self.driver.current_window_handle
        WeeklyOffer_button = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[7]")
        self.driver.execute_script("arguments[0].scrollIntoView();", WeeklyOffer_button)
        self.driver.execute_script("arguments[0].click();", WeeklyOffer_button)
        # time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        # time.sleep(5)
        WeeklyOffer_button_url = self.driver.current_url
        # time.sleep(5)
        assert self.url_path in WeeklyOffer_button_url, "Weekly Offer Page URL Not Matched."
        logger.info(': Assertion Weekly Offer Button URL with: ' + WeeklyOffer_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_facebook_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started facebook_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("EMAILPage", 11, 2)
        parent_window = self.driver.current_window_handle
        Facebook_button = self.driver.find_element_by_xpath("//a[@_label='Facebook']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Facebook_button)
        self.driver.execute_script("arguments[0].click();", Facebook_button)
        # time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        # time.sleep(5)
        Facebook_button_url = self.driver.current_url
        # time.sleep(5)
        assert self.url_path in Facebook_button_url, "Facebook Page URL Not Matched."
        logger.info(': Assertion Facebook Button URL with: ' + Facebook_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_instagram_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started instagram_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("EMAILPage", 12, 2)
        parent_window = self.driver.current_window_handle
        Instagram_button = self.driver.find_element_by_xpath("//a[@_label='Instagram']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Instagram_button)
        self.driver.execute_script("arguments[0].click();", Instagram_button)
        # time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        # time.sleep(5)
        Instagram_button_url = self.driver.current_url
        # time.sleep(5)
        # assert self.url_path in Instagram_button_url, "Instagram Page URL Not Matched."
        logger.info(': Assertion Instagram Button URL with: ' + Instagram_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_twitter_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started twitter_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("EMAILPage", 13, 2)
        parent_window = self.driver.current_window_handle
        Twitter_button = self.driver.find_element_by_xpath("//a[@_label='Twitter']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Twitter_button)
        self.driver.execute_script("arguments[0].click();", Twitter_button)
        # time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        # time.sleep(5)
        Twitter_button_url = self.driver.current_url
        # time.sleep(5)
        # assert self.url_path in Twitter_button_url, "Twitter Page URL Not Matched."
        logger.info(': Assertion Twitter Button URL with: ' + Twitter_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_youtube_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started youtube_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("EMAILPage", 14, 2)
        parent_window = self.driver.current_window_handle
        Youtube_button = self.driver.find_element_by_xpath("// a[@_label='Youtube']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Youtube_button)
        self.driver.execute_script("arguments[0].click();", Youtube_button)
        # time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        # time.sleep(5)
        Youtube_button_url = self.driver.current_url
        # time.sleep(5)
        assert self.url_path in Youtube_button_url, "Youtube Page URL Not Matched."
        logger.info(': Assertion YouTube Button URL with: ' + Youtube_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')