import os
import time

from configuration.config_builder import ConfigBuilder
from simple_log import simple_log as log
from string_utils.string_utils import get_str
from zip_runner import ZipRunner


class Backup(object):

    def __init__(self):
        self.__config = None

    def backup(self):
        # building configuration. Main source - console. additional(default) - yaml configuration
        self.__config = ConfigBuilder() \
            .from_console() \
            .from_yaml('configuration/configuration.yml') \
            .get_configuration()

        target_name = self.__build_target_path()

        if ZipRunner.run_zip(self.__config.source, target_name):
            log.info("Backup copy was successfully created: {}".format(target_name))
        else:
            log.error("Backup wasn't created for source {}".format(self.__config.source))

    def __build_target_path(self):
        return "{}{}{}-{}.zip" \
            .format(self.__config.target,
                    os.sep,
                    get_str(self.__config.comment).replace(' ', '_'),
                    time.strftime("%Y%m%d"))


if __name__ == '__main__':
    Backup().backup()
    # input("Press Enter to continue...")
