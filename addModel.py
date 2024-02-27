from selenium.webdriver.common.keys import Keys
import json

class AddModelPage:
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
        
    def click_single_upload(self):
        single_upload = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("series-details").shadowRoot.querySelector("models-table-card").shadowRoot.querySelector("content-card > div > mwc-button.saltmine-button-secondary").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(single_upload)

    def set_brand_name(self):
        brand_name = self.driver.execute_script('''
        return document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(1) > div.collapsable-section-content > div:nth-child(1) > div > mwc-textfield:nth-child(1)").shadowRoot.querySelector("input");
        ''')
        brand_name.send_keys(Keys.BACKSPACE * 100)
        self.main_application.normal_wait()
        brand_name.send_keys(self.config['CertConfig']['user_agent']['brand'])

    def set_model_name(self):
        model_name = self.driver.execute_script('''
        return document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(1) > div.collapsable-section-content > div:nth-child(1) > div > mwc-textfield:nth-child(2)").shadowRoot.querySelector("input");
        ''')
        model_name.send_keys(Keys.BACKSPACE * 100)
        self.main_application.normal_wait()
        model_name.send_keys(self.config['CertConfig']['user_agent']['model'])

    def switchWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def device_type(self):
        click_on_tv = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(1) > div.collapsable-section-content > div:nth-child(2) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(click_on_tv)

    def display_type(self):
        click_on_LCD = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(1) > div.collapsable-section-content > div:nth-child(3) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(click_on_LCD)

    def av_details(self):
        avdetails = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(2) > div.collapsable-section-title > h2").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(avdetails)

    def decoded_resolution(self):
        video_decode_resolution = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(2) > div.collapsable-section-content > div:nth-child(1) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(video_decode_resolution)

    def video_display(self):
        video_display_resolution = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(2) > div.collapsable-section-content > div:nth-child(2) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(video_display_resolution)

    def viewport_resolution(self):
        viewport = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(2) > div.collapsable-section-content > div:nth-child(3) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(viewport)
    
    def orientation_capability(self):
        orientation = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(2) > div.collapsable-section-content > div:nth-child(4) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(orientation)

    def frame_rate(self):
        framerate = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(2) > div.collapsable-section-content > div:nth-child(5) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(framerate)  

    def vp9_profile(self):
        vp9profile = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(2) > div.collapsable-section-content > div:nth-child(6) > div > chip-toggle-set:nth-child(1)").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''    
        self.main_application.normal_wait()
        self.driver.execute_script(vp9profile)  
    
    def av1_profile(self):
        av1profile = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(2) > div.collapsable-section-content > div:nth-child(6) > div > chip-toggle-set:nth-child(2)").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(av1profile) 

    def audio_decoder(self):
        audiodecoder = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(2) > div.collapsable-section-content > div:nth-child(7) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(audiodecoder)    
    def _features(self):
        features = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(3) > div.collapsable-section-title > h2").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(features)

    def input_method(self):
        inputmethod = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(3) > div.collapsable-section-content > div:nth-child(1) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''   
        self.main_application.normal_wait()
        self.driver.execute_script(inputmethod)

    def supprted_feautres(self):
        HDR = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(3) > div.collapsable-section-content > div:nth-child(2) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(HDR)

    def accessablitity_features(self):
        high_contarst = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(3) > div.collapsable-section-content > div:nth-child(3) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(high_contarst)

    def voice_assistant(self):
        alexa = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(3) > div.collapsable-section-content > div:nth-child(4) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(alexa)

    def evergreen_type(self):
        full = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(3) > div.collapsable-section-content > div:nth-child(6) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(2)").shadowRoot.querySelector("paper-button > span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(full)

    def _hardware(self):
        hardware = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(4) > div.collapsable-section-title > h2").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(hardware)

    def system_storage(self):
        systemstorage = self.driver.execute_script('''
        return document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(4) > div.collapsable-section-content > div:nth-child(1) > div > mwc-textfield").shadowRoot.querySelector("input");
        ''')
        self.main_application.normal_wait()
        systemstorage.send_keys(Keys.BACKSPACE * 100)
        self.main_application.normal_wait()
        systemstorage.send_keys("234")

    def system_memory(self):
        systemmemory = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(4) > div.collapsable-section-content > div:nth-child(2) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(systemmemory)

    def dial_version(self):
        dialversion = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(4) > div.collapsable-section-content > div:nth-child(3) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(dialversion)

    def open_GL_ES_version(self):
        openGL = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(4) > div.collapsable-section-content > div:nth-child(4) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(openGL)

    def widevine_resource(self):
        widevine = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(4) > div.collapsable-section-content > div:nth-child(5) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(widevine)

    def crypto_version(self):
        crypto = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(4) > div.collapsable-section-content > div:nth-child(6) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(crypto)

    def HDCP_version(self):
        HDCP = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(4) > div.collapsable-section-content > div:nth-child(7) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(HDCP)

    def HDMI_version(self):
        HDMI = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > iron-form > form > div:nth-child(4) > div.collapsable-section-content > div:nth-child(8) > div > chip-toggle-set").shadowRoot.querySelector("div > chip-toggle:nth-child(1)").shadowRoot.querySelector("span").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(HDMI)

    def create_model(self):
        createmodel = '''
        document.querySelector("saltmine-app").shadowRoot.querySelector("device-list").shadowRoot.querySelector("series-page").shadowRoot.querySelector("model-form-v2").shadowRoot.querySelector("mwc-dialog > div.footer > mwc-button.gm3-label-large.saltmine-button.button-submit").click();
        '''
        self.main_application.normal_wait()
        self.driver.execute_script(createmodel)

    def quit_browser(self):
        self.main_application.normal_wait()
        self.driver.quit()








        