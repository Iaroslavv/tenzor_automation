from selenium.common.exceptions import NoSuchElementException,TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import SearchPageLocators
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:
    def __init__(self, browser: str, url: str, timeout=20):
        """Class constructor.
        :param browser:
        :param url:
        """
        self.browser = browser
        self.url = url
        self.timeout = timeout
    
    def open(self):
        """ 
        Opens the page using the method (get)
        """
        self.browser.get(self.url)
    
    def input_text_into_search_field(self, input_text):
        """
        Inputs text into the search field
        :param input_text:
        """
        self.browser.implicitly_wait(25)
        self.browser.find_element(*SearchPageLocators.SEARCH_TEXT_FIELD).send_keys(input_text)
    
    def click_on_search_field_button(self, how, what):
        self.browser.implicitly_wait(15)
        self.browser.find_element(how, what).click()
    
    def is_element_present(self, how, what):
        """
        Checks if element is presented on the page
        :param how: the way how searching functions
        :param what: what to look for
        """
        try:
            self.browser.implicitly_wait(25)
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    
    def is_suggest_list_present(self, how, what):
        
        try:
            self.browser.implicitly_wait(5)
            suggest_list = self.browser.find_element(how, what)
            suggestions_present = suggest_list.find_elements(By.TAG_NAME, "li")
        except NoSuchElementException:
            return False
        return len(suggestions_present) > 0
    
    def is_tenzor_in_search_results(self, how, what):
        try:
            self.browser.implicitly_wait(5)
            search_results = self.browser.find_elements(how, what)
            results_links = [link for link in search_results]
            print(results_links)        
        except NoSuchElementException:
            return False
        print("RESULT LINKS:", results_links)
        return True
