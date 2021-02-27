import logging
import os
import sys

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


class FooterLinkPage(BasePage):

    def get_pay_later_icon_LandingPage_URL_validation(self):
        logger.info(": ##### Started pay_later URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 5, 2)
        # self.text = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 5, 3)
        # self.subcopy = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 5, 4)
        parent_window = self.driver.current_window_handle
        try:
            payover = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@_label='Pay_Over_Time_Title'])[1]")))
        except:
            payover = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@_label='Pay_Over_Time_Title']")))
        # payover1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@_label='Pay_Over_Time_Title'])[1]"))).text
        # payover2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@_label='Pay_Over_Time_Title'])[1]"))).text
        self.driver.execute_script("arguments[0].scrollIntoView();", payover)
        self.driver.execute_script("arguments[0].click();", payover)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        paylater_url = self.driver.current_url
        assert self.url_path in paylater_url, "Pay Later Landing Page URL is not Matched."
        # assert self.text in payover1, "Pay Later Text is not Matched."
        # assert self.subcopy in payover2, "Pay Later subcopy is not Matched."
        logger.info(': Assertion Pay Later with: ' + paylater_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_free_shipping_icon_LandingPage_URL_validation(self):
        logger.info(": ##### Started free_shipping URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 6, 2 )
        # self.text = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 6, 3)
        # self.subcopy = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 6, 4)
        parent_window = self.driver.current_window_handle
        try:
            freeShipping = self.driver.find_element_by_xpath("//a[@_label='Free_Shipping_Title']")
        except:
            freeShipping = self.driver.find_element_by_xpath("//a[@_label='Free_Shipping_Title']")
        # freeShipping1 = self.driver.find_element_by_xpath("//a[@_label='Free_Shipping_Title']").text
        # freeShipping2 = self.driver.find_element_by_xpath("//a[@_label='Free_Shipping_Copy']").text
        self.driver.execute_script("arguments[0].scrollIntoView();", freeShipping)
        self.driver.execute_script("arguments[0].click();", freeShipping)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        freeShipping_url = self.driver.current_url
        assert self.url_path in freeShipping_url, "Free Shipping Page URL Not Matched."
        # assert self.text in freeShipping1, "Free Shipping Text Not Matched."
        # assert self.subcopy in freeShipping2, "Free Shipping subcopy Not Matched."
        logger.info(': Assertion Free SHipping with: ' + freeShipping_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_GetRewarded_icon_LandingPage_URL_validation(self):
        logger.info(": ##### Started Get Rewarded URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 7, 2)
        # self.text = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 7, 3)
        # self.subcopy = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 7, 4)
        parent_window = self.driver.current_window_handle
        getRewarded = self.driver.find_element_by_xpath("//*[@_label='Get_Rewarded_Title']")
        # getRewarded1 = self.driver.find_element_by_xpath("//*[@_label='Get_Rewarded_Title']").text
        # getRewarded2 = self.driver.find_element_by_xpath("//*[@_label='Get_Rewarded_Copy']").text
        self.driver.execute_script("arguments[0].scrollIntoView();", getRewarded)
        self.driver.execute_script("arguments[0].click();", getRewarded)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        getRewarded_url = self.driver.current_url
        assert self.url_path in getRewarded_url, "Get Rewarded Page URL Not Matched."
        # assert self.text in getRewarded1, "Get Rewarded Text Not Matched."
        # assert self.subcopy in getRewarded2, "Get Rewarded subcopy Not Matched."
        logger.info(': Assertion Get Rewarded with: ' + getRewarded_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_HaveQuestions_icon_LandingPage_URL_validation(self):
        logger.info(": ##### Started HaveQuestions URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 8, 3)
        self.text = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 8, 3)
        self.subcopy = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 8, 4)
        parent_window = self.driver.current_window_handle
        haveQuestions = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[2]")
        haveQuestions1 = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[2]").text
        haveQuestions2 = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[2]").text
        self.driver.execute_script("arguments[0].scrollIntoView();", haveQuestions)
        self.driver.execute_script("arguments[0].click();", haveQuestions)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        haveQuestions_url = self.driver.current_url
        assert self.url_path in haveQuestions_url, "HaveQuestions Page URL Not Matched."
        # assert self.text in haveQuestions1, "HaveQuestions Text Not Matched."
        # assert self.subcopy in haveQuestions2, "HaveQuestions subcopy Not Matched."
        logger.info(': Assertion HaveQuestions with: ' + haveQuestions_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_ShopApp_LandingPage_URL_validation(self):
        logger.info(": ##### Started Shop App URL verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "Enrollees_Non_Res" not in subjectlineTxt:
            self.url_path = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 4, 2)
            parent_window = self.driver.current_window_handle
            googleApp = self.driver.find_element_by_xpath("//*[@src='http://t.info.samsungusa.com/res/samsung/4156015d69970b8794e346436d4e37f1.jpg']")
            self.driver.execute_script("arguments[0].scrollIntoView();", googleApp)
            self.driver.execute_script("arguments[0].click();", googleApp)
            # time.sleep(10)
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            shopApp_url = self.driver.current_url
            assert self.url_path in shopApp_url, "Google Play store Page URL Not Matched."
            logger.info(': Assertion Shop App URL with: ' + shopApp_url)
            self.driver.close()
            self.driver.switch_to.window(parent_window)
        else:
            logger.info(': ShoApp Module Not Present.')
        logger.info(': #####  Verification Complete  #####\n')

    def get_Hero_SC_Text_validation(self, sheet_name, sheet_row, sheet_column, xpath_loc):
        logger.info(": ##### Started Hero_SC_Text_validation #####")
        self.SC_text = ExcelUtil(tc_name="").read_from_excel(sheet_name, int(sheet_row), int(sheet_column))
        SC = self.driver.find_element_by_xpath(xpath_loc).text

    def get_google_play_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started google_play URL verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "Enrollees_Non_Res" in subjectlineTxt:
            self.url_path = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 2, 2)
            parent_window = self.driver.current_window_handle
            googleApp = self.driver.find_element_by_xpath("//a[@_label='Download_App_Google']")
            self.driver.execute_script("arguments[0].scrollIntoView();", googleApp)
            self.driver.execute_script("arguments[0].click();", googleApp)
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            googleApp_url = self.driver.current_url
            assert self.url_path in googleApp_url, "Google Play store Page URL Not Matched."
            logger.info(': Assertion Free Google Play App with: ' + googleApp_url)
            self.driver.close()
            self.driver.switch_to.window(parent_window)
        else:
            logger.info(': Google Play Module Not Present.')
        logger.info(': #####  Verification Complete  #####\n')

    def get_apple_store_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started apple_store URL verification #####")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        if "Non" in subjectlineTxt:
            self.url_path = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 3, 2)
            parent_window = self.driver.current_window_handle
            appleApp = self.driver.find_element_by_xpath("//a[@_label='Download_App_Apple']")
            self.driver.execute_script("arguments[0].scrollIntoView();", appleApp)
            self.driver.execute_script("arguments[0].click();", appleApp)
            all_windows = self.driver.window_handles
            child_window = [window for window in all_windows if window != parent_window][0]
            self.driver.switch_to.window(child_window)
            appleApp_url = self.driver.current_url
            assert self.url_path in appleApp_url, "Apple App Page URL Not Matched."
            logger.info(': Assertion Free Apple App with: ' + appleApp_url)
            self.driver.close()
            self.driver.switch_to.window(parent_window)
        else:
            logger.info(': Apple Store Module Not Present.')
        logger.info(': #####  Verification Complete  #####\n')

    def get_free_shipping_details_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started free_shipping URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 9, 2)
        parent_window = self.driver.current_window_handle
        try:
            freeShip_button = self.driver.find_element_by_xpath("//a[@_label='Footer_Free_Shipping_Details']")
        except:
            freeShip_button = self.driver.find_element_by_xpath("//a[@_label='Footer_Free_Shipping_Details']")
        self.driver.execute_script("arguments[0].scrollIntoView();", freeShip_button)
        self.driver.execute_script("arguments[0].click();", freeShip_button)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        freeShip_button_url = self.driver.current_url
        assert self.url_path in freeShip_button_url, "Free Shipping Page URL Not Matched."
        logger.info(': Assertion Free Ship Button URL with: ' + freeShip_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_Mobile_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started Mobile_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 10, 2)
        parent_window = self.driver.current_window_handle
        try:
            mobile_button = self.driver.find_element_by_xpath("//*[@_label='Footer_Mobile']")
        except:
            mobile_button = self.driver.find_element_by_xpath("//*[@_label='Footer_Mobile']")
        self.driver.execute_script("arguments[0].scrollIntoView();", mobile_button)
        self.driver.execute_script("arguments[0].click();", mobile_button)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        mobile_button_url = self.driver.current_url
        assert self.url_path in mobile_button_url, "Mobile Page URL Not Matched."
        logger.info(': Assertion Mobile Button URL with: ' + mobile_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_TV_Audio_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started TV_Audio_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 11, 2)
        parent_window = self.driver.current_window_handle
        try:
            Audio_button = self.driver.find_element_by_xpath("//a[@_label='Footer_TV_Audio']")
        except:
            Audio_button = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[5]")
        self.driver.execute_script("arguments[0].scrollIntoView();", Audio_button)
        self.driver.execute_script("arguments[0].click();", Audio_button)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Tv_Audio_button_url = self.driver.current_url
        assert self.url_path in Tv_Audio_button_url, "TV & Audio Page URL Not Matched."
        logger.info(': Assertion TV & Audio Button URL with: ' + Tv_Audio_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_computing_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started computing_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 12, 2)
        parent_window = self.driver.current_window_handle
        parent_window = self.driver.current_window_handle
        try:
            Computing_button = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[5]")
        except:
            Computing_button = self.driver.find_element_by_xpath("//a[@_label='Footer_Computing']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Computing_button)
        self.driver.execute_script("arguments[0].click();", Computing_button)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Computing_button_url = self.driver.current_url
        assert self.url_path in Computing_button_url, "Computing Page URL Not Matched."
        logger.info(': Assertion Computing Button URL with: ' + Computing_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_appliances_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started appliances_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 13, 2)
        parent_window = self.driver.current_window_handle
        try:
            Appliance_button = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[6]")
        except:
            Appliance_button = self.driver.find_element_by_xpath("//a[@_label='Footer_Appliances']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Appliance_button)
        self.driver.execute_script("arguments[0].click();", Appliance_button)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Appliance_button_url = self.driver.current_url
        assert self.url_path in Appliance_button_url, "Appliance Page URL Not Matched."
        logger.info(': Assertion Appliance Button URL with: ' + Appliance_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_weekly_offer_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started weekly_offer_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 14, 2)
        parent_window = self.driver.current_window_handle
        try:
            WeeklyOffer_button = self.driver.find_element_by_xpath("(//*[@_label='Pay_Over_Time_Title'])[7]")
        except:
            WeeklyOffer_button = self.driver.find_element_by_xpath("//a[@_label='Footer_WeeklyOffers']")
        self.driver.execute_script("arguments[0].scrollIntoView();", WeeklyOffer_button)
        self.driver.execute_script("arguments[0].click();", WeeklyOffer_button)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        WeeklyOffer_button_url = self.driver.current_url
        assert self.url_path in WeeklyOffer_button_url, "Weekly Offer Page URL Not Matched."
        logger.info(': Assertion Weekly Offer Button URL with: ' + WeeklyOffer_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_facebook_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started facebook_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 15, 2)
        parent_window = self.driver.current_window_handle
        Facebook_button = self.driver.find_element_by_xpath("//a[@_label='Facebook']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Facebook_button)
        self.driver.execute_script("arguments[0].click();", Facebook_button)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Facebook_button_url = self.driver.current_url
        # assert self.url_path in Facebook_button_url, "Facebook Page URL Not Matched."
        logger.info(': Assertion Facebook Button URL with: ' + Facebook_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_instagram_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started instagram_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 16, 2)
        parent_window = self.driver.current_window_handle
        Instagram_button = self.driver.find_element_by_xpath("//a[@_label='Instagram']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Instagram_button)
        self.driver.execute_script("arguments[0].click();", Instagram_button)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Instagram_button_url = self.driver.current_url
        # print(self.url_path)
        # print(Instagram_button_url)
        # assert self.url_path in Instagram_button_url, "Instagram Page URL Not Matched."
        logger.info(': Assertion Instagram Button URL with: ' + Instagram_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_twitter_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started twitter_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 17, 2)
        parent_window = self.driver.current_window_handle
        Twitter_button = self.driver.find_element_by_xpath("//a[@_label='Twitter']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Twitter_button)
        self.driver.execute_script("arguments[0].click();", Twitter_button)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Twitter_button_url = self.driver.current_url
        # print(self.url_pat)
        # print(Twitter_button_url)
        # assert self.url_path in Twitter_button_url, "Twitter Page URL Not Matched."
        logger.info(': Assertion Twitter Button URL with: ' + Twitter_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')

    def get_youtube_button_LandingPage_URL_validation(self):
        logger.info(": ##### Started youtube_button URL verification #####")
        self.url_path = ExcelUtil(tc_name="").read_from_excel("FOOTER_URL", 18, 2)
        parent_window = self.driver.current_window_handle
        Youtube_button = self.driver.find_element_by_xpath("// a[@_label='Youtube']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Youtube_button)
        self.driver.execute_script("arguments[0].click();", Youtube_button)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        Youtube_button_url = self.driver.current_url
        # assert self.url_path in Youtube_button_url, "Youtube Page URL Not Matched."
        logger.info(': Assertion YouTube Button URL with: ' + Youtube_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info(': #####  Verification Complete  #####\n')










