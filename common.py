import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from main_application import MainApplication
from colorama import Fore, Style

class TestFixtureBase:
    @pytest.fixture(scope="session")
    def driver(self):

        self.launching_driver()
        chrome_user_data_directory = "C:\\Users\\ppsde\\AppData\\Local\\Google\\Chrome\\User Data"
        chrome_profile_directory = "Profile 18"
        options = webdriver.ChromeOptions()
        options.add_argument(f"--user-data-dir={chrome_user_data_directory}")
        options.add_argument(f"--profile-directory={chrome_profile_directory}")
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        yield driver
        # driver.quit()
        

    @pytest.fixture(scope="session")
    def main_application(self, driver):
        app = MainApplication(driver)
        return app

    def launching_driver(self):
        print(f"{Fore.GREEN}Launching the WebDriver...{Style.RESET_ALL}")
        MainApplication.normal_wait(self=1)

    