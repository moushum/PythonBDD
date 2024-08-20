from selenium import webdriver
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


#@given(u'I navigate to home page')
def test_google():
    driver = webdriver.Chrome(options=Options())
    driver.implicitly_wait(10)
    driver.get('https://google.com')
    assert driver.title == 'Google'
    driver.quit()
