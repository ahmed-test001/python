import glob
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),".."))


class utilityPage:
    unique_list = []

    # def write_CC_Category_URL(self):
    #     path = 'C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/Test_w_47_HolidayDeals_T3_Remail/creative/*.htm'
    #     with open('../TextFolder_Unique_URL/UniqueList_2.txt',"w")as f:
    #         files = glob.glob(path)
    #         for x in files:
    #             if "CC" in x:
    #                 self.unique_list.append(x)
    #                 someline = x + '\n'
    #                 f.writelines(someline)
    #                 print(someline)

    def write_DD_Category_URL(self):
        path = 'C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/Test_w_47_HolidayDeals_T3_Remail/creative/*.htm'
        with open('../TextFolder_Unique_URL/UniqueList_2.txt',"w")as f:
            files = glob.glob(path)
            for x in files:
                # if "DD" not in x:
                    if "CC" in x:
                        self.unique_list.append(x)
                        someline = x + '\n'
                        f.writelines(someline)
                        print(someline)

    # def write_ALL_Category_URL(self):
    #     path = 'C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/Test_w_47_HolidayDeals_T3_Remail/creative/*.htm'
    #     with open('../TextFolder_Unique_URL/UniqueList_2.txt',"w")as f:
    #         files = glob.glob(path)
    #         for x in files:
    #             # if "DD" in x:
    #             self.unique_list.append(x)
    #             someline = x + '\n'
    #             f.writelines(someline)
    #             print(someline)

    def total_count_URL(self):
        count=0
        with open('../TextFolder_Unique_URL/UniqueList_2.txt')as f:
            for x in f:
                count += 1
        print("Total Number of URL: ", count)


if __name__ == '__main__':
    util = utilityPage()
    # util.write_CC_Category_URL()
    util.write_DD_Category_URL()
    # util.write_ALL_Category_URL()
    util.total_count_URL()
