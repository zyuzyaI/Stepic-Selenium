from selenium import webdriver
import math
import time
import os 

def main():
	try:
		browser = webdriver.Firefox()
		browser.get("http://suninjuly.github.io/file_input.html")

		browser.find_element_by_css_selector("input").send_keys("d")
		browser.find_element_by_name("lastname").send_keys("d")
		browser.find_element_by_name("email").send_keys("d")

		current_dir = os.path.abspath(os.path.dirname(__file__))
		file_path = os.path.join(current_dir, 'f.txt')

		browser.find_element_by_id("file").send_keys(file_path)

		browser.find_element_by_css_selector("button").click()

		time.sleep(15)
	finally:
		browser.quit()

if __name__ == "__main__":
	main()
	print("(.)(.)----------------Nice work!---------------(.)(.)")