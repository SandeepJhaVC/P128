import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

# Initialize the webdriver
driver = webdriver.Chrome()


url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
response = requests.get(url)

driver.get(url)


time.sleep(5)


soup = BeautifulSoup(response.content, 'html.parser')

all_tables = soup.find_all('table')


scraped_data = []


def scrape_row(row):
    columns = row.find_all('td')
    if len(columns) >= 5:

        temp_list = []
        

        temp_list.append(columns[0].text.strip())
        temp_list.append(columns[1].text.strip())
        temp_list.append(columns[2].text.strip())
        temp_list.append(columns[3].text.strip())
        temp_list.append(columns[4].text.strip())

        return temp_list

for table in all_tables:
    all_rows = table.find_all('tr')
    for row in all_rows:
        star_data = scrape_row(row)
        if star_data:
            scraped_data.append(star_data)


df = pd.DataFrame(scraped_data, columns=['Star Name', 'Distance', 'Mass', 'Radius', 'Luminosity'])


df.to_csv('stars_data.csv', index=False)


print(df)
