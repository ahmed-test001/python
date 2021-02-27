@echo off
for /F "tokens=2" %%i in ('date /t') do set mydate=%%i
set mytime=%time%
echo "Current time is::" %mydate%:%mytime%

"C:\Users\a.ferdous.CORP\Anaconda3\envs\com.CheckProofing\python.exe" "C:\Users\a.ferdous.CORP\PycharmProjects\com.CheckProofing\Test_Campaign_2021\scripts\python\test_main_Page.py" >> C:\Users\a.ferdous.CORP\PycharmProjects\com.CheckProofing\Test_Campaign_2021\logs\logReport.log 2>&1
echo "Execution Done" %time%  >> C:\Users\a.ferdous.CORP\PycharmProjects\com.CheckProofing\Test_Campaign_2021\logs\logReport.log 2>&1

exit