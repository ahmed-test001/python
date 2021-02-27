import json
from urllib.parse import parse_qs, urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from custom_functions.my_function import *
import multiprocessing as mp


class extract_hyper_links:
    def __init__(self, **kwargs):
        self.config_file = {}
        self.input_html_file = kwargs['input_html_file']
        self.output_dir = kwargs['output_dir']
        self.output_file_name = kwargs['Hyper_Links']
        self.filename = kwargs['Report_File']
        self.headers = {
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
                       }
        self.query_list = ['offerCID', 'promoCode', 'skipCarrier', 'tradeIn', 'utm_source', 'utm_medium', 'utm_campaign', 'marsLinkCategory', 'MKM_RID', 'MKM_MID', 'cid', 'bpid']
        self.chromedriver = "/Users/l.reddy/Downloads/chromedriver_v87"

    def extract_hyper_links(self):
        print("#################### HREF Links ####################")
        ahref_links = []
        validation_array = []
        hyper_links_json = {}
        validations_json = {}
        h_cols = {"pass": 0, "fail": 0, "missed": 0}

        for link in self.input_html_file.find_all("a"):
            anchor_link = link
            d_cols = {}
            raw_url = anchor_link.get("href")
            print(raw_url)
            requests_array = []
            try:
                chrome_options = Options()
                chrome_options.add_argument("--window-size=300,300")
                driver = webdriver.Chrome(self.chromedriver, chrome_options=chrome_options)
                driver.get(raw_url)
                decrypted_url = driver.current_url
                # r = requests.get(raw_url)
                # time.sleep(1)
                # decrypted_url = r.url
                print("Link Label: ", anchor_link.get("_label"))
                print("Raw URL: ", raw_url)
                print("Landing Page URL: ", decrypted_url, "\n")
                # for element in r.history:
                #     requests_array.append(str(element))
                driver.quit()
            except:
                print("no")
                decrypted_url = raw_url
            d_cols['inner_text'] = anchor_link.text.strip().replace("   ", "").replace("\n", "").replace("\r", "")
            d_cols['label'] = anchor_link.get("_label")
            d_cols['title'] = anchor_link.get("title")
            d_cols['href'] = decrypted_url
            d_cols['class'] = anchor_link.get("class")
            # parse url beginning
            parsed_url = urlparse(decrypted_url)
            d_cols['scheme'] = parsed_url.scheme
            d_cols['netloc'] = parsed_url.netloc
            d_cols['path'] = parsed_url.path
            # d_cols['params'] = parsed_url.params
            d_cols['query'] = parsed_url.query
            # d_cols['fragment'] = parsed_url.fragment
            # redirect history
            # r = requests.get(decrypted_url, headers=self.headers)
            # requests_array = []
            # for element in r.history:
            #     requests_array.append(str(element))
            # d_cols['redirect_history'] = requests_array
            # parse query
            pair = parse_qs(parsed_url.query)
            # print(pair.keys())

            for key in pair.keys():
                d_cols[key] = pair[key][0]

            # validating the object

            check_hyper_links_key_value(d_cols, '-'.join(self.filename.split('-')[-3:-1]))
            check_common_key_value(d_cols, 'common_links')
            #test_run(d_cols, '-'.join(self.filename.split('-')[-3:-1]))

            if not check_key_exist(d_cols, 'status_code'):
                d_cols['status_code'] = 'ORANGE'
                d_cols['exception'] = "NO_MATCH"

            if d_cols['status_code'] == "GREEN":
                h_cols['pass'] = h_cols['pass'] + 1
            elif d_cols['status_code'] == "RED":
                h_cols['fail'] = h_cols['fail'] + 1
            elif d_cols['status_code'] == "ORANGE":
                h_cols['missed'] = h_cols['missed'] + 1

            ahref_links.append(d_cols)

        validation_array.append(h_cols)
        hyper_links_json['alerts'] = ahref_links
        validations_json['alerts'] = validation_array
        # print(hyper_links_json)
        final_hyber_links = json.dumps(hyper_links_json, indent=4, sort_keys=False, ensure_ascii=False)
        final_validations = json.dumps(validations_json, indent=4, sort_keys=False, ensure_ascii=False)
        file = open(self.output_dir + "proof_files/" + self.output_file_name + '_' + '-'.join(self.filename.split('-')[-3:-1]) + ".json", "w")
        file.write(final_hyber_links)
        file.close()
        validations_file = open(self.output_dir + "proof_files/" + self.output_file_name + '_Validations' + '_' + '-'.join(self.filename.split('-')[-3:-1]) + ".json", "w")
        validations_file.write(final_validations)
        validations_file.close()
