from common import TestFixtureBase
import pytest, json
from automatedSubmission import AutomatedSubmissionPage

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        with open(config_file, 'r') as f:
            self.config = json.load(f)
'''
class TestCreateSeries(TestFixtureBase):
    @pytest.fixture(scope="session")
    def device_list_page(self, main_application, edit_page=False):
        name_of_instance = ConfigLoader()
        page_url = name_of_instance.config['CertConfig']['test_url']
        device_list_page = main_application.open_device_list_page(page_url)
        return device_list_page
    
    def test_devices_tab(self,device_list_page):
        device_list_page.click_devices_tab()
        
    def test_add_series_fab(self,device_list_page):
        device_list_page.click_add_series_fab()

    def test_switch_window(self,device_list_page):
        device_list_page.switchWindow()

    def test_set_series_name(self,device_list_page):
        device_list_page.set_series_name()

    def test_set_series_description(self,device_list_page):
        device_list_page.set_description()

    def test_set_series_year(self,device_list_page):
        device_list_page.set_year()

    def test_set_series_date(self,device_list_page):
        device_list_page.set_date()

    def test_set_series_market_volume(self,device_list_page):
        device_list_page.set_market_volume()

    def test_select_chipset_vendor(self,device_list_page):
        device_list_page.select_chipset_vendor()

    def test_select_chipset_model(self,device_list_page):
        device_list_page.select_chipset_model()

    def test_click_create_button(self,device_list_page):
        device_list_page.click_create_button()

    def test_close_browser(self,device_list_page):
        device_list_page.quit_browser()



class TestEditSeries(TestFixtureBase):

    @pytest.fixture(scope="session")
    def device_list_page(self, main_application, edit_page=False):
        name_of_instance = ConfigLoader()
        page_url = name_of_instance.config['CertConfig']['test_url']
        device_list_page = main_application.open_device_edit_page(page_url)
        return device_list_page
    
    def test_devices_tab(self, device_list_page):
        device_list_page.click_devices_tab()

    def test_click_specific_series(self, device_list_page):
        device_list_page.click_specific_series()

    def test_click_edit_button(self, device_list_page):
        device_list_page.click_edit_series_button()

    def test_switch(self, device_list_page):
        device_list_page.switchWindow()

    def test_edit_name(self, device_list_page):
        device_list_page.edit_series_name()

    def test_edit_description(self, device_list_page):
        device_list_page.edit_description()

    def test_update_button(self,device_list_page):
        device_list_page.update_button()

    def test_close_browser(self,device_list_page):
        device_list_page.quit_browser()

  

class TestAddModel(TestFixtureBase):

    @pytest.fixture(scope="session")
    def device_list_page(self, main_application, add_page=False):
        name_of_instance = ConfigLoader()
        page_url = name_of_instance.config['CertConfig']['test_url']
        device_list_page = main_application.open_add_model_page(page_url)
        return device_list_page
    
    def test_click_devices_tab(self, device_list_page):
        device_list_page.devices_tab()
    
    def test_click_specific_series(self, device_list_page):
        device_list_page.click_specific_series()

    def test_click_upload_bulk(self,device_list_page):
        device_list_page.click_single_upload()

    def test_switch(self, device_list_page):
        device_list_page.switchWindow()

    def test_set_brand_name(self,device_list_page):
        device_list_page.set_brand_name()

    def test_set_model_name(self,device_list_page):
        device_list_page.set_model_name()

    def test_click_device_type(self,device_list_page):
        device_list_page.device_type()

    def test_click_display_type(self,device_list_page):
        device_list_page.display_type()

    def test_click_av_details(self,device_list_page):
        device_list_page.av_details()

    def test_click_decoded_res(self,device_list_page):
        device_list_page.decoded_resolution()

    def test_click_display_res(self,device_list_page):
        device_list_page.video_display()

    def test_click_viewport(self,device_list_page):
        device_list_page.viewport_resolution()

    def test_click_orientation(self,device_list_page):
        device_list_page.orientation_capability()

    def test_click_frame_rate(self,device_list_page):
        device_list_page.frame_rate()

    def test_click_vp9_profile(self,device_list_page):
        device_list_page.vp9_profile()

    def test_click_av1_profile(self,device_list_page):
        device_list_page.av1_profile()

    def test_click_audio_decoder(self,device_list_page):
        device_list_page.audio_decoder()

    def test_click_features(self,device_list_page):
        device_list_page._features()

    def test_click_input_method(self,device_list_page):
        device_list_page.input_method()

    def test_click_supprted_feautres(self,device_list_page):
        device_list_page.supprted_feautres()

    def test_click_accessablitity_features(self,device_list_page):
        device_list_page.accessablitity_features()

    def test_click_voice_assistant(self,device_list_page):
        device_list_page.voice_assistant()

    def test_click_evergreen_type(self,device_list_page):
        device_list_page.evergreen_type()

    def test_click_hardware(self,device_list_page):
        device_list_page._hardware()

    def test_click_system_storage(self,device_list_page):
        device_list_page.system_storage()

    def test_click_system_memory(self,device_list_page):
        device_list_page.system_memory()

    def test_click_dial_version(self,device_list_page):
        device_list_page.dial_version()

    def test_click_open_GL_ES_version(self,device_list_page):
        device_list_page.open_GL_ES_version()

    def test_click_widevine_resource(self,device_list_page):
        device_list_page.widevine_resource()

    def test_click_crypto_version(self,device_list_page):
        device_list_page.crypto_version()

    def test_click_HDCP_version(self,device_list_page):
        device_list_page.HDCP_version()

    def test_click_HDMI_version(self,device_list_page):
        device_list_page.HDMI_version()

    def test_click_create_model(self,device_list_page):
        device_list_page.create_model()

    def test_close_browser(self,device_list_page):
        device_list_page.quit_browser()

class TestEditModel(TestFixtureBase):

    @pytest.fixture(scope="session")
    def device_list_page(self, main_application, edit_page=False):
        name_of_instance = ConfigLoader()
        page_url = name_of_instance.config['CertConfig']['test_url']
        device_list_page = main_application.open_edit_model_page(page_url)
        return device_list_page
    
    def test_click_devices_tab(self, device_list_page):
        device_list_page.devices_tab()
    
    def test_click_specific_series(self, device_list_page):
        device_list_page.click_specific_series()

    def test_click_edit(self,device_list_page):
        device_list_page.click_edit_model()

    def test_switch(self, device_list_page):
        device_list_page.switchWindow()

    def test_edit_display_type(self, device_list_page):
        device_list_page.edit_display_type()
    
    def test_click_update_model(self,device_list_page):
        device_list_page.click_update_model()

    def test_close_browser(self,device_list_page):
        device_list_page.quit_browser()


class TestRemoveModel(TestFixtureBase):

    @pytest.fixture(scope="session")
    def device_list_page(self, main_application, edit_page=False):
        name_of_instance = ConfigLoader()
        page_url = name_of_instance.config['CertConfig']['test_url']
        device_list_page = main_application.open_remove_model_page(page_url)
        return device_list_page
    
    def test_click_specific_series(self, device_list_page):
        device_list_page.click_specific_series()

    def test_click_delete(self,device_list_page):
        device_list_page.click_delete_model()

    def test_switch(self, device_list_page):
        device_list_page.switchWindow()
    
    def test_click_confirm_delete(self,device_list_page):
        device_list_page.confirm_delete()

    def test_close_browser(self,device_list_page):
        device_list_page.quit_browser()

class TestAddModelDuplicate(TestFixtureBase):

    @pytest.fixture(scope="session")
    def device_list_page(self, main_application, add_page=False):
        name_of_instance = ConfigLoader()
        page_url = name_of_instance.config['CertConfig']['test_url']
        device_list_page = main_application.open_add_model_page(page_url)
        return device_list_page
    
    def test_click_devices_tab(self, device_list_page):
        device_list_page.devices_tab()
    
    def test_click_specific_series(self, device_list_page):
        device_list_page.click_specific_series()

    def test_click_upload_bulk(self,device_list_page):
        device_list_page.click_single_upload()

    def test_switch(self, device_list_page):
        device_list_page.switchWindow()

    def test_set_brand_name(self,device_list_page):
        device_list_page.set_brand_name()

    def test_set_model_name(self,device_list_page):
        device_list_page.set_model_name()

    def test_click_device_type(self,device_list_page):
        device_list_page.device_type()

    def test_click_display_type(self,device_list_page):
        device_list_page.display_type()

    def test_click_av_details(self,device_list_page):
        device_list_page.av_details()

    def test_click_decoded_res(self,device_list_page):
        device_list_page.decoded_resolution()

    def test_click_display_res(self,device_list_page):
        device_list_page.video_display()

    def test_click_viewport(self,device_list_page):
        device_list_page.viewport_resolution()

    def test_click_orientation(self,device_list_page):
        device_list_page.orientation_capability()

    def test_click_frame_rate(self,device_list_page):
        device_list_page.frame_rate()

    def test_click_vp9_profile(self,device_list_page):
        device_list_page.vp9_profile()

    def test_click_av1_profile(self,device_list_page):
        device_list_page.av1_profile()

    def test_click_audio_decoder(self,device_list_page):
        device_list_page.audio_decoder()

    def test_click_features(self,device_list_page):
        device_list_page._features()

    def test_click_input_method(self,device_list_page):
        device_list_page.input_method()

    def test_click_supprted_feautres(self,device_list_page):
        device_list_page.supprted_feautres()

    def test_click_accessablitity_features(self,device_list_page):
        device_list_page.accessablitity_features()

    def test_click_voice_assistant(self,device_list_page):
        device_list_page.voice_assistant()

    def test_click_evergreen_type(self,device_list_page):
        device_list_page.evergreen_type()

    def test_click_hardware(self,device_list_page):
        device_list_page._hardware()

    def test_click_system_storage(self,device_list_page):
        device_list_page.system_storage()

    def test_click_system_memory(self,device_list_page):
        device_list_page.system_memory()

    def test_click_dial_version(self,device_list_page):
        device_list_page.dial_version()

    def test_click_open_GL_ES_version(self,device_list_page):
        device_list_page.open_GL_ES_version()

    def test_click_widevine_resource(self,device_list_page):
        device_list_page.widevine_resource()

    def test_click_crypto_version(self,device_list_page):
        device_list_page.crypto_version()

    def test_click_HDCP_version(self,device_list_page):
        device_list_page.HDCP_version()

    def test_click_HDMI_version(self,device_list_page):
        device_list_page.HDMI_version()

    def test_click_create_model(self,device_list_page):
        device_list_page.create_model()

    def test_close_browser(self,device_list_page):
        device_list_page.quit_browser()
'''
class TestSubmitForReview(TestFixtureBase):

    @pytest.fixture(scope="session")
    def device_list_page(self, main_application, edit_page=False):
        name_of_instance = ConfigLoader()
        page_url = name_of_instance.config['CertConfig']['test_url']
        device_list_page = main_application.open_submit_review_page(page_url)
        return device_list_page
    
    def test_click_specific_series(self, device_list_page):
        device_list_page.click_specific_series()

    def test_click_submit_for_review(self,device_list_page):
        device_list_page.click_submit_for_review()

    def test_create_secret_key(self,device_list_page):
        device_list_page.create_secret_key()

    def test_close_browser(self,device_list_page):
        device_list_page.quit_browser()


