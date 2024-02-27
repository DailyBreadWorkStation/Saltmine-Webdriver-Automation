class ManualSubmissionPage:
    def __init__(self, driver, main_application):
        self.driver = driver
        self.main_application = main_application
        self.main_application.normal_wait()

    def click_devices_tab(self):
        devicestab = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("#content > iron-pages > device-list").shadowRoot.querySelector("iron-pages > div.background.iron-selected > div > a:nth-child(2)").click();
        '''
        self.main_application.high_wait()
        self.driver.execute_script(devicestab)

    def click_specific_series(self):
        series_tab = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("device-series-table").shadowRoot.querySelector("data-table").shadowRoot.querySelector("table > tbody > tr.row-hover > td.gm3-body-small.text-color-secondary").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(series_tab)

    def click_testing_tab(self):
        testing_tab = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("a:nth-child(2)").click();
        ''' 
        self.main_application.normal_wait()
        self.driver.execute_script(testing_tab)

    def click_filter_option(self):
        filter_option = '''
        document.querySelector("body > saltmine-app").shadowRoot.querySelector("#content > iron-pages > device-list").shadowRoot.querySelector("iron-pages > series-page").shadowRoot.querySelector("iron-pages > div.iron-selected > testing-tab").shadowRoot.querySelector("test-results-table").shadowRoot.querySelector("content-card > div:nth-child(1) > div > data-table-filter-v2").shadowRoot.querySelector("div > div:nth-child(2) > mwc-button").shadowRoot.querySelector("#button > span.mdc-button__label").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(filter_option)

    def click_manual_tests(self):
        manualtest = '''
        document.querySelector("body > saltmine-app").shadowRoot.querySelector("#content > iron-pages > device-list").shadowRoot.querySelector("iron-pages > series-page").shadowRoot.querySelector("iron-pages > div.iron-selected > testing-tab").shadowRoot.querySelector("test-results-table").shadowRoot.querySelector("content-card > div:nth-child(1) > div > data-table-filter-v2").shadowRoot.querySelector("div > div:nth-child(2) > mwc-menu > mwc-check-list-item:nth-child(2)").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(manualtest)

    def click_filtered_manual_tests(self):
        manualtest = '''
        document.querySelector("body > saltmine-app").shadowRoot.querySelector("#content > iron-pages > device-list").shadowRoot.querySelector("iron-pages > series-page").shadowRoot.querySelector("iron-pages > div.iron-selected > testing-tab").shadowRoot.querySelector("test-results-table").shadowRoot.querySelector("content-card > div.table-overflow-container > data-table").shadowRoot.querySelector("table > tbody > tr > td.gm3-label-large.text-color-primary > div").click()
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(manualtest)

    def live_channal_test(self):
        live_channal_test_case = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("testing-tab").shadowRoot.querySelector("test-results-table").shadowRoot.querySelector("data-table").shadowRoot.querySelector("table > tbody > tr.row-hover > td.col-testTitle.gm3-body-medium.sub-row-indent > div").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(live_channal_test_case)

    def switchWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def click_on_pass(self):
        _pass = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("testing-tab").shadowRoot.querySelector("test-result-modal.manual-modal").shadowRoot.querySelector("interactive-test-result").shadowRoot.querySelector("div.input-fields > div:nth-child(1) > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(_pass)

    def click_on_fail(self):
        fail = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("testing-tab").shadowRoot.querySelector("test-result-modal.manual-modal").shadowRoot.querySelector("interactive-test-result").shadowRoot.querySelector("div.input-fields > div:nth-child(1) > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(2)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(fail)

    def quit_browser(self):
        self.main_application.normal_wait()
        self.driver.quit()

    