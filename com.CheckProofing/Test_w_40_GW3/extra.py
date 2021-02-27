#
# @classmethod # this is for assertion with url(practice)
# def test_h_verify_pay_later_icon(self):
#     logger.info(': ' + self.test_h_verify_pay_later_icon.__name__ + "\n #####  Starting TEST  ##### ")
#     parent_window = self.driver.current_window_handle
#     # payHere_link = self.driver.find_element_by_xpath("//a[@_label='Pay_Over_Time_Title']")
#     # payHere_link = self.driver.find_element_by_xpath("//a[@_label='Free_Returns_Title']")
#     # payHere_link = self.driver.find_element_by_xpath("//a[@_label='Get_Rewarded_Title']")
#     # payHere_link = self.driver.find_element_by_xpath("(//img[@class='fluid custom7'])[5]")
#     payHere_link = self.driver.find_element_by_xpath("// a[@_label='Youtube']")
#     self.driver.execute_script("arguments[0].scrollIntoView();", payHere_link)
#     self.driver.execute_script("arguments[0].click();", payHere_link)
#     # payHere_link.click()
#     time.sleep(3)
#     all_windows = self.driver.window_handles
#     child_window = [window for window in all_windows if window != parent_window][0]
#     self.driver.switch_to.window(child_window)
#     time.sleep(5)
#     url10 = self.driver.current_url
#     print(url10)
#     time.sleep(5)
#     # assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage','pay_later_url') in url10
#     # assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage', 'free_shipping_url') in url10
#     # assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage', 'get_rewarded_url') in url10
#     # assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage', 'weekly_offer_button_url') in url10
#     assert ReadConfig.read_w38_S7_Fold2_configData('HTMLPage', 'youtube_url') in url10
#     logger.info(': Assertion Pay Later with: ' + url10)
#     self.driver.close()
#     self.driver.switch_to.window(parent_window)
#
# ## below code is verify trade-in price from header text if it always remain in header line
#
# def test_b_pre_header_text_validation(self):
#     logger.info(': ' + self.test_b_pre_header_text_validation.__name__ + "\n #####  Starting TEST  ##### ")
#     pheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
#     print(pheaderTxt)
#     assert "Plus, save up to $450 with eligible trade‑in.‡" in pheaderTxt
#     logger.info(": Pre-Header text assert with : " + pheaderTxt)
#     res = re.sub("\D", "", pheaderTxt)
#     price='$'+str(res)
#     logger.info(": The numbers list is : " + price)
#     config = configparser.RawConfigParser()
#     config.read('../ConfigData/w_38_S7_&_Fold2.ini')
#     config.set("S7Generic", "number", price)
#     cfgfile = open('../ConfigData/w_38_S7_&_Fold2.ini', 'w')
#     config.write(cfgfile, space_around_delimiters=False)  # use flag in case case you need to avoid white space.
#     cfgfile.close()
#
# @classmethod
# def test_x1_fold2_CTA_validation(self):
#     logger.info(': '+self.test_x1_fold2_CTA_validation.__name__ + "\n #####  Starting TEST  ##### ")
#     time.sleep(2)
#     parent_window = self.driver.current_window_handle
#     linkT = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]")
#     linkT.click()
#     time.sleep(3)
#     all_windows = self.driver.window_handles
#     child_window = [window for window in all_windows if window != parent_window][0]
#     self.driver.switch_to.window(child_window)
#     time.sleep(5)
#     instantCredit = self.driver.find_element_by_xpath("(//*[@class='title'])[4]").text
#     time.sleep(5)
#     assert ReadConfig.read_w38_S7_Fold2_configData('S7Generic', 'number') in instantCredit
#     self.driver.close()
#     logger.info(": Assertion : " + ReadConfig.read_w38_S7_Fold2_configData('S7Generic', 'number'))
#     self.driver.switch_to.window(parent_window)

#
# @classmethod
# def test_t_SeroTV_InstantCredit_from_CART_ItemPage_validation(self):
#     logger.info(': ' + self.test_t_SeroTV_InstantCredit_from_CART_ItemPage_validation.__name__ + "\n #####  Starting TEST  ##### ")
#     subheaderTxt = self.driver.find_element_by_xpath("(//a[@target='_blank'])[1]").text
#     assert SeroTV_ReadConfig.read_seroTV_configData('SeroTVData', 'pre_headertext') in subheaderTxt
#     logger.info(": Verified Pre Header Text is : " + subheaderTxt)
#     res = re.sub("\D", "", subheaderTxt)
#     price1 = '$' + str(res)
#     price = '$' +price1[4:]
#     logger.info(": Identified Sero TV Instant Credit from Pre Header text is : " + price)
#     config = configparser.RawConfigParser()
#     config.read('../Test_w_39_SeroTV/SeroTV.ini')
#     config.set("SeroTVData", "Instant_Credit", price)
#     cfgfile = open('../Test_w_39_SeroTV/SeroTV.ini', 'w')
#     config.write(cfgfile, space_around_delimiters=False)
#     cfgfile.close()
#     time.sleep(2)
#     parent_window = self.driver.current_window_handle
#     linkT = self.driver.find_element_by_xpath("(//*[@target='_blank'])[1]")
#     linkT.click()
#     time.sleep(2)
#     all_windows = self.driver.window_handles
#     child_window = [window for window in all_windows if window != parent_window][0]
#     self.driver.switch_to.window(child_window)
#     WebDriverWait(self.driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "(//p[@class='type-p2'])[2]"))).click()
#     logger.info(": Navigate to Cart Total Page")
#     Credittxt = WebDriverWait(self.driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, "(//*[@_target='_blank'])")))
#     instantCredit = Credittxt.text
#     print(instantCredit)
#     logger.info(": Identify Samsung Gift Vaucher Text: "+instantCredit)
#     time.sleep(5)
#     assert SeroTV_ReadConfig.read_seroTV_configData('SeroTVData', 'Instant_Credit') in instantCredit, "Instant Credit from Pre Header Text is not matching with samsung vaucher of CART Total Page "
#     self.driver.close()
#     logger.info(": Successfully verified Instant Credit from Pre Header with CART Total Page is: " + price)
#     self.driver.switch_to.window(parent_window)
