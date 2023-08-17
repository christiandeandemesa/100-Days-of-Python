import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

response = requests.get("https://homefinder.com/rentals/CA/San-Francisco")
my_soup=BeautifulSoup(response.text,"html.parser")
all_offered_houses=my_soup.findAll(name="a",class_="listing-tile d-flex flex-column")
house_prices=[i.find(name="div",class_="h4 text-primary mb-0").text[9:15] for i in all_offered_houses]
house_address=[i.select_one("div .strip div").text[9:-8] for i in all_offered_houses]
house_links=[f"https://homefinder.com{i['href']}" for i in all_offered_houses]

driver=webdriver.Chrome(service=Service())
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfIAjuTgwXkkPdzXUdLFUw1llYvryT2VLTvFWaA2slNS7FVGA/viewform?usp=sf_link")
time.sleep(15)

for i in range(len(all_offered_houses)):
    address_answer_input=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_answer_input=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_answer_input=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    address_answer_input.send_keys(house_address[i])
    price_answer_input.send_keys(house_prices[i])
    link_answer_input.send_keys(house_links[i])

    send_key=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    send_key.click()

    time.sleep(3)
    send_another_reply=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    send_another_reply.click()