class TestAutomatedSubmission(TestFixtureBase):

    @pytest.fixture(scope="session")
    def run_automated(self):
        automated_submission = AutomatedSubmissionPage()
        automated_submission.run_yts_command()

    def test_run_yts(run_automated):
        automated_submission = AutomatedSubmissionPage()
        automated_submission.run_yts_command()
  

class TestManualSubmission(TestFixtureBase):

    @pytest.fixture(scope="session")
    def device_list_page(self, main_application, edit_page=False):
        name_of_instance = ConfigLoader()
        page_url = name_of_instance.config['CertConfig']['test_url']
        device_list_page = main_application.open_manual_submission_page(page_url)
        return device_list_page
    
    def test_click_devices_tab(self, device_list_page):
        device_list_page.click_devices_tab()

    def test_click_specific_series(self, device_list_page):
        device_list_page.click_specific_series()

    def test_click_testing_tab(self, device_list_page):
        device_list_page.click_testing_tab()

    def test_click_filter_option(self, device_list_page):
        device_list_page.click_filter_option()

    def test_switchWindow(self, device_list_page):
        device_list_page.switchWindow()

    def test_click_manual_tests(self, device_list_page):
        device_list_page.click_manual_tests()

    def test_click_filtered_manual_tests(self, device_list_page):
        device_list_page.click_filtered_manual_tests()

    def test_live_channal_test(self, device_list_page):
        device_list_page.live_channal_test()

    def test_switchWindow(self, device_list_page):
        device_list_page.switchWindow()

    def test_click_on_pass(self, device_list_page):
        device_list_page.click_on_pass()

    def test_click_on_fail(self, device_list_page):
        device_list_page.click_on_fail()

    def test_close_browser(self,device_list_page):
        device_list_page.quit_browser()

