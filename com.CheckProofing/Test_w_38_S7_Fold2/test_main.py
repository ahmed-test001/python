import datetime
import sys
import unittest
import os

sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from Test_w_38_S7_Fold2.test_w_38_Fold2_EPP_HTML_page import HTMLPage_W_38_Fold2_EPPTest
from Test_w_38_S7_Fold2.test_w_38_Fold2_EPP_URL_segment import URLSegment_W_38_Fold2_EPPTest
from Test_w_38_S7_Fold2.test_w_38_Fold2_EPP_WEB_page import webPage_W_38_Fold2_EPPTest
from Test_w_38_S7_Fold2.test_w_38_Fold2_Generic_HTML_page import HTMLPage_W_38_Fold2_GenericTest
from Test_w_38_S7_Fold2.test_w_38_Fold2_Generic_URL_segment import URLSegment_W_38_Fold2_GenericTest
from Test_w_38_S7_Fold2.test_w_38_Fold2_Generic_WEB_page import webPage_W_38_Fold2_GenericTest
from Test_w_38_S7_Fold2.test_w_38_S7_EPP_HTML_page import HTMLPage_W_38_S7_EPPTest
from Test_w_38_S7_Fold2.test_w_38_S7_EPP_URL_segment import URLSegment_W_38_S7_EPPTest
from Test_w_38_S7_Fold2.test_w_38_S7_EPP_WEB_page import webPage_W_38_S7_EPPTest
from Test_w_38_S7_Fold2.test_w_38_S7_Generic_HTML_page import HTMLPage_W_38_S7_GenericTest
from Test_w_38_S7_Fold2.test_w_38_S7_Generic_URL_segment import URLSegment_W_38_S7_GenericTest
from Test_w_38_S7_Fold2.test_w_38_S7_Generic_WEB_page import webPage_W_38_S7_GenericTest
from Utility_Files.HTMLTestRunner import HTMLTestRunner

DOWNLOAD_PATH = "../HTMLReport/"


class MainTest(unittest.TestCase):

    def test_run(self):

        # The test results dictionary, for the JSON.
        result_value = {"Pass":0, "Failures": 0, "Errors": 0, "Skipped": 0, "Test_Image Runs": 0}

        # List of all Test_Image Classes
        tests =[HTMLPage_W_38_S7_GenericTest]
        #tests = [HTMLPage_W_38_S7_EPPTest, webPage_W_38_S7_EPPTest, URLSegment_W_38_S7_EPPTest]  #EPP-Test_Image-S7
        tests = [HTMLPage_W_38_S7_GenericTest, webPage_W_38_S7_GenericTest, URLSegment_W_38_S7_GenericTest] #Generic-Test_Image-S7
        #tests = [HTMLPage_W_38_Fold2_EPPTest, webPage_W_38_Fold2_EPPTest, URLSegment_W_38_Fold2_EPPTest]  #EPP-Test_Image-Fold2
        #tests = [HTMLPage_W_38_Fold2_GenericTest, webPage_W_38_Fold2_GenericTest, URLSegment_W_38_Fold2_GenericTest] #Generic-Test_Image-Fold2
        list_of_tests = [unittest.TestLoader().loadTestsFromTestCase(test) for test in tests]

        # create a test suite combining search_text and home_page_test
        test_suite = unittest.TestSuite(list_of_tests)

        # configure HTMLTestRunner options
        # report_file = os.path.join(DOWNLOAD_PATH, "TestReport_1.html")
        report_file = os.path.join(DOWNLOAD_PATH, "TestReport_S7Gen_sample3_{}.html".format(datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")))
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