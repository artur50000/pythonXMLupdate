from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard
import re
import keyring


driver = webdriver.Chrome(path_to_your_webdriver)
driver.maximize_window()

p = re.compile(
    r'https:\W{2}' +
    main_web_url +
    r'\WT24-Updates\Wservlet\W.*xml')
p1 = re.compile(
    r'https\W+' +
    main_web_url +
    r'\WT24-Updates\Wservlet\WR18_[A-Za-z]+_[A-Za-z]+_[0-9]+.xml')

f = open(path_to_file + "your.html", "r")
f1 = open(path_to_file + "MypythonFileold.txt", "r")
f2 = open(path_to_file + "MypythonFilenew.txt", "w")

setold = set()
setnew = set()
setdiff = set()

for line in f:
    result = p.search(line)
    if result:
        f2.write(result.group() + "\n")

f2.close()

f2 = open(path_to_file + "MypythonFilenew.txt", "w")


for line in f1:
    setold.add(line)

for line in f2:
    setnew.add(line)


setdiff = setnew.difference(setold)

if setdiff:

    driver.get(url_to_login_form)
    element = driver.find_element_by_id('userNameInput')

    element.send_keys('user')
    element.send_keys(Keys.TAB)

    element = driver.find_element_by_id('passwordInput')
    element.send_keys(keyring.get_password("xmlupdate", "user"))
    element.send_keys(Keys.ENTER)

    time.sleep(2)

    for item in setdiff:
        driver.get(item)

        keyboard.press_and_release('ctrl+s')

        time.sleep(2)
        keyboard.press_and_release('enter')


f.close()
f1.close()
f2.close()
