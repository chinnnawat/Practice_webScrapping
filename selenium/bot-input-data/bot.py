from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open chrom browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # ไม่ปิดหน้าต่างโดยอัตโนมัติ
driver = webdriver.Chrome(options=chrome_options)

# source web page
driver.get('https://pypi.org/')

# direction
time.sleep(1)
click_login = driver.find_element(By.XPATH, '/html/body/header/div/div/div[2]/div/nav[1]/ul/li[3]/a')
click_login.click()

# username and password
username = "your_username"
password = "your_password"

# input username and password
time.sleep(0.1)
input_username = driver.find_element(By.XPATH, '//*[@id="username"]')
input_username.send_keys(username)

time.sleep(0.1)
input_password = driver.find_element(By.XPATH, '//*[@id="password"]')
input_password.send_keys(password)

time.sleep(0.1)
click_submit = driver.find_element(By.XPATH, '/html/body/main/div/div/form/div[2]/div[3]/div/div/input')
click_submit.click()
