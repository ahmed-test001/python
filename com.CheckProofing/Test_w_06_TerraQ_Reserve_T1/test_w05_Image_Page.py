# import urllib
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
#
#
#
#
#
# # html = urlopen('file:///C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/Test_w_05_PANDA_EVERGREEN/creative/Proof_R2-N1A_eComm_Panda_EverGreen_3M-Generic-A51-S1-JEFFREY-V11.htm')
# # bs = BeautifulSoup(html, 'html.parser')
# # images = bs.find_all('img', {'src': re.compile('.png')})
# # for image in images:
# #     print(image['src'] + '\n')
# # import re
# # with open('file:///C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/Test_w_05_PANDA_EVERGREEN/creative/Proof_R2-N1A_eComm_Panda_EverGreen_3M-Generic-A51-S1-JEFFREY-V11.htm') as html:
# #     content = html.read()
# #     matches = re.findall(r'\ssrc="([^"]+)"', content)
# #     matches = ' '.join(matches)
# #
# # print(matches)
# from PIL import Image, ImageChops
# from pytesseract import pytesseract
#
# # # Defining paths to tesseract.exe
# # # and the image we would be using
# # path_to_tesseract = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
# # image_path = r"C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/creative_analyzer_final_copy/data/output/proof_images/c7577bf5f191649d0cf0599dde9b8280.jpg"
# #
# # # Opening the image & storing it in an image object
# # img = Image.open(image_path)
# #
# # # Providing the tesseract
# # # executable location to pytesseract library
# # pytesseract.tesseract_cmd = path_to_tesseract
# #
# # # Passing the image object to
# # # image_to_string() function
# # # This function will
# # # extract the text from the image
# # text = pytesseract.image_to_string(img)
# #
# # # Displaying the extracted text
# # print(text[:-1])
#
# img_url = "file:///C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/Test_w_04_Palette_PO_T4_LastChance/creative/Proof_R1-N1_eComm_Week04_Palette_PreOrder_LastChance_T4_EPP_N10+_Stephanie.htm"
#
# fileN = open('C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/creative_analyzer_final_copy/data/output/proof_images/6cbbb2d814e37c04931674a78decec40.jpg','wb')
# fileN .write(urllib.request.urlopen(img_url).read())
# fileN .close()
#
# Comparediff = ImageChops.difference(img_url, fileN).getbbox()
# print (Comparediff)


import urllib.request
import hashlib
from selenium import webdriver

from Utility_Files import ReadConfig


def hash_it(path):
    with open(path, 'rb') as f:
        hasher = hashlib.md5()
        hasher.update(f.read())
        return hasher.hexdigest()


directory = "C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/Test_w_05_PANDA_EVERGREEN/image_comparison"
remote_img = "{}/{}".format(directory, "remote.jpg")
local_img = "{}/{}".format(directory, "local.jpg")
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver'), options=option)
driver.get("file:///C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/Test_w_05_PANDA_EVERGREEN/creative/Proof_R2-N1A_eComm_Panda_EverGreen_3M-Generic-A51-S1-JEFFREY-V11.htm")
logo = driver.find_element_by_xpath("//img[@alt='Shop fast charges to get powered super-fast.']").get_attribute("src")
logo2 = driver.find_element_by_xpath("//img[@src='http://t.info.samsungusa.com/res/samsung/c607d9ffe0fcca1d8ba4342e4193a50b.jpg']").get_attribute('alt')
print(logo2)
# urllib.urlretrieve(logo, remote_img)
urllib.request.urlretrieve(logo, remote_img)

local_img_hash = hash_it(local_img)
remote_img_hash = hash_it(remote_img)
# assert local_img_hash == remote_img_hash, "Hashes do not match. {} vs {}".format(local_img_hash, remote_img_hash)

driver.quit()