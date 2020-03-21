from selenium import webdriver
import math
import time
import os 

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

def main():
	try:
		browser = webdriver.Firefox()
		browser.get("http://suninjuly.github.io/alert_accept.html")

		browser.find_element_by_css_selector("button").click()
		time.sleep(3)
		alert = browser.switch_to.alert
		alert = browser.switch_to.alert
		alert.accept()
		time.sleep(0.9)

		x = browser.find_element_by_id("input_value").text 
		y = calc(x)

		browser.find_element_by_id("answer").send_keys(y)
		browser.find_element_by_css_selector("button").click()

		time.sleep(15)
	finally:
		browser.quit()

if __name__ == "__main__":
	main()
	print("(.)(.)----------------Nice work!---------------(.)(.)")