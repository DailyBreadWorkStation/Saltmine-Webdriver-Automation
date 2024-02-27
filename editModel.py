import json

class EditModelPage:
    def __init__(self, driver,main_application,config_file='config.json'):
        self.driver = driver
        self.main_application = main_application
        with open(config_file, 'r') as f:
            self.config = json.load(f)

    def devices_tab(self):
        devices = '''
        document.querySelector("body > saltmine-app").shadowRoot.querySelector("#content > iron-pages > device-list").shadowRoot.querySelector("iron-pages > div.background.iron-selected > div > a:nth-child(2)").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(devices)

    def click_specific_series(self):
        series_tab = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("device-series-table").shadowRoot.querySelector("data-table").shadowRoot.querySelector("table > tbody > tr.row-hover > td.col-updateTime.gm3-body-small.text-color-secondary").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(series_tab)

    def click_edit_model(self):
        editmodel = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("iron-pages > series-page").shadowRoot.querySelector("series-details").shadowRoot.querySelector("models-table-card").shadowRoot.querySelector("content-card > div.table-overflow-container > data-table").shadowRoot.querySelector("table > tbody > tr > td > paper-menu-button > paper-listbox > paper-item:nth-child(1)").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(editmodel)

    def edit_display_type(self):
        OLED = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(1) > div.collapsable-section-content > div:nth-child(3) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(2)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(OLED)

    def click_update_model(self):
        updatemodel = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("iron-pages > series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > div.footer > mwc-button.gm3-label-large.saltmine-button.button-submit").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(updatemodel)

    def switchWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def quit_browser(self):
        self.main_application.normal_wait()
        self.driver.quit()