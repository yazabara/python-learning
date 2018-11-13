from simple_log import simple_log as log

dictionary = {
    'first': 'first.com',
    'second': 'second.com',
    'third': 'third.com',
    'fourth': 'fourth.com',
    'fifth': 'fifth.com',
}

if __name__ == '__main__':
    log.info(dictionary)
    log.info(dictionary['first'])
    del dictionary['fifth']
    log.info(dictionary)
    dictionary['fifth'] = int(123)
    log.info(dictionary)
    for key in dictionary.keys():
        if str.startswith(key, 'f'):
            log.info("Keys with start character f: {0}".format(dictionary[key]))
