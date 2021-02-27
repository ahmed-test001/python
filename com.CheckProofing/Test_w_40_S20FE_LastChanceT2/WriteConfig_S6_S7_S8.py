import configparser
import time
import warnings
from urllib.parse import urlparse, parse_qs
from selenium import webdriver
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from Utility_Files import ReadConfig


class writeData:
    driver =None
    URL = ""
    html_path = "file:///C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/Test_w_40_Wearable/creative/wearable_3.htm"
    file_path = "../ConfigData/w40/w_40_Wearable.ini"
    Section = "WearableData"

    def email_text_extract(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=ReadConfig.readconfigData('paths', 'chromedriver1'), options=option)
        warnings.filterwarnings(action="ignore",message="unclosed",category=ResourceWarning)
        self.driver.get(self.html_path)
        time.sleep(2)
        # # ######## Subject Line Text Print ########
        parent_window = self.driver.current_window_handle
        subjectlineTxt = self.driver.find_element_by_xpath("(//p[@class='MsoNormal'])[4]/span").text
        time.sleep(5)
        config = configparser.RawConfigParser()
        config.read(self.file_path)
        config.set(self.Section, "html_path", self.html_path)
        config.set(self.Section, "subject_line", subjectlineTxt)
        cfgfile = open(self.file_path, 'w')
        config.write(cfgfile, space_around_delimiters=False)
        cfgfile.close()
        time.sleep(3)
        ######## Header Text Print ########
        linkT = self.driver.find_element_by_xpath("(//*[@target='_blank'])[1]")
        preHeadertext = linkT.text
        time.sleep(5)
        config = configparser.RawConfigParser()
        config.read(self.file_path)
        time.sleep(3)
        config.set(self.Section, "pre_headertext", preHeadertext)
        cfgfile = open(self.file_path, 'w')
        config.write(cfgfile, space_around_delimiters=False)
        cfgfile.close()
        time.sleep(3)
        ######## URL Full Print ########
        linkT.click()
        time.sleep(2)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        time.sleep(5)
        self.URL = self.driver.current_url
        time.sleep(1)
        config = configparser.RawConfigParser()
        config.read(self.file_path)
        config.set(self.Section, "url", self.URL)
        cfgfile = open(self.file_path, 'w')
        config.write(cfgfile, space_around_delimiters=False)
        cfgfile.close()
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        self.driver.quit()

    def UrlSegment(self):
        parsed_url = urlparse(self.URL)
        pair = parse_qs(parsed_url.query)
        for k,  v in pair.items():
            s =" ".join([str(elem) for elem in v])
            config = configparser.RawConfigParser()
            config.read(self.file_path)
            config.set(self.Section, k, s)
            print(k+"="+s)
            cfgfile = open(self.file_path, 'w')
            config.write(cfgfile, space_around_delimiters=False)
            cfgfile.close()


if __name__ == '__main__':
    wdata = writeData()
    wdata.email_text_extract()
    wdata.UrlSegment()