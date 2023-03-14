from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()

usernameInput = os.environ.get('GIFUSERNAME')
passwordInput = os.environ['GIFPASSWORD']

def waitForEle(xpath):
    return wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

def waitAndClick(xpath):
    ele = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    ele.click()


def find(xpath):
    return driver.find_element(By.XPATH, xpath)

def login():
    find('//*[@id="root"]/div/div/header/div/div[3]/a[1]/div').click()
    username = waitForEle('//*[@id="root"]/div/div/div/main/section/form/div[1]/div[2]/input')
    password = waitForEle('//*[@id="root"]/div/div/div/main/section/form/div[2]/div[2]/input')
    username.send_keys(usernameInput)
    password.send_keys(passwordInput)
    find('//*[@id="root"]/div/div/div/main/section/form/button').click()

def navToGifs():

    waitAndClick('//*[@id="root"]/div/div/header/div/div[3]/div')
    waitAndClick('//*[@id="root"]/div/div/nav/section/a[1]')
    waitAndClick('//*[@id="root"]/div/div/div/main/div/div[3]/div[1]/div/div/a[3]/div')

def setSettings():
    waitAndClick('//*[@id="root"]/div/div/div/main/div/div[3]/div[1]/div/div/a[3]/div')
    waitAndClick('//*[@id="root"]/div/div/div/main/div/div[3]/div[2]/div[1]/div/div[2]')
    waitAndClick('//*[@id="root"]/div/div/div/main/div/div[3]/div[2]/div[1]/div/div[3]/div[3]')


def saveInformation():
    pass
    for i in range(1, 100):
        mainCard = '//*[@id="root"]/div/div/div/main/div/div[3]/div[3]/div/div['+str(i)+']'
        title = mainCard+'/div[3]/div/div/div/input'
        link = mainCard+'/div[3]/div[3]/div/div/input'
        date = mainCard+'/div[4]/div[1]'
        time = mainCard+'/div[4]/div[2]'




s = Service('C:\Code\Python\chromedriver\chromedriver.exe')
driver = webdriver.Chrome(service=s)
wait = WebDriverWait(driver, 10)

driver.get('https://gfycat.com/')

login()
navToGifs()
setSettings()
saveInformation()


driver.close()
s.stop();