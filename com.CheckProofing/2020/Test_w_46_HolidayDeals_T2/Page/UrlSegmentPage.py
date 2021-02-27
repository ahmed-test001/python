import glob
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

class URLSegemntPage:
    unique_list = []
    @staticmethod
    def get_segment():
        final_json = {}
        final_array = []
        bpid_array = []
        final_bpid = {}
        dir_name = "../OutputT/"
        test = os.listdir(dir_name)
        for item in test:
            if item.endswith(".json"):
                os.remove(os.path.join(dir_name, item))
        with open('../TextFolder_Unique_URL/UniqueList.txt')as f:
            urls = f.read().splitlines()
            for url in urls:
                parsed_url = urlparse(url)
                pair = parse_qs(parsed_url.query)
                bpidValue = pair.get('bpid')
                pair['url_deep_link'] = url.split()
                bpid_array.append(bpidValue)
                final_array.append(pair)
            final_json['check_list'] = final_array
            final_bpid['bpid_list'] = bpid_array
            final_json = json.dumps(final_json, indent=4, sort_keys=False)
            # final_bpid = json.dumps(final_bpid, indent=4, sort_keys=False)
            f = open("../OutputT/OutResult.json", "w")
            f.write(final_json)
            logger.info(": Printing URL Segment values Below:" + final_json)
            f.close()
            # f = open("../OutputT/bpIdList.json", "w")
            # f.write(final_bpid)
            # logger.info(": Printing BPID Below:" + final_bpid)
            # f.close()








