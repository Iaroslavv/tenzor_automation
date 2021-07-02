from pages.base_page import BasePage
from pages.locators import SearchPageLocators

class SearchPage(BasePage):
    """
    Contains assert methods checking if functionality is working properly.
    """
    
    def should_be_search_field(self):
        assert self.is_element_present(*SearchPageLocators.SEARCH_TEXT_FIELD), "There's no search field"
    
    def should_be_search_suggestions(self):
        assert self.is_suggest_list_present(*SearchPageLocators.SUGGEST_LIST), "There's no list of suggestions"
    
    def click_on_search_button(self):
        assert self.click_on_search_field_button(*SearchPageLocators.SEARCH_BUTTON), "There's no search button"
    
    def should_tensor_be_in_search_results(self):
        assert self.is_tensor_in_search_results(*SearchPageLocators.SEARCH_RESULTS), "In one of the first 5 results there's no link to tensor.ru"
        