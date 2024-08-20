from behave import *
from selenium import webdriver
from selenium import webdriver
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome("/Users/moushum/PycharmProjects/pythonProject/driver/chromedriver")
# driver = webdriver.Chrome()

@given('launch browser')
def launchBrowser(context):
    driver.maximize_window()
    driver.implicitly_wait(10)


@when('I navigate to home page')
def iNavigateToHomePage(context):
    driver.get("https://google.com")


@then('make sure the logo is present')
def makeSureTheLogoIsPresent(context):
    assert driver.title == 'Google'


@then('I search for "{text}"')
def step_impl(context, text):
    search_bar = driver.find_element(By.ID, 'input')
    search_bar.send_keys(text)


@when('close browser')
def closeBrowser(context):
    driver.quit()