class TestReportIssue(TestFixtureBase):

    @pytest.fixture(scope="session")
    def device_list_page(self, main_application, edit_page=False):
        name_of_instance = ConfigLoader()
        page_url = name_of_instance.config['CertConfig']['test_url']
        device_list_page = main_application.open_report_issue_page(page_url)
        return device_list_page

    def test_click_specific_series(self, device_list_page):
        device_list_page.click_specific_series()

    def test_click_testing_tab(self, device_list_page):
        device_list_page.click_testing_tab()

    def test_click_manual_tests(self, device_list_page):
        device_list_page.click_manual_tests()

    def test_material_icon(self, device_list_page):
        device_list_page.material_icon()

    def test_switchWindow(self, device_list_page):
        device_list_page.switchWindow()

    def test_click_report_issue(self, device_list_page):
        device_list_page.click_report_issue()

    def test_switchWindow(self, device_list_page):
        device_list_page.switchWindow()

    def test_Link_to_existing_issue(self, device_list_page):
        device_list_page.Link_to_existing_issue()

    def test_enter_issue_id(self, device_list_page):
        device_list_page.enter_issue_id()

    def test_click_on_submit(self, device_list_page):
        device_list_page.click_on_submit()

    def test_material_icon(self, device_list_page):
        device_list_page.material_icon()

    def test_click_unlink_issue(self, device_list_page):
        device_list_page.click_unlink_issue()

    def test_close_browser(self,device_list_page):
        device_list_page.quit_browser()


class TestReportNewIssue(TestFixtureBase):

    @pytest.fixture(scope="session")
    def device_list_page(self, main_application, edit_page=False):
        name_of_instance = ConfigLoader()
        page_url = name_of_instance.config['CertConfig']['test_url']
        device_list_page = main_application.open_report_issue_page(page_url)
        return device_list_page

    def test_click_specific_series(self, device_list_page):
        device_list_page.click_specific_series()

    def test_click_testing_tab(self, device_list_page):
        device_list_page.click_testing_tab()

    def test_click_manual_tests(self, device_list_page):
        device_list_page.click_manual_tests()

    def test_material_icon(self, device_list_page):
        device_list_page.material_icon()

    def test_switchWindow(self, device_list_page):
         device_list_page.switchWindow()

    def test_click_report_issue(self, device_list_page):
        device_list_page.click_report_issue()

    def test_switchWindow(self, device_list_page):
         device_list_page.switchWindow()

    def test_click_file_new_issue(self, device_list_page):
        device_list_page.click_file_new_issue()

    def test_Detail_failed_issue(self, device_list_page):
        device_list_page.Detail_failed_issue()

    def test_click_on_submit(self, device_list_page):
        device_list_page.click_on_submit()

    def test_close_browser(self,device_list_page):
        device_list_page.quit_browser()

    

