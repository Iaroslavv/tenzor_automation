from pages.search_page import SearchPage
import pytest

@pytest.mark.skip
def test_search_field_is_present(browser):
    link = "https://yandex.ru"
    page = SearchPage(browser, link)
    page.open()
    page.should_be_search_field()

def test_tensor_in_first_5_links_present(browser):
    link = "https://yandex.ru"
    page = SearchPage(browser, link)
    word = "Тензор"
    page.open()
    page.input_text_into_search_field(word)
    page.should_be_search_suggestions()
    page.click_on_search_button()
    page.should_tensor_be_in_search_results()
 