from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\snash\\PycharmProjects\\webDriver\\chromedriver.exe")
# automatic site views
# driver.get("https://uap-bd.edu/")
# print(driver.current_url)
# print(driver.title)
# time.sleep(4)
#
# driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
# print(driver.current_url)
# print(driver.title)
# time.sleep(4)
#
# driver.back()
# print("Back in: ")
# print(driver.current_url)
# time.sleep(4)
#
# driver.forward()
# print("Forward to: ")
# print(driver.current_url)

# Automate google search
driver.get("https://google.com/")
print(driver.current_url)
print(driver.title)
time.sleep(4)
driver.find_element_by_name("q").send_keys("Hero Alom")
time.sleep(4)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

time.sleep(2)
driver.close()
print("Test script run successfully")
