import glob
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..\..\.."))
from Test_Campaign_2021.scripts.python.Util_Data import ReadConfig



class utilityPage:
    unique_list = []

    def write_List_URL(self):
        # path = 'C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/Test_Campaign_2021/creative/*.htm'
        path = ReadConfig.readFilePathData('FilePaths', 'creative')
        with open(ReadConfig.readFilePathData('FilePaths', 'url_list'),'w+')as f:
            files = glob.glob(path)
            for x in files:
                self.unique_list.append(x)
                someline = x + '\n'
                f.writelines(someline)
                print(someline)

    def count_Total_URL(self):
        count=0
        with open(ReadConfig.readFilePathData('FilePaths', 'url_list'))as f:
            for x in f:
                count += 1
        print("Total Number of URL: ", count)


if __name__ == '__main__':
    util = utilityPage()
    util.write_List_URL()
    util.count_Total_URL()


