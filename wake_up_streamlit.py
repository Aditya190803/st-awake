from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import datetime
import traceback
from streamlit_app import STREAMLIT_APPS

# Initialize log file
log_file = open("wakeup_log.txt", "a")
log_file.write("Execution started at: {}\n".format(datetime.datetime.now()))

# Set up Selenium webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)



for url in STREAMLIT_APPS:
    try:
        log_file.write(f"Processing URL: {url}\n")
        # Open the URL
        driver.get(url)

        # Wait for the "Yes, get this app back up!" button to appear
        try:
            wakeup_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='wakeup-button-owner']"))
            )
            # Click the button
            wakeup_button.click()
            log_file.write(f"Successfully woke up app at: {url}\n")
        except TimeoutException:
            log_file.write(f"Wake-up button not found or not clickable at: {url}\n")

    except Exception as e:
        log_file.write(f"Error processing {url}: {e}\n")
        log_file.write(f"Traceback: {traceback.format_exc()}\n")

# Close the browser
driver.quit()

# Log completion
log_file.write("Execution completed at: {}\n".format(datetime.datetime.now()))
log_file.close()
