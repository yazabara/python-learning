import datetime


class Level(object):
    OFF = 0
    FATAL = 100
    ERROR = 200
    WARN = 300
    INFO = 400
    DEBUG = 500
    TRACE = 600
    ALL = 700


__level_messages = {
    Level.ALL: "All",
    Level.FATAL: "FATAL",
    Level.ERROR: "ERROR",
    Level.WARN: "WARN",
    Level.INFO: "INFO",
    Level.OFF: "OFF",
    Level.TRACE: "TRACE"
}


def __log(message, level):
    if level is None or message is None:
        return
    if level not in __level_messages or level is Level.OFF:
        return
    print("{} {} : {}".format(datetime.datetime.now(), __level_messages[level], message))


def info(message):
    __log(message, Level.INFO)


if __name__ == '__main__':
    __log("No message", Level.OFF)
    __log("This is a FATAL message", Level.FATAL)
    __log("This is a ERROR message", Level.ERROR)
    __log("This is a WARN message", Level.WARN)
    __log("This is a INFO message", Level.INFO)
    __log("This is a DEBUG message", Level.DEBUG)
    __log("This is a TRACE message", Level.TRACE)
    __log("This is a ALL message", Level.ALL)
