import argparse

from configuration.backup_config import BackupConfig
from configuration.extractor.config_extractor import ConfigExtractor

from simple_log import simple_log as log


class ConsoleConfigExtractor(ConfigExtractor):

    def __init__(self):
        log.info("Console config extractor initialized")
        self.__parser = argparse \
            .ArgumentParser(description='Confuguration parser for backup application')

        self.__parser.add_argument('--source', required=False, type=str)
        self.__parser.add_argument('--target', required=False, type=str)
        self.__parser.add_argument('--comment', required=False, type=str)

    def extract(self):
        args = self.__parser.parse_args()
        return BackupConfig(args.source,
                            args.target,
                            args.comment)
