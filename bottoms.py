import requests
from bs4 import BeautifulSoup
import csv
from flask import Flask, render_template

url = 'https://us.burberry.com/mens-trousers-shorts/#/shorts/'

def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def parse(soup):
    items = []
    results = soup.find_all('div', {'class': 'product-card__detail-wrapper'})

    for item in results [:20]:
        title = item.find('p', {'class': 'product-card__content-title'}).text
        price = item.find('span', {'class': 'product-card__price-current'}).text.replace('$', '').replace(',', '').strip()
        items.append({'Title': title, '$Price': price})

    return items


soup = get_data(url)
data = parse(soup)


with open('bottoms.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Title', '$Price'])
    writer.writeheader()
    for item in data:
        writer.writerow(item)
        print(item)