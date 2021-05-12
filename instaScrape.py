#Selenium imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#Other imports here
import os
import wget

driver = webdriver.ChromeDriver('C:\chromedriver_win32\chromedriver.exe')
drover.get('https://www.instagram.com')
