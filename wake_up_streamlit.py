from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from streamlit_apps import STREAMLIT_APPS
import datetime

# Set up Selenium webdriver (assuming Chrome)
driver = webdriver.Chrome()

# Initialize log file
log_file = open("wakeup_log.txt", "a")

# Log the current date and time
log_file.write("Execution started at: {}\n".format(datetime.datetime.now()))

# Iterate through each URL in the list
for url in STREAMLIT_APPS:
    try:
        # Navigate to the webpage
        driver.get(url)

        # Wait for the button to appear
        wakeup_button = driver.find_element_by_css_selector("button[data-testid='wakeup-button-owner']")

        # Click the button to wake up the Streamlit app
        wakeup_button.click()
        
        # Log success
        log_file.write("Successfully woke up app at: {}\n".format(url))
    except NoSuchElementException:
        # Log button not found
        log_file.write("Button not found for app at: {}\n".format(url))

# Close the browser
driver.quit()

# Close the log file
log_file.close()
