import argparse

import yaml
from configuration.backup_config import BackupConfig


class ConfigBuilder(object):

    def __init__(self):
        self.__config = None

    def from_yaml(self, path, rewrite_if_absent=False):
        # rewrite configuration if it absent
        if (not self.__is_config_valid()) or (rewrite_if_absent and not self.__is_config_valid()):
            yaml_config = ConfigBuilder.__load_config(path)
            self.__config = BackupConfig(yaml_config['backup']['source'],
                                         yaml_config['backup']['target'],
                                         yaml_config['backup']['comment'])
        return self

    def from_console(self, rewrite_if_absent=False):
        # rewrite configuration if it absent
        if (not self.__is_config_valid()) or (rewrite_if_absent and not self.__is_config_valid()):
            parser = argparse.ArgumentParser(description='Confuguration parser for backup application')
            parser.add_argument('--source', required=True, type=str)
            parser.add_argument('--target', required=True, type=str)
            parser.add_argument('--comment', required=False, type=str)
            args = parser.parse_args()
            self.__config = BackupConfig(args.source,
                                         args.target,
                                         args.comment)
        return self

    def get_configuration(self):
        if not self.__is_config_valid():
            raise Exception('Configuration not present')
        return self.__config

    def __is_config_valid(self):
        if self.__config is not None and not self.__config.is_empty():
            return True
        return False

    @staticmethod
    def __load_config(path):
        with open(path, 'r') as yml_file:
            config = yaml.load(yml_file)
        return config
