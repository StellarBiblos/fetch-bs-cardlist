import sys
import os
from datetime import datetime
from selenium import webdriver
import requests

url = sys.argv[1]
dir = url[url.rfind("/") + 1:]
os.makedirs(dir, exist_ok=True)

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options = options)
driver.get(url)

for li in driver.find_elements_by_css_selector(".cardListCol li"):
    a = li.find_element_by_css_selector("a")
    img = a.find_element_by_css_selector("img")
    src = img.get_attribute("src")
    print(src)
    res = requests.get(src)
    filename = src[src.rfind("/") + 1:]
    savepath = '/'.join([os.getcwd(), dir, filename])
    with open(savepath, 'wb') as file:
        file.write(res.content)

driver.quit()
