import requests
from bs4 import BeautifulSoup


def get_quote(quote_number):
    """Function to scrape quotes from quotes.toscrape.com"""
    all_quotes = parsed.find_all('div', class_='quote')
    quote_number = int(quote_number)
    quote = all_quotes[quote_number - 1].find('span', class_='text').text
    author = all_quotes[quote_number - 1].find('small', class_='author').text
    tags = all_quotes[quote_number - 1].find_all('a', class_='tag')
    tags_list = []
    for tag in tags:
        tags_list.append(tag.text)
    tags_string = 'Tags: ' + ', '.join(tags_list)
    return f'{quote} - {author}\n{tags_string}'


url = requests.get('https://quotes.toscrape.com/page/1/')

parsed = BeautifulSoup(url.text, 'html.parser')
print(parsed.title.text)


while True:
    quote_number = input('Enter the number of the quote: ')
    if quote_number.isdigit() and 1 <= int(quote_number) <= 10:
        break
    else:
        print('Please enter a valid quote number!')


print(get_quote(quote_number))
