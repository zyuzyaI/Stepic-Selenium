from selenium.webdriver.support.ui import Select
from selenium import webdriver
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

def main():
	try:
		browser = webdriver.Firefox()
		browser.get("http://suninjuly.github.io/selects1.html")

		num1 = int(browser.find_element_by_id("num1").text)
		num2 = int(browser.find_element_by_id("num2").text)
		sum_n1_n2 = num1 + num2

		select = Select(browser.find_element_by_tag_name("select"))
		select.select_by_value(str(sum_n1_n2))

		browser.find_element_by_css_selector("button").click()

		time.sleep(15)
	finally:
		browser.quit()

if __name__ == "__main__":
	main()
	print("(.)(.)----------------Nice work!---------------(.)(.)")