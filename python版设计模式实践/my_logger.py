class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def _write_log(self, level, msg):
        with open(self.file_name, 'a') as log_file:
            log_file.write("[{0}] {1}\n".format(level, msg))

    def critical(self, msg):
        self._write_log('CRITICAL', msg)

    def error(self, msg):
        self._write_log('ERROR', msg)

    def warnning(self, msg):
        self._write_log('WARNNING', msg)

    def info(self, msg):
        self._write_log('INFO', msg)

    def debug(self, msg):
        self._write_log('DEBUG', msg)
