from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.example.com/")

time.sleep(15)

driver.quit()