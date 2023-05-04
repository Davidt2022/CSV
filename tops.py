import requests
from bs4 import BeautifulSoup
import csv
from flask import Flask, render_template

url = 'https://us.burberry.com/mens-polo-shirts-t-shirts/#/t-shirts/'


def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def parse(soup):
    items = []
    results = soup.find_all('div', {'class': 'product-card__detail-wrapper'})


    for result in results:
        title = result.find('p', {'class': 'product-card__content-title'}).text.strip()
        price = result.find('span', {'class': 'product-card__price-current'}).text.strip()
        items.append({'Title': title, '$Price': price})


    return items


soup = get_data(url)
data = parse(soup)


with open('tops.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Title', '$Price'])
    writer.writeheader()
    for item in data:
        writer.writerow(item)
        print(item)