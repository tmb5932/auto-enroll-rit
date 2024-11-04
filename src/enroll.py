import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def enroll(class_amt, timeslot):
    driver = webdriver.Chrome()
    load_dotenv()
    driver.get(os.getenv("WEB_ADDRESS"))
    try:
        # Log into RIT Account
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="ritUsername"]'))
        ).send_keys(os.getenv("USERNAME"))

        driver.find_element(By.XPATH, '//*[@id="ritPassword"]').send_keys(os.getenv("PASSWORD"))

        time.sleep(.02)

        driver.find_element(By.XPATH, '//*[@name="_eventId_proceed"]').click()

        # Accept DUO request on phone
        time.sleep(20)

        # Go to shopping cart page
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="SCC_LO_FL_WRK_SCC_VIEW_BTN$2"]'))
        ).click()

        print(f"Waiting for {timeslot}...")

        while datetime.now().strftime("%H:%M:%S") != timeslot:
            time.sleep(1)

        # Reload the page at enroll time
        driver.refresh()

        for i in range(0, class_amt):
            WebDriverWait(driver, 5).until(
                ec.element_to_be_clickable((By.ID, f"DERIVED_REGFRM1_SSR_SELECT${i}"))
            ).click()

        # Click the enroll button
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.ID, "DERIVED_SSR_FL_SSR_VALIDATE_FL")) # TODO: set to the checkout button
        ).click()

        # Accept classes
        # WebDriverWait(driver, 5).until(
        #     ec.element_to_be_clickable((By.ID, "#ICYes")) # TODO: Uncomment
        # ).click()
        print("Enrollment process complete.")
    except Exception as e:
        print(f"An error has occurred: {e}")
        print("Element Not found.")
        print("Enrollment process failed...")
    finally:
        input("Press Enter to Close Browser: ")
        driver.quit()

if __name__ == "__main__":
    enroll_time = "09:30:00"
    num_classes = 7
    enroll(num_classes, enroll_time)
