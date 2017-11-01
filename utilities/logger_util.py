import logging
import errno
import time
import os

def setup_logger(logger_name, log_file, level=logging.INFO):
    top_package = __import__(__name__.split('.')[0])
    directory = "logs"

    # setup environment
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    timestr = time.strftime("%Y%m%d")
    full_path = directory+"/"+timestr+"_"+log_file

    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s : %(name)s : %(module)s : %(lineno)s : [ %(levelname)s ] : %(message)s')
    fileHandler = logging.FileHandler(full_path, mode='a')
    fileHandler.setFormatter(formatter)
    l.addHandler(fileHandler)

    l.setLevel(level)
    if(l.getEffectiveLevel() == logging.DEBUG):
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)
        l.addHandler(streamHandler)
    return full_path

def main():
    log1_full_path = setup_logger('log1', 'log1.log')
    log2_full_path = setup_logger('log2', 'log2.log')
    log3_full_path = setup_logger('log3', 'log3.log', logging.DEBUG)

    log1 = logging.getLogger('log1')
    log2 = logging.getLogger('log2')
    log3 = logging.getLogger('log3')

    log1.info('Info for log 1!')
    log2.info('Info for log 2!')
    log3.info('Info for log 3!')

    log1.error('Oh, no! Something went wrong!')
    log2.warning('Watch it boi!')
    log3.warning('I told you, watch it!')

    log3.debug('I do what I want!')


    assert os.path.exists(log1_full_path)
    print "\nPASS: log1_full_path"

    assert os.path.exists(log2_full_path)
    print "PASS: log2_full_path"

    assert os.path.exists(log3_full_path)
    print "PASS: log3_full_path\n"

if __name__ == "__main__":
    main()
