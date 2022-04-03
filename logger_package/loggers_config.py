import enums


class LogsFormat(enums):
    BASIC_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    FUNC_NAME_FORMAT = '%(asctime)s - %(name)s -  %(funcName)s - %(levelname)s - %(message)s'
    PROCESS_NAME_FORMAT = '%(asctime)s - %(name)s -  %(processName)s - %(levelname)s - %(message)s'
    PROCESS_ID_FORMAT = '%(asctime)s - %(name)s -  %(process)s - %(levelname)s - %(message)s'
    THREAD_ID_FORMAT = '%(asctime)s - %(name)s -  %(thread)s - %(levelname)s - %(message)s'
    THREAD_NAME_FORMAT = '%(asctime)s - %(name)s -  %(threadName)s - %(levelname)s - %(message)s'
