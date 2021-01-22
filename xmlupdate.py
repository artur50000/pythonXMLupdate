from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard
import keyring


driver = webdriver.Chrome(path_to_webdriver)
driver.maximize_window()

driver.get(web_url_to_login_form)

element = driver.find_element_by_id('userNameInput')

element.send_keys('user')
element.send_keys(Keys.TAB)

element = driver.find_element_by_id('passwordInput')

element.send_keys(keyring.get_password("xmlupdate", "user"))
element.send_keys(Keys.ENTER)

time.sleep(2)
element = driver.find_element_by_id('systems')

element.click()
time.sleep(2)

elem = driver.find_elements_by_link_text('Select System')
time.sleep(2)
elem[0].click()

time.sleep(4)
keyboard.press_and_release('ctrl+s')

time.sleep(2)
keyboard.press_and_release('enter')
time.sleep(2)

driver.close()
