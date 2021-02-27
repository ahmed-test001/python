import json
from urllib.parse import urlparse, parse_qs
import sys
import os
import logging
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from Test_Campaign_2021.scripts.python.Page.BasePageClass import BasePage
from Test_Campaign_2021.scripts.python.Util_Data.ExcelReaderUtil import ExcelUtil
from Test_Campaign_2021.scripts.python.Util_Data.HTMLTestRunner import stdout_redirector
from Test_Campaign_2021.scripts.python.Util_Data import ReadConfig
logger = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class URLSegmentPage(BasePage):
    unique_list = []
    driver = None

    @staticmethod
    def get_segment():
        final_json = {}
        final_array = []
        bpid_array = []
        final_bpid = {}
        dir_name = ReadConfig.readFilePathData('FilePaths', 'json_dir')
        test = os.listdir(dir_name)
        for item in test:
            if item.endswith(".json"):
                os.remove(os.path.join(dir_name, item))
        with open(ReadConfig.readFilePathData('FilePaths', 'json_segment'))as f:
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
            f = open(ReadConfig.readFilePathData('FilePaths', 'json_outResult'), "w")
            f.write(final_json)
            logger.info(": Printing URL Segment values Below:" + final_json)
            f.close()

    @staticmethod
    def get_URL_Segment_validation():
        with open(ReadConfig.readFilePathData('FilePaths', 'json_outResult'), 'r')as jsonfile:
            readdata = json.load(jsonfile)
            if "utm_source" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 3, 2) in readdata['check_list'][0][
                    'utm_source']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 3, 2) in readdata['check_list'][0][
                        'utm_source'], "utm_source Not Matching."
                    logger.info(": utm_source==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 3, 2))
                else:
                    logger.info(": FAIL:: utm_source NOT matched.")
            else:
                logger.info(": utm_source segment NOT present.")
            if "utm_medium" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 4, 2) in readdata['check_list'][0][
                    'utm_medium']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 4, 2) in readdata['check_list'][0][
                        'utm_medium'], "utm_medium Not Matching."
                    logger.info(": utm_medium==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 4, 2))
                else:
                    logger.info(": FAIL:: utm_medium NOT matched.")
            else:
                logger.info(": utm_medium segment NOT present.")
            if "utm_campaign" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 2) in readdata['check_list'][0][
                    'utm_campaign']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 2) in readdata['check_list'][0][
                        'utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": utm_campaign==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 2))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 3) in readdata['check_list'][0][
                    'utm_campaign']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 3) in readdata['check_list'][0][
                        'utm_campaign'], "utm_campaign Not Matching."
                    logger.info(": utm_campaign==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 5, 3))
                else:
                    logger.info(": FAIL:: utm_campaign NOT matched.")
            else:
                logger.info(": utm_campaign segment NOT present.")

            if "marsLinkCategory" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 2) in readdata['check_list'][0][
                    'marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 2) in readdata['check_list'][0][
                        'marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 2))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 3) in readdata['check_list'][0][
                    'marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 3) in readdata['check_list'][0][
                        'marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 3))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 4) in readdata['check_list'][0][
                    'marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 4) in readdata['check_list'][0][
                        'marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 4))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 5) in readdata['check_list'][0][
                    'marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 5) in readdata['check_list'][0][
                        'marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 5))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 6) in readdata['check_list'][0][
                    'marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 6) in readdata['check_list'][0][
                        'marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 6))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 7) in readdata['check_list'][0][
                    'marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 7) in readdata['check_list'][0][
                        'marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 7))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 8) in readdata['check_list'][0][
                    'marsLinkCategory']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 8) in readdata['check_list'][0][
                        'marsLinkCategory'], "marsLinkCategory Not Matching."
                    logger.info(": marsLinkCategory==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 6, 8))
                else:
                    logger.info(": FAIL:: marsLinkCategory NOT matched.")
            else:
                logger.info(": marsLinkCategory segment NOT present.")
            if "cid" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 2) in readdata['check_list'][0]['cid']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 2) in readdata['check_list'][0][
                        'cid'], "cid Not Matching."
                    logger.info(": cid==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 2))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 3) in readdata['check_list'][0]['cid']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 3) in readdata['check_list'][0][
                        'cid'], "cid Not Matching."
                    logger.info(": cid==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 3))
                elif ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 4) in readdata['check_list'][0]['cid']:
                    assert ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 4) in readdata['check_list'][0][
                        'cid'], "cid Not Matching."
                    logger.info(": cid==" + ExcelUtil(tc_name="").read_from_excel("URL_SEGMENT", 7, 4))
                else:
                    logger.info(": FAIL:: cid NOT matched.")
            else:
                logger.info(": cid segment NOT present.")

    @staticmethod
    def get_tradeinDevice_validation():
        logger.info(": ##### Started Trade-in Device validation From Landing Page #####")
        with open(ReadConfig.readFilePathData('FilePaths', 'json_outResult'), 'r')as jsonfile:
            readdata = json.load(jsonfile)
            if "tradeIn" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 4, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 4, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 5, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 5, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 6, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 6, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 7, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 7, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 8, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 8, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 9, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 9, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 10, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 10, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 11, 2) in readdata['check_list'][0]['tradeIn']:
                    # assert "82ac4f16-9db5-4660-8178-6300d0bb3ac3" == readdata['check_list'][0]['tradeIn']
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 11, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 12, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 12, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 13, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 13, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 14, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 14, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 15, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 15, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 16, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 16, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 17, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 17, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 18, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 18, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 19, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 19, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 20, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 20, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 21, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 21, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 22, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 22, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 23, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 23, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 24, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 24, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 25, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 25, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 26, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 26, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 27, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 27, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 28, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 28, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 29, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 29, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 30, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 30, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 31, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 31, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 32, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 32, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 33, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 33, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 34, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 34, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 35, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 35, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 36, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 36, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 37, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 37, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 38, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 38, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 39, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 39, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 40, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 40, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 41, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 41, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 42, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 42, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 43, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 43, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 44, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 44, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 45, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 45, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 46, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 46, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 47, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 47, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 48, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 48, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 49, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 49, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 50, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 50, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 51, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 51, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 52, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 52, 1))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 53, 2) in readdata['check_list'][0]['tradeIn']:
                    logger.info(": Trade-In DeviceName ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 53, 1))
                else:
                    logger.info(": DeviceName NOT Matched.")
            else:
                logger.info(": tradeIn segment NOT present.")

    @staticmethod
    def get_skipCarrier_validation():

        with open(ReadConfig.readFilePathData('FilePaths', 'json_outResult'), 'r')as jsonfile:
            readdata = json.load(jsonfile)
            logger.info(": ##### Started skipCarrier validation From Landing Page #####")
            if "skipCarrier" in readdata['check_list'][0]:
                if ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 4, 3) in readdata['check_list'][0]['skipCarrier']:
                    logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 4, 3))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 5, 3) in readdata['check_list'][0]['skipCarrier']:
                    logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 5, 3))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 6, 3) in readdata['check_list'][0]['skipCarrier']:
                    logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 6, 3))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 7, 3) in readdata['check_list'][0]['skipCarrier']:
                    # assert "unlocked" in readdata['check_list'][0]['skipCarrier'], "carrier Name Not Present"
                    logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 7, 3))
                elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 8, 3) in readdata['check_list'][0]['skipCarrier']:
                    logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 8, 3))
            elif "carrier" in readdata['check_list'][0]:
                    if ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 4, 3) in readdata['check_list'][0]['carrier']:
                        logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 4, 3))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 5, 3) in readdata['check_list'][0][
                        'carrier']:
                        logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 5, 3))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 6, 3) in readdata['check_list'][0][
                        'carrier']:
                        logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 6, 3))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 7, 3) in readdata['check_list'][0][
                        'carrier']:
                        # assert "unlocked" in readdata['check_list'][0]['skipCarrier'], "carrier Name Not Present"
                        logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 7, 3))
                    elif ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 8, 3) in readdata['check_list'][0][
                        'carrier']:
                        logger.info(": Carrier Name ==" + ExcelUtil(tc_name="").read_from_excel("TradeIn_ID", 8, 3))
            else:
                logger.info(": skipCarrier segment NOT present.")







