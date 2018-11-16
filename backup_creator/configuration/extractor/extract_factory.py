from configuration.extractor.console_config_extractor import ConsoleConfigExtractor
from configuration.extractor.yaml_config_extractor import YamlConfigExtractor


class ExtractFactory(object):

    def __init__(self):
        self.__console_extractor = None
        self.__yaml_extractor = None

    def get_console_extractor(self):
        if self.__console_extractor is None:
            self.__console_extractor = ConsoleConfigExtractor()
        return self.__console_extractor

    def get_yaml_extractor(self, path):
        if self.__yaml_extractor is None:
            self.__yaml_extractor = YamlConfigExtractor(path)
        return self.__yaml_extractor
