#!/usr/bin/python3
"""SPort check scraping"""
#link = "https://www.sportchek.ca/en/pdp/columbia-women-s-arcadia-ii-hooded-rain-jacket-waterproof-breathable-packable-shell-12545911f.html?loc=plp&&colorCode=COLOUR_BLACK"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

def Sportchek(link):
    
    """driver = webdriver.Firefox()"""
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(link)
    time.sleep(3)
    # giving time for the page to load as it seems to be a dynamically loaded website
    driver.execute_script("window.scrollTo(0, 2000);")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0, 3000);")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0, 4000);")

    review_list = []
    no_of_reviews = 0
    while no_of_reviews < 15:
        reviews_container = WebDriverWait(driver, timeout=10).until(
                EC.presence_of_element_located((By.ID, 'reviews_container')))
        reviews_box = reviews_container.find_elements(By.TAG_NAME, 'section')
        time.sleep(10)
        no_of_reviews += len(reviews_box)
        for reviews in reviews_box:
            try:
                review = reviews.find_element(By.CLASS_NAME, 'lhBFto')
                review_list.append(review.text)
                print(review.text)            
                no_of_reviews += 1

            except:
                try:
                    # You can locate the button by its ID
                    button = driver.find_element(By.ID, 'kplDeferButton')
                    button.click()
                    print("Button clicked successfully.")
                except NoSuchElementException:
                    pass
                driver.execute_script("window.scrollTo(0, 500);")
                continue
        next = driver.find_element(By.CLASS_NAME, 'next')
        next.click()
    return review_list



# writing to the csv file
"""with open('sport_check_reviews.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(['username', 'num_of_stars', 'review', 'time'])
    for review in review_list:
        writer.writerow(review)"""

"""            username = reviews.find_element(By.CLASS_NAME, 'hYfEUK')
            no_stars = reviews.find_elements(By.CLASS_NAME, 'gddjnx')
            review = reviews.find_element(By.CLASS_NAME, 'lhBFto')
            time_post = reviews.find_element(By.CLASS_NAME, 'XPWAe')
            review_list.append([username.text, len(no_stars), review.text, time_post.text])"""


