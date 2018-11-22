class WrongSingleton(object):
    instance = None

    class __InstanceData(object):

        def __init__(self, args):
            self.__some_data = None
            self.set_some_data(args)

        def set_some_data(self, args):
            self.__some_data = args

        def __str__(self):
            return "memory: {}, data: {}".format(repr(self), self.__some_data)

    def __init__(self, args):
        if not WrongSingleton.instance:
            WrongSingleton.instance = WrongSingleton.__InstanceData(args)
        else:
            WrongSingleton.instance.set_some_data(args)

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __str__(self):
        return "memory: {}".format(repr(self))


class TrueSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        print("__new__", cls._instance)
        if not cls._instance:
            print("creating new object")
            cls._instance = object.__new__(TrueSingleton)
        return cls._instance

    def __init__(self, name):
        print("__init__")
        self.name = name

    def __str__(self):
        return "memory: {}, name: {}".format(repr(self), self.name)


if __name__ == '__main__':
    first = WrongSingleton("first")
    print(first)
    second = WrongSingleton("second")
    print(second)
    third = WrongSingleton("third")
    print(third)

    test1 = TrueSingleton('test1')
    print(test1)
    test2 = TrueSingleton('test2')
    print(test1 == test2)
    print(test1)
    print(test2)
