from simple_log import simple_log as log


class ConfigValidator(object):

    def __init__(self, config):
        self.__config = config
        log.info("Config validator initialized for configuration {} ".format(config))

    def is_valid(self):
        """
        Method checks configuration (not absent)
        :return: true - if config valid, false - otherwise
        """
        if self.__config is not None and not self.__config.is_empty():
            return True
        # TODO add more specific validation
        return False
