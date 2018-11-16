import yaml

from configuration.backup_config import BackupConfig
from configuration.extractor.config_extractor import ConfigExtractor
from simple_log import simple_log as log


class YamlConfigExtractor(ConfigExtractor):

    def __init__(self, path):
        log.info("Yaml config extractor initialized. Configuration location : {}".format(path))
        self.configuration_path = path

    def extract(self):
        yaml_config = self.__load_config()
        return BackupConfig(yaml_config['backup']['source'],
                            yaml_config['backup']['target'],
                            yaml_config['backup']['comment'])

    def __load_config(self):
        with open(self.configuration_path, 'r') as yml_file:
            config = yaml.load(yml_file)
        return config
