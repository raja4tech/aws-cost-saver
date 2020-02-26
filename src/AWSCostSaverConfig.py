import json

class AWSCostSaverConfig:
    def __init__(self, filename):
        self.filename = filename
        self.config_json_content = ''

    def read_config(self):
        print('Reading config from file: %s' %self.filename)
        try:
            with open(self.filename) as config_file:
                json_content = json.load(config_file)
                self.config_json_content = json_content
                return json_content
        except Exception as ex:
            print(str(ex))

    def get_instances_to_be_ignored(self):
        print('Getting EC2Instances section from config file')
        instances = [x for x in self.config_json_content['EC2Instances']]
        return instances
        #print(self.config_json_content['EC2Instances'])


def __init__():
    pass