#!/usr/bin/python3
"""Scraping Nike stores"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import csv
import time

#https://www.adidas.ca/en/gazelle-shoes/IG6212.html

def Adidas(link):
    url = link
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)    
    driver.maximize_window()
    driver.get(url)
    time.sleep(5)

    driver.execute_script("window.scrollTo(0,800);")

    show_reviews = driver.find_element(By.CSS_SELECTOR, '#navigation-target-reviews > div:nth-child(1) > button:nth-child(1)')
    show_reviews.click()

    more_reviews = driver.find_element(By.CSS_SELECTOR, 'button.gl-cta--secondary:nth-child(1)')

    review_boxes = []
    review_list = []

    try:
        while len(review_boxes) < 25:
            more_reviews.click()
            review_boxes = driver.find_elements(By.CSS_SELECTOR, 'div.review___KFNQH')
    except Exception as e:
        print(e)
        pass

    time.sleep(5)


    for review_box in review_boxes:

        review = review_box.find_element(By.CLASS_NAME, 'text___uiKSX').get_attribute('innerHTML')

        review_list.append(review)
    print(review_list)    
    
    return review_list

"""if __name__ == "__main__":
    Adidas(link)"""
    #username = review_box.find_element(By.CLASS_NAME, 'user-name___2Ra0t').text
    #rating_box = review_box.find_elements(By.CLASS_NAME, 'gl-star-rating__mask')
    #no_of_rating = len([star for star in rating_box if star.get_attribute('style') == 'width: 88%;'])  # get the number of 'colored' stars that depict rating based on the difference in width
    #time_post = review_box.find_element(By.CLASS_NAME, 'date___1Ikvn').text    
    #review_list.append([username, no_of_rating, review, time_post])
    # writing to the csv file
"""
    with open('adidas_reviews.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(['username', 'num_of_stars', 'review', 'time'])
        for review in review_list:
            writer.writerow(review)
"""    


