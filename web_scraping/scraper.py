import requests
from bs4 import BeautifulSoup


def get_wiki_page(url,tag,title):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.find_all(tag, title=title)

def get_citations_needed_count(url):
    """
    used to count the the number of citations needed
    
    arguments : url -> String
    
    returns   : count -> int
    """
    pass

def get_citations_needed_report(url):
    """
    used to return all citations needed
    
    arguments : url -> String
    
    returns   : count -> int
    """
    pass
 
