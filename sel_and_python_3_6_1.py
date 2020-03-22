from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time
import math

urls = ["https://stepik.org/lesson/236895/step/1",
		"https://stepik.org/lesson/236896/step/1",
		"https://stepik.org/lesson/236897/step/1",
		"https://stepik.org/lesson/236898/step/1",
		"https://stepik.org/lesson/236899/step/1",
		"https://stepik.org/lesson/236903/step/1",
		"https://stepik.org/lesson/236904/step/1",
		"https://stepik.org/lesson/236905/step/1"
		]

@pytest.fixture
def browser():
	print("\nstart browser for test..")
	browser = webdriver.Chrome()
	time.sleep(2)
	return browser

class TestUrls():
	# вызываем фикстуру в тесте, передав ее как параметр
	def test_url0(self, browser):
		browser.get(urls[0])
		
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


	def test_url1(self, browser):
		browser.get(urls[1])
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

	def test_url2(self, browser):
		browser.get(urls[2])
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

	def test_url3(self, browser):
		browser.get(urls[3])
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
		assert answer != "correct", "second"
		
	def test_url4(self, browser):
		browser.get(urls[4])
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
		assert answer != "correct", "thirth"

	def test_url5(self, browser):
		browser.get(urls[5])
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
		assert answer != "correct", "Fouht"

	def test_url6(self, browser):
		browser.get(urls[6])
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
		assert answer != "correct", "Fifth"

	def test_url7(self, browser):
		browser.get(urls[7])
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
		assert answer != "correct", "sixth"