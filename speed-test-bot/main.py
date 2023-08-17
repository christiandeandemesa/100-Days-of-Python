from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class InternetSpeedBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        sleep(3)
        go_button = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        go_button.click()

        sleep(60)
        test_up = self.driver.find_element(By.CLASS_NAME,"upload-speed").text
        test_down = self.driver.find_element(By.CLASS_NAME,"download-speed").text
        print(test_up, test_down)

bot = InternetSpeedBot()
bot.get_internet_speed()