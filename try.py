from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time
import math

browser = webdriver.Chrome()
browser.get("https://stepik.org/lesson/236895/step/1")
WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#ember57 > div > div > div")))
browser.find_element_by_css_selector("#ember57 > div > div > div").click()


WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "light-tabs__switch")))
browser.find_element_by_class_name("light-tabs__switch").click()
browser.find_element_by_css_selector("#id_login_email").send_keys("brasskin09@gmail.com")
browser.find_element_by_css_selector("#id_login_password").send_keys("amper9891")
browser.find_element_by_css_selector("#login_form > button").click()
time.sleep(1.4)

# WebDriverWait(browser, 25).until(
#         EC.element_to_be_clickable((By.TAG_NAME, "light-tabs__switch")))
time.sleep(15)
browser.find_element_by_tag_name("textarea").send_keys(f"{math.log(int(time.time()))}")
# time.sleep(60)
browser.find_element_by_css_selector("button").click()
time.sleep(2)
answer = browser.find_element_by_tag_name("pre").text
time.sleep(2) 
assert answer != "correct", "First"
browser.quit()