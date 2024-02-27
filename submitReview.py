class SubmitReviewPage:
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
        

    def click_submit_for_review(self):
        submitreview = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("series-details").shadowRoot.querySelector("mwc-button").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(submitreview)
        self.main_application.high_wait()
        self.main_application.normal_wait()

    def create_secret_key(self):
        secretkey = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("iron-pages > div.iron-selected > series-details").shadowRoot.querySelector("series-details-card").shadowRoot.querySelector("content-card > div.series-properties.series-keys > mwc-button").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(secretkey)
        self.main_application.high_wait()
        self.main_application.normal_wait()

    def quit_browser(self):
        self.main_application.normal_wait()
        self.driver.quit()