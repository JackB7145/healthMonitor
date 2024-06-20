#Importing all of the dependencies
import pandas
from datetime import date
from selenium import webdriver
import subprocess
import time

def load_driver(url):
    #Launching the website of choice
    driver = webdriver.Chrome()
    driver.maximize_window()
    address = url
    driver.get(address)
    while True: time.sleep(1)

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
