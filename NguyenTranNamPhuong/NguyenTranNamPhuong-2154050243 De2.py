from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import csv
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get('https://vnexpress.net')
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '#wrap-main-nav li.doisong').click()
print(driver.title)

articles = driver.find_elements(By.CSS_SELECTOR, 'article.item-news')
with open('NguyenTranNamPhuong.csv', 'w', newline='', encoding='utf-8') as f:
    fieldName = ['Title', 'Description', 'Link']
    writer = csv.DictWriter(f, fieldnames=fieldName)
    writer.writeheader()
    for a in articles:
        try:
            title = a.find_element(By.TAG_NAME, 'h3').text
            description = a.find_element(By.TAG_NAME, 'p').text
            link = a.find_element(By.CSS_SELECTOR, 'h3.title-news > a').get_attribute('href')
            print(title)
            print(description)
            print(link)
            print("---------------")
            writer.writerow({'Title': title, 'Description': description, 'Link': link})
        except NoSuchElementException:
            continue

driver.quit()