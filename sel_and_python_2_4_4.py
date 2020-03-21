from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

def main():
	try:
		browser = webdriver.Firefox()
		browser.get("http://suninjuly.github.io/explicit_wait2.html")
		
		button = WebDriverWait(browser, 12).until(
							 EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

		browser.find_element_by_css_selector("button").click()

		browser.implicitly_wait(2)
		x = browser.find_element_by_id("input_value").text 
		y = calc(x)

		browser.find_element_by_id("answer").send_keys(y)
		browser.find_element_by_id("solve").click()

		browser.implicitly_wait(10)
	finally:
		browser.quit()

if __name__ == "__main__":
	main()
	print("(.)(.)----------------Nice work!---------------(.)(.)")	