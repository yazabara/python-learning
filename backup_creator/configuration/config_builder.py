from configuration.extractor.extract_factory import ExtractFactory


class ConfigBuilder(object):

    def __init__(self):
        self.__config = None
        self.__extract_factory = ExtractFactory()

    def from_yaml(self, path, rewrite_if_absent=False):
        # rewrite configuration if it absent
        if (not self.__is_config_valid()) or (rewrite_if_absent and not self.__is_config_valid()):
            self.__config = self \
                .__extract_factory \
                .get_yaml_extractor(path) \
                .extract()
        return self

    def from_console(self, rewrite_if_absent=False):
        # rewrite configuration if it absent
        if (not self.__is_config_valid()) or (rewrite_if_absent and not self.__is_config_valid()):
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
        if not self.__is_config_valid():
            raise Exception('Configuration not present')
        return self.__config

    def __is_config_valid(self):
        """
        Method checks configuration (not absent)
        :return: true - if config valid, false - otherwise
        """
        if self.__config is not None and not self.__config.is_empty():
            return True
        return False
