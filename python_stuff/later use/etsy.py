from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

no_of_reviews = 0
review_list =[]



url = 'https://www.etsy.com/ca?utm_source=google&utm_medium=cpc&utm_term=etsy%20canada_e&utm_campaign=Search_CA_Brand_GGL_ENG_General-Brand_Core_All_Exact&utm_ag=A1&utm_custom1=_k_CjwKCAjw17qvBhBrEiwA1rU9wwwgcvrtllS7j85Qlj6jDIuOjAy1tkk_jCaxuM8zdMClenqXZfMfmxoC48EQAvD_BwE_k_&utm_content=go_1463443864_59403767200_679371939093_kwd-307732359762_m_&utm_custom2=1463443864&gad_source=1&gbraid=0AAAAADutTMfOwlrKLhdXxc_jUJ9bVeH9c&gclid=CjwKCAjw17qvBhBrEiwA1rU9wwwgcvrtllS7j85Qlj6jDIuOjAy1tkk_jCaxuM8zdMClenqXZfMfmxoC48EQAvD_BwE'

url = 'https://www.etsy.com/listing/1700218027/womens-cotton-vest-ready-to-ship-summer?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sc_gallery-1-3&sts=1&plkey=2892b6bee75d27eb9f18f8d3fa2906779abdc89b%3A1700218027'

url = 'https://www.etsy.com/listing/1666024421/womens-linen-vest-linen-vest-cropped?ref=listing_page_ad_row-3&sts=1&plkey=9871ca7799275aa94fdf1eda173f6e54ee022fc1%3A1666024421&listing_id=1666024421&listing_slug=womens-linen-vest-linen-vest-cropped'
driver = webdriver.Firefox()
driver.get(url)
print('gotten')


time.sleep(2)
print('started')

def get_reviews():
    """Function to get reviews from a page"""
    reviews = driver.find_elements(By.CLASS_NAME, 'wt-text-body')
    time.sleep(2)
    if reviews[0].text:
        for i in range(0, len(reviews), 2):
            if i < len(reviews):
                review_list.append(reviews[i].text)

while no_of_reviews < 51:
    nav = driver.find_elements(By.XPATH, '//nav[@aria-label="Pagination"]')
    nav = nav[0]
    ul = nav.find_elements(By.XPATH, './*')
    ul = ul[0]
    buttons = ul.find_elements(By.XPATH, './*')
    next = buttons[-1]
    get_reviews()
    no_of_reviews += 1
    next.click()
    time.sleep(5)
    

print(review_list)


with open('reviews.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(['ETSY'])
    for review in review_list:
        writer.writerow([review])