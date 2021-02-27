# import json
# import re
# import os
# import sys
# import requests
# import pytesseract
# # import cv2
# from urllib.parse import urlparse
#
# from bs4 import BeautifulSoup
# from selenium.webdriver.support.wait import WebDriverWait
#
# from Test_Campaign_2021.scripts.python.Util_Data import ReadConfig
#
#
# class extract_images:
#     output_dir = "../../data/output/"
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(self.driver, 10)
#
#     def check_key_exist(self, test_dict, key):
#         try:
#             value = test_dict[key]
#             return True
#         except KeyError:
#             return False
#
#     def extract_images(self):
#
#         with open(ReadConfig.readFilePathData('FilePaths', 'url_list'), 'w') as f:
#             urls = f.read().splitlines()
#             contents = urls[0]
#             input_html_file = BeautifulSoup(contents, 'html.parser')
#         f.close()
#         print("#################### Extract Images Start ####################")
#         pytesseract.pytesseract.tesseract_cmd = (r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe")
#
#         png_images = input_html_file.find_all('img', {'src': re.compile('.png')})
#         jpg_images = input_html_file.find_all('img', {'src': re.compile('.jpg')})
#         ahref_links = []
#         hyper_links_json = {}
#         for image in jpg_images:
#             d_cols = {}
#             d_cols['src'] = image['src']
#             source = urlparse(image['src'])
#             print("Image Source: ", source)
#             filename = os.path.basename(source.path)
#             response = requests.get(image['src'])
#             image_file = open(self.output_dir+"/proof_images/" + filename, "wb+")
#             image_file.write(response.content)
#             image_file.close()
#             d_cols['filename'] = filename
#             # if image['alt'] == "":
#             #     continue
#             d_cols['alt'] = image['alt'] if self.check_key_exist(image, 'alt') else ""
#             # d_cols['alt'] = image['alt']
#             img = cv2.imread(self.output_dir+"/proof_images/" + filename)
#             img = cv2.resize(img, None, fx=7, fy=7)
#             data = pytesseract.image_to_string(img)
#             d_cols['data'] = data.strip()
#             ahref_links.append(d_cols)
#
#         for image in png_images:
#             d_cols = {}
#             d_cols['src'] = image['src']
#             source = urlparse(image['src'])
#             print("Image Source: ", source)
#             filename = os.path.basename(source.path)
#             response = requests.get(image['src'])
#             image_file = open(self.output_dir+"/proof_images/" + filename, "wb+")
#             image_file.write(response.content)
#             image_file.close()
#             d_cols['filename'] = filename
#
#             # if image['alt']=="":
#             #     continue
#             d_cols['alt'] = image['alt'] if self.check_key_exist(image, 'alt') else ""
#             # d_cols['alt'] = image['alt']
#             img = cv2.imread(self.output_dir+"/proof_images/" + filename)
#             img = cv2.resize(img, None, fx=7, fy=7)
#             data = pytesseract.image_to_string(img)
#             d_cols['data'] = data
#             ahref_links.append(d_cols)
#
#         # hyper_links_json['alerts'] = ahref_links
#         # final_hyber_links = json.dumps(hyper_links_json, indent=4, sort_keys=False, ensure_ascii=False)
#         # file = open(self.output_dir+"proof_files/" + "abc" + ".json", "w", encoding="utf-8")
#         # # file = open(self.output_dir+"proof_files/" + self.output_file_name + '_' + '-'.join(self.filename.split('-')[-3:-1]) + ".json", "w", encoding="utf-8")
#         # # file.write(final_hyber_links)
#         # file.close()
#         print("#################### Extract Images End ####################")
