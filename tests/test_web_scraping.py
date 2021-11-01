from web_scraping import __version__, scraper


def test_version():
    assert __version__ == '0.1.0'

def test_successfully_return_citations_needed_count():
    # Arrange
    my_url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    # Actual
    actual = scraper.get_citations_needed_count(my_url)
    # Expected
    excepted = 5
    # Assert
    assert actual == excepted

