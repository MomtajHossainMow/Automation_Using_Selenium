#Step-1: Import driver from selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
print("Test started...")
#Step-2: Open the Google Chrome browser
driver = webdriver.Chrome()
#Step-3: Maximize the browser and delete all the cookies
driver.maximize_window()
driver.delete_all_cookies()
#Step-4: Navigate to the home page Gmail application
driver.get("https://www.gmail.com")
#Step-5: Identify the username text box and pass the value
driver.find_element(By.NAME, "identifier").send_keys("momtajhossainmow@gmail.com")
time.sleep(2)
#Step-6: Click on the next button
driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()  
time.sleep(3)
#Step-7: Identify the password text box and pass the value
driver.find_element(By.CLASS_NAME, "Passwd").send_keys("########")  
time.sleep(3) 
#Step-8: Click on the next button
driver.find_element(By.ID, "password").click()  
time.sleep(3)  
#Step-9: Close the browser
driver.close() 
print("Gmail login has been successfully completed")