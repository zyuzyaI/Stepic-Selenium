from selenium import webdriver
import math
import time

def main():
	try:
		driver = webdriver.Firefox()
		driver.get("http://suninjuly.github.io/find_link_text")
		link = driver.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
		link.click()
		get_reg(driver)
		time.sleep(15)
	finally:
		driver.quit()

def get_reg(browser):

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


if __name__ == "__main__":
	main()