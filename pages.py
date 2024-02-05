from selenium.webdriver.common.keys import Keys

class DeviceListPage:
    def __init__(self, driver,main_application):
        self.driver = driver
        self.main_application = main_application
        self.main_application.high_wait()

    def click_add_series_fab(self):
            add_series_fab_script = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("device-series-table").shadowRoot.querySelector("div > div.card-header > div:nth-child(2) > mwc-button").click();
            '''
            self.main_application.high_wait()
            self.driver.execute_script(add_series_fab_script)
            return add_series_fab_script

    def switchWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
    def set_series_name(self):
            series_name_script = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("div:nth-child(1) > div > mwc-textfield:nth-child(1)").shadowRoot.querySelector("input").value = "LG";
            '''
            self.driver.execute_script(series_name_script)
            return series_name_script

    def set_description(self):
            description_script = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("div:nth-child(1) > div > mwc-textfield:nth-child(2)").shadowRoot.querySelector("input").value = "saltmine-testing";
            '''
            self.driver.execute_script(description_script)
            return description_script

    def set_year(self):
            year_script = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("div:nth-child(2) > div > chip-toggle-set").shadowRoot.querySelector("chip-toggle.option-toggle").shadowRoot.querySelector("paper-button").click();
            '''
            self.driver.execute_script(year_script)
            return year_script
        

    def set_date(self):
        date_input = self.driver.execute_script('''
        return document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("div:nth-child(3) > div > mwc-textfield").shadowRoot.querySelector("input");
    ''')
        date_input.send_keys(Keys.BACKSPACE * 10)
        date_input.send_keys("01/26/2022")  
        date_input.send_keys(Keys.RETURN)
        

    def set_market_volume(self):
            marketVolume = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("div:nth-child(4) > div > mwc-textfield").shadowRoot.querySelector("input").value = 2000;
            '''
            self.driver.execute_script(marketVolume)    
            return marketVolume   
        

    def select_chipset_vendor(self):
            chipsetVendor = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(5) > div > mwc-select:nth-child(1) > mwc-list-item:nth-child(4)").click();
            '''
            self.driver.execute_script(chipsetVendor)
            return chipsetVendor

    def select_chipset_model(self):
            chipsetModel = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(5) > div > mwc-select:nth-child(2) > mwc-list-item:nth-child(4)").click();
            '''
            self.driver.execute_script(chipsetModel)
            return chipsetModel
        

    def click_cancel_button(self):
            cancel_button_script = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("mwc-button.saltmine-button.button-cancel").click();
            '''
            self.driver.execute_script(cancel_button_script)
            return cancel_button_script

            
    
 
        
    

