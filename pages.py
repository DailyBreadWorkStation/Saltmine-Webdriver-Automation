from selenium.webdriver.common.keys import Keys

class DeviceListPage:
    def __init__(self, driver,main_application):
        self.driver = driver
        self.main_application = main_application
        self.main_application.normal_wait()

    def click_add_series_fab(self):
        try:
            add_series_fab_script = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("device-series-table").shadowRoot.querySelector("div > div.card-header > div:nth-child(2) > mwc-button").click();
            '''
            self.driver.execute_script(add_series_fab_script)
        except Exception:
            print("Error clicking add series")
        self.main_application.normal_wait()

    def switchWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
    def set_series_name(self):
        try:
            series_name_script = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("div:nth-child(1) > div > mwc-textfield:nth-child(1)").shadowRoot.querySelector("input").value = "LG";
            '''
            self.driver.execute_script(series_name_script)
        except Exception:
            print("Error sending value series name")
        self.main_application.normal_wait()

    def set_description(self):
        try:
            description_script = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("div:nth-child(1) > div > mwc-textfield:nth-child(2)").shadowRoot.querySelector("input").value = "saltmine-testing";
            '''
            self.driver.execute_script(description_script)
        except Exception:
            print("Error sending value on description")
        self.main_application.normal_wait()

    def set_year(self):
        try:
            year_script = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("div:nth-child(2) > div > chip-toggle-set").shadowRoot.querySelector("chip-toggle.option-toggle").shadowRoot.querySelector("paper-button").click();
            '''
            self.driver.execute_script(year_script)
        except Exception:
            print("Error clicking on year")
        self.main_application.normal_wait()

    def set_date(self):
        date_input = self.driver.execute_script('''
        return document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("div:nth-child(3) > div > mwc-textfield").shadowRoot.querySelector("input");
    ''')
        date_input.send_keys(Keys.BACKSPACE * 10)
        date_input.send_keys("01/26/2022")  
        date_input.send_keys(Keys.RETURN)
        self.main_application.normal_wait()

    def set_market_volume(self):
        try:
            marketVolume = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("div:nth-child(4) > div > mwc-textfield").shadowRoot.querySelector("input").value = 2000;
            '''
            self.driver.execute_script(marketVolume)
        except Exception:
            print("Error sending value market vloume")        
        self.main_application.normal_wait()

    def select_chipset_vendor(self):
        try:
            chipsetVendor = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(5) > div > mwc-select:nth-child(1) > mwc-list-item:nth-child(4)").click();
            '''
            self.driver.execute_script(chipsetVendor)
        except Exception:
            print("Error clicking chipset vendor")
        self.main_application.normal_wait()

    def select_chipset_model(self):
        try:
            chipsetModel = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(5) > div > mwc-select:nth-child(2) > mwc-list-item:nth-child(4)").click();
            '''
            self.driver.execute_script(chipsetModel)
        except Exception:
            print("Error clicking chipset model")
        self.main_application.normal_wait()

    def click_cancel_button(self):
        try:
            cancel_button_script = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("mwc-button.saltmine-button.button-cancel").click();
            '''
            self.driver.execute_script(cancel_button_script)
        except Exception:
            print("Error clicking cancel button")
        self.main_application.normal_wait()
