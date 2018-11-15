import yaml


class BackupConfig(object):

    def __init__(self, path):
        cfg = self.__load_config(path)
        self.source = cfg['backup']['source']
        self.target = cfg['backup']['target']
        self.comment = cfg['backup']['comment']

    @staticmethod
    def __load_config(path):
        with open(path, 'r') as yml_file:
            config = yaml.load(yml_file)
        return config


if __name__ == '__main__':
    BackupConfig()
