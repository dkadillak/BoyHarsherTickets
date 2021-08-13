from urllib.request import Request, urlopen
import os
from bs4 import BeautifulSoup

tix_not_on_sale_page =  os.path.join(os.getcwd(),'tickets_html.txt')
tickets_url = r'https://dice.fm/partner/bk-made-llc-dba-brooklyn-made-presents/event/bk39x-boy-harsher-31st-oct-brooklyn-made-new-york-tickets'

def fetch_webpage():
    req = Request(tickets_url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read().decode('utf-8')
    return page


def ticket_alert():
    old_page = open(tix_not_on_sale_page, 'r').read()
    soup = BeautifulSoup(old_page, 'html.parser')
    span_elements = soup.find_all("span")
    for span in span_elements:
        if "On Sale Now" in span:
            return span






if __name__== '__main__':
    print(ticket_alert())