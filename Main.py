import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

#PATH = r"C:\Program Files\ChromeDriver\chromedriver"
driver = webdriver.Chrome()
driver.get("https://www.twilightwars.com/login")
email = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME, "password")
my_username = input("Username")
my_password = input("Password")


email.send_keys(my_username)
password.send_keys(my_password)

driver.find_element(By.TAG_NAME, "button").click()
driver.implicitly_wait(1)
driver.get("https://www.twilightwars.com/games/66208b559a33e30015a5f1c2")
message = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "desktop-turn-display"))).get_attribute("value")
game = driver.title.rstrip(" | Twilight Wars")
element = driver.find_element(By.CLASS_NAME, "player-name")
player = element.get_attribute("innerText")
text = " is waiting for @"
outbound = game+text+player
print(outbound)
