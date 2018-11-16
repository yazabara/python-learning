def is_empty(s):
    if s is None:
        return True
    if not isinstance(s, str):
        raise Exception('Input argument is not a string: {}'.format(s))
    if len(s) == 0:
        return True


def is_blank(s):
    if is_empty(s):
        return True
    if len(s.strip()) == 0:
        return True
    return False


def get_str(input):
    if isinstance(input, str):
        return input
    else:
        return str(input)
