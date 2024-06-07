from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# List of Streamlit app URLs
STREAMLIT_APPS = [
    "https://aditya190803-streamlit-example-streamlit-app-t7tdrs.streamlit.app/",
    "https://generate-a-blog.streamlit.app/",
]

# Set up Selenium webdriver (assuming Chrome)
driver = webdriver.Chrome()

# Iterate through each URL in the list
for url in STREAMLIT_APPS:
    # Navigate to the webpage
    driver.get(url)

    # Wait for the button to appear
    wakeup_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='wakeup-button-owner']"))
    )

    # Click the button to wake up the Streamlit app
    wakeup_button.click()

# Close the browser
driver.quit()
