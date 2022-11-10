import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path="chromedriver.exe")

# driver.get('https://erp.aktu.ac.in/webpages/oneview/oneview.aspx')
driver.get("https://erp.aktu.ac.in/webpages/oneview/oneview.aspx")

Roll_In =driver.find_element_by_name("txtRollNo")

print(captcha.is_displayed())
driver.close()




#/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]
