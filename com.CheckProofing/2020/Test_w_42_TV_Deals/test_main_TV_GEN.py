import datetime
import sys
import unittest
import os
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from Test_w_42_TV_Deals.test_w_42_TV_Deals_GEN_All_Deals_url_segment import URLSegment_W_42_TV_Deals_GEN_allDeals_Test
from Test_w_42_TV_Deals.test_w_42_TV_Deals_GEN_Frame_QLED4K_url_segment import URLSegment_W_42_TV_Deals_GEN_FrameQLED4k_Test
from Test_w_42_TV_Deals.test_w_42_TV_Deals_GEN_Html_Page import HTMLPage_W_42_TV_Deals_GEN_Test
from Test_w_42_TV_Deals.test_w_42_TV_Deals_GEN_QLEDTV4K_url_segment import URLSegment_W_42_TV_Deals_GEN_QLEDTV4K_Test
from Test_w_42_TV_Deals.test_w_42_TV_Deals_GEN_QLEDTV8K_url_segment import URLSegment_W_42_TV_Deals_GEN_QLEDTV8K_Test
from Test_w_42_TV_Deals.test_w_42_TV_Deals_GEN_SerifTV4K_url_segment import URLSegment_W_42_TV_Deals_GEN_SerifTV4K_Test
from Test_w_42_TV_Deals.test_w_42_TV_Deals_GEN_SeroTV4K_url_segment import URLSegment_W_42_TV_Deals_GEN_SeroTV4K_Test
from Test_w_42_TV_Deals.test_w_42_TV_Deals_GEN_SignupSavings_url_segment import URLSegment_W_42_TV_Deals_GEN_SignupSavings_Test
from Test_w_42_TV_Deals.test_w_42_TV_Deals_GEN_SoundBarQ900T_url_segment import URLSegment_W_42_TV_Deals_GEN_SoundBarQ900T_Test
from Test_w_42_TV_Deals.test_w_42_TV_Deals_GEN_SoundBarQ950_url_segment import URLSegment_W_42_TV_Deals_GEN_SoundBarQ950_Test
from Test_w_42_TV_Deals.test_w_42_TV_Deals_GEN_Terrace4K_url_segment import URLSegment_W_42_TV_Deals_GEN_Terrace4K_Test

from Utility_Files.HTMLTestRunner import HTMLTestRunner

DOWNLOAD_PATH = "../HTMLReport/"


class MainTest(unittest.TestCase):

    def test_run(self):

        # The test results dictionary, for the JSON.
        result_value = {"Pass":0, "Failures": 0, "Errors": 0, "Skipped": 0, "Test_Image Runs": 0}

        # List of all Test_Image Classes
        tests =[HTMLPage_W_42_TV_Deals_GEN_Test,URLSegment_W_42_TV_Deals_GEN_allDeals_Test,URLSegment_W_42_TV_Deals_GEN_FrameQLED4k_Test,
                URLSegment_W_42_TV_Deals_GEN_Terrace4K_Test,URLSegment_W_42_TV_Deals_GEN_SeroTV4K_Test,
                URLSegment_W_42_TV_Deals_GEN_SerifTV4K_Test,URLSegment_W_42_TV_Deals_GEN_SoundBarQ950_Test,
                URLSegment_W_42_TV_Deals_GEN_SoundBarQ900T_Test,URLSegment_W_42_TV_Deals_GEN_QLEDTV8K_Test,
                URLSegment_W_42_TV_Deals_GEN_QLEDTV4K_Test,URLSegment_W_42_TV_Deals_GEN_SignupSavings_Test]

        list_of_tests = [unittest.TestLoader().loadTestsFromTestCase(test) for test in tests]

        # create a test suite combining search_text and home_page_test
        test_suite = unittest.TestSuite(list_of_tests)

        # configure HTMLTestRunner options
        # report_file = os.path.join(DOWNLOAD_PATH, "TestReport_1.html")
        report_file = os.path.join(DOWNLOAD_PATH, "TVDEALS_ReportGEN_{}.html".format(datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")))
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