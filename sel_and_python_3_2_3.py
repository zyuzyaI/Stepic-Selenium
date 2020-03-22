import unittest
from selenium import webdriver
import time
# from sel_and_python_1_6 import main 

class MyTEst(unittest.TestCase):

	def test_right_url(self):
		driver = webdriver.Firefox()
		driver.get("http://suninjuly.github.io/registration1.html")
		
		driver.find_element_by_css_selector(".first_block .first").send_keys("first name")
		driver.find_element_by_css_selector(".first_block .second").send_keys("last name")
		driver.find_element_by_css_selector(".third").send_keys("email")
		driver.find_element_by_css_selector(".second_block .first").send_keys("XXXXXXXXXXX")
		driver.find_element_by_css_selector(".second_block .second").send_keys("addres")

		driver.find_element_by_css_selector("button").click()
		time.sleep(3)

		final_text = "Congratulations! You have successfully registered!"
		self.assertEqual(driver.find_element_by_css_selector("div").text, final_text, "Equal")
		# if driver.find_element_by_css_selector("div").text == final_text:

	def test_wron(self):
		driver = webdriver.Firefox()
		driver.get("http://suninjuly.github.io/registration2.html"	)
		
		driver.find_element_by_css_selector(".first_block .first").send_keys("first name")
		driver.find_element_by_css_selector(".first_block .second").send_keys("last name")
		driver.find_element_by_css_selector(".third").send_keys("email")
		driver.find_element_by_css_selector(".second_block .first").send_keys("XXXXXXXXXXX")
		driver.find_element_by_css_selector(".second_block .second").send_keys("addres")

		driver.find_element_by_css_selector("button").click()
		time.sleep(3)

		final_text = "Congratulations! You have successfully registered!"
		self.assertEqual(driver.find_element_by_css_selector("div").text, final_text, "Equal")

if __name__ == "__main__":
	unittest.main()