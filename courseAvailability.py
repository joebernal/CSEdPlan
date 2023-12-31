from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from bs4 import BeautifulSoup
import time

website = "https://sra.citruscollege.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=search"
driver = webdriver.Chrome()
driver.get(website)