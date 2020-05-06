from easydict import EasyDict
import yaml

def _load_config_files():
    with open('config/config.yaml', 'r') as config_file:
        dictionary = yaml.load(config_file)
    return EasyDict(dictionary)

config = _load_config_files()
