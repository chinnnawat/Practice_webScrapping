from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import bs4
import time
import json

# เปิดเบราว์เซอร์ Firefox
chrome_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=chrome_options)

# เปิดหน้าเว็บ
driver.get('https://www.adidas.co.th/en?cm_mmc=AdieSEM_Google-_-adidas-SEAPAC-eCom-PPC-B-Brand-Multiple-Exact-TH_EN-SEAPAC-eCom-Paid_Search-_-Brand-adidas-Shop-_-adidas+shop-_-dv:eCom&cm_mmc1=TH&cm_mmc2=e&gad_source=1&gclid=CjwKCAiA8sauBhB3EiwAruTRJqbUvNcUk63e42nUH8ZlcrjI2zTx0gaz6beSkcx5XYs_7Y4naKeCmBoC6c4QAvD_BwE&gclsrc=aw.ds')

# ยอมรับการติดตาม
time.sleep(2)
acceptTrack = driver.find_element(By.XPATH, '//*[@id="glass-gdpr-default-consent-accept-button"]')
acceptTrack.click()

# ค้นหาสินค้า
time.sleep(1)
search = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/header/div[2]/div/div[2]/div/input')
search.send_keys("joggers")
time.sleep(0.5)
search.send_keys(Keys.RETURN)

# สแครปข้อมูล
time.sleep(20)  # หน่วงเวลาเพิ่มเติม
data = driver.page_source  # ดึงข้อมูลจากหน้าเว็บ
soup = bs4.BeautifulSoup(data, features="html.parser")

products = soup.select(".plp-grid___1FP1J > div")  # 48 ชิ้น

# รายการสำหรับเก็บข้อมูล
results = []

# สแครปข้อมูลสินค้าทั้งหมด
for product in products:
    product_info = {}

    # ดึงชื่อสินค้า
    name1 = product.select_one("div.grid-item > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3) > div:nth-child(1) > p:nth-child(1)")
    name2 = product.select_one("div.grid-item > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2) > div:nth-child(1) > p:nth-child(1)")
    product_info['name'] = name1.text.strip() if name1 else (name2.text.strip() if name2 else "N/A")

    # ดึงราคา
    price_normal = product.select_one("div.grid-item > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
    price_discount = product.select_one("div.grid-item > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)")

    product_info['price_normal'] = price_normal.text.strip() if price_normal else "N/A"
    product_info['price_discount'] = price_discount.text.strip() if price_discount else "N/A"

    # ดึงรายละเอียด
    detail1 = product.select_one("div.grid-item > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3) > div:nth-child(1) > p:nth-child(2)")
    detail2 = product.select_one("div.grid-item > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2) > div:nth-child(1) > p:nth-child(2)")

    product_info['detail'] = detail1.text.strip() if detail1 else (detail2.text.strip() if detail2 else "N/A")

    # เพิ่มข้อมูลในรายการ
    results.append(product_info)

# บันทึกข้อมูลเป็น JSON
with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

# ปิดเบราว์เซอร์
driver.quit()
