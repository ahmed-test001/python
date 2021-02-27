from bs4 import BeautifulSoup
import json
import re
import os
import requests
import pytesseract
import cv2
from urllib.parse import parse_qs, urlparse

from Utility_Files import ReadConfig

# pytesseract.pytesseract.tesseract_cmd = ReadConfig.readImageconfigData('paths', 'tesseractpath')
pytesseract.pytesseract.tesseract_cmd =(r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe")


class Scrapper:
    def __init__(self, **kwargs):
        self.config_file = {}
        self.headers = {
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
                       }

    def check_key_exist(self, test_dict, key):
        try:
            value = test_dict[key]
            return True
        except KeyError:
            return False

    def html_scrapper(self):
        headers = {
            'User-Agent': 'Mozilla\/5.0 (Windows NT 6.1; WOW64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/45.0.2454.101 Safari\/537.36'
        }
        #with open('Canvas-simple_modified_redirect.html', 'r') as f:
        with open('Canvas-simple_modified_noredirect.html', 'r') as f:
        # with open('fold2_t2.html', 'r') as f:
            contents = f.read()
            soup = BeautifulSoup(contents, 'html.parser')
            ahref_links = []
            hyper_links_json = {}
            for link in soup.find_all("a"):
                d_cols = {}
                d_cols['inner_text'] = link.text.strip().replace("   ", "")
                d_cols['label'] = link.get("_label")
                d_cols['title'] = link.get("title")
                d_cols['href'] = link.get("href")
                d_cols['class'] = link.get("class")
                parsed_url = urlparse(d_cols['href'])
                d_cols['scheme'] = parsed_url.scheme
                d_cols['netloc'] = parsed_url.netloc
                d_cols['path'] = parsed_url.path
                d_cols['params'] = parsed_url.params
                d_cols['query'] = parsed_url.query
                d_cols['fragment'] = parsed_url.fragment
                r = requests.get(d_cols['href'], headers=self.headers)
                requests_array = []
                for element in r.history:
                    requests_array.append(str(element))
                d_cols['redirect_history'] = requests_array
                pair = parse_qs(parsed_url.query)
                d_cols['offerCID'] = pair['offerCID'] if self.check_key_exist(pair, 'offerCID') else None
                d_cols['promoCode'] = pair['promoCode'] if self.check_key_exist(pair, 'promoCode') else None
                d_cols['skipCarrier'] = pair['skipCarrier'] if self.check_key_exist(pair, 'skipCarrier') else None
                d_cols['tradeIn'] = pair['tradeIn'] if self.check_key_exist(pair, 'tradeIn') else None
                d_cols['utm_source'] = pair['utm_source'] if self.check_key_exist(pair, 'utm_source') else None
                d_cols['utm_medium'] = pair['utm_medium'] if self.check_key_exist(pair, 'utm_medium') else None
                d_cols['utm_campaign'] = pair['utm_campaign'] if self.check_key_exist(pair, 'utm_campaign') else None
                d_cols['marsLinkCategory'] = pair['marsLinkCategory'] if self.check_key_exist(pair, 'marsLinkCategory') else None
                d_cols['MKM_RID'] = pair['MKM_RID'] if self.check_key_exist(pair, 'MKM_RID') else None
                d_cols['MKM_MID'] = pair['MKM_MID'] if self.check_key_exist(pair, 'MKM_MID') else None
                d_cols['cid'] = pair['cid'] if self.check_key_exist(pair, 'cid') else None
                d_cols['bpid'] = pair['bpid'] if self.check_key_exist(pair, 'bpid') else None
                ahref_links.append(d_cols)
            hyper_links_json['alerts'] = ahref_links
            #print(hyper_links_json)
            final_hyber_links = json.dumps(hyper_links_json, indent=4, sort_keys=False, ensure_ascii=True)
            file = open("./output_json_files/hyper_links.json", "w")
            file.write(final_hyber_links)
            file.close()

            png_images = soup.find_all('img', {'src': re.compile('.png')})
            jpg_images = soup.find_all('img', {'src': re.compile('.jpg')})
            ahref_links = []
            hyper_links_json = {}
            for image in jpg_images:
                d_cols = {}
                d_cols['src'] = image['src']
                source = urlparse(image['src'])
                filename = os.path.basename(source.path)
                response = requests.get(image['src'])
                image_file = open("./proof_images/" + filename, "wb+")
                image_file.write(response.content)
                image_file.close()
                d_cols['filename'] = filename
                d_cols['alt'] = image['alt']
                img = cv2.imread("./proof_images/" + filename)
                img = cv2.resize(img, None, fx=7, fy=7)
                data = pytesseract.image_to_string(img)
                d_cols['data'] = data
                ahref_links.append(d_cols)
                print("done")

            for image in png_images:
                d_cols = {}
                d_cols['src'] = image['src']
                source = urlparse(image['src'])
                filename = os.path.basename(source.path)
                response = requests.get(image['src'])
                image_file = open("./proof_images/" + filename, "wb+")
                image_file.write(response.content)
                image_file.close()
                d_cols['filename'] = filename
                d_cols['alt'] = image['alt']
                img = cv2.imread("./proof_images/" + filename)
                img = cv2.resize(img, None, fx=7, fy=7)
                data = pytesseract.image_to_string(img)
                d_cols['data'] = data
                print("png done")
                ahref_links.append(d_cols)

            hyper_links_json['alerts'] = ahref_links
            final_hyber_links = json.dumps(hyper_links_json, indent=4, sort_keys=False, ensure_ascii=True)
            file = open("./output_json_files/template_images.json", "w")
            file.write(final_hyber_links)
            file.close()

            div = soup.find('div', class_='mobileBorder')  # get div of mobile order
            gdp_table = div.find_all("table", attrs={"role": "presentation"})  # get tables in div
            ahref_links = []
            hyper_links_json = {}
            gdp_table_data = gdp_table[1].find_all("tr")
            for every_tr in gdp_table_data:
                d_cols = {}
                value = every_tr.text.strip().replace("   ", "")
                if len(value)!= 0:
                    d_cols['baseline'] = value
                    ahref_links.append(d_cols)
            hyper_links_json['alerts'] = ahref_links
            final_hyber_links = json.dumps(hyper_links_json, indent=4, sort_keys=False, ensure_ascii=True)
            file = open("./output_json_files/proofs_baseline_text.json", "w")
            file.write(final_hyber_links)
            file.close()
        f.close()


def main_scrapper():
    scrapper_obj = Scrapper()
    scrapper_obj.html_scrapper()


if __name__ == "__main__":
    main_scrapper()
