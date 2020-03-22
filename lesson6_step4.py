from selenium import webdriver
import time

# link = 'http://suninjuly.github.io/registration1.html'
link = "http://suninjuly.github.io/registration2.html" # NoSuchElementException


driver = webdriver.Firefox()
try:
    browser = webdriver.Firefox()
    browser.get(link)

    for i in ('first', 'second', 'third'):
        element = browser.find_element_by_css_selector('div.first_block input[required].form-control.' + i)
        element.send_keys(i)

    button = browser.find_element_by_css_selector("button[type=submit]")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert 'Congratulations! You have successfully registered!' == welcome_text
except Exception as error:
    print(error)
finally:
    driver.close()
    time.sleep(3)
    browser.quit()

