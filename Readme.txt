This is a test suite for www.goformz.com to test the webpages using selenium and python
This framework will work only under the following platform

#Requirements:
#Chrome Browser - Version 58.0(64-bit)
#OS - MAC OSx
#Python - 2.7
#Selenium - 2.4
#Python Unittest
#HTMLTestRunner.py

Any other browser is not tested with this framework.

The test frame work is created in the POM (Python Object Model).

The files in the framework are as follows:

 - gfbase.py (The basic page object)
 - gfpages.py (The actions to do with the page)
 - gflocators.py (The locator identifier for each action on the file)
 - gftestCases.py ( The test cases file)
 - gfrunsuites.py (The various suites of the tests which needs to be run)
 - gftestreport.text ( The actual test report form unittest)
 - gftestsuites_**.html  (The HTMLRunner output for the test cases)
 - __init__.py ( A basic text file as of now)
 - Readme.txt (which is this file - about the instructions)
 
 
Each web page is designed as independent test suites as needed.
More test cases can be added to this suite at a later stage as and when needed.
This also allows the suite to be run independently.

Inside the suite, each test cas is also independent.

This adds the regression to make sure the stability of the suite.

This framework is very modular and needs only very little changes as you move forward.

Challenges:

 How to Execute ?
 
 Each test file can be run independently as follows.
 
 $python gfbase.py
 $python gfpages.py
 $python gflocators.py
 $python gftestCases.py
 
 The test suites can be fully run as 
 $python gfrunsuites.py 
 
 Each of the independent suites can be run as by modifying the gfrunsuites.py as follows:
 
 Modify the line in gfrunsuites.py as follows:
 
 unittest.TextTestRunner(verbosity=2).run(Suite) to 
 unittest.TextTestRunner(verbosity=2).run(NewWorkOrderPageSuite) if you have to run only the
 NewWorkOrderPageSuite
 
 The HTMLRunner portion is commented.
 If you want to run the HTML report, uncomment that part and comment the 
 #unittest.TextTestRunner(verbosity=2).run(Suite)
 
