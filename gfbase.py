'''
#gfbase.py

__author__ = "Jay"
__version__ = "0.0.3"

"""
Change History

Version 0.0.1

* created the file , Added the find_element()

Version 0.0.2

* Added the open(), get_url(),get_title()

Version in 0.0.3

* Added the hover()

"""
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


# this Base class is serving basic attributes for every single page inherited from Page class


class Page(object):

    def __init__(self, driver, base_url=' '):

        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
 
    def find_element(self, *locator):
        '''
        Returns the object of the locator.
        :param locator: 
        :return: the object address.
        '''
        return self.driver.find_element(*locator)
 
    def open(self,url):
        '''
        Opens the passed URL
        :param url: 
        :return:
        '''
        #url = self.base_url + url
        self.driver.get(url)
        
    def get_title(self):
        """
        Returns the title of the URl
        :return: the title of the url
        """
        return self.driver.title
        
    def get_url(self):
        '''
        Get the URL 
        :return: URL address.
        '''
        return self.driver.current_url

    def hover(self,*locator):
        '''
        Hover the mouse over passed locator
        :param locator: 
        :return: 
        '''
        element =self.find_element(*locator)
        hover=ActionChains(self.driver).move_to_element(element).click().perform()

'''
Copyright (c) 2017, Jayakumar (Jay)
All rights reserved.
'''