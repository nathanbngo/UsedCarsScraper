import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    service = Service('chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scrape_car_data(driver, url):
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    cars = []
    listings = soup.find_all('div', class_='listing-class')
    for listing in listings:
        try:
            brand = listing.find('h2', class_='brand-class').text.strip()
            year = listing.find('span', class_='year-class').text.strip()
            price = listing.find('span', class_='price-class').text.strip()
            mileage = listing.find('span', class_='mileage-class').text.strip()
            cars.append({'Brand': brand, 'Year': year, 'Price': price, 'Mileage': mileage})
        except AttributeError:
            continue
    return cars

def save_to_excel(data, filename):
    pd.DataFrame(data).to_excel(filename, index=False)

def visualize_data(filename):
    df = pd.read_excel(filename)
    df['Price'] = df['Price'].replace('[\$,]', '', regex=True).astype(float)
    df['Mileage'] = df['Mileage'].replace('[,]', '', regex=True).astype(int)
    plt.scatter(df['Mileage'], df['Price'], alpha=0.5)
    plt.title('Price vs Mileage')
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.show()
