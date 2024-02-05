import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from main_application import MainApplication

@pytest.fixture(scope="session")
def driver():
    chrome_user_data_directory = "C:\\Users\\ppsde\\AppData\\Local\\Google\\Chrome\\User Data"
    chrome_profile_directory = "Profile 5"
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={chrome_user_data_directory}")
    options.add_argument(f"--profile-directory={chrome_profile_directory}")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture
def main_application(driver):
    app = MainApplication(driver)
    return app

@pytest.fixture
def device_list_page(main_application):
    device_list_page = main_application.open_device_list_page('https://devicecertification.youtube/?nonprodApi=true#/devices/list')
    return device_list_page

def test_click_add_series_fab(device_list_page):
    device_list_page.click_add_series_fab()

def test_switch_window(device_list_page):
    device_list_page.switchWindow()

def test_set_series_name(device_list_page):
    device_list_page.set_series_name()

def test_set_description(device_list_page):
    device_list_page.set_description()

def test_set_year(device_list_page):
    device_list_page.set_year()

def test_set_date(device_list_page):
    device_list_page.set_date()

def test_set_market_volume(device_list_page):
    device_list_page.set_market_volume()

def test_select_chipset_vendor(device_list_page):
    device_list_page.select_chipset_vendor()

def test_select_chipset_model(device_list_page):
    device_list_page.select_chipset_model()

def test_click_cancel_button(device_list_page):
    device_list_page.click_cancel_button()
    
def close_the_app(device_list_page):
    device_list_page.quit_driver()
    


