import pytest

from pages.result import DuckDuckGoResultsPage
from pages.search import DuckDuckGoSearchPage

def test_search_from_results_page(browser):
    # GIVEN: the DuckduckGo home page is displayed
    # WHEN: the user searches for <phrase>
    # AND: user changes the search in the results page to <phrase>
    # THEN: the search results are changed into the new <phrase> (all links)
    # AND: the search result title contains <phrase>
    # AND: the search result query is <phrase>
    raise Exception("Not Implemented Test")

def test_search_images(browser):
    # GIVEN: the DuckduckGo home page is displayed
    # WHEN: the user searches for <phrase>
    # AND: user select images results
    # THEN: the search results are changed into images with titles containing <phrase>
    # AND: image resolution label appears
    raise Exception("Not Implemented Test")

def test_search_videos(browser):
    # GIVEN: the DuckduckGo home page is displayed
    # WHEN: the user searches for <phrase>
    # AND: user select videos results
    # THEN: the search results are changed into videos with video names containing <phrase>
    # AND: video source img and label appears
    raise Exception("Not Implemented Test")

def test_search_news(browser):
    # GIVEN: the DuckduckGo home page is displayed
    # WHEN: the user searches for <phrase>
    # AND: user select news results
    # THEN: the search results are changed into news
    raise Exception("Not Implemented Test")