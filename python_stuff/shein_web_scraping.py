#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

link = 'https://ca.shein.com/SHEIN-LUNE-Floral-Print-2-In-1-Short-Sleeve-T-Shirt-p-29793312.html?src_identifier=fc%3DWomen%20Clothing%60sc%3DWomen%20Clothing%60tc%3DShop%20by%20category%60oc%3DTops%60ps%3Dtab03navbar03menu01dir04%60jc%3DitemPicking_017175498&src_module=topcat&src_tab_page_id=page_goods_detail1713244365136&mallCode=1&pageListType=2&imgRatio=3-4'

def SHEIN(link):
    review_list =[]
    chrome_options = webdriver.ChromeOptions()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    chrome_options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(link)
    print('started')

    # Close the pop up advertisement and puzzle thing
    try:
        puzzle_element = WebDriverWait(driver, timeout=20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "geetest_close")))
        time.sleep(5)
        puzzle_element.click()
        print('puzzle closed')
    except:
        print('no puzzle found')

    try:
        ad_close = WebDriverWait(driver, timeout=10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.c-coupon-box > i:nth-child(1)')))
        ad_close.click()
        print('ad closed')
    except:
        print('no ad found')

    try:
        ad2_close = WebDriverWait(driver, timeout=10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'svgicon.svgicon-arrow-left')))
        ad2_close.click()
        print('ad2 closed')
    except:
        print('no ad2 found')



    # Function to get reviews from a page
    def get_reviews():
        try:
            rate_description_elements = driver.find_elements(By.CLASS_NAME, 'rate-des')
            for rate_description_element in rate_description_elements:
                review_list.append(rate_description_element.text)

                    
        except Exception as e:
            print("failure")



    driver.execute_script(f"window.scrollTo(0, 2000);")
    time.sleep(5)
    page_nav = driver.find_element(By.CLASS_NAME, 'sui-pagination.sui-pagination__right')
    page_num = 2
    while page_num <= 3:
        get_reviews()
        try:
            next = page_nav.find_element(By.XPATH, f"//span[text()='{page_num}']")
            page_num += 1
            print(page_num)
            time.sleep(1)
            next.click()
        except NoSuchElementException:
            print('404 not found')
            print(review_list)   
            break
        return review_list  # return the list of comment back to the flask app for further processing

if __name__ == "__main__":
    SHEIN(link)

"""with open('shein_reviews.csv', 'a') as f:
    writer = csv.writer(f)
    # writer.writerow(['SHEIN'])
    for review in review_list:
        writer.writerow([review])"""


"""reviews = driver.find_elements(By.CLASS_NAME, 'rate-des')
    for i in range(0, len(reviews), 2):
        if i < len(reviews):
            rev = reviews[i].get_attribute('innerHTML')
            if rev != '':
                review_list.append(rev)"""

