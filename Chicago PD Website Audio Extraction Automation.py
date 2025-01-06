from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Configuration
BASE_URL = "https://openmhz.com/system/chi_cpd"
download_dir = r"C:\Users\admin\Desktop\Audio Files PD"  # Replace with your desired folder

# Set up Chrome options for downloads
options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,  # Set download directory
    "download.prompt_for_download": False,      # Disable download prompt
    "download.directory_upgrade": True,         # Automatically overwrite files
    "safebrowsing.enabled": True                # Disable safe browsing checks
})

# Initialize WebDriver
service = Service(executable_path="chromedriver.exe")  # Update with the correct path to chromedriver.exe
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open the target page
    driver.get(BASE_URL)

    # Wait for the "Listen" button and click it
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Listen')]"))
    )
    listen_button = driver.find_element(By.XPATH, "//*[contains(text(),'Listen')]")
    listen_button.click()

    print("Listening for audio to play...")

    # Add an initial delay to ensure the first audio starts
    time.sleep(5)

    # Variable to track if the current audio has been downloaded
    audio_downloaded = False

    while True:
        try:
            # Wait for the timer element to load
            timer_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ui.black.label"))
            )

            # Get the current timer value
            timer_text = timer_element.text.strip()
            print(f"Current timer: {timer_text}")

            # Check if the timer has reached 0 and the audio has not been downloaded
            if timer_text == "0Sec" and not audio_downloaded:
                print("Timer reached 0Sec. Clicking 'Download' button...")
                # Wait for the Download button and click it
                download_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Download')]"))
                )
                download_button.click()
                print("Download initiated.")
                audio_downloaded = True  # Mark the audio as downloaded

                

            # Reset the download status when a new audio starts playing
            if timer_text != "0Sec":
                audio_downloaded = False

        except Exception as e:
            print(f"Error occurred: {e}. Waiting for the next audio...")

except KeyboardInterrupt:
    print("Bot stopped by user.")
finally:
    driver.quit()
