import sys
import unittest
import os
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from Test_canvas.test_URL_segment_validation_from_HTML_page import URLSegmentvalidationTest
from Test_canvas.test_HTML_page_validation import HTMLPageTest
from Test_canvas.test_webpage import webPageTest
from Utility_Files.HTMLTestRunner import HTMLTestRunner

DOWNLOAD_PATH = "../HTMLReport/"


class MainTest(unittest.TestCase):

    def test_run(self):

        # The test results dictionary, for the JSON.
        result_value = {"Pass":0, "Failures": 0, "Errors": 0, "Skipped": 0, "Test_Image Runs": 0}

        # List of all Test_Image Classes
        # tests = [ReserveTest, URLSegmentTest,EmailPageTest]
        tests = [HTMLPageTest, webPageTest, URLSegmentvalidationTest]  # use for e-mail template to direct segment only
        list_of_tests = [unittest.TestLoader().loadTestsFromTestCase(test) for test in tests]

        # create a test suite combining search_text and home_page_test
        test_suite = unittest.TestSuite(list_of_tests)

        # configure HTMLTestRunner options
        report_file = os.path.join(DOWNLOAD_PATH, "TestReport_1.html")
        with open(report_file, "w") as f:
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