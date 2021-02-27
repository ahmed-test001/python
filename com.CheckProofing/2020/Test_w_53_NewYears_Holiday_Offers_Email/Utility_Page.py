import glob
import sys
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from Utility_Files.ExcelReaderUtil import ExcelUtil


class utilityPage:
    unique_list = []

    def write_Category_URL(self):
        path = 'C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/Test_w_53_NewYears_Holiday_Offers_Email/creative/*.htm'
        with open('../TextFolder_Unique_URL/UniqueList_2.txt',"w")as f:
            files = glob.glob(path)
            for x in files:
                # if "DD" in x:
                    self.unique_list.append(x)
                    someline = x + '\n'
                    f.writelines(someline)
                    print(someline)

    def total_Count_URL(self):
        count=0
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            for x in f:
                count += 1
        print("Total Number of URL: ", count)

    def get_Text(self):

        url = "file:///C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/Test_w_53_NewYears_Holiday_Offers_Email/creative/Proof_R1-N1_eComm_Week53_New_Years_Holiday_Offers_201230-Generic-Catch_All-S1-G.htm"
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out

        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        # print(ReadConfig.readconfigData2("Test_01", 'test1'))
        # SL = ExcelUtil(tc_name="").read_from_excel("SL_PH", 3, 18).strip()
        print(text.encode('utf-8'))


if __name__ == '__main__':
    util = utilityPage()
    # util.write_Category_URL()
    # util.total_Count_URL()
    util.get_Text()