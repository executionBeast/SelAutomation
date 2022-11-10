import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path="chromedriver.exe")

# driver.get('https://erp.aktu.ac.in/webpages/oneview/oneview.aspx')
driver.get("https://www.google.com")
print(driver.title) #Google
driver.get("https://www.youtube.com")
print(driver.title) #Youtube

driver.back()   #back to google website
print(driver.title) #Google
driver.forward() # forward to youtube
print(driver.title) #Youtube


driver.close()
