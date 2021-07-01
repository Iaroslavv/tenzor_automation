from selenium.webdriver.common.by import By

class SearchPageLocators:
    
    """
    Locators which are used to locate elements on the webpage in the methods in
    'base_page.py'.
    """
    SEARCH_TEXT_FIELD = (By.CSS_SELECTOR, "#text")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUGGEST_LIST = (By.CSS_SELECTOR, "ul[role='listbox']")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "li[class='serp-item']")
    