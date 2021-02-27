import logging
import os
import sys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Utility_Files import ReadConfig
from Utility_Files.HTMLTestRunner import stdout_redirector
logger=logging.getLogger(__name__)
out_hdlr=logging.StreamHandler(stdout_redirector)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s%(levelname)s%(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)


class BasePage(object):
    web_Text = ""
    page_url=""
    url_list = []
    method_list_in_Url = []

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        self.wait = WebDriverWait(self.driver, 10)
        web_element = self.wait.until(EC.presence_of_element_located(by_locator))
        self.web_Text=web_element.text
        return print(self.web_Text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def newwindow_Url(self, by_locator):
        self.wait = WebDriverWait(self.driver, 10)
        parent_window = self.driver.current_window_handle
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        all_windows = self.driver.window_handles
        child_window = [window for window in all_windows if window != parent_window][0]
        self.driver.switch_to.window(child_window)
        self.page_url = self.driver.current_url
        self.url_list.append(self.page_url)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        return self.page_url

    def unique_url(self):
        with open('../TextFolder/TestIn_UniqueURL_List.txt', 'w')as f:
            unique_list = []
            for x in self.url_list:
                # check unique_list or not
                if x not in unique_list:
                    unique_list.append(x)

            for x in unique_list:
                someline = x + '\n'
                f.writelines(someline)
                logger.info("##### Get unique URL List:  " + x)