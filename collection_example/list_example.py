some_list = ['apple', 'banana', 'orange', 'pineapple']


def compare(str1, str2):
    if str1 is None:
        return -1
    return len(str1) - len(str2)


def custom_filter(value):
    return value is not None and len(value) > 6


if __name__ == '__main__':
    print some_list
    some_list.sort()
    print some_list
    some_list.reverse()
    print some_list
    some_list.append('watermelon')
    some_list.append(None)
    # function returns new sorted list (using comparator)
    some_list = sorted(some_list, cmp=compare)
    print some_list
    print 'watermelon' in some_list
    print filter(custom_filter, some_list)
