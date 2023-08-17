import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

ACCOUNT_EMAIL = os.environ("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.environ("ACCOUNT_PASSWORD")
PHONE = os.environ("PHONE")

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3673151317&f_AL=true&keywords=python%20developer&refresh=true")

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

# Waits 2 seconds for the next page to load.
time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()

    time.sleep(2)

    # Tries to locate the apply button, but skips if it can't find it.
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)
        
        # If phone field is empty, then fills your phone number.
        phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")

        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        # If the submit_button is a "Next" button then this is a multi-step application, so skip it.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()
    
        # Once application is completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    # If I already applied to the job or job is no longer accepting applications, then skip it.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()