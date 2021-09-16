import requests
from bs4 import BeautifulSoup
import os
import shutil
import time

url="https://www.chrisbukard.com"

web_request = requests.get(url)
web_soup = BeautifulSoup(web_request)

print(web_soup.find_all("img"))

from selenium import webdriver
driver = webdriver.Firefox()

driver.get(url)


iterations = 0
while iterations < 10:
    html = driver.execute_script("return document.documentElement.outerHTML")
    sel_soup = BeautifulSoup(html, 'html.parser')
    print(len(sel_soup.find_all("img")))
    images = []
    for i in sel_soup.findAll("img"):
        print(i)
        print(dir(i))
        src = i["src"]
        images.append(src)
    print(images)
    
    current_path = os.getcwd()
    for img in images:
        try:
            file_name = os.path.basename(img)
            img_request = requests.get(img, stream=True)
            new_path = os.path.join(current_path, "images", "filename.jpg")
            with open(new_path, "wb") as out_f:
                shutil.copyfileobj(img_request.raw, out_f)
            del img_request
        except:
            pass

    iterations+= 1
    time.sleep(5)
