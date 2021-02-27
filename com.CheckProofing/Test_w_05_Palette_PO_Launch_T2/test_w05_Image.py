from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil

url = "https://www.samsung.com/us/"
# url = "file:///C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/Test_w_05_PANDA_EVERGREEN/creative/Proof_R2-N1A_eComm_Panda_EverGreen_3M-Generic-A51-S1-JEFFREY-V11.htm"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# aas = soup.find_all("a", class_='entry-featured-image-url')
aas = soup.find_all("a")

image_info = []

for a in aas:
    image_tag = a.findChildren("img")
    print(image_info)
    # image_info.append((image_tag[0]["src"], image_tag[0]["alt"]))


def download_image(image):
    response = requests.get(image[0], stream=True)
    realname = ''.join(e for e in image[1] if e.isalnum())

    file = open("../Test_w_05_Palette_PO_Launch_T2/images/{}.jpg".format(realname), 'wb')
    # file = open("C://images//bs//{}.jpg".format(realname), 'wb')

    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response


for i in range(0, len(image_info)):
    download_image(image_info[i])