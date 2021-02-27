import json
from urllib.parse import urlparse, parse_qs
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


def url_segment():
    final_json = {}
    final_array = []
    bpid_array = []
    # final_bpid = {}
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
        # final_bpid['bpid_list'] = bpid_array
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


# def segment_validation():
#
#     with open('../OutputT/OutResult.json', 'r')as jsonfile:
#         # try:
#             readdata=json.load(jsonfile)
#             if ReadConfig.read_w44_TVSoundBar_Auto_configData('TVSoundBarDataGEN', 'category') in readdata['check_list'][0]['category']:
#                 logger.info(": category matched")
#             else:
#                 logger.info(": category NOT matched")
#             if ReadConfig.read_w44_TVSoundBar_Auto_configData('TVSoundBarDataGEN', 'sku_id') in readdata['check_list'][0]['sku_id']:
#                 logger.info(": sku_id matched")
#             else:
#                 logger.info(": sku_id NOT matched")
#             if ReadConfig.read_w44_TVSoundBar_Auto_configData('TVSoundBarDataGEN', 'cid') in readdata['check_list'][0]['CID']:
#                 logger.info(": cid matched")
#             else:
#                 logger.info(": cid NOT matched")
#             if ReadConfig.read_w44_TVSoundBar_Auto_configData('TVSoundBarDataGEN', 'promocode') in readdata['check_list'][0]['promoCode']:
#                 logger.info(": promocode matched")
#             else:
#                 logger.info(": promocode NOT matched")
#             if ReadConfig.read_w44_TVSoundBar_Auto_configData('TVSoundBarDataGEN', 'marslinkcategory') in readdata['check_list'][0]['marsLinkCategory']:
#                 logger.info(": marslinkcategory matched")
#             else:
#                 logger.info(": marslinkcategory NOT matched")
#             if ReadConfig.read_w44_TVSoundBar_Auto_configData('TVSoundBarDataGEN', 'utm_source') in readdata['check_list'][0]['utm_source']:
#                 logger.info(": utm_source matched")
#             else:
#                 logger.info(": utm_source NOT matched")
#             if ReadConfig.read_w44_TVSoundBar_Auto_configData('TVSoundBarDataGEN', 'utm_medium') in readdata['check_list'][0]['utm_medium']:
#                 logger.info(": utm_medium matched")
#             else:
#                 logger.info(": utm_medium NOT matched")
#         # except:
#         #     pass









