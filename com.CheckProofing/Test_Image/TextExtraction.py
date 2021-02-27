import pytesseract
from Utility_Files import ReadConfig
import cv2
import logging

pytesseract.pytesseract.tesseract_cmd = ReadConfig.readImageconfigData('paths', 'tesseractpath')
logging.basicConfig(filename='./Logs/TextExtraction.log', level=logging.INFO,
                    format='%(levelname)s:%(asctime)s:%(message)s')

img = cv2.imread(ReadConfig.readImageconfigData('path', 'image3'))
logging.info('Read the image from the directory.')
img = cv2.resize(img, None, fx=6, fy=3)
logging.info('Reformat the image size.')
data = pytesseract.image_to_string(img)
logging.info('Read Text from the image')
logging.info(data)
try:
    assert ReadConfig.readImageconfigData('value', 'price') in data
    logging.info('###### Coupon Price FOUND #######')
    logging.info(ReadConfig.readImageconfigData('value', 'price'))
except:

    logging.info('Coupon price not FOUND')
