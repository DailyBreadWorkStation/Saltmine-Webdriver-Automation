from selenium.webdriver.common.keys import Keys
import json

class DeviceListPage:
    def __init__(self, driver,main_application,config_file='config.json'):
        self.driver = driver
        self.main_application = main_application
        with open(config_file, 'r') as f:
            self.config = json.load(f)
           
    def click_add_series_fab(self):
          add_series_fab_script = '''
          document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("device-series-table").shadowRoot.querySelector("div > div.card-header > div:nth-child(2) > mwc-button").click();
          '''
          self.main_application.normal_wait()
          self.driver.execute_script(add_series_fab_script)
            
    def click_devices_tab(self):
          devices_tab =  '''
          document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("iron-pages > div.background.iron-selected > div > a:nth-child(2)").click();        
          '''
          self.main_application.high_wait()
          self.driver.execute_script(devices_tab)

    def switchWindow(self):
          self.driver.switch_to.window(self.driver.window_handles[-1])
        
    def set_series_name(self):
          series_input = self.driver.execute_script('''
          return document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("div:nth-child(1) > div > mwc-textfield:nth-child(1)").shadowRoot.querySelector("input");
          ''')
          self.main_application.normal_wait()
          series_input.send_keys(Keys.BACKSPACE * 10)
          series_input.send_keys(self.config['CertConfig']['series_name'])
          series_input.send_keys(Keys.RETURN)
            

    def set_description(self):
          description_input = self.driver.execute_script( '''
          return document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("div:nth-child(1) > div > mwc-textfield:nth-child(2)").shadowRoot.querySelector("input");
          ''')
          self.main_application.normal_wait()
          description_input.send_keys(Keys.BACKSPACE * 10)
          description_input.send_keys("Saltmine-testing")
          description_input.send_keys(Keys.RETURN)

    def set_year(self):
          year_script = '''
          document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("div:nth-child(2) > div > chip-toggle-set").shadowRoot.querySelector("chip-toggle.option-toggle").shadowRoot.querySelector("paper-button").click();
          '''
          self.main_application.normal_wait()
          self.driver.execute_script(year_script)
        
    def set_date(self):
          date_input = self.driver.execute_script('''
          return document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("div:nth-child(3) > div > mwc-textfield").shadowRoot.querySelector("input");
          ''')
          date_input.send_keys(Keys.BACKSPACE * 10)
          date_input.send_keys("01/26/2022")  
          date_input.send_keys(Keys.RETURN)
        

    def set_market_volume(self):
            market_input = self.driver.execute_script('''
            return document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("div:nth-child(4) > div > mwc-textfield").shadowRoot.querySelector("input");
            ''')
            self.main_application.normal_wait()
            market_input.send_keys(Keys.BACKSPACE * 10)
            market_input.send_keys(2000)
            market_input.send_keys(Keys.RETURN)    
              
    def select_chipset_vendor(self):
            chipsetVendor = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(5) > div > mwc-select:nth-child(1) > mwc-list-item:nth-child(4)").click();
            '''
            self.main_application.normal_wait()
            self.driver.execute_script(chipsetVendor)

    def select_chipset_model(self):
            chipsetModel = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(5) > div > mwc-select:nth-child(2) > mwc-list-item:nth-child(4)").click();
            '''
            self.main_application.normal_wait()
            self.driver.execute_script(chipsetModel)
            
    def click_create_button(self):
            create_button_script = '''
            document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("mwc-button.saltmine-button.button-submit").click();
            '''
            self.main_application.normal_wait()
            self.driver.execute_script(create_button_script)
            self.main_application.high_wait()

    def quit_browser(self):
            self.main_application.normal_wait()
            self.driver.quit()

 
         

            
    
 
        
    

