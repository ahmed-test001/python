@echo off
for /F "tokens=2" %%i in ('date /t') do set mydate=%%i
set mytime=%time%
set t=%date%_%time%
set d=%t:~10,4%%t:~7,2%%t:~4,2%_%t:~15,2%%t:~18,2%%t:~21,2%
echo "Current time is::" %mydate%:%mytime%


"C:\Users\a.ferdous.CORP\Anaconda3\envs\com.CheckProofing\python.exe" "C:\Users\a.ferdous.CORP\PycharmProjects\com.CheckProofing\Test_Campaign_2021\scripts\python\Utility_Page.py" >> C:\Users\a.ferdous.CORP\PycharmProjects\com.CheckProofing\Test_Campaign_2021\logs\logReport_%d%.log 2>&1
echo "URLs Extracted" %time%  >> C:\Users\a.ferdous.CORP\PycharmProjects\com.CheckProofing\Test_Campaign_2021\logs\logReport_%d%.log 2>&1




"C:\Users\a.ferdous.CORP\Anaconda3\envs\com.CheckProofing\python.exe" "C:\Users\a.ferdous.CORP\PycharmProjects\com.CheckProofing\Test_Campaign_2021\scripts\python\test_mainRunner.py" >> C:\Users\a.ferdous.CORP\PycharmProjects\com.CheckProofing\Test_Campaign_2021\logs\logReport_%d%.log 2>&1
echo "Execution Done" %time%  >> C:\Users\a.ferdous.CORP\PycharmProjects\com.CheckProofing\Test_Campaign_2021\logs\logReport_%d%.log 2>&1

exit