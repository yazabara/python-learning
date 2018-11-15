import os
import time

# TODO is import correct?
from configuration.backup_config import BackupConfig

from simple_log import simple_log as log


class Backup(object):

    def __init__(self, config):
        self.config = config

    def backup(self):
        target_name = "{}{}{}{}{}.zip" \
            .format(self.config.target, os.sep, self.config.comment.replace(' ', '_'), os.sep, time.strftime("%Y%m%d"))

        # command = os.system("zip -qr {} {}".format(target_name, self.config.source)) == 0:
        command = "Compress-Archive {} {}".format(self.config.source, target_name)
        if os.system(command) == 0:
            log.info("Backup copy was successfully created: {}".format(target_name))
        else:
            log.error("Backup wasn't created from {}".format(self.config.source))


if __name__ == '__main__':
    backup = Backup(BackupConfig('configuration/configuration.yml'))
    backup.backup()
    input("Press Enter to continue...")
