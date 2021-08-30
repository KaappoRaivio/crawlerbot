import os
import time
import sys


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# driver =


url = sys.argv[1]

if os.name == "nt":
    geckopath = "./driver/geckodriver.exe"
else:
    geckopath = "./driver/geckodriver"



with webdriver.Firefox() as driver1:
    # driver1.get("https://www.nettiauto.com/audi/a4/bensiini?id_vehicle_type=1&id_gear_type=3&id_country[]=73")
    driver1.get(url)
    totalPages = int(driver1.find_element(By.CLASS_NAME, "totPage").text)
    print(totalPages)



    print("make;model;year;mileage;price;link")
    for page in range(totalPages):
        # print("page")
        with webdriver.Firefox() as driver:
            driver.get(f"{url}&page={page + 1}")
            listingData = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "listingData")))
            time.sleep(1)
            # listingData = driver.find_element(By.ID, "listingData")
            children = listingData.find_elements(By.CLASS_NAME, "childVifUrl")
            # children = listingData.find_elements_by_xpath(".//*")
            for child in children:
                # print(child.get_attribute("class"))
                print(child.get_attribute("data-make"),
                      child.get_attribute("data-model"),
                      child.get_attribute("data-year"),
                      child.get_attribute("data-mileage"),
                      child.get_attribute("data-price"),
                      child.get_attribute("href"),
                      sep=";")

    # print(children)
