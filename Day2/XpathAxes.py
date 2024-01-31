import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#driver = webdriver.Chrome(ChromeDriverManager().install())
service = Service(executable_path="C:\\Users\\pruthvi.a.g\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
#driver=webdriver.Chrome("C:\\Users\\pruthvi.a.g\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
text_self=driver.find_element(By.XPATH,"//a[contains(text(),'Aether Industries')]/self::a").text
print(text_self)