from json_logging import JSONLogFormatter


class JsonLogger(JSONLogFormatter):
    def __init__(self, logs_level, logger_format, *args, **kw):
        super().__init__(*args, **kw)
        self.logs_level = logs_level
        self.logger_format = logger_format
