import json
import sys
from logging import StreamHandler

terminator = '\n'

class StreamJsonHandler(StreamHandler):

    def __init__(self, logs_format,level):
        StreamHandler.__init__(self)
        self.format = logs_format
        self.level = level

    def emit(self, record):
        """
        Emit a record.

        If a formatter is specified, it is used to format the record.
        The record is then written to the stream with a trailing newline.  If
        exception information is present, it is formatted using
        traceback.print_exception and appended to the stream.  If the stream
        has an 'encoding' attribute, it is used to determine how to do the
        output to the stream.
        """
        try:
            msg = self.format(record)
            stream = self.stream
            # issue 35046: merged two stream.writes into one.
            stream.write(msg + self.terminator)
            self.flush()
        except RecursionError:  # See issue 36272
            raise
        except Exception:
            self.handleError(record)
    # def logs_to_json_format(self, stream_logs):
    #     logs = stream_logs.read().splitlines()
    #     json_logs_format = json.dumps(logs)
    #     sys.stdout.write(json_logs_format)
    #
    #
    # def emit(self, record):
    #     """
    #     Emit a record.
    #
    #     If a formatter is specified, it is used to format the record.
    #     The record is then written to the stream with a trailing newline.  If
    #     exception information is present, it is formatted using
    #     traceback.print_exception and appended to the stream.  If the stream
    #     has an 'encoding' attribute, it is used to determine how to do the
    #     output to the stream.
    #     """
    #     try:
    #         type(record)
    #         msg = self.format(record)
    #         print(msg, '------> tests')
    #         stream = self.stream
    #         # issue 35046: merged two stream.writes into one.
    #         stream.dumps(msg + self.terminator)
    #         self.flush()
    #     except RecursionError:  # See issue 36272
    #         raise
    #     except Exception:
    #         self.handleError(record)