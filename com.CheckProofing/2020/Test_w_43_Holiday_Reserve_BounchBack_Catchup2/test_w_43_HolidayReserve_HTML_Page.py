import time
import unittest
import sys
import os
import logging
import warnings
from selenium import webdriver
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Utility_Files import ReadConfig
from Utility_Files.HTMLTestRunner import stdout_redirector
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class HTMLPage_W_43_HolidayReserve_Test(unittest.TestCase):
    driver = None
    url_list = []
    method_list_in_Url = []

    @classmethod
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver1'), options=option)
        warnings.filterwarnings(action="ignore",message="unclosed",category=ResourceWarning)
        self.driver.get(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('RH_DATA','html_path'))

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_a1_subjectLine_text_validation(self):
        logger.info(': '+self.test_a1_subjectLine_text_validation.__name__ + "\n #####  Starting TEST  ##### ")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        self.assertIn(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('RH_DATA', 'subject_line'), subjectlineTxt,
                      msg="Subject Line Text Not Matching")
        logger.info(": Subject Line text assert with : " + ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('RH_DATA', 'subject_line'))
        logger.info('####  TEST Complete  ####')

    def test_a2_pre_header_text_validation(self):
        logger.info(': '+self.test_a2_pre_header_text_validation.__name__ + "\n #####  Starting TEST  ##### ")
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        self.assertEqual(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('RH_DATA', 'pre_headertext'), pheaderTxt, msg="Pre Header Text Not Matching")
        logger.info(": Pre-Header text assert with : " + pheaderTxt)
        logger.info('####  TEST Complete  ####')

    def test_a3_pre_header_link_validation(self):
        logger.info(': '+self.test_a3_pre_header_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("(//*[@target='_blank'])[1]")
        linkT.click()
        time.sleep(2)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        Pre_Header_URL = self.driver.current_url
        time.sleep(1)
        self.url_list.append(Pre_Header_URL)
        self.method_list_in_Url.append(self.test_a3_pre_header_link_validation.__name__)
        self.assertEqual(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('RH_DATA', 'url'), Pre_Header_URL, msg="Web Landing Page URL is not Matching by Pre_Header_URL")
        self.driver.close()
        logger.info(": Reference URL: " + Pre_Header_URL)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_a4_Hero_SignUpForSavings_link_validation(self):
        logger.info(': '+self.test_a4_Hero_SignUpForSavings_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("//*[@id='_x0000_i1032']")
        linkT.click()
        time.sleep(2)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        Signup_URL = self.driver.current_url
        time.sleep(1)
        self.url_list.append(Signup_URL)
        self.method_list_in_Url.append(self.test_a4_Hero_SignUpForSavings_link_validation.__name__)
        self.assertEqual(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('RH_DATA', 'url'), Signup_URL, msg="Web Landing Page URL is not Matching by Pre Order_Now_URL")
        self.driver.close()
        logger.info(": Reference URL: " + Signup_URL)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_a5_Module2_ShopNow_link_validation(self):
        logger.info(': '+self.test_a5_Module2_ShopNow_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("//*[@id='_x0000_i1035']")
        linkT.click()
        time.sleep(2)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        ShopNow_URL = self.driver.current_url
        time.sleep(1)
        self.url_list.append(ShopNow_URL)
        self.method_list_in_Url.append(self.test_a5_Module2_ShopNow_link_validation.__name__)
        self.assertEqual(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('RH_DATA', 'url'), ShopNow_URL, msg="Web Landing Page URL is not Matching by Pre Order_Now_URL")
        self.driver.close()
        logger.info(": Reference URL: " + ShopNow_URL)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_b1_pay_later_icon_LandingPage_URL_validation(self):
        logger.info(
            ': ' + self.test_b1_pay_later_icon_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        payover = self.driver.find_element_by_xpath("//a[@_label='Pay_Over_Time_Title']")
        self.driver.execute_script("arguments[0].scrollIntoView();", payover)
        self.driver.execute_script("arguments[0].click();", payover)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        paylater_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('EMAILPage', 'pay_later_url'), paylater_url,
                      msg="Pay Later Landing Page URL is not Matched.")
        logger.info(': Assertion Pay Later with: ' + paylater_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_b2_free_shipping_icon_LandingPage_URL_validation(self):
        logger.info(
            ': ' + self.test_b2_free_shipping_icon_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        freeShipping = self.driver.find_element_by_xpath("//a[@_label='Free_Shipping_Title']")
        self.driver.execute_script("arguments[0].scrollIntoView();", freeShipping)
        self.driver.execute_script("arguments[0].click();", freeShipping)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        freeShipping_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('EMAILPage', 'free_shipping_url'), freeShipping_url,
                      msg="Free Shipping Landing Page URL is not Matched.")
        logger.info(': Assertion Free SHipping with: ' + freeShipping_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_b3_GetRewarded_icon_LandingPage_URL_validation(self):
        logger.info(
            ': ' + self.test_b3_GetRewarded_icon_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        freeShipping = self.driver.find_element_by_xpath("//*[@_label='Get_Rewarded_Title']")
        self.driver.execute_script("arguments[0].scrollIntoView();", freeShipping)
        self.driver.execute_script("arguments[0].click();", freeShipping)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        getRewarded_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('EMAILPage', 'get_rewarded_url'), getRewarded_url,
                      msg="Get Rewarded Landing Page URL is not Matched.")
        logger.info(': Assertion Get Rewarded with: ' + getRewarded_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_c1_google_play_button_LandingPage_URL_validation(self):
        logger.info(
            ': ' + self.test_c1_google_play_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        googleApp = self.driver.find_element_by_xpath("//a[@_label='Download_App_Google']")
        self.driver.execute_script("arguments[0].scrollIntoView();", googleApp)
        self.driver.execute_script("arguments[0].click();", googleApp)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        googleApp_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('EMAILPage', 'google_play_url'), googleApp_url,
                      msg="Google Play store Page URL Not Matched.")
        logger.info(': Assertion Free Google Play App with: ' + googleApp_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_c2_apple_store_button_LandingPage_URL_validation(self):
        logger.info(
            ': ' + self.test_c2_apple_store_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        appleApp = self.driver.find_element_by_xpath("//a[@_label='Download_App_Apple']")
        self.driver.execute_script("arguments[0].scrollIntoView();", appleApp)
        self.driver.execute_script("arguments[0].click();", appleApp)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        appleApp_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('EMAILPage', 'apple_url'), appleApp_url,
                      msg="Apple App Page URL Not Matched.")
        logger.info(': Assertion Free Apple App with: ' + appleApp_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_d1_free_shipping_details_button_LandingPage_URL_validation(self):
        logger.info(
            ': ' + self.test_d1_free_shipping_details_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        freeShip_button = self.driver.find_element_by_xpath("//a[@_label='Footer_Free_Shipping_Details']")
        self.driver.execute_script("arguments[0].scrollIntoView();", freeShip_button)
        self.driver.execute_script("arguments[0].click();", freeShip_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        freeShip_button_url = self.driver.current_url
        time.sleep(5)
        self.assertEqual(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('EMAILPage', 'free_shipping_url'), freeShip_button_url,
                         msg="Free Shipping Page URL Not Matched.")
        logger.info(': Assertion Free Ship Button URL with: ' + freeShip_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_d2_Mobile_button_LandingPage_URL_validation(self):
        logger.info(
            ': ' + self.test_d2_Mobile_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        freeShip_button = self.driver.find_element_by_xpath("//*[@_label='Footer_Mobile']")
        self.driver.execute_script("arguments[0].scrollIntoView();", freeShip_button)
        self.driver.execute_script("arguments[0].click();", freeShip_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        mobile_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('EMAILPage', 'mobile_button_url'), mobile_button_url,
                      msg="Mobile Page URL Not Matched.")
        logger.info(': Assertion Mobile Button URL with: ' + mobile_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_d3_TV_Audio_button_LandingPage_URL_validation(self):
        logger.info(
            ': ' + self.test_d3_TV_Audio_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        Audio_button = self.driver.find_element_by_xpath("//a[@_label='Footer_TV_Audio']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Audio_button)
        self.driver.execute_script("arguments[0].click();", Audio_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        Tv_Audio_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('EMAILPage', 'tv_audio_button_url'), Tv_Audio_button_url,
                      msg="TV & Audio Page URL Not Matched.")
        logger.info(': Assertion TV & Audio Button URL with: ' + Tv_Audio_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_d4_computing_button_LandingPage_URL_validation(self):
        logger.info(
            ': ' + self.test_d4_computing_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        Computing_button = self.driver.find_element_by_xpath("//a[@_label='Footer_Computing']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Computing_button)
        self.driver.execute_script("arguments[0].click();", Computing_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        Computing_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('EMAILPage', 'computing_button_url'), Computing_button_url,
                      msg="Computing Page URL Not Matched.")
        logger.info(': Assertion Computing Button URL with: ' + Computing_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_d5_appliances_button_LandingPage_URL_validation(self):
        logger.info(
            ': ' + self.test_d5_appliances_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        Appliance_button = self.driver.find_element_by_xpath("//a[@_label='Footer_Appliances']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Appliance_button)
        self.driver.execute_script("arguments[0].click();", Appliance_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        Appliance_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('EMAILPage', 'appliances_button_url'), Appliance_button_url,
                      msg="Appliance Page URL Not Matched.")
        logger.info(': Assertion Appliance Button URL with: ' + Appliance_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_d6_weekly_offer_button_LandingPage_URL_validation(self):
        logger.info(
            ': ' + self.test_d6_weekly_offer_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        WeeklyOffer_button = self.driver.find_element_by_xpath("//a[@_label='Footer_WeeklyOffers']")
        self.driver.execute_script("arguments[0].scrollIntoView();", WeeklyOffer_button)
        self.driver.execute_script("arguments[0].click();", WeeklyOffer_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        WeeklyOffer_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('EMAILPage', 'weekly_offer_button_url'),
                      WeeklyOffer_button_url, msg="Weekly Offer Page URL Not Matched.")
        logger.info(': Assertion Weekly Offer Button URL with: ' + WeeklyOffer_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_e1_facebook_button_LandingPage_URL_validation(self):
        logger.info(
            ': ' + self.test_e1_facebook_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        Facebook_button = self.driver.find_element_by_xpath("//a[@_label='Facebook']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Facebook_button)
        self.driver.execute_script("arguments[0].click();", Facebook_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        Facebook_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('EMAILPage', 'facebook_url'), Facebook_button_url,
                      msg="Facebook Page URL Not Matched.")
        logger.info(': Assertion Facebook Button URL with: ' + Facebook_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_e2_instagram_button_LandingPage_URL_validation(self):
        logger.info(
            ': ' + self.test_e2_instagram_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        Instagram_button = self.driver.find_element_by_xpath("//a[@_label='Instagram']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Instagram_button)
        self.driver.execute_script("arguments[0].click();", Instagram_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        Instagram_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('EMAILPage', 'instagram_url'), Instagram_button_url,
                      msg="Instagram Page URL Not Matched.")
        logger.info(': Assertion Instagram Button URL with: ' + Instagram_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_e3_twitter_button_LandingPage_URL_validation(self):
        logger.info(
            ': ' + self.test_e3_twitter_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        Twitter_button = self.driver.find_element_by_xpath("//a[@_label='Twitter']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Twitter_button)
        self.driver.execute_script("arguments[0].click();", Twitter_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        Twitter_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('EMAILPage', 'twitter_url'), Twitter_button_url,
                      msg="Twitter Page URL Not Matched.")
        logger.info(': Assertion Twitter Button URL with: ' + Twitter_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_e4_youtube_button_LandingPage_URL_validation(self):
        logger.info(
            ': ' + self.test_e4_youtube_button_LandingPage_URL_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        Youtube_button = self.driver.find_element_by_xpath("// a[@_label='Youtube']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Youtube_button)
        self.driver.execute_script("arguments[0].click();", Youtube_button)
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        Youtube_button_url = self.driver.current_url
        time.sleep(5)
        self.assertIn(ReadConfig.read_w43_HolidayRsv_BounchBck_Catch2_configData('EMAILPage', 'youtube_url'), Youtube_button_url,
                      msg="Youtube Page URL Not Matched.")
        logger.info(': Assertion YouTube Button URL with: ' + Youtube_button_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    def test_f1_collect_unique_URL_with_method_Name(self):
        logger.info(
            ' ##### ' + self.test_f1_collect_unique_URL_with_method_Name.__name__ + "\n #####  Starting TEST  ##### ")
        with open('../TextFolder/TestOut_UniqueURL_DictList.txt', 'w')as f:
            res_dct = dict(zip(self.method_list_in_Url, self.url_list))
            temp = []
            res = dict()
            for key, val in res_dct.items():
                if val not in temp:
                    temp.append(val)
                    res[key] = val
            # print(res)
            f.writelines(str(res))
            logger.info("### Collected Unique URL with Method Name: " + str(res) + "\n")
        logger.info('####  TEST Complete  ####')

    def test_f2_get_unique_URL_list(self):
        logger.info(' ##### ' + self.test_f2_get_unique_URL_list.__name__ + "\n #####  Starting TEST  ##### ")
        with open('../TextFolder/TestIn_UniqueURL_List.txt', 'w')as f:
            unique_list = []
            for x in self.url_list:
                # check unique_list or not
                if x not in unique_list:
                    unique_list.append(x)

            for x in unique_list:
                someline = x + '\n'
                f.writelines(someline)
                logger.info("##### Get unique URL List:  " + x)
        logger.info('####  TEST Complete  ####')


if __name__ == '__main__':
    unittest.main()