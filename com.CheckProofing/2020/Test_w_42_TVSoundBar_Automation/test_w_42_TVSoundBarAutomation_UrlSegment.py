import json
from urllib.parse import urlparse, parse_qs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import sys
import os
import logging
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from Utility_Files import ReadConfig
from Utility_Files.HTMLTestRunner import stdout_redirector
logger = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class URLSegment_W_42_TVSoundBarAutomation_Test(unittest.TestCase):

    def test_UrlSegmentvalidation(self):
        logger.info(': ' + self.test_UrlSegmentvalidation.__name__ + "\n #####  Starting TEST  ##### ")
        final_json = {}
        final_array = []
        bpid_array = []
        final_bpid = {}
        dir_name = "../OutputT/"
        test = os.listdir(dir_name)
        for item in test:
            if item.endswith(".json"):
                os.remove(os.path.join(dir_name, item))
        with open('../TextFolder/TestIn_UniqueURL_List.txt')as f:
            # urls = f.readline().split()
            urls = f.read().splitlines()
            for url in urls:

                if ReadConfig.read_w42_TVSoundBarAutomation_configData('TVSoundBarData', 'url') in url:
                    try:
                        option = webdriver.ChromeOptions()
                        option.add_experimental_option('excludeSwitches', ['enable-logging'])
                        self.driver = webdriver.Chrome(executable_path='../Drivers/chromedriver_01.exe', options=option)
                        self.driver.get(url)
                        txt = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "(//div[@class ='device-label'])[2]"))).text
                        txt1 = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//p[@class ='title']"))).text
                        self.driver.quit()
                    except:
                        try:
                            txt = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='title'])[2]"))).text
                            if len(txt) == 0:
                                txt = "No Device Present"
                            txt1 = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//p[@class ='title']"))).text
                        except:
                            txt = "No Device Present"
                            txt1 = "Title Promo not Available"
                    parsed_url = urlparse(url)
                    pair = parse_qs(parsed_url.query)
                    bpidValue = pair.get('bpid')
                    pair['tradeIn_ModelName'] = txt.split(',')
                    pair['preorder_text_banner'] = txt1.split(',')
                    pair['url_deep_link'] = url.split()
                    bpid_array.append(bpidValue)
                    final_array.append(pair)
                    self.driver.quit()
            final_json['check_list'] = final_array
            final_bpid['bpid_list'] = bpid_array
            final_json = json.dumps(final_json, indent=4, sort_keys=False)
            final_bpid = json.dumps(final_bpid, indent=4, sort_keys=False)
            f = open("../OutputT/OutResult.json", "w")
            f.write(final_json)
            logger.info(": Printing URL Segment values:" + final_json)
            f.close()
            f = open("../OutputT/bpIdList.json", "w")
            f.write(final_bpid)
            logger.info(": Printing BPID:" + final_bpid)
            f.close()

        logger.info('####  TEST Complete  ####')

    def test_segment_validation(self):
        logger.info(': ' + self.test_segment_validation.__name__ + "\n #####  Starting TEST  ##### ")
        with open('../OutputT/OutResult.json', 'r')as jsonfile:
            readdata=json.load(jsonfile)
            if ReadConfig.read_w42_TVSoundBarAutomation_configData('TVSoundBarData', 'promocode') in readdata['check_list'][0]['promoCode']:
                logger.info(": promocode matched")
            else:
                logger.info(": promocode NOT matched")
            if ReadConfig.read_w42_TVSoundBarAutomation_configData('TVSoundBarData', 'marsLinkCategory') in readdata['check_list'][0]['marsLinkCategory']:
                logger.info(": marsLinkCategory matched")
            else:
                logger.info(": marsLinkCategory NOT matched")
            if ReadConfig.read_w42_TVSoundBarAutomation_configData('TVSoundBarData', 'cid') in readdata['check_list'][0]['CID']:
                logger.info(": cid matched")
            else:
                logger.info(": cid NOT matched")
            if ReadConfig.read_w42_TVSoundBarAutomation_configData('TVSoundBarData', 'bpid') in readdata['check_list'][0]['bpid']:
                logger.info(": bpid matched")
            else:
                logger.info(": bpid NOT matched")
            if ReadConfig.read_w42_TVSoundBarAutomation_configData('TVSoundBarData', 'utm_source') in readdata['check_list'][0]['utm_source']:
                logger.info(": utm_source matched")
            else:
                logger.info(": utm_source NOT matched")
            if ReadConfig.read_w42_TVSoundBarAutomation_configData('TVSoundBarData', 'utm_medium') in readdata['check_list'][0]['utm_medium']:
                logger.info(": utm_medium matched")
            else:
                logger.info(": utm_medium NOT matched")
        logger.info('####  TEST Complete  ####')


if __name__ == '__main__':
    unittest.main()

