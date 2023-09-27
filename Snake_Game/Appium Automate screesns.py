# test_app.py

import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Define Appium desired capabilities for your app and device
desired_caps = {
    "platformName": "Android",  # or "iOS"
    "platformVersion": "YOUR_PLATFORM_VERSION",
    "deviceName": "YOUR_DEVICE_NAME",
    "appPackage": "com.example.app",  # Replace with your app's package name
    "appActivity": "com.example.app.MainActivity",  # Replace with your app's main activity
    "noReset": True,
}

# Appium server URL
appium_url = "http://localhost:4723/wd/hub"

@pytest.fixture
def driver():
    driver = webdriver.Remote(appium_url, desired_caps)
    yield driver
    driver.quit()

def test_login_and_home(driver):
    # Perform login
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login_button")))

    username_field.send_keys("your_username")
    password_field.send_keys("your_password")
    login_button.click()

    # Verify successful login
    welcome_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "welcome_message")))
    assert "Welcome" in welcome_message.text

    # Interact with home screen
    home_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "home_button")))
    home_button.click()

    # Verify successful navigation to home screen
    home_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "home_title")))
    assert "Home" in home_title.text

# Add more tests for other screens in a similar fashion

