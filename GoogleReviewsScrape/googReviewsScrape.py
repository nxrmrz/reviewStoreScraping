from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup, Comment
import csv
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

    #clicking show more button when it appears
    if driver.find_elements_by_xpath("//div[@class='PFAhAf']/div[@role='button']"):
        driver.find_elements_by_xpath("//div[@class='PFAhAf']/div[@role='button']")[0].click()

#parsing the page after scrolling down to bottom
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

# opening a csv file for writing reviews into, instantiating writer object
googReviews = open('SparkSportReviews-Google.csv', 'w')
csvWriter = csv.writer(googReviews)

# writing the reviews header
reviews_head = ["username", "comment", "date", "rating"]
csvWriter.writerow(reviews_head)

#getting each review
reviews = soup.findAll("div",{'jscontroller' : 'H6eOGe'})

#for each review, get the username, comment, date and rating
for review in reviews:
    entry = []

    userName = review.find("span", {'class' : 'X43Kjb'}).text
    entry.append(userName)

    comment = review.find("span", {'jsname': 'bN97Pc'}).text
    entry.append(comment)

    date = review.find("span", {'class': 'p2TkOb'}).text
    entry.append(date)

    #change rating to a number instead of a phrase, grabbing the number from that phrase
    rating = review.find("div", {'role': 'img'})['aria-label']
    numRating = rating.split()[1]
    entry.append(numRating)

    csvWriter.writerow(entry)

googReviews.close()





