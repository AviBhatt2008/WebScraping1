import requests
from bs4 import BeautifulSoup
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
headers = ["name", "distance", "mass", "radius"]
star_data = []

page = requests.get(START_URL)
soup = BeautifulSoup(page.content, "html.parser")

for index, tr in enumerate(soup.find_all("tr")):
    # not including row of headers
    if index != 0:
        temp_list = []

        for index, td in enumerate(tr.find_all("td")):
            # the planet name
            if index == 1:
                # these have no <a> tag
                if td.contents[0] == "Atria\n" or td.contents[0] == "Peacock\n" or td.contents[0] == "Alsephina":
                    temp_list.append(td.contents[0])
                else:
                    temp_list.append(td.find_all("a")[0].contents[0])
            # the planet distance, mass, radius
            elif index == 3 or index == 5 or index == 6:
                temp_list.append(td.contents[0])
            
        star_data.append(temp_list)

#print(star_data)

with open("starData.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    #only writing Sun data for now
    csv_writer.writerow(star_data[0])