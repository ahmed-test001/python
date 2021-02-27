import subprocess
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..\..\.."))
from Test_Campaign_2021.scripts.python.Util_Data import ReadConfig


class runnerPage:

    def run_loop_url(self):
        fh = open(ReadConfig.readFilePathData('FilePaths', 'url_list'))
        for line in fh:
            print(line)
            #subprocess.call([r'C:\Users\a.ferdous.CORP\PycharmProjects\com.CheckProofing\Test_Campaign_2021\scripts\shell\runner.bat'])
            subprocess.call([r'C:\Users\a.ferdous.CORP\Anaconda3\envs\com.CheckProofing\python.exe', r'C:\Users\a.ferdous.CORP\PycharmProjects\com.CheckProofing\Test_Campaign_2021\scripts\python\test_main_Page.py'])
            with open(ReadConfig.readFilePathData('FilePaths', 'url_list'), 'r+') as f:
                f.readline()
                data = f.read()
                f.seek(0)
                f.write(data)
                f.truncate()
        fh.close()


if __name__ == '__main__':
    util = runnerPage()
    util.run_loop_url()
