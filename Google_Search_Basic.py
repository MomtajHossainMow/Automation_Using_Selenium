import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Step 1: Set the path to your Chrome WebDriver (if not already in PATH)
driver = webdriver.Chrome()

# Step 2: Maximize the browser window (optional)
driver.maximize_window()

# Step 3: Navigate to the Google home page
driver.get("https://www.google.com/")

# Step 4: Identify the Google search text box
search_box = driver.find_element(By.NAME, "q")

# Step 5: Pass the search query and submit (using send_keys with ENTER key)
search_box.send_keys("momtaj hossain mow")
search_box.send_keys(Keys.ENTER)

# Step 6: Optional wait for page to load (adjust time as needed)
time.sleep(3)

# Step 7: Close the browser
driver.quit()