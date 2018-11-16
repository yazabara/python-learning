import os
import platform

from simple_log import simple_log as log


class ZipRunner(object):

    @staticmethod
    def run_zip(source, target):
        command = ZipRunner.__create_zip_command(source, target)
        log.info('Zip command to execute: {}'.format(command))
        return os.system(command) == 0

    @staticmethod
    def __create_zip_command(source, target):
        if platform.system() is 'Linux':
            return "zip -qr {} {}".format(target, source)
        if platform.system() is 'Windows':
            return "Compress-Archive {} {}".format(source, target)
        raise Exception('Application doesn\'t support OS {}'.format(platform.system()))
