import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Creates a webdriver for chrome.
driver = webdriver.Chrome()
# Gives the webdriver access to this website.
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Finds one element with the id of cookie.
cookie = driver.find_element(By.ID, "cookie")

# Finds multiple elements with the css selector of #store div
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
twenty_sec = time.time() + 20

while True:
    cookie.click()

    # Every 5 seconds...
    if time.time() > timeout:

        # Get all the upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        # Converts <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Creates dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Gets current cookie count
        money_element = driver.find_element(By.ID, "money").text

        if "," in money_element:
            money_element = money_element.replace(",", "")

        cookie_count = int(money_element)

        # Finds upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchases the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        driver.find_element(By.ID, to_purchase_id).click()
        
        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > twenty_sec:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break
