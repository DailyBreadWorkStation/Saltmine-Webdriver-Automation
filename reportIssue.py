from selenium.webdriver.common.keys import Keys

class ReportIssuePage:
    def __init__(self, driver, main_application):
        self.driver = driver
        self.main_application = main_application
        self.main_application.normal_wait()
    
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

    def click_testing_tab(self):
        testing_tab = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("a:nth-child(2)").click();
        ''' 
        self.main_application.normal_wait()
        self.driver.execute_script(testing_tab)

    def click_manual_tests(self):
        manualtest = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("#content > iron-pages > device-list").shadowRoot.querySelector("iron-pages > series-page").shadowRoot.querySelector("iron-pages > div.iron-selected > testing-tab").shadowRoot.querySelector("test-results-table").shadowRoot.querySelector("content-card > div.table-overflow-container > data-table").shadowRoot.querySelector("table > tbody > tr.row-hover > td.text-color-primary > div").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(manualtest)

    def switchWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def material_icon(self):
        icon = '''
        document.querySelector("body > saltmine-app").shadowRoot.querySelector("#content > iron-pages > device-list").shadowRoot.querySelector("iron-pages > series-page").shadowRoot.querySelector("iron-pages > div.iron-selected > testing-tab").shadowRoot.querySelector("test-results-table").shadowRoot.querySelector("content-card > div.table-overflow-container > data-table").shadowRoot.querySelector("table > tbody > tr.row-0175CD3F-F2E4-404E-8A44-687ACCF7DCA1.row-hover > td.row-0175CD3F-F2E4-404E-8A44-687ACCF7DCA1.col-actions > paper-menu-button > mwc-icon-button").shadowRoot.querySelector("button > i").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(icon)

    def click_report_issue(self):
        report = '''
        document.querySelector("body > saltmine-app").shadowRoot.querySelector("#content > iron-pages > device-list").shadowRoot.querySelector("iron-pages > series-page").shadowRoot.querySelector("iron-pages > div.iron-selected > testing-tab").shadowRoot.querySelector("test-results-table").shadowRoot.querySelector("content-card > div.table-overflow-container > data-table").shadowRoot.querySelector("table > tbody > tr.row-0175CD3F-F2E4-404E-8A44-687ACCF7DCA1.row-hover > td.row-0175CD3F-F2E4-404E-8A44-687ACCF7DCA1.col-actions > paper-menu-button > paper-listbox > paper-item:nth-child(2)").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(report)

    def Link_to_existing_issue(self):
        existing_issue = '''
        document.querySelector("body > saltmine-app").shadowRoot.querySelector("#content > iron-pages > device-list").shadowRoot.querySelector("iron-pages > series-page").shadowRoot.querySelector("iron-pages > div.iron-selected > testing-tab").shadowRoot.querySelector("report-issue-modal").shadowRoot.querySelector("mwc-dialog > iron-form > form > div > mwc-formfield:nth-child(1) > mwc-radio").shadowRoot.querySelector("div > input").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(existing_issue)

    def enter_issue_id(self):
        issue_id = self.driver.execute_script('''
        return document.querySelector("body > saltmine-app").shadowRoot.querySelector("#content > iron-pages > device-list").shadowRoot.querySelector("iron-pages > series-page").shadowRoot.querySelector("iron-pages > div.iron-selected > testing-tab").shadowRoot.querySelector("report-issue-modal").shadowRoot.querySelector("mwc-dialog > iron-form > form > div > mwc-textfield").shadowRoot.querySelector("label > input");
        ''')
        issue_id.send_keys(Keys.BACKSPACE * 100)
        self.main_application.normal_wait()
        issue_id.send_keys("326167444")

    def click_on_submit(self):
        submit = '''
        document.querySelector("body > saltmine-app").shadowRoot.querySelector("#content > iron-pages > device-list").shadowRoot.querySelector("iron-pages > series-page").shadowRoot.querySelector("iron-pages > div.iron-selected > testing-tab").shadowRoot.querySelector("report-issue-modal").shadowRoot.querySelector("mwc-dialog > div.form-footer > mwc-button.saltmine-button.button-submit").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(submit)
        self.main_application.high_wait()

    def click_unlink_issue(self):
        unlink_issue = '''
        document.querySelector("body > saltmine-app").shadowRoot.querySelector("#content > iron-pages > device-list").shadowRoot.querySelector("iron-pages > series-page").shadowRoot.querySelector("iron-pages > div.iron-selected > testing-tab").shadowRoot.querySelector("test-results-table").shadowRoot.querySelector("content-card > div.table-overflow-container > data-table").shadowRoot.querySelector("table > tbody > tr.row-0175CD3F-F2E4-404E-8A44-687ACCF7DCA1.row-hover > td.row-0175CD3F-F2E4-404E-8A44-687ACCF7DCA1.col-actions > paper-menu-button > paper-listbox > paper-item:nth-child(4)").click();
        '''
        self.main_application.high_wait()
        self.driver.execute_script(unlink_issue)
        self.main_application.high_wait()

    def click_file_new_issue(self):
        filenewissue = '''
        document.querySelector("body > saltmine-app").shadowRoot.querySelector("#content > iron-pages > device-list").shadowRoot.querySelector("iron-pages > series-page").shadowRoot.querySelector("iron-pages > div.iron-selected > testing-tab").shadowRoot.querySelector("report-issue-modal").shadowRoot.querySelector("mwc-dialog > iron-form > form > div > mwc-formfield:nth-child(2) > mwc-radio").shadowRoot.querySelector("div > input").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(filenewissue)

    def Detail_failed_issue(self):
        issue_id = '''
        document.querySelector("body > saltmine-app").shadowRoot.querySelector("#content > iron-pages > device-list").shadowRoot.querySelector("iron-pages > series-page").shadowRoot.querySelector("iron-pages > div.iron-selected > testing-tab").shadowRoot.querySelector("report-issue-modal").shadowRoot.querySelector("mwc-dialog > iron-form > form > div > div:nth-child(3) > div > mwc-textfield").shadowRoot.querySelector("label > input").value = 'Saltmine Testing';
        '''

        self.main_application.normal_wait()
        self.driver.execute_script(issue_id)

    def quit_browser(self):
        self.main_application.normal_wait()
        self.driver.quit()
