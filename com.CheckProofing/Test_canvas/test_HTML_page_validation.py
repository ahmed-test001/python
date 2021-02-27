import configparser
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


class HTMLPageTest(unittest.TestCase):
    driver = None
    url_list=[]
    method_list_in_Url=[]

    @classmethod
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver1'),
                                       options=option)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        self.driver.get(ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'url_req1'))
        # config = configparser.ConfigParser()
        # config.read("../ConfigData/test_canvas.ini")
        # valuelist = list(config['HTMLPage'].values())
        # for url in valuelist:
        # # with open('../TextFolder/URLS.txt','r')as f:
        # #     url = f.read().splitlines()
        #     option = webdriver.ChromeOptions()
        #     option.add_experimental_option('excludeSwitches', ['enable-logging'])
        #     self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths','chromedriver1'),options=option)
        #     warnings.filterwarnings(action="ignore",message="unclosed",category=ResourceWarning)
        #     self.driver.get(url)


    @classmethod
    def tearDown(self):
        self.driver.quit()

    @classmethod
    def test_a_get_pre_headerlinks_URL(self):
        logger.info(' ##### '+self.test_a_get_pre_headerlinks_URL.__name__ + " Execution start  ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]")
        linkText=linkT.text
        linkT.click()
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        url1 = self.driver.current_url
        self.url_list.append(url1)
        self.method_list_in_Url.append(self.test_a_get_pre_headerlinks_URL.__name__)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'pre_headertext') in linkText
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'url') in url1
        self.driver.close()
        logger.info("#### Pre-Header text assert with : " + linkText)
        logger.info("#### Collected assert url: "+ url1)
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_b_get_image1_URL(self):
        logger.info(' ##### '+self.test_b_get_image1_URL.__name__ + " Execution start  ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("(//a[@target='_blank'])[4]")
        linkT.click()
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        url2 = self.driver.current_url
        self.url_list.append(url2)
        self.method_list_in_Url.append(self.test_b_get_image1_URL.__name__)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'url') in url2
        self.driver.close()
        logger.info("#### Collected assert url: "+ url2)
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_c_get_image2_subcopy_URL(self):
        logger.info(' ##### '+self.test_c_get_image2_subcopy_URL.__name__ + " Execution start  ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("(//a[@target='_blank'])[6]")
        linkT.click()
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        url3 = self.driver.current_url
        self.url_list.append(url3)
        self.method_list_in_Url.append(self.test_c_get_image2_subcopy_URL.__name__)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'url') in url3
        self.driver.close()
        logger.info("#### Collected assert url: "+url3)
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_d_get_image3_greatPrice_URL(self):
        logger.info(' ##### '+self.test_d_get_image3_greatPrice_URL.__name__ + " Execution start  ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("//img[@alt='Great pricing options with trade in']")
        linkT.click()
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        url4 = self.driver.current_url
        self.url_list.append(url4)
        self.method_list_in_Url.append(self.test_d_get_image3_greatPrice_URL.__name__)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'url') in url4
        self.driver.close()
        logger.info("#### Collected assert url: "+url4)
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_e_get_preOrder_now_button1_URL(self):
        logger.info(' ##### '+self.test_e_get_preOrder_now_button1_URL.__name__ + " Execution start  ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("(//a[@target='_blank'])[9]")
        linkT.click()
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        url5 = self.driver.current_url
        self.url_list.append(url5)
        self.method_list_in_Url.append(self.test_e_get_preOrder_now_button1_URL.__name__)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'url') in url5
        self.driver.close()
        logger.info("#### Collected assert url: "+url5)
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_f_get_image4_galaxy_ecosystem_pre_order_now_URL(self):
        logger.info(' ##### '+self.test_f_get_image4_galaxy_ecosystem_pre_order_now_URL.__name__ + "Execution start "
                                                                                                   "##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("(//a[@target='_blank'])[11]")
        linkT.click()
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        url6 = self.driver.current_url
        self.url_list.append(url6)
        self.method_list_in_Url.append(self.test_f_get_image4_galaxy_ecosystem_pre_order_now_URL.__name__)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'url') in url6
        self.driver.close()
        logger.info("#### Collected assert url: "+url6)
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_g_get_image5_play_game_URL(self):
        logger.info(' ##### '+self.test_g_get_image5_play_game_URL.__name__ + " Execution start ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("//img[@src='http://t.info.samsungusa.com/res/samsung"
                                                  "/M8_eComm_WK32_Canvas_Reserve_PreOrder_T1_200731_03.png']")
        linkT.click()
        time.sleep(3)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        url7 = self.driver.current_url
        self.url_list.append(url7)
        self.method_list_in_Url.append(self.test_g_get_image5_play_game_URL.__name__)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'url') in url7
        self.driver.close()
        logger.info("#### Collected assert url: "+url7)
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_h_get_preOrder_now_button2_URL(self):
        logger.info(' ##### '+self.test_h_get_preOrder_now_button2_URL.__name__ + " Execution start ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        linkT = self.driver.find_element_by_xpath("(//td[@class='btn-hover'])[2]")
        linkT.click()
        time.sleep(2)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        url8 = self.driver.current_url
        self.url_list.append(url8)
        self.method_list_in_Url.append(self.test_h_get_preOrder_now_button2_URL.__name__)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'url') in url8
        self.driver.close()
        logger.info("#### Collected assert url: "+url8)
        time.sleep(3)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_i_verify_pay_later_icon(self):
        logger.info(' ##### ' + self.test_i_verify_pay_later_icon.__name__ + " Execution start ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        payHere_link = self.driver.find_element_by_xpath("//a[@_label='Pay_Over_Time_Title']")
        payHere_link.click()
        time.sleep(2)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'pay_later') in self.driver.title
        logger.info(' assertion complete with: ' + self.driver.title)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_j_verify_free_shipping_icon(self):
        logger.info(' ##### ' + self.test_j_verify_free_shipping_icon.__name__ + " Execution start ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        freeShipping_link = self.driver.find_element_by_xpath("//a[@_label='Free_Returns_Title']")
        freeShipping_link.click()
        time.sleep(2)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'free_shipping') in self.driver.title
        logger.info(' assertion complete with: ' + self.driver.title)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_k_verify_get_rewarded_icon(self):
        logger.info(' ##### ' + self.test_k_verify_get_rewarded_icon.__name__ + " Execution start ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        getRewarded_link = self.driver.find_element_by_xpath("//a[@_label='Get_Rewarded_Title']")
        getRewarded_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'get_rewarded') in self.driver.title
        logger.info(' assertion complete with: ' + self.driver.title)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_l_verify_google_play_button(self):
        logger.info(' ##### ' + self.test_l_verify_google_play_button.__name__ + " Execution start ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        googlePlay_link = self.driver.find_element_by_xpath("//a[@_label='Download_App_Google']")
        googlePlay_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'google_play') in self.driver.title
        logger.info(' assertion complete with: ' + self.driver.title)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_m_verify_apple_store_button(self):
        logger.info(' ##### ' + self.test_m_verify_apple_store_button.__name__ + " Execution start ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        googlePlay_link = self.driver.find_element_by_xpath("(//img[@class='fluid custom5'])[2]")
        googlePlay_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        print(self.driver.title)
        assert "Shop Samsung on the App Store" in self.driver.title
        # assert ReadConfig.read_test_canvas_Page_configData('HTMLPage','apple') in self.driver.title
        logger.info(' assertion complete with: ' + self.driver.title)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_n_verify_free_shipping_details_button(self):
        logger.info(' ##### ' + self.test_n_verify_free_shipping_details_button.__name__ + " Execution start ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        freeShippingdetails_link = self.driver.find_element_by_xpath("(//img[@class='fluid custom7'])[1]")
        freeShippingdetails_link.click()
        time.sleep(2)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'free_shipping') in self.driver.title
        logger.info(' assertion complete with: ' + self.driver.title)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_o_verify_mobile_button(self):
        logger.info(' ##### ' + self.test_o_verify_mobile_button.__name__ + " Execution start ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        mobile_link = self.driver.find_element_by_xpath("(//img[@class='fluid custom7'])[2]")
        mobile_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'mobile_button') in self.driver.title
        logger.info(' assertion complete with: ' + self.driver.title)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_p_verify_TV_Audio_button(self):
        logger.info(' ##### ' + self.test_p_verify_TV_Audio_button.__name__ + " Execution start ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        TV_Audio_link = self.driver.find_element_by_xpath("//img[@class ='fluid custom7 custom7']")
        TV_Audio_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'TV_Audio_button') in self.driver.title
        logger.info(' assertion complete with: ' + self.driver.title)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_q_verify_computing_button(self):
        logger.info(' ##### ' + self.test_q_verify_computing_button.__name__ + " Execution start ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        TV_Audio_link = self.driver.find_element_by_xpath("(//img[@class='fluid custom7'])[3]")
        TV_Audio_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'computing_button') in self.driver.title
        logger.info(' assertion complete with: ' + self.driver.title)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_r_verify_appliances_button(self):
        logger.info(' ##### ' + self.test_r_verify_appliances_button.__name__ + " Execution start ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        TV_Audio_link = self.driver.find_element_by_xpath("(//img[@class='fluid custom7'])[4]")
        TV_Audio_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'appliances_button') in self.driver.title
        logger.info(' assertion complete with: ' + self.driver.title)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_s_verify_weekly_offer_button(self):
        logger.info(' ##### ' + self.test_s_verify_weekly_offer_button.__name__ + " Execution start ##### ")
        time.sleep(2)
        parent_window = self.driver.current_window_handle
        TV_Audio_link = self.driver.find_element_by_xpath("(//img[@class='fluid custom7'])[5]")
        TV_Audio_link.click()
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)
        assert ReadConfig.read_test_canvas_Page_configData('HTMLPage', 'weekly_offer_button') in self.driver.title
        logger.info(' assertion complete with: ' + self.driver.title)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(parent_window)
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_t_collect_unique_URL_with_method_Name(self):
        logger.info(' ##### ' + self.test_t_collect_unique_URL_with_method_Name.__name__ + " Execution start ##### ")
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
            logger.info("### Collected Unique URL with Method Name: "+str(res))
        logger.info('####  TEST Complete  ####')

    @classmethod
    def test_u_get_unique_URL_list(self):
        logger.info(' ##### ' + self.test_u_get_unique_URL_list.__name__ + " Execution start ##### ")
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