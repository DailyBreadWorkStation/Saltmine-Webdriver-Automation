from pages import DeviceListPage
import time

class MainApplication:
    def __init__(self, driver):
        self.driver = driver

    def open_device_list_page(self, url):
        self.driver.get(url)
        return DeviceListPage(self.driver,self)
    
    def normal_wait(self):
        time.sleep(2)

    def high_wait(self):
        time.sleep(7)

