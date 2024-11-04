import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

def enroll(class_amt, timeslot):
    driver = webdriver.Chrome()
    load_dotenv()
    driver.get(os.getenv("WEB_ADDRESS"))

    time.sleep(1)

    # Log into RIT Account
    username = driver.find_element(By.XPATH, '//*[@id="ritUsername"]')
    username.send_keys(os.getenv("USERNAME"))
    time.sleep(.025)

    password = driver.find_element(By.XPATH, '//*[@id="ritPassword"]')
    password.send_keys(os.getenv("PASSWORD"))
    time.sleep(.075)

    login = driver.find_element(By.XPATH, '//*[@name="_eventId_proceed"]')
    login.click()

    # Accept DUO request on phone & Wait for SIS to load
    time.sleep(20)

    # Go to shopping cart page
    shopping_cart_button = driver.find_element(By.XPATH, '//*[@id="SCC_LO_FL_WRK_SCC_VIEW_BTN$2"]')
    shopping_cart_button.click()
    # Wait for page to load
    time.sleep(2)

    print(f"Waiting for {timeslot}...")

    while datetime.now().strftime("%H:%M:%S") != timeslot:
        time.sleep(1)

    # Reload the page at enroll time
    driver.refresh()
    time.sleep(2)  # Allow the page to fully reload

    for i in range(0, class_amt):
        checkbox = driver.find_element(By.ID, f"DERIVED_REGFRM1_SSR_SELECT${i}")
        checkbox.click()
        time.sleep(0.075)  # Very small delay for stability

    # Click the enroll button
    enroll_button = driver.find_element(By.ID, "DERIVED_SSR_FL_SSR_VALIDATE_FL") # TODO: set to the checkout button
    enroll_button.click()
    time.sleep(1)

    # Accept classes
    # accept_button = driver.find_element(By.ID, "#ICYes") # TODO: Uncomment
    # accept_button.click()

    input("Close Browser? ")
    print("Completed.")
    driver.quit()
    return

if __name__ == "__main__":
    enroll_time = "09:30:00"
    num_classes = 7
    enroll(num_classes, enroll_time)
