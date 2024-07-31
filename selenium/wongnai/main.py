from selenium import webdriver
from selenium.webdriver.common.by import By
import bs4
import time
import json

# ตั้งค่าเบราว์เซอร์
chrome_options = webdriver.FirefoxOptions()
driver = webdriver.Chrome(options=chrome_options)

# กำหนดพารามิเตอร์
radius = 50
latitude = 13.7675485
longitude = 100.5633786
size = 100
url = f"https://www.wongnai.com/businesses?spatialInfo.radius={radius}&spatialInfo.coordinate.latitude={latitude}&spatialInfo.coordinate.longitude={longitude}&page.size={size}&rerank=false&domain=1"

# เปิด URL
driver.get(url)

# รอให้โหลดข้อมูล
time.sleep(5)
acceptTrack = driver.find_element(By.XPATH, '//*[@id="c-p-bn"]')
acceptTrack.click()

# ดึงข้อมูลจากหน้าเว็บ
data = driver.page_source
soup = bs4.BeautifulSoup(data, features="html.parser")

# เลือกผลิตภัณฑ์
products = soup.select(".ejocme-0 > div")

results = []

# ตรวจสอบจำนวนผลิตภัณฑ์
print(f"Number of products found: {len(products)}")

# ดึงข้อมูลที่ต้องการ
for product in products:
    product_info = {}

    # ดึงชื่อธุรกิจและคะแนนจาก div:nth-child(3) จนถึง div สุดท้าย
    for i in range(3, len(products) + 1):  # เริ่มจาก div:nth-child(3) จนถึง div สุดท้าย
        name_selector = f".ejocme-0 > div:nth-child({i}) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > h2:nth-child(1)"
        rating_selector = f".ejocme-0 > div:nth-child({i}) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)"
        reviews_selector = f".ejocme-0 > div:nth-child({i}) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2) > span:nth-child(1)"
        type_selector = f".ejocme-0 > div:nth-child({i}) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1) > a:nth-child(1)"
        status_selector = f".ejocme-0 > div:nth-child({i}) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div[class*='sc-1e2uewk-0 hhqfsj sc-1ajs1oj-1 hfQlGI rg16']"

        name = product.select_one(name_selector)
        rating = product.select_one(rating_selector)
        reviews_num = product.select_one(reviews_selector)
        type_food = product.select_one(type_selector)
        status = product.select_one(status_selector)

        if name:
            product_info['name'] = name.text.strip()  # เก็บชื่อธุรกิจเป็นสตริง
        
        if rating:
            product_info['rating'] = rating.text.strip()  # เก็บคะแนนเป็นสตริง

        if reviews_num:
            product_info['reviews_num'] = reviews_num.text.strip()  # เก็บจำนวนรีวิวเป็นสตริง
        else:
            product_info['reviews_num'] = "N/A"  # กรณีไม่มีจำนวนรีวิว

        if type_food:
            product_info['type_food'] = type_food.text.strip()  # เก็บประเภทอาหารเป็นสตริง

        if status:
            product_info['status'] = status.text.strip()  # เก็บสถานะธุรกิจเป็นสตริง
        else:
            product_info['status'] = "N/A"  # กรณีไม่มีสถานะ

    results.append(product_info)

# เขียนผลลัพธ์ลงไฟล์ JSON
with open("results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

# ปิดเบราว์เซอร์
driver.quit()
