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

The chrome browser has some problem in the click() function since it is pixel based.
So, some of the click() functions are giving problems than I anticipated and is still 
working on it. 

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

However, there is a little caveat for this design since it consumes more time.
But considering the stability and the independency, this may not be a big problem.
However, when the test cases increases to more than a 100, I prefer within the framework
removing the independency of the test cases and keeping the independency of the suite alone.

This framework is very modular and needs only very little changes as you move forward.

Challenges:

This framework is tested only with Chrome Browser. However, since the website itself has 
more images, and javascript driven, it has more click() functionality than any other 
standard websites and when it comes to click, its mostly pixel based in chrome browser. 
So, I have my own challenges for each click to work properly on the Chrome. The easiest 
workaround will be by using Firefox and I do not have a machine with Firefox..

So, the requested test cases for the page is still under work and once I get the right 
locator,it is very easy to create test cases and add on to the suite.

Hence, the test case test_04_hover_More_Button(SignedPageTests) may fail in chrome, even 
though the logic is correct.It is so far not tested with any other browser.

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
 