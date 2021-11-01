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
    citations_needed = get_wiki_page(url,"a", title="Wikipedia:Citation needed")
    return len(citations_needed)

def get_citations_needed_report(url):
    """
    used to return all citations needed
    
    arguments : url -> String
    
    returns   : count -> int
    """

    cites = get_wiki_page(url,"a", title="Wikipedia:Citation needed")
 
    cn_content = ''
    for cite in cites:
        parent_p = cite.find_parent("p")
        paragraph = str(parent_p.text).replace('[citation needed]','').replace('[6]','')
        cn_content += paragraph + "\n"
    return cn_content


print(get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico'))
print(get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico'))
