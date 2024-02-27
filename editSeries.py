from selenium.webdriver.common.keys import Keys

class EditSeriesPage:
    def __init__(self, driver, main_application):
        self.driver = driver
        self.main_application = main_application
        self.main_application.normal_wait()

    def click_devices_tab(self):
        devices_tab =  '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("iron-pages > div.background.iron-selected > div > a:nth-child(2)").click();        
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(devices_tab)

    def click_specific_series(self):
        series_tab = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("device-series-table").shadowRoot.querySelector("data-table").shadowRoot.querySelector("table > tbody > tr.row-hover > td.col-updateTime.gm3-body-small.text-color-secondary").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(series_tab)

    def click_edit_series_button(self):
        edit_button = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("series-details").shadowRoot.querySelector("series-details-card").shadowRoot.querySelector("content-card > div:nth-child(2) > mwc-button.saltmine-button.button-edit").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(edit_button)
        self.main_application.normal_wait()
        
    def switchWindow(self):
        self.main_application.normal_wait()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def edit_series_name(self):
          series_input = self.driver.execute_script('''
            return document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(1) > div > mwc-textfield:nth-child(1)").shadowRoot.querySelector("input");
          ''')
          self.main_application.normal_wait()
          series_input.send_keys(Keys.BACKSPACE * 100)
          self.main_application.normal_wait()
          series_input.send_keys(self.config['CertConfig']['series_name'])
          series_input.send_keys(Keys.RETURN)
            

    def edit_description(self):
          description_input = self.driver.execute_script( '''
           return document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(1) > div > mwc-textfield:nth-child(2)").shadowRoot.querySelector("input");          ''')
          self.main_application.normal_wait()
          description_input.send_keys(Keys.BACKSPACE * 100)
          self.main_application.normal_wait()
          description_input.send_keys("Saltmine-testing-update")
          description_input.send_keys(Keys.RETURN)

    def update_button(self):
        update_input = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("series-form-v2").shadowRoot.querySelector("mwc-dialog > div.form-footer > mwc-button.saltmine-button.button-submit").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(update_input)

    def quit_browser(self):
        self.main_application.normal_wait()
        self.driver.quit()