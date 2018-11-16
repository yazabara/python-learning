import yaml

from configuration.backup_config import BackupConfig


class ConfigBuilder(object):

    def __init__(self):
        self.__config = None

    def from_yaml(self, path, rewrite):
        # if no need to rewrite and config already loaded - skip
        if not rewrite and self.__config is not None:
            return self

        yaml_config = ConfigBuilder.__load_config(path)
        self.__config = BackupConfig(yaml_config['backup']['source'],
                                     yaml_config['backup']['target'],
                                     yaml_config['backup']['comment'])
        return self

    def from_console(self, rewrite):
        # if no need to rewrite and config already loaded - skip
        if not rewrite and self.__config is not None:
            return self
        # TODO
        return self

    def get_configuration(self):
        if self.__config is None or self.__config.is_empty():
            raise Exception('Configuration not present')
        return self.__config

    @staticmethod
    def __load_config(path):
        with open(path, 'r') as yml_file:
            config = yaml.load(yml_file)
        return config
