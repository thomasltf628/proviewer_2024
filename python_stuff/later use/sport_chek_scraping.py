#!/usr/bin/python3
"""SPort check scraping"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import csv
import time

url = "https://www.sportchek.ca/en/pdp/columbia-women-s-arcadia-ii-hooded-rain-jacket-waterproof-breathable-packable-shell-12545911f.html?loc=plp&&colorCode=COLOUR_BLACK"

driver = webdriver.Firefox()
driver.get(url)
time.sleep(10)


# giving time for the page to load as it seems to be a dynamically loaded website
driver.execute_script("window.scrollTo(0, 2000);")
time.sleep(10)
driver.execute_script("window.scrollTo(0, 3000);")
time.sleep(20)
driver.execute_script("window.scrollTo(0, 4000);")


review_list = []
no_of_reviews = 0
time.sleep(2)


while no_of_reviews< 25:
    reviews_container = driver.find_element(By.ID, 'reviews_container')
    reviews_box = reviews_container.find_elements(By.TAG_NAME, 'section')
    time.sleep(10)
    no_of_reviews += len(reviews_box)
    for reviews in reviews_box:
        try:
            no_of_reviews += 1
            username = reviews.find_element(By.CLASS_NAME, 'hYfEUK')
            no_stars = reviews.find_elements(By.CLASS_NAME, 'gddjnx')
            review = reviews.find_element(By.CLASS_NAME, 'lhBFto')
            time_post = reviews.find_element(By.CLASS_NAME, 'XPWAe')
            review_list.append([username.text, len(no_stars), review.text, time_post.text])
        except:
            driver.execute_script("window.scrollTo(0, 500);")
            continue
    next = driver.find_element(By.CLASS_NAME, 'next')
    next.click()
    
driver.quit()

# writing to the csv file
with open('sport_check_reviews.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(['username', 'num_of_stars', 'review', 'time'])
    for review in review_list:
        writer.writerow(review)




