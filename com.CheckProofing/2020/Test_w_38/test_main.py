import datetime
import sys
import unittest
import os
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from Test_w_38.test_w_38_WEB_page_VRZ import webPageVRZTest
from Test_w_38.test_w_38_WEB_page_Generic import webPageGenericTest
from Test_w_38.test_w_38_WEB_page_Non_Res import webPageNonResTest
from Test_w_38.test_w_38_WEB_page_Sprint import webPageSprintTest
from Test_w_38.test_w_38_WEB_page_EPP import webPageEPPTest
from Test_w_38.test_w_38_HTML_page_VRZ import HTMLPageVRZTest
from Test_w_38.test_w_38_URL_segment_VRZ import URLSegmentVRZTest
from Test_w_38.test_w_38_HTML_page_Sprint import HTMLPageSprintTest
from Test_w_38.test_w_38_URL_segment_Sprint import URLSegmentSprintTest
from Test_w_38.test_w_38_HTML_page_Non_Res import HTMLPageNonResTest
from Test_w_38.test_w_38_URL_segment_Non_Res import URLSegmentNonResTest
from Test_w_38.test_w_38_HTML_page_Generic import HTMLPageGenericTest
from Test_w_38.test_w_38_URL_segment_Generic import URLSegmentGenericTest
from Test_w_38.test_w_38_HTML_page_EPP import HTMLPageEPPTest
from Test_w_38.test_w_38_URL_segment_EPP import URLSegmentEPPTest
from Test_w_38.test_w_38_WEB_page_fold2 import webPageFold2Test
from Test_w_38.test_w_38_WEB_page_tabS7 import webPageTabS7Test
from Utility_Files.HTMLTestRunner import HTMLTestRunner

DOWNLOAD_PATH = "../HTMLReport/"


class MainTest(unittest.TestCase):

    def test_run(self):

        # The test results dictionary, for the JSON.
        result_value = {"Pass":0, "Failures": 0, "Errors": 0, "Skipped": 0, "Test_Image Runs": 0}

        # List of all Test_Image Classes
        tests = [HTMLPageEPPTest, webPageEPPTest,webPageFold2Test,webPageTabS7Test,URLSegmentEPPTest]  #EPP-Test_Image
        #tests = [HTMLPageGenericTest, webPageGenericTest, webPageFold2Test, webPageTabS7Test, URLSegmentGenericTest] #Generic-Test_Image
        #tests = [HTMLPageNonResTest, webPageNonResTest, webPageFold2Test, webPageTabS7Test, URLSegmentNonResTest] #NonRes-Test_Image
        #tests = [HTMLPageSprintTest, webPageSprintTest, webPageFold2Test, webPageTabS7Test,URLSegmentSprintTest]  #Sprint-Test_Image
        #tests = [HTMLPageVRZTest, webPageVRZTest, webPageFold2Test, webPageTabS7Test,URLSegmentVRZTest]  # VRZ-Test_Image
        list_of_tests = [unittest.TestLoader().loadTestsFromTestCase(test) for test in tests]

        # create a test suite combining search_text and home_page_test
        test_suite = unittest.TestSuite(list_of_tests)

        # configure HTMLTestRunner options
        # report_file = os.path.join(DOWNLOAD_PATH, "TestReport_1.html")
        report_file = os.path.join(DOWNLOAD_PATH, "TestReport_&&_{}.html".format(datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")))
        with open(report_file, "w", encoding="utf-8") as f:
            runner = HTMLTestRunner(title="Sample Test_Image Report", stream=f)

            # run the suite using HTMLTestRunner
            result = runner.run(test_suite)

            # Passes the Result
            result_value["Pass"] += result.testsRun - (len(result.failures) + len(result.errors) +len(result.skipped))
            result_value["Failures"] += len(result.failures)
            result_value["Errors"] += len(result.errors)
            result_value["Skipped"] += len(result.skipped)
            result_value["Test_Image Runs"] += result.testsRun

        print(result_value)

        # return the test result as boolean to docker host
        if result.wasSuccessful():
            print("All tests were executed successfully.")
        else:
            print("Tests failed. Please check the Report.")


if __name__ == '__main__':
    # begin the tests
    obj = MainTest()
    obj.test_run()