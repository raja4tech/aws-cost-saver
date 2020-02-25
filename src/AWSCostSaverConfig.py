import json

class AWSCostSaverConfig:
    def __init__(self, filename):
        self.filename = filename

    def read_config(self):
        try:
            with open(self.filename) as config_file:
                json_content = json.load(config_file)
                return json_content
        except Exception as ex:
            print(str(ex))


def __init__():
    pass