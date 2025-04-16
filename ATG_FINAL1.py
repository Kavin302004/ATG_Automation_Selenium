#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import requests
import random

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("selenium_log.txt"), logging.StreamHandler()])

driver = webdriver.Chrome()

try:
    base_url = "https://atg.party"
    site_response = requests.get(base_url)
    logging.info(f"HTTP Status Code: {site_response.status_code}")

    start_time = time.time()
    driver.get(base_url)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    load_time = time.time() - start_time
    logging.info(f"Page Load Time: {load_time:.2f} seconds")

    login_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Log in')]"))
    )
    login_btn.click()
    logging.info("Clicked the Login button.")

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "email_landing"))).send_keys("autotest@yopmail.com")
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "password_landing"))).send_keys("Pass@123")
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "landing-signin-btn"))).click()
    logging.info("Logged in successfully.")

    time.sleep(5)
    driver.get("https://atg.party/edit-user-bio")

    cover_icon = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "upload_cover_img"))
    )
    cover_icon.click()

    cover_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "upload1"))
    )
    cover_input.send_keys(r"C:\Users\user\Pictures\Spring\Screenshot 2025-04-14 113501.png")
    logging.info("Cover photo selected.")

    save_cover_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "profile_submit1"))
    )
    save_cover_btn.click()
    logging.info("Cover photo saved successfully.")

    current_page = driver.current_url
    try:
        confirm_response = requests.get(current_page)
        logging.info(f"Post-save HTTP Status Code: {confirm_response.status_code}")
    except Exception as e:
        logging.error(f"Error fetching status after save: {e}")

    try:
        close_popup_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#profile-modal1 > div > div > div.modal-header > button"))
        )
        close_popup_btn.click()
        logging.info("Cover photo popup closed successfully.")
    except Exception as e:
        logging.warning(f"Could not close the popup: {e}")

    time.sleep(1)

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "new_user_name"))).clear()

    username = f"kavin_test_{random.randint(1000, 9999)}"

    username_input = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "new_user_name"))
    )
    username_input.clear()
    username_input.send_keys(username)

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "about_me"))).clear()

    about_me_input = driver.find_element(By.ID, "about_me")
    about_me_input.send_keys("Kavin updated bio using Python Selenium automation.")

    save_bio_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.acc-save.atg-primarybtn-tiny"))
    )
    driver.execute_script("arguments[0].click();", save_bio_btn)

    logging.info("Successfully clicked the Save button.")
    logging.info("Bio information updated successfully.")

finally:
    time.sleep(10)
    driver.quit()


# In[ ]:




