'''
#gfrunsuites.py

__author__ = "Jay"
__version__ = "0.0.3"

"""
Change History

Version 0.0.1

* created the file , Added the MainPageTests

Version 0.0.2

* Added the LogInPageTests,SignInPageTests,SignedPageTests

Version in 0.0.3

* Added the NewWorkOrderPageTests

"""
'''


import unittest
import gfpages
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gftestCases import gformz_test_cases
from gflocators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import HTMLTestRunner
import time

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})



class MainPageTests(unittest.TestCase):
    
    def setUp(self):
        self.driver =webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://www.goformz.com")
    
    def test_01_main_page_load(self):
        print "\n" +str(gformz_test_cases(0))
        page=gfpages.MainPage(self.driver)
        self.assertTrue(page.page_loaded())
    
    def tearDown(self):
        self.driver.close()

class LogInPageTests(unittest.TestCase):
    
    def setUp(self):
        self.driver =webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://www.goformz.com")
    
    def test_01_login_link(self):
        print "\n" +str(gformz_test_cases(1))
        #Here the Assignment of the MainPage is done.
        page=gfpages.LogInPage(self.driver)
        #self.assertTrue(page.click_Login_link())
        loginpage=page.login_Link()
        self.driver.implicitly_wait(10)
        self.assertIn("accounts.goformz.com",loginpage.get_url())
        login_url=self.driver.current_url
        
    def tearDown(self):
        self.driver.close() 

class SignInPageTests(unittest.TestCase):

    def setUp(self):
        self.driver =webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://www.goformz.com")
    
    def test_01_sign_in_button(self):
        print "\n" +str(gformz_test_cases(2))
        page=gfpages.LogInPage(self.driver)
        loginPage=page.login_Link()
        signinpage=gfpages.SignInPage(self.driver)
        self.driver.implicitly_wait(10)
        #user logs in with the user name and password
        signinpage.login()
        self.assertIn("app.goformz.com",signinpage.get_url())
        signed_url=self.driver.current_url
        print "Logged In Page :" +signed_url
    
    def tearDown(self):
        self.driver.close()

class SignedPageTests(unittest.TestCase):

    def setUp(self):
        self.driver =webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://www.goformz.com")
    
    def test_01_click_Templates(self):
        print "\n" +str(gformz_test_cases(3))
        page=gfpages.LogInPage(self.driver)
        loginPage=page.login_Link()
        signinpage=gfpages.SignInPage(self.driver)
        self.driver.implicitly_wait(10)
        signinpage.login()
        signedpage=gfpages.SignedPage(self.driver)
        templatelink=signedpage.click_Templates()
        self.assertIn("#Template",signedpage.get_url())
        template_url=self.driver.current_url
        print "Dashboard Page : " +template_url
    
    def test_02_click_Sample_Work_Order(self):
        print "\n" +str(gformz_test_cases(4))
        page=gfpages.LogInPage(self.driver)
        loginPage=page.login_Link()
        signinpage=gfpages.SignInPage(self.driver)
        self.driver.implicitly_wait(10)
        signinpage.login()
        signedpage=gfpages.SignedPage(self.driver)
        templatelink=signedpage.click_Templates()
        signedpage = gfpages.SignedPage(self.driver)
        signedpage.click_Sample_Work_Order()
        self.assertIn("/#Template/edit?",signedpage.get_url())
        saveresult=self.driver.current_url
        print "Template Page :" +saveresult

    def test_03_load_Sample_Work_Order_Image(self):
        print "\n" + str(gformz_test_cases(5))
        page = gfpages.LogInPage(self.driver)
        loginPage = page.login_Link()
        signinpage = gfpages.SignInPage(self.driver)
        self.driver.implicitly_wait(10)
        signinpage.login()
        signedpage = gfpages.SignedPage(self.driver)
        templatelink = signedpage.click_Templates()
        signedpage = gfpages.SignedPage(self.driver)
        signedpage.click_Sample_Work_Order()
        swo_img_load = signedpage.load_Sample_Work_Order_Image()
        self.assertIn("/#Template/edit?", signedpage.get_url())

    #This test case logic is correct. May work under Firefox.But Chrome has some problem.

    def test_04_hover_More_Button(self):
        print "\n" + str(gformz_test_cases(6))
        page = gfpages.LogInPage(self.driver)
        loginPage = page.login_Link()
        signinpage = gfpages.SignInPage(self.driver)
        self.driver.implicitly_wait(10)
        signinpage.login()
        signedpage = gfpages.SignedPage(self.driver)
        templatelink = signedpage.click_Templates()
        signedpage = gfpages.SignedPage(self.driver)
        signedpage.click_Sample_Work_Order()
        swo_img_load = signedpage.load_Sample_Work_Order_Image()
        hovermenu_button = signedpage.hover_More_Button()
        self.assertEqual('More', hovermenu_button.text)

    def tearDown(self):
        self.driver.close()

