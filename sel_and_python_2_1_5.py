from selenium import webdriver
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

def main():
	try:
		browser = webdriver.Firefox()
		browser.get("http://suninjuly.github.io/get_attribute.html")

		x_element = browser.find_element_by_id("treasure").get_attribute("valuex") 
		y = calc(x_element)
		browser.find_element_by_id("answer").send_keys(y)

		browser.find_element_by_id("robotCheckbox").click()
		browser.find_element_by_id("robotsRule").click()
		browser.find_element_by_css_selector("button").click()

		time.sleep(15)
	finally:
		browser.quit()

if __name__ == "__main__":
	main()
	print("(.)(.)----------------Nice work!---------------(.)(.)")