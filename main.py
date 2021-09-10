import os
from urllib.request import Request, urlopen
from datetime import datetime
from bs4 import BeautifulSoup
from emailSender import send_mail
from dotenv import load_dotenv
from bs4 import ResultSet

load_dotenv()

tickets_url = os.getenv('TICKETS_URL')

def fetch_webpage() -> str:
    '''
    Fetches the raw html as one giant string
    :return: str representation of entire web page
    '''
    req = Request(tickets_url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read().decode('utf-7')
    return page


def find_span(raw_html: str) -> ResultSet:
    '''
    Takes in raw html string, returns only spans containing "On Sale Now"
    :param raw_html:
    :return: ResultSet of html elements that are spans and have "On Sale Now" in the text of the span
    '''
    soup = BeautifulSoup(raw_html, 'html.parser')
    span_elements = soup.find_all("span")
    for span in span_elements:
        if "On Sale Now" in span:
            return span
    return None


def is_on_sale() -> None:
    '''
    Responsible for fetching html of page, parsing the spans from it, and determining if tickets are on sale. This method will send an email updating the 'TO_EMAIL' with the information it finds regarding tickets being on sale
    :return: None
    '''
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