class NewWorkOrderPageTests(unittest.TestCase):

        def setUp(self):
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get("http://www.goformz.com")

        def test_01_load_New_Work_Order_page(self):
            print "\n" + str(gformz_test_cases(7))
            page = gfpages.LogInPage(self.driver)
            loginPage = page.login_Link()
            signinpage = gfpages.SignInPage(self.driver)
            self.driver.implicitly_wait(10)
            signinpage.login()
            signedpage = gfpages.SignedPage(self.driver)
            templatelink = signedpage.click_Templates()
            signedpage = gfpages.SignedPage(self.driver)
            signedpage.click_Sample_Work_Order()
            swo_img_load = signedpage.load_Sample_Work_Order_Image()
            signedpage_url = self.driver.current_url
            print "Sample Work Order Page : " + signedpage_url
            print " "
            #Round about way of getting the editor page since my click has problem with Chrome Browser.
            newworkorderpage_url=signedpage_url.replace('/#Template/edit?','/editor#?f')
            print "NewWorkOrder Page :" +newworkorderpage_url
            newworkorderpage_url=self.driver.get(newworkorderpage_url)
            self.driver.implicitly_wait(10)
            self.assertIn("editor#?f",self.driver.current_url)

        #Still Under construction .Only to get the right parameters by trial and error method. Then it is easy
        #to add further test cases.
        '''
        def test_02_click_Company_Name(self):
            print "\n" + str(gformz_test_cases(8))
            page = gfpages.LogInPage(self.driver)
            loginPage = page.login_Link()
            signinpage = gfpages.SignInPage(self.driver)
            self.driver.implicitly_wait(10)
            signinpage.login()
            signedpage = gfpages.SignedPage(self.driver)
            templatelink = signedpage.click_Templates()
            signedpage = gfpages.SignedPage(self.driver)
            signedpage.click_Sample_Work_Order()
            swo_img_load = signedpage.load_Sample_Work_Order_Image()
            signedpage_url = self.driver.current_url
            print signedpage_url
            newworkorderpage_url = signedpage_url.replace('/#Template/edit?', '/editor#?f')
            print newworkorderpage_url
            newworkorderpage_url = self.driver.get(newworkorderpage_url)
            self.driver.implicitly_wait(10)
            newworkorderpage=newworkorderpage_url(self.driver)
            click_company_name =newworkorderpage.click_Company_Name()
        '''
        def tearDown(self):
            self.driver.close()

if __name__ == "__main__":

    MainPageSuite = unittest.TestLoader().loadTestsFromTestCase(MainPageTests)

    LogInPageSuite = unittest.TestLoader().loadTestsFromTestCase(LogInPageTests)

    SignInPageSuite = unittest.TestLoader().loadTestsFromTestCase(SignInPageTests)

    SignedPageSuite = unittest.TestLoader().loadTestsFromTestCase(SignedPageTests)

    NewWorkOrderPageSuite = unittest.TestLoader().loadTestsFromTestCase(NewWorkOrderPageTests)

    Suite = unittest.TestSuite([MainPageSuite,LogInPageSuite,SignInPageSuite,SignedPageSuite,NewWorkOrderPageSuite])

    #unittest.TextTestRunner(verbosity=2).run(Suite)
    dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    buf = file("gftestsuites" +"_" +dateTimeStamp + ".html",'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='HTML Test Report for goformz.com',
        description='Result of all Test Suites'
    )
    runner.run(Suite)

'''
Copyright (c) 2017, Jayakumar (Jay)
All rights reserved.
'''