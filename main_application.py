
from editSeries import EditSeriesPage
from createSeries import DeviceListPage
from addModel import AddModelPage
from removeModel import RemoveModelPage
from editModel import EditModelPage
from submitReview import SubmitReviewPage
from manualSubmission import ManualSubmissionPage
from reportIssue import ReportIssuePage
import time

class MainApplication:
    def __init__(self, driver):
        self.driver = driver

    def open_device_list_page(self, url):
        self.driver.get(url)
        return DeviceListPage (self.driver,self)
    
    def open_device_edit_page(self, url):
        self.driver.get(url)
        return EditSeriesPage (self.driver,self)
    
    def open_add_model_page(self, url):
        self.driver.get(url)
        return AddModelPage (self.driver,self)
    
    def open_remove_model_page(self, url):
        self.driver.get(url)
        return RemoveModelPage (self.driver,self)
    
    def open_edit_model_page(self, url):
        self.driver.get(url)
        return EditModelPage (self.driver,self)
    
    def open_submit_review_page(self, url):
        self.driver.get(url)
        return SubmitReviewPage (self.driver,self)
    
    def open_manual_submission_page(self, url):
        self.driver.get(url)
        return ManualSubmissionPage (self.driver,self)
    
    def open_report_issue_page(self, url):
        self.driver.get(url)
        return ReportIssuePage (self.driver,self)
        
    def normal_wait(self):
        time.sleep(2)

    def high_wait(self):
        time.sleep(10)

