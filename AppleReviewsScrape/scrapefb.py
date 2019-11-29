from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

import pandas as pd

webdriver = "/usr/local/bin/chromedriver"

driver = Chrome(webdriver)

#simulating a log in, entering credentials (for mobile site)
driver.get('https://www.facebook.com')
print ("Opened facebook...")

#email
loginemail = driver.find_element_by_xpath("//input[@type='email']")
loginemail.send_keys("pspslovex3@yahoo.com")
print ("entered email")

#password
loginemail = driver.find_element_by_xpath("//input[@type='password']")
loginemail.send_keys("y0urc@1L1234")
print ("password entered")

# passemail = driver.find_element_by_id('m_login_password')
# passemail.send_keys("y0urc@1L1234")
# print ("Password entered...")

#login after waiting for 2s
sleep(2)
button = driver.find_element_by_xpath("//input[@aria-label = 'Log In']")
button.click()

#navigating to my homepage and writing a comment to my status box
# sleep(2)
# driver.get("https://www.facebook.com/nicole.ramirez1272")
# post_box=driver.find_element_by_xpath("//*[@data-text='true']")
# post_box.send_keys("hello world")

#navigating to search bar and searching spark sport
driver.get("https://www.facebook.com/search/top/?q=spark%20sport&epa=SEARCH_BOX")

post = driver.find_element_by_xpath("//a[@href='https://www.facebook.com/nzherald/*']")
post.click()

#clicking on a post
# driver.find_element_by_xpath("//a[@data-sigil='feed-ufi-trigger']")
#driver.find_element_by_xpath("//*[@class=_5eay]").sendKeys("spark sport")
# post_box.send_keys("Testing using Name not ID.Selenium is easy.")
# sleep(2)
# post_it=driver.find_element_by_xpath("//*[@id='u_0_1a']/div/div[6]/div/ul/li[2]/button")
# post_it.click()
# print "Posted..."