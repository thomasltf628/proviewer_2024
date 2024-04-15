#!/usr/bin/python3
"""roots scraping"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import csv
import time



def Roots(link):
    url = link

    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(3)

    # to close pop up 
    try:
        close_pop = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".close"))
        )
        close_pop.click()
        print('clicked button1')
    except:
        pass

    try:
        # Wait for the element to be clickable
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.extole-js-widget-close"))
        )    
        # Click on the element
        element.click()
        print('Clicked button2')
    except Exception as e:
        print("Error:", e)

    time.sleep(3)
    # Scroll a thousand pixels down to bring the required window to view
    driver.execute_script("window.scrollTo(0, 1000);")
    review_box = driver.find_element(By.CSS_SELECTOR, '.bv-content-list-container')
    driver.execute_script("arguments[0].scrollIntoView(true);", review_box)

    review_list = []

    no_of_reviews = 0

    while no_of_reviews < 15:
        reviews = driver.find_elements(By.CSS_SELECTOR, 'li.bv-content-top-review')
        no_of_reviews += len(reviews)
        for review in reviews:
            try:

                review_s = review.find_element(By.CLASS_NAME, 'bv-content-summary-body-text')
                review_text = review_s.find_element(By.TAG_NAME, 'p').text
                review_list.append(review_text)  
            except NoSuchElementException:
                driver.execute_script("window.scrollTo(0, 500);")  # scroll the page down to bring more review elements to view
                continue
        next_button = review_box.find_element(By.CSS_SELECTOR, '.bv-content-btn-pages-last')  # next button for the next page for reviews
        if next_button.get_attribute('disabled') is not None:  # check if the next button has been disabled
            print('end')
            break
        next_button.click()
        time.sleep(2)
    print(review_list)

    return review_list

    

"""# writing to the csv file
    with open('roots_reviews.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(['username', 'num_of_stars', 'review', 'time'])
        for review in review_list:
            writer.writerow(review)"""



# to bring attention the webpage and prevent overlay by the dropdown bar
"""element = driver.find_element(By.CLASS_NAME, 'user-name')
action = ActionChains(driver)
action.move_to_element(element).perform()
time.sleep(1)"""

"""
            username_box = review.find_element(By.CLASS_NAME, 'bv-author-avatar')
            username = username_box.find_element(By.TAG_NAME, 'h3').text
            rating_box = review.find_element(By.CLASS_NAME, 'bv-rating-stars-container')
            rate = rating_box.find_element(By.CLASS_NAME, 'bv-off-screen').text[0]
            time_box = review.find_element(By.CLASS_NAME, 'bv-content-datetime')
            time_stamp = time_box.find_elements(By.TAG_NAME, 'meta')[1].get_attribute('content')
            review_list.append([username, rate, review_text, time_stamp])  
"""