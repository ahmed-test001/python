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


class HTMLPage_W_38_Fold2_GenericTest(unittest.TestCase):
    driver = None
    url_list=[]
    method_list_in_Url=[]

    @classmethod
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver1'), options=option)
        warnings.filterwarnings(action="ignore",message="unclosed",category=ResourceWarning)
        self.driver.get(ReadConfig.read_w38_S7_Fold2_configData('Fold2Generic', 'html_path_Fold2_Generic'))


    @classmethod
    def tearDown(self):
        self.driver.quit()


    @classmethod
    def test_a_pre_subjectLine_text_validation(self):
        logger.info(': '+self.test_a_pre_subjectLine_text_validation.__name__ + "\n #####  Starting TEST  ##### ")
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        assert ReadConfig.read_w38_S7_Fold2_configData('Fold2Generic', 'subject_line_Fold2_Generic') in subjectlineTxt
        logger.info(": Pre-Header text assert with : " + ReadConfig.read_w38_S7_Fold2_configData('Fold2Generic', 'subject_line_Fold2_Generic'))
        logger.info('####  TEST Complete  ####')

    def test_b_pre_header_text_validation(self):
        logger.info(': '+self.test_b_pre_header_text_validation.__name__ + "\n #####  Starting TEST  ##### ")
        pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
        print(pheaderTxt)
        assert "Plus, don't miss up to $500 with trade-in‡" in pheaderTxt
        logger.info(": Pre-Header text assert with : " + pheaderTxt)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_c_get_sub_pre_header_link_validation(self):
        logger.info(': '+self.test_c_get_sub_pre_header_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("(//a[@target='_blank'])[4]")
        linkT.click()
        time.sleep(2)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        url2 = self.driver.current_url
        time.sleep(1)
        self.url_list.append(url2)
        self.method_list_in_Url.append(self.test_c_get_sub_pre_header_link_validation.__name__)
        assert ReadConfig.read_w38_S7_Fold2_configData('Fold2Generic', 'url_Fold2_Generic') in url2
        self.driver.close()
        logger.info(": Reference URL: " + url2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')
    @classmethod
    def test_d_get_galaxyNote20_eligible_tradein_link_validation(self):
        logger.info(': '+self.test_d_get_galaxyNote20_eligible_tradein_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("//*[@_label='Hero_Text']")
        linkT.click()
        time.sleep(2)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        url3 = self.driver.current_url
        time.sleep(1)
        self.url_list.append(url3)
        self.method_list_in_Url.append(self.test_d_get_galaxyNote20_eligible_tradein_link_validation.__name__)
        assert ReadConfig.read_w38_S7_Fold2_configData('Fold2Generic', 'url_Fold2_Generic') in url3
        self.driver.close()
        logger.info(": Reference URL: " + url3)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_e_CTA_link_validation(self):
        logger.info(': '+self.test_e_CTA_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("//*[@id='_x0000_i1036']")
        linkT.click()
        time.sleep(2)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        url5 = self.driver.current_url
        time.sleep(1)
        self.url_list.append(url5)
        self.method_list_in_Url.append(self.test_e_CTA_link_validation.__name__)
        assert ReadConfig.read_w38_S7_Fold2_configData('Fold2Generic', 'url_Fold2_Generic') in url5
        self.driver.close()
        logger.info(": Reference URL: " + url5)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_f_get_redeem_credit_link_validation(self):
        logger.info(': '+self.test_f_get_redeem_credit_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("//*[@id='_x0000_i1039']")
        linkT.click()
        time.sleep(2)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        url6 = self.driver.current_url
        time.sleep(1)
        self.url_list.append(url6)
        self.method_list_in_Url.append(self.test_f_get_redeem_credit_link_validation.__name__)
        assert ReadConfig.read_w38_S7_Fold2_configData('Fold2Generic', 'url_Fold2_Generic') in url6
        self.driver.close()
        logger.info(": Reference URL: " + url6)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_g_powerPhone_WorknPlay_link_validation(self):
        logger.info(': '+self.test_g_powerPhone_WorknPlay_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("//*[@id='_x0000_i1042']")
        linkT.click()
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        url9 = self.driver.current_url
        time.sleep(2)
        self.url_list.append(url9)
        self.method_list_in_Url.append(self.test_g_powerPhone_WorknPlay_link_validation.__name__)
        assert ReadConfig.read_w38_S7_Fold2_configData('Fold2Generic', 'url_Fold2_Generic') in url9
        self.driver.close()
        logger.info(": Reference URL: " + url9)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_h_ownS7_link_validation(self):
        logger.info(': '+self.test_h_ownS7_link_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("//*[@id='_x0000_i1045']")
        linkT.click()
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        url10 = self.driver.current_url
        time.sleep(2)
        self.url_list.append(url10)
        self.method_list_in_Url.append(self.test_h_ownS7_link_validation.__name__)
        assert ReadConfig.read_w38_S7_Fold2_configData('Fold2Generic', 'url_Fold2_Generic') in url10
        self.driver.close()
        logger.info(": Reference URL: " + url10)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_i_verify_pay_later_icon(self):
        logger.info(': ' + self.test_i_verify_pay_later_icon.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        payHere_link = self.driver.find_element_by_xpath("//a[@_label='Pay_Over_Time_Title']")
        payHere_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage', 'pay_later') in self.driver.title
        logger.info(': Assertion Pay Later with: ' + self.driver.title)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_j_verify_free_shipping_icon(self):
        logger.info(': ' + self.test_j_verify_free_shipping_icon.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        freeShipping_link = self.driver.find_element_by_xpath("//a[@_label='Free_Returns_Title']")
        freeShipping_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage', 'free_shipping') in self.driver.title
        logger.info(': Assertion Free Shipping with: ' + self.driver.title)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_k_verify_get_rewarded_icon(self):
        logger.info(': ' + self.test_k_verify_get_rewarded_icon.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        getRewarded_link = self.driver.find_element_by_xpath("//a[@_label='Get_Rewarded_Title']")
        getRewarded_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage', 'get_rewarded') in self.driver.title
        logger.info(': Assertion Get Rewarded with: ' + self.driver.title)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_l_verify_google_play_button(self):
        logger.info(': ' + self.test_l_verify_google_play_button.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        googlePlay_link = self.driver.find_element_by_xpath("//a[@_label='Download_App_Google']")
        googlePlay_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage', 'google_play') in self.driver.title
        logger.info(': Assertion Google Play Button with: ' + self.driver.title)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_m_verify_apple_store_button(self):
        logger.info(': ' + self.test_m_verify_apple_store_button.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        googlePlay_link = self.driver.find_element_by_xpath("(//img[@class='fluid custom5'])[2]")
        googlePlay_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert "Shop Samsung on the App Store" in self.driver.title
        logger.info(': Assertion Apple Store with: ' + self.driver.title)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_n_verify_free_shipping_details_button(self):
        logger.info(': ' + self.test_n_verify_free_shipping_details_button.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        freeShippingdetails_link = self.driver.find_element_by_xpath("(//img[@class='fluid custom7'])[1]")
        freeShippingdetails_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage', 'free_shipping') in self.driver.title
        logger.info(': Assertion Free Shipping Button with: ' + self.driver.title)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_o_verify_mobile_button(self):
        logger.info(': ' + self.test_o_verify_mobile_button.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        mobile_link = self.driver.find_element_by_xpath("(//img[@class='fluid custom7'])[2]")
        mobile_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage', 'mobile_button') in self.driver.title
        logger.info(': Assertion Mobile Button with: ' + self.driver.title)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_p_verify_TV_Audio_button(self):
        logger.info(' ##### ' + self.test_p_verify_TV_Audio_button.__name__ + "\n #####  Starting TEST  ##### ")
        #time.sleep(2)
        parent_window = self.driver.current_window_handle
        TV_Audio_link = self.driver.find_element_by_xpath("//img[@class ='fluid custom7 custom7']")
        TV_Audio_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage', 'TV_Audio_button') in self.driver.title
        logger.info(': Assertion Tv & Audio Button with: ' + self.driver.title)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_q_verify_computing_button(self):
        logger.info(': ' + self.test_q_verify_computing_button.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        computing_link = self.driver.find_element_by_xpath("(//img[@class='fluid custom7'])[3]")
        computing_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage', 'computing_button') in self.driver.title
        logger.info(': Assertion Computing Button with: ' + self.driver.title)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_r_verify_appliances_button(self):
        logger.info(': ' + self.test_r_verify_appliances_button.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        appliances_link = self.driver.find_element_by_xpath("(//img[@class='fluid custom7'])[4]")
        appliances_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage', 'appliances_button') in self.driver.title
        logger.info(': Assertion Appliances Button with: ' + self.driver.title)
        self.driver.close()
        # time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_s_verify_weekly_offer_button(self):
        logger.info(': ' + self.test_s_verify_weekly_offer_button.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        weeklyDeals_link = self.driver.find_element_by_xpath("(//img[@class='fluid custom7'])[5]")
        weeklyDeals_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage', 'weekly_offer_button') in self.driver.title
        logger.info(': Assertion Weekly Deals Button with: ' + self.driver.title)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_t_verify_facebook_button(self):
        logger.info(': ' + self.test_t_verify_facebook_button.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        facebook = self.driver.find_element_by_xpath("//a[@_label='Facebook']")
        self.driver.execute_script("arguments[0].scrollIntoView();", facebook)
        self.driver.execute_script("arguments[0].click();", facebook)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage', 'facebook') in self.driver.title
        logger.info(': Assertion Facebook Button with: ' + self.driver.title)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_u_verify_instagram_button(self):
        logger.info(': ' + self.test_u_verify_instagram_button.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        Instagram = self.driver.find_element_by_xpath("//a[@_label='Instagram']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Instagram)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", Instagram)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert "Samsung Mobile USA (@samsungmobileusa) • Instagram photos and videos" in self.driver.title
        logger.info(': Assertion Facebook Button with: ' + self.driver.title)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_v_verify_twitter_button(self):
        logger.info(': ' + self.test_v_verify_twitter_button.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        Twitter = self.driver.find_element_by_xpath("//a[@_label='Twitter']")
        self.driver.execute_script("arguments[0].scrollIntoView();", Twitter)
        self.driver.execute_script("arguments[0].click();", Twitter)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage', 'twitter') in self.driver.title
        logger.info(': Assertion Facebook Button with: ' + self.driver.title)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_w_verify_youtube_button(self):
        logger.info(': ' + self.test_w_verify_youtube_button.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        youtube = self.driver.find_element_by_xpath("// a[@_label='Youtube']")
        self.driver.execute_script("arguments[0].scrollIntoView();", youtube)
        self.driver.execute_script("arguments[0].click();", youtube)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage', 'youtube') in self.driver.title
        logger.info(': Assertion Facebook Button with: ' + self.driver.title)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_x_get_pre_headerlink_validation(self):
        logger.info(': '+self.test_x_get_pre_headerlink_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]")
        linkT.click()
        time.sleep(2)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        url1 = self.driver.current_url
        time.sleep(1)
        self.url_list.append(url1)
        self.method_list_in_Url.append(self.test_x_get_pre_headerlink_validation.__name__)
        assert ReadConfig.read_w38_S7_Fold2_configData('Fold2Generic', 'url_Fold2_Generic') in url1
        self.driver.close()
        logger.info(": Reference URL: " + url1)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_y1_S7_CTA_validation(self):
        logger.info(': '+self.test_y1_S7_CTA_validation.__name__ + "\n #####  Starting TEST  ##### ")
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("//*[@id='_x0000_i1045']")
        linkT.click()
        time.sleep(2)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        shoptypetxt=self.driver.find_element_by_xpath("(//*[@class='button  PRE-ORDER'])[1]").text
        time.sleep(5)
        assert ReadConfig.read_w38_S7_Fold2_configData('WEBPage', 'ShopTypeText2') in shoptypetxt
        self.driver.close()
        logger.info(": Assertion S7 CTA Text: " + shoptypetxt)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_y_collect_unique_URL_with_method_Name(self):
        logger.info(' ##### ' + self.test_y_collect_unique_URL_with_method_Name.__name__ + "\n #####  Starting TEST  ##### ")
        with open('../TextFolder/TestOut_UniqueURLDictFile.txt', 'w')as f:
            res_dct = dict(zip(self.method_list_in_Url,self.url_list))
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

    @classmethod
    def test_z_get_unique_URL_list(self):
        logger.info(' ##### ' + self.test_z_get_unique_URL_list.__name__ + "\n #####  Starting TEST  ##### ")
        with open('../TextFolder/Test_InputFile_URLSegment.txt', 'w')as f:
            unique_list = []
            for x in self.url_list:
                # check unique_list or not
                if x not in unique_list:
                    unique_list.append(x)

            for x in unique_list:
                someline = x+'\n'
                f.writelines(someline)
                logger.info("##### Get unique URL List:  "+x)
        logger.info('####  TEST Complete  ####')


if __name__ == '__main__':
    unittest.main()