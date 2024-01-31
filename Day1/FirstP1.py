import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver=webdriver.Firefox()

driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("standard_user")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@name='login-button']").click()
act_title=driver.title
exp_title="Swag Labs"
if act_title==exp_title:
    print("login pass")
else:
    print("login failed")
driver.find_element(By.CSS_SELECTOR,"div.inventory_item_name").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR,"button[data-test=back-to-products]")
links=driver.find_elements(By.CLASS_NAME,"inventory_item")
print(len(links))
driver.close()
