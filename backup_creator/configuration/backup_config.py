from string_utils.string_utils import is_blank


class BackupConfig(object):

    def __init__(self, source, target, comment):
        self.source = source
        self.target = target
        self.comment = comment

    def is_empty(self):
        if is_blank(self.source) or is_blank(self.target):
            return True
        return False
