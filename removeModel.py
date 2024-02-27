from selenium.webdriver.common.keys import Keys

class RemoveModelPage:
    def __init__(self, driver, main_application):
        self.driver = driver
        self.main_application = main_application
        self.main_application.normal_wait()

    def click_specific_series(self):
        series_tab = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("device-series-table").shadowRoot.querySelector("data-table").shadowRoot.querySelector("table > tbody > tr.row-hover > td.col-updateTime.gm3-body-small.text-color-secondary").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(series_tab)

    def click_delete_model(self):
        delete = '''
        document.querySelector("body > saltmine-app").shadowRoot.querySelector("#content > iron-pages > device-list").shadowRoot.querySelector("iron-pages > series-page").shadowRoot.querySelector("iron-pages > div.iron-selected > series-details").shadowRoot.querySelector("models-table-card").shadowRoot.querySelector("content-card > div.table-overflow-container > data-table").shadowRoot.querySelector("table > tbody > tr > td > paper-menu-button > paper-listbox > paper-item:nth-child(2)").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(delete)

    def confirm_delete(self):
        confirm = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("series-details").shadowRoot.querySelector("confirmation-modal").shadowRoot.querySelector("paper-dialog > div > paper-button.gm3-label-large.button-primary").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(confirm)

    def switchWindow(self):
        self.main_application.normal_wait()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def quit_browser(self):
        self.main_application.normal_wait()
        self.driver.quit()