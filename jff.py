
from openpyxl import Workbook,load_workboo
from CivilRollNo import *
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep


#-----------initializing IT2ndYearResult.xlsx  Excel File ------------
wb = load_workbook('Electric2ndYearResult.xlsx')
ws = wb.active


s = Service("chromedriver.exe")
driver = webdriver.Chrome(service = s)




# opening the website of AKTU ONE VIEW
driver.get("https://erp.aktu.ac.in/webpages/oneview/oneview.aspx")
sleep(1)
driver.maximize_window()


#Finding Roll no. input field
Roll_In =driver.find_element(By.NAME,"txtRollNo")


#Finding searchbtn
searchbtn= driver.find_element(By.NAME,"btnSearch")




rollno = "2007350209xxxx"
#----------------------------------------------------------------------------


def Login(rolno):
    
    #clicking on captcha button
    
    if Roll_In.is_displayed():
        
        #sending entry into the roll no. input field
        Roll_In.send_keys(rolno)
        
        pg.click(568,468) #to resolve the captcha
        sleep(2)
        captchatxtlocate = pg.locateOnScreen('captchapresent.tiff')
        print(captchatxtlocate)
        
        if captchatxtlocate != None:  
            sleep(18)
        
        else:
            print("captcha resolved smoothly")

        #clicking on search button
        if searchbtn.is_displayed():
            searchbtn.click()


        else:
            print("haven't found the searchbtn")        
      
            
    else:
        print("haven't found the input roll no")




   


#-----------------------------------------------------------------------------------------------------


#//*[@id="ctl04_ctl00_ctl00_grdViewSubjectMarksheet"]




Login(rollno)


tbody = driver.find_element(By.XPATH,"/html/body/form/div[3]/table/tbody/tr/td/div/table[2]/tbody/tr[2]/td/div[1]/div[2]/div/div/div/div[2]/table/thead/tr[6]/td/table/tbody/tr/td/div/table/tbody")

TheoryPhy = tbody.find_element(By.XPATH,"tr[2]")   #Theory Physics table row table row


PracticalPhys = tbody.find_element(By.XPATH,"tr[6]")
Pphysmarks = PracticalPhys.find_elements(By.TAG_NAME,"td")
Tphysmarks = TheoryPhy.find_elements(By.TAG_NAME,"td")    #yeh only td isliye hai kyonki ham lo theory physics ke row me jaake td data access kar rahe


Session = driver.find_element(By.ID,'ctl04_lblSession').text


stmarks= []

#-------------name of the candidate-----------
name = driver.find_element(By.ID,"lblFullName").text
print("Candidate name is :",name)




#---------------marks variable--------
TphysIntrnlmark = Tphysmarks[3].get_attribute("textContent")
TphysExternalmark = Tphysmarks[4].get_attribute("textContent")


PphysIntrnlmark = Pphysmarks[3].get_attribute("textContent")
PphysExternalmark = Pphysmarks[4].get_attribute("textContent")


print("theory physics internal mark is: ",TphysIntrnlmark)
print("theory physics external mark is: ",TphysExternalmark)


print("practical physics internal mark is: ",PphysIntrnlmark)
print("practical physics external mark is: ",PphysExternalmark)


#---------adding data in list----------------
stmarks.append(name)
stmarks.append(int(rollno))
stmarks.append(Session)
stmarks.append(int(TphysIntrnlmark))
stmarks.append(int(TphysExternalmark))
stmarks.append(int(PphysIntrnlmark))
stmarks.append(int(PphysExternalmark))


print("marks list of student :",stmarks)


def addMarksToExcel():
    ws.append(stmarks)                      #adding data to excel file
    wb.save('Electric2ndYearResult.xlsx')
    wb.close()


addMarksToExcel()


#----------------------------------------------------------------------------   
 
#Logout button
oneViewBtn = driver.find_element(By.ID,"hlpkSearchOV")


#----------------------------------------------------------------------------


def Logout():
    if oneViewBtn.is_displayed():
        oneViewBtn.click()
    else:
        print("one view logout button haven't found")


#----------------------------------------------------------------------------


logout()


sleep(5)


#closing the window
#driver.close()




#/html/body/form/div[3]/table/tbody/tr/td/div/table[2]/tbody/tr[2]/td/div[1]/div[2]/div/div/div/div[2]/table/thead/tr[6]/td/table/tbody/tr/td/div/table




#/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]

k
 