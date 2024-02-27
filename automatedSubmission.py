import subprocess, json

class AutomatedSubmissionPage:

    def __init__(self, config_file='config.json'):
        with open(config_file, 'r') as f:
            self.config = json.load(f)

    def run_yts_command(self):
        cert_scope = self.config['CertConfig']['cert_scope']
        user_agent_main = self.config['CertConfig']['user_agent']['main']
        user_agent_brand = self.config['CertConfig']['user_agent']['brand']
        user_agent_model = self.config['CertConfig']['user_agent']['model']
        api_type = self.config['CertConfig']['api_type']
        submit_option = self.config['CertConfig']['submit_option']
        skip_options = " ".join(self.config['CertConfig']['skip_options'])
        device_id = self.config['CertConfig']['device_id']

        user_agent = f"{user_agent_main} ({user_agent_brand},{user_agent_model})"
        
        command = f"yts cert {device_id} --cert-scope=\"{cert_scope}\" --user-agent=\"{user_agent}\" --{api_type} {submit_option} {skip_options} --rerun"
        
        try:
            subprocess.run(command, shell=True, check=True)
            print("Command executed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
