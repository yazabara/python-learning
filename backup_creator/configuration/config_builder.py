from configuration.config_validator import ConfigValidator
from configuration.extractor.extract_factory import ExtractFactory


class ConfigBuilder(object):

    def __init__(self):
        self.__config = None
        self.__extract_factory = ExtractFactory()

    def from_yaml(self, path):
        # rewrite configuration if it absent
        if not ConfigValidator(self.__config).is_valid():
            self.__config = self \
                .__extract_factory \
                .get_yaml_extractor(path) \
                .extract()
        return self

    def from_console(self):
        # rewrite configuration if it absent
        if not ConfigValidator(self.__config).is_valid():
            self.__config = self \
                .__extract_factory \
                .get_console_extractor() \
                .extract()
        return self

    def get_configuration(self):
        """
        Method checks configuration and if it valid - return extracted config
        :return: extracted config
        """
        if not ConfigValidator(self.__config).is_valid():
            raise Exception('Configuration not present')
        return self.__config
