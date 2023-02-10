from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
from selenium.webdriver.common.by import By

START_URL ="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/devar/Downloads/chromedriver_win32(1)")
browser.get(START_URL)
time.sleep(10)

#Function to scrape the data
def scrape():
    headers = ["proper_name", "distance", "mass", "radius"]
    planet_data = []
    for i in range(0, 210):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for tr_tag in soup.find_all("tr", attrs={"class", "exoplanet"}):
             li_tags = tr_tag.find_all("li")
             temp_list = []
             for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
        planet_data.append(temp_list)
        browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)

#calling function                
scrape()