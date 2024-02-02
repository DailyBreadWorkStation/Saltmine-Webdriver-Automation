from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from main_application import MainApplication
from selenium import webdriver
import time

chrome_user_data_directory = "C:\\Users\\ppsde\\AppData\\Local\\Google\\Chrome\\User Data"
chrome_profile_directory = "Profile 5"
options = webdriver.ChromeOptions()
options.add_argument(f"--user-data-dir={chrome_user_data_directory}")
options.add_argument(f"--profile-directory={chrome_profile_directory}")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

app = MainApplication(driver)
device_list_page = app.open_device_list_page('https://devicecertification.youtube/?nonprodApi=true#/devices/list')
device_list_page.click_add_series_fab()
device_list_page.switchWindow()
device_list_page.set_series_name()
device_list_page.set_description()
device_list_page.set_year()
device_list_page.set_date()
device_list_page.set_market_volume()
device_list_page.select_chipset_vendor()
device_list_page.select_chipset_model()
device_list_page.click_cancel_button()
driver.quit()
