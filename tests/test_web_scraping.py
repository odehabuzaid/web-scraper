from web_scraping.scraper import (get_citations_needed_count,
                                  get_citations_needed_report)


def test_successfully_return_citations_needed_count():
    # Arrange
    my_url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    # Actual
    actual = get_citations_needed_count(my_url)
    # Expected
    excepted = 5
    # Assert
    assert actual == excepted

def test_successfully_return_citations_needed_report():
    # Arrange
    my_url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    # Actual
    actual = get_citations_needed_report(my_url)
    # Expected
    text = open('expected.txt', 'r')
    excepted = text.read()
    assert "".join(actual) == excepted





