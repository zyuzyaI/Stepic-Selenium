#Для запуска данного кода нужно Firefox (geckodriver.exe - для Windows)

from selenium import webdriver
import time

def main(url):
	try:
		driver = webdriver.Firefox()
		driver.get(url)
		
		driver.find_element_by_css_selector(".first_block .first").send_keys("first name")
		driver.find_element_by_css_selector(".first_block .second").send_keys("last name")
		driver.find_element_by_css_selector(".third").send_keys("email")
		driver.find_element_by_css_selector(".second_block .first").send_keys("XXXXXXXXXXX")
		driver.find_element_by_css_selector(".second_block .second").send_keys("addres")

		driver.find_element_by_css_selector("button").click()
		time.sleep(3)

		final_text = "Congratulations! You have successfully registered!"
		if driver.find_element_by_css_selector("div").text == final_text:
			print("--------Nice work!---------")
	finally:
		driver.quit()

if __name__ == "__main__":
	urls = ["http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html"]
	for url in urls:
		main(url)
	print("-------DONE--------")