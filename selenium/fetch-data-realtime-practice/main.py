from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.set.or.th/th/market/product/stock/quote/PTTEP/price')


def showInfFunc():
    name = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[2]/h1').text 
    price = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div[1]/div[5]/div[2]/div[2]/div[3]/div[2]').text
    maxValue = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[1]/span').text
    time = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[1]/div[2]/span').text
    minValue = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/span').text 
    status = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div[6]/div/div/div[1]/div[1]/span').text

    driver.refresh()
    return name, price, maxValue, time, minValue, status

while True:
    data = showInfFunc()
    print("ชื่อหุ้น:", data[0])
    print("ราคา = {} บาท".format(data[1]))
    print("ราคาสูงสุด = {} บาท".format(data[2]))
    print("ราคาต่ำสุด = {} บาท".format(data[4]))
    print(data[3])
    print("สถานะตลาด : {}".format(data[5]))

    time.sleep(5) # Delay 5 sec
