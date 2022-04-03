import logging
import os
from loggers_config import *

logging.basicConfig()
logger = logging.getLogger('basic_logger')


# set level
# logging.FileHandler
# formatter=  logging.Formatter
class Logger:
    def __init__(self, logs_severity, handler_types):
        self.handler_types = handler_types
        self.logs_severity = logs_severity.upper()
        # self.format = format
        logger = logging.getLogger()
        logging.getLogger().hasHandlers()

        self.logger.setLevel(self.logs_severity)
        self.setup_formats()



    def set_logger(self):
        return logging.getLogger(os.path.basename(os.getcwd()))
    # def set_logs_severity(self):
    #     return self.logger.setLevel(self.logs_severity)

    def set_basic_formatter(self):
        return logging.Formatter(LogsFormat.BASIC_FORMAT.value)

    def set_func_name_format(self):
        return logging.Formatter(LogsFormat.FUNC_NAME_FORMAT.value)

    def set_process_name_format(self):
        return logging.Formatter(LogsFormat.PROCESS_NAME_FORMAT.value)

    def set_process_id_format(self):
        return logging.Formatter(LogsFormat.PROCESS_ID_FORMAT.value)

    def set_thread_id_format(self):
        return logging.Formatter(LogsFormat.THREAD_ID_FORMAT.value)

    def set_thread_name_format(self):
        return logging.Formatter(self.threadName_format)

    def set_stream_handler(self):
        return logging.StreamHandler()

    def set_file_handler(self, file_name):
        return logging.FileHandler(filename=file_name)

    def set_logger_config(self, format):
        return logging.basicConfig(format=format, level=self.logs_severity)

    def ERROR_log(self, message_str):
        return self.logger.error(message_str)

    def INFO_log(self, message_str):
        return self.logger.info(message_str)

    def DEBUG_log(self, message_str):
        return self.logger.debug(message_str)

    def WARNING_log(self, message_str):
        return self.logger.warning(message_str)

    def CRITICAL_log(self, message_str):
        return self.logger.critical(message_str)

## get severity level of logging
## create format options
# create log output format options





test = Logger('error')
loggingStreamHandler = logging.StreamHandler()
format1 = test.set_basic_formatter()

# loggingStreamHandler = logging.FileHandler("test.json",mode='a') #to save to file
loggingStreamHandler.setFormatter(format1)
logger.addHandler(loggingStreamHandler)
logger.critical('test')

