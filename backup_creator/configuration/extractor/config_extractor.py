from abc import ABCMeta, abstractmethod


class ConfigExtractor(metaclass=ABCMeta):

    @abstractmethod
    def extract(self):
        pass
