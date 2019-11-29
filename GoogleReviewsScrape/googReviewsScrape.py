from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup, Comment
import pandas as pd 
import lxml

#setting up an automated google chrome browser. the webdriver points to where the chrome driver is downloaded
webdriver = "/Applications/Google/chromedriver"
driver = Chrome(webdriver)

#navigating to desired URL
driver.get("https://play.google.com/store/apps/details?id=nz.co.sparksport&hl=en&showAllReviews=true")

# scroll down infinitely until the show more button displays, click, then continue scrolling infinitely
SCROLL_PAUSE_TIME = 2
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#parsing the page after scrolling down to bottom
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

# button
# if driver.find_elements_by_xpath("//div[@class='PFAhAf']/div[@role='button']"):
#     print("Element Exists")

# # get reviews
count = 0
reviews = soup.findAll("div",{'jscontroller' : 'H6eOGe'})

for review in reviews:
    count = count + 1

print(count) #prints # of reviews

# #get username, rating, date, comment




