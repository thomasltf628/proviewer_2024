
"""Scraping the puma website for reviews"""
#https://ca.puma.com/ca/en/pd/cali-wedge-womens-sneakers/373438?swatch=01&referrer-category=womens-shop-all-womens
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import csv

def Puma(link):
    review_list =[]
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)

    # click the button that ask for location
    try:
        close_btn = WebDriverWait(driver, timeout=10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-test-id='close-btn']")))
        close_btn.click()
        print("location Button clicked successfully.")
    except Exception as e:
        print("Error:", e)

    # click the button that ask for cookies
    try:
        close_btn = WebDriverWait(driver, timeout=10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-test-id='cookie-banner-close-btn']")))
        close_btn.click()
        print("cookies Button clicked successfully.")
    except Exception as e:
        print("Error:", e)        

    # locate the product reviews block and scroll to it
    product_reviews_block = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "product-reviews"))
        )
    print("product_reviews located successfully.")
    element_position = product_reviews_block.location['y']
    driver.execute_script(f"window.scrollTo(0, {element_position});") 

    # locate the more reviews button and scroll to it, then click
    review = WebDriverWait(driver, timeout=10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'button.tw-19fr0v0:nth-child(2)')))
    element_position = review.location['y'] - 100
    driver.execute_script(f"window.scrollTo(0, {element_position});")
    time.sleep(10)
    review.click()

    review_box = driver.find_element(By.CSS_SELECTOR, 'div.h-full') #The review pop up
    time.sleep(2)

    more_rev = review_box.find_element(By.CSS_SELECTOR, '.tw-12ffx9c')  # the more review button


    #Generate all reviews in the review box using the button
    print('started')
    continue_to_click = 1
    try:
        while continue_to_click < 0:
            more_rev.click()
            time.sleep(1)
            continue_to_click -= 1
    except:    # incase of Stale element exception
        pass


    reviews = review_box.find_elements(By.CLASS_NAME, 'break-words')
    for rev in reviews:
        review_list.append(rev.text)

    return review_list



# write to csv file

"""driver.execute_script("window.scrollTo(0, 3500);") # scroll to where the review arrow can be selected
    print("scrolled")"""

"""options = Options()
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    options.headless = True  # Run headless
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)"""

"""review_df = pd.DataFrame(review_list)
review_df.to_csv(f'{website}.csv', index=False)"""

"""with open('puma_reviews.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(['PUMA'])
    for review in review_list:
        writer.writerow([review])
"""

