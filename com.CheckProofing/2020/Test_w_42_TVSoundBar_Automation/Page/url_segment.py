import json
from urllib.parse import urlparse, parse_qs
import sys
import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from Utility_Files import ReadConfig
from Utility_Files.HTMLTestRunner import stdout_redirector
logger = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class baseCLass:
    driver = None

    def window_handle(self):
        self.wait = WebDriverWait(self.driver, 10)
        parent_window = self.driver.current_window_handle
        payover = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@_label='Pay_Over_Time_Title'])[1]")))
        self.driver.execute_script("arguments[0].scrollIntoView();", payover)
        self.driver.execute_script("arguments[0].click();", payover)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        # self.wait.until(EC.number_of_windows_to_be(child_window))
        self.driver.switch_to.window(child_window)
        self.paylater_url = self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        return self.paylater_url

# def url_segment():
#     final_json = {}
#     final_array = []
#     bpid_array = []
#     final_bpid = {}
#     dir_name = "../OutputT/"
#     test = os.listdir(dir_name)
#     for item in test:
#         if item.endswith(".json"):
#             os.remove(os.path.join(dir_name, item))
#     with open('../Test_w_42_PrimeDay_Disrupt/URLFolder/UniqueList.txt')as f:
#         urls = f.read().splitlines()
#         for url in urls:
#                 parsed_url = urlparse(url)
#                 pair = parse_qs(parsed_url.query)
#                 bpidValue = pair.get('bpid')
#                 pair['url_deep_link'] = url.split()
#                 bpid_array.append(bpidValue)
#                 final_array.append(pair)
#         final_json['check_list'] = final_array
#         final_bpid['bpid_list'] = bpid_array
#         final_json = json.dumps(final_json, indent=4, sort_keys=False)
#         final_bpid = json.dumps(final_bpid, indent=4, sort_keys=False)
#         f = open("../OutputT/OutResult.json", "w")
#         f.write(final_json)
#         logger.info(": Printing URL Segment values Below:" + final_json)
#         f.close()
#         f = open("../OutputT/bpIdList.json", "w")
#         f.write(final_bpid)
#         logger.info(": Printing BPID Below:" + final_bpid)
#         f.close()
#
#
# def segment_validation():
#
#     with open('../OutputT/OutResult.json', 'r')as jsonfile:
#
#         readdata=json.load(jsonfile)
#         if ReadConfig.read_w42_PrimeDay_configData('PrimeDataGEN', 'utm_source') in readdata['check_list'][0]['utm_source']:
#             logger.info(": utm_source matched")
#         else:
#             logger.info(": utm_source NOT matched")
#         if ReadConfig.read_w42_PrimeDay_configData('PrimeDataGEN', 'utm_medium') in readdata['check_list'][0]['utm_medium']:
#             logger.info(": utm_medium matched")
#         else:
#             logger.info(": utm_medium NOT matched")
#         if ReadConfig.read_w42_PrimeDay_configData('PrimeDataGEN', 'cid') in readdata['check_list'][0]['cid']:
#             logger.info(": cid matched")
#         else:
#             logger.info(": cid NOT matched")
#         if ReadConfig.read_w42_PrimeDay_configData('PrimeDataGEN', 'bpid') in readdata['check_list'][0]['bpid']:
#             logger.info(": bpid matched")
#         else:
#             logger.info(": bpid NOT matched")









