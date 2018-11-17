some_list = ['apple', 'banana', 'orange', 'pineapple']


def compare(str1):
    if str1 is None:
        return -1
    return len(str1)


def custom_filter(value):
    return value is not None and len(value) > 6


if __name__ == '__main__':
    print(some_list)
    some_list.sort()
    print(some_list)
    some_list.reverse()
    print(some_list)
    some_list.append('watermelon')
    some_list.append(None)
    # function returns new sorted list (using comparator)
    some_list = sorted(some_list, key=compare)
    print(some_list)
    some_list = sorted(some_list, key=lambda val: -1 if val is None else len(val))
    print(some_list)
    print('watermelon' in some_list)
    print(list(filter(custom_filter, some_list)))
    generated = [2 * i for i in (0, 10, 100, 200) if i == 10]
    print(generated)
