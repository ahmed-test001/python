import json
import re
import os
import requests
import pytesseract
import cv2
from urllib.parse import urlparse




class extract_images:
    def __init__(self, **kwargs):
        self.config_file = {}
        self.input_html_file = kwargs['input_html_file']
        self.output_dir = kwargs['output_dir']
        self.output_file_name = kwargs['Image_Text']
        self.filename = kwargs['Report_File']
        self.headers = {
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
                       }
        self.query_list = ['offerCID', 'promoCode', 'skipCarrier', 'tradeIn', 'utm_source', 'utm_medium', 'utm_campaign', 'marsLinkCategory', 'MKM_RID', 'MKM_MID', 'cid', 'bpid']


    def check_key_exist(self, test_dict, key):
        try:
            value = test_dict[key]
            return True
        except KeyError:
            return False

    def extract_images(self):
        print("#################### Extract Images Start ####################")
        pytesseract.pytesseract.tesseract_cmd = (r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe")

        png_images = self.input_html_file.find_all('img', {'src': re.compile('.png')})
        jpg_images = self.input_html_file.find_all('img', {'src': re.compile('.jpg')})
        ahref_links = []
        hyper_links_json = {}
        for image in jpg_images:
            d_cols = {}
            d_cols['src'] = image['src']
            source = urlparse(image['src'])
            print("Image Source: ", source)
            filename = os.path.basename(source.path)
            response = requests.get(image['src'])
            image_file = open(self.output_dir+"/proof_images/" + filename, "wb+")
            image_file.write(response.content)
            image_file.close()
            d_cols['filename'] = filename
            # if image['alt'] == "":
            #     continue
            d_cols['alt'] = image['alt'] if self.check_key_exist(image, 'alt') else ""
            # d_cols['alt'] = image['alt']
            img = cv2.imread(self.output_dir+"/proof_images/" + filename)
            img = cv2.resize(img, None, fx=7, fy=7)
            data = pytesseract.image_to_string(img)
            d_cols['data'] = data.strip()
            ahref_links.append(d_cols)

        for image in png_images:
            d_cols = {}
            d_cols['src'] = image['src']
            source = urlparse(image['src'])
            print("Image Source: ", source)
            filename = os.path.basename(source.path)
            response = requests.get(image['src'])
            image_file = open(self.output_dir+"/proof_images/" + filename, "wb+")
            image_file.write(response.content)
            image_file.close()
            d_cols['filename'] = filename

            # if image['alt']=="":
            #     continue
            d_cols['alt'] = image['alt'] if self.check_key_exist(image, 'alt') else ""
            # d_cols['alt'] = image['alt']
            img = cv2.imread(self.output_dir+"/proof_images/" + filename)
            img = cv2.resize(img, None, fx=7, fy=7)
            data = pytesseract.image_to_string(img)
            d_cols['data'] = data
            ahref_links.append(d_cols)

        hyper_links_json['alerts'] = ahref_links
        final_hyber_links = json.dumps(hyper_links_json, indent=4, sort_keys=False, ensure_ascii=False)
        file = open(self.output_dir+"proof_files/" + self.output_file_name + '_' + '-'.join(self.filename.split('-')[-3:-1]) + ".json", "w", encoding="utf-8")
        file.write(final_hyber_links)
        file.close()
        print("#################### Extract Images End ####################")
