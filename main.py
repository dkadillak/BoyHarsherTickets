from urllib.request import Request, urlopen
import os
from datetime import datetime
from bs4 import BeautifulSoup
from emailSender import send_mail

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
    time = datetime.now().strftime('%d-%m-%Y @ %H:%M')

    if new_page_span is None:
        send_mail('you should probably check it out', f'Something seems wrong with scraper   [{time}]')

    elif 'disabled' in str(new_page_span):
        send_mail('get em next time champ', f'Bad news :(   [{time}]')

    else:
        message = f'Tickets are on sale, go buy! \n \n {tickets_url}'
        send_mail(message, f"TICKETS ARE ON SALE, I REPEAT TICKETS ARE ON SALE   [{time}]")


if __name__== '__main__':
    is_on_sale()