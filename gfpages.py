'''
#gfpages.py

__author__ = "Jay"
__version__ = "0.0.3"

"""
Change History

Version 0.0.1

* created the file , Added the MainPage(Page)

Version 0.0.2

* Added the LogInPage(Page),SignInPage(Page),SignedPage(Page)

Version in 0.0.3

* Added the NewWorkOrderPage(Page)

"""
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from gfbase import Page
from gflocators import *

class MainPage(Page):

    def page_loaded(self):
        return True if self.find_element(*MainPageLocators.BRAND) else False

class LogInPage(Page):

    def login_Link(self):
        self.find_element(*LoginPageLocators.LOGIN)
        self.find_element(*LoginPageLocators.LOGIN).click()
        return SignInPage(self.driver)

class SignInPage(Page):

    #The below two are the only 2 variables which needs to be changed for a different user
    #Later , a seperate page of users can be created as and when needed minimizing the modification
    #on this page since created.
    
    USER_EMAIL    = "smartweb2u@gmail.com"
    USER_PASSWORD ='smartweb2u'

    def enter_Email(self):
        #print self.USER_EMAIL
        self.find_element(*LoginPageLocators.EMAIL).send_keys(self.USER_EMAIL)

    def enter_Password(self):
        #print self.USER_PASSWORD
        self.find_element(*LoginPageLocators.PASSWORD).send_keys(self.USER_PASSWORD)

    def sign_In_Button(self):
        self.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        #return TemplatePage(self.driver)

    def login(self):
        self.enter_Email()
        self.enter_Password()
        self.sign_In_Button()
        #return TemplatePage(self.driver)

    def login_Valid_User(self):
        self.login()
        return SignedPage(self.driver)

class SignedPage(Page):

    def click_Templates(self):
            self.find_element(*SignedPageLocators.TEMPLATE_LINK).click()

    def click_Sample_Work_Order(self):
            self.find_element(*SignedPageLocators.SAMPLE_WORK_ORDER_LINK).click()

    def load_Sample_Work_Order_Image(self):
        WebDriverWait(self.driver, 10).until(lambda s:self.find_element(*SignedPageLocators.SWO_IMG))

    def hover_More_Button(self):
        self.hover(*SignedPageLocators.MORE_HOVER)


class NewWorkOrderPage(Page):

    def load_New_Work_Order_page(self):
    	WebDriverWait(self.driver, 10).until(lambda s:self.find_element(*NewWorkOrderPageLocators.NWO_PAGE_LOAD))

    def click_Company_Name(self):
        self.find_element(*NewWorkOrderPageLocators.COMPANY_NAME_CLICK)

'''
Copyright (c) 2017, Jayakumar (Jay)
All rights reserved.
'''












 