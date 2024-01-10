import requests
from bs4 import BeautifulSoup
import pandas as pd

START_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
headers = ["Name", "Distance", "Mass", "Radius"]

page = requests.get(START_URL)
soup = BeautifulSoup(page.content, 'html.parser')


tables = soup.find_all('table', {'class': 'wikitable'})
table = tables[2]  

rows = table.find_all('tr')

stars_data = []

for row in rows[1:]:
    columns = row.find_all('td')
    name = columns[0].text.strip()
    distance = columns[5].text.strip()
    mass = columns[7].text.strip()
    radius = columns[8].text.strip()
    
    star_info = {
        "Name": name,
        "Distance": distance,
        "Mass": mass,
        "Radius": radius
    }
    
    stars_data.append(star_info)

planet_df = pd.DataFrame(stars_data, columns=headers)
planet_df.to_csv("brown_dwarfs_data.csv", index=False)
