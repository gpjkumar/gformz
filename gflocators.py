'''
#gflocators.py

__author__ = "Jay"
__version__ = "0.0.3"

"""
Change History

Version 0.0.1

* created the file , Added the MainPageLocators()

Version 0.0.2

* Added the LogInPageLocators(),SignedPageLocators()

Version in 0.0.3

* Added the NewWorkOrderPageLocators()

"""
'''
from selenium.webdriver.common.by import By

#Different locators for Different web pages

class MainPageLocators(object):
	BRAND          = (By.ID, 'goformz-brand')

class LoginPageLocators(object):
	LOGIN			 = (By.LINK_TEXT, 'Login')
	EMAIL		     = (By.NAME,'username')
	PASSWORD	     = (By.NAME, 'password')
	LOGIN_BUTTON     = (By.XPATH,'//*[@id="gflogin"]/div[1]/form/fieldset/div[3]/button')

class SignedPageLocators(object):
	TEMPLATE_LINK    		= (By.LINK_TEXT,'Templates')
	STARTER_TEMPLATE_LINK 	= (By.LINK_TEXT,'Starter Templates')
	SAMPLE_WORK_ORDER_LINK	= (By.LINK_TEXT,'Sample Work Order')
	SWO_PAGE_RESULT			= (By.XPATH,'//*[@id="saveResult"]')
	SWO_IMG					= (By.TAG_NAME,'img')
	MORE_HOVER				= (By.CSS_SELECTOR,'div.x-btn.secondary-cta-btn button span.x-btn-inner')


class NewWorkOrderPageLocators(object):
	NWO_PAGE_LOAD =(By.ID,'mainCanvas')
	COMPANY_NAME_CLICK =(By.XPATH,'//*[@id="editor"]')

'''
Copyright (c) 2017, Jayakumar (Jay)
All rights reserved.
'''