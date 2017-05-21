'''
#gftestCases.py

__author__ = "Jay"
__version__ = "0.0.3"

"""
Change History

Version 0.0.1

* created the file , Added the Main Page Test Cases

Version 0.0.2

* Added the Logn Page Test Cases,Sign In Page Test Cases,Signed Page Test Cases

Version in 0.0.3

* Added the NewWorkOrder Page Test Cases

"""
'''

#Different test cases for different pages

def gformz_test_cases(number):
	return TestCases[number]

#Severity,Description
TestCases=[
    #[severity, description]
    #Main Page Test Cases
    ['Blocker', 'TEST_01_main_Page_Load - User goes to main page, page should be loaded'],
    #Login Page Test cases
    ['Blocker', 'LOGIN PAGE -TEST_01_login_Link - User click "Login " button, should see Login in Page'],
    #Sign In page Test cases
    ['Blocker', 'SIGIN PAGE -TEST_01_sign_In_Button - User enters the user emai and password'],
    #Signed Page Test Cases 
    ['Blocker', 'SIGNED PAGE -TEST_01_click_Templates - User clicks  the Template link'],
    ['Blocker', 'SIGNED PAGE -TEST_02_click_Sample_Work_Order - User clicks  the Sample Work Oder'],
    ['Blocker', 'SIGNED PAGE -TEST_03_load_Sample_Work_Order_Image - Wait for the Sample Work Oder Image Loaded'],
    ['Blocker', 'SIGNED PAGE -TEST_04_hover_More_Button - Hover the More Button'],
    #NewWorkOrder Page Test Cases
    ['Blocker', 'NEWWORKORDER PAGE - Test_01_load_New_Work_Order_page - The New Work Order page is Loaded'],
    ['Blocker', 'NEWWORKORDER PAGE - Test_02_click_Company_Name - User Clicks the Company Name'],

]

'''
Copyright (c) 2017, Jayakumar (Jay)
All rights reserved.
'''