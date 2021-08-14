from urllib.request import Request, urlopen
import os
from bs4 import BeautifulSoup

tix_not_on_sale_page =  os.path.join(os.getcwd(),'tickets_html.txt')
tickets_url = r'https://dice.fm/partner/bk-made-llc-dba-brooklyn-made-presents/event/bk39x-boy-harsher-31st-oct-brooklyn-made-new-york-tickets'

def fetch_webpage():
    req = Request(tickets_url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read().decode('utf-8')
    return page


def find_span(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    span_elements = soup.find_all("span")
    for span in span_elements:
        if "On Sale Now" in span:
            return span
    return None


def is_on_sale():
    new_page = fetch_webpage()
    new_page_span = find_span(new_page)
    
    return 'disabled' not in str(new_page_span)

def ping_for_tickets():



if __name__== '__main__':
    print(is_on_sale())