from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import bs4
import time
import re
import pandas as pd

# Open chrom browser
chrome_options = webdriver.FirefoxOptions()
# chrome_options.add_experimental_option("detach", True)  # ไม่ปิดหน้าต่างโดยอัตโนมัติ
driver = webdriver.Chrome(options=chrome_options)

# source web page
driver.get('https://www.adidas.co.th/en?cm_mmc=AdieSEM_Google-_-adidas-SEAPAC-eCom-PPC-B-Brand-Multiple-Exact-TH_EN-SEAPAC-eCom-Paid_Search-_-Brand-adidas-Shop-_-adidas+shop-_-dv:eCom&cm_mmc1=TH&cm_mmc2=e&gad_source=1&gclid=CjwKCAiA8sauBhB3EiwAruTRJqbUvNcUk63e42nUH8ZlcrjI2zTx0gaz6beSkcx5XYs_7Y4naKeCmBoC6c4QAvD_BwE&gclsrc=aw.ds')

# Accep track
time.sleep(2)
acceptTrack = driver.find_element(By.XPATH, '//*[@id="glass-gdpr-default-consent-accept-button"]')
acceptTrack.click()

# searchbar
time.sleep(1)
search = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/header/div[2]/div/div[2]/div/input')
search.send_keys("joggers")
time.sleep(0.5)
search.send_keys(Keys.RETURN)

# Scrapping
time.sleep(20)  # หน่วงเวลาเพิ่มเติม
data = driver.page_source #ดึงข้อมูลจากหน้าเว็บ
soup = bs4.BeautifulSoup(data, features="html.parser")

products = soup.select(".plp-grid___1FP1J > div")  # 48 ชิ้น

# Scrapping Name
# for product in products:
#     name1 = product.select_one("div.grid-item > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3) > div:nth-child(1) > p:nth-child(1)")
#     name2 = product.select_one("div.grid-item > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2) > div:nth-child(1) > p:nth-child(1)")
    
#     name = name1 + name2

#     # ใช้ .text.strip() เพื่อดึงข้อความที่อยู่ภายใน element และลบช่องว่างหน้าและท้ายของข้อความออกไป (หากมี)
#     print(name1.text.strip() if name1 else name2.text.strip())

product = products[7]

# name
product.select_one("div.grid-item > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3) > div:nth-child(1) > p:nth-child(1)")
product.select_one("div.grid-item > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2) > div:nth-child(1) > p:nth-child(1)")

# price
price_normai = product.select_one("div.grid-item > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
price_discount = product.select_one("div.grid-item > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)")

# detail
detail1 = product.select_one("div.grid-item > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3) > div:nth-child(1) > p:nth-child(2)")
detail2 = product.select_one("div.grid-item > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2) > div:nth-child(1) > p:nth-child(2)")
