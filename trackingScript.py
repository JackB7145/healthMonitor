# Importing all of the dependencies
import pandas
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import time
from dotenv import dotenv_values

def load_driver(url):
    # Launching the website of choice
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    
    # Explicit wait to ensure elements are loaded
    wait = WebDriverWait(driver, 10)
    
    # Locate username and password fields and input the credentials
    config = dotenv_values(".env")
    username = wait.until(EC.presence_of_element_located((By.NAME, "userLoginId")))
    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    username.send_keys(config['USERNAME'])
    password.send_keys(config['PASSWORD'])
    
    # Locate and click the submit button
    submitButton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submitButton.click()
  
    # Infinite loop to keep the browser open
    while True: 
        pass

# Calling the batch file to close applications except for VS Code, Discord, and Command Prompt
subprocess.run(["closeAllApplications.bat"], shell=True)

#Prompting the user for all of the relevent information
date = date.today()
df = pandas.read_csv('Progress.csv', index_col=False)
w = eval(input("Enter your weight in pounds: "))
s = eval(input("Enter your hours of sleep: "))
q = int(input("Enter your quality of productiveness from 1-10: "))
e = input("Did you workout today (Yes/No)? ")

#Recording this information to a csv
newLine = pandas.DataFrame([{"Date":date, "Weight (lb)": w, "Sleep (Hours)":s, "Work Completed (1-10)":q, "Worked Out":e}])
df = pandas.concat([df, newLine], ignore_index=True)
df.to_csv('./Progress.csv', index=False)

driver = load_driver('https://www.netflix.com/browse')
