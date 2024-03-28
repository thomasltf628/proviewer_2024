from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

def scrapping_Shein():
    url = "https://ca.shein.com/SHEIN-Frenchy-Square-Neck-Puff-Sleeve-Ditsy-Floral-Dress-p-10143212-cat-1727.html?src_identifier=st%3D6%60sc%3DDress%60sr%3D0%60ps%3D1&src_module=search&src_tab_page_id=page_goods_detail1709357446550&mallCode=1&pageListType=4&imgRatio=3-4"
    PATH = "C:/Program Files (x86)/chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    chrome_options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(10)

# Close the pop up advertisement
    try: 
        ad_element = WebDriverWait(driver, timeout=10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "c-coupon-box"))
                )
        print('found the ad')
        time.sleep(3)
        button_element = ad_element.find_element(By.TAG_NAME, 'i')
        print('found the buttun')
        time.sleep(3)
        driver.execute_script("arguments[0].click();", button_element)
        print('closed')

    except:
        print('no ad or not found')

    list_of_comment = []
    # find the element containing comment
    try:
        rate_description_elements = driver.find_elements(By.CLASS_NAME, 'rate-des')
        for rate_description_element in rate_description_elements:
            list_of_comment.append(rate_description_element.text)

                
    except Exception as e:
        print("failure")


    driver.quit()
    print(list_of_comment)

if (__name__ == "__main__"):
    scrapping_Shein()

"""
    text_box = WebDriverWait(driver, timeout=10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "common-reviews__list"))
            )
    time.sleep(10)
    blocks = text_box.find_elements(By.CLASS_NAME, 'j-expose__common-reviews__list-item')
    for block in blocks:
        detail = block.find_element(By.CLASS_NAME, 'common-reviews__list-item-detail')
        element = detail.find_element(By.CLASS_NAME, 'rate-des')
        print(element.text)
        ul = detail.find_element(By.TAG_NAME, 'ul')
        lists = detail.find_elements(By.TAG_NAME, 'li')
        for li in lists:
            aspect = li.find_element(By.CLASS_NAME, 'tag-name')
            content = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'tag-content')))
            print(content.text)"""