# import os
# import collections
# import datetime
# import json
# import logging
# from typing import Any, Dict

import json_logging, logging, sys

# log is initialized without a web framework name
json_logging.init_non_web(enable_json=True)

logger = logging.getLogger("test-logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

logger.info("test logging statement")


# This example shows how the logger can be set up to use a custom JSON format.
import json
import logging
import sys


import json_logging.framework


def extra(**kw):
    '''Add the required nested props layer'''
    return {'extra': {'props': kw}}


class CustomJSONLog(json_logging.formatters.JSONLogFormatter):
    """
    Customized logger
    """

    def format(self, record):
        json_customized_log_object = ({
            "customized_prop": "customized value",
            "message": record.getMessage()
        })

        return json.dumps(json_customized_log_object)


# You would normally import logger_init and setup the logger in your main module - e.g.
# main.py

json_logging.init_non_web(custom_formatter=CustomJSONLog, enable_json=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stderr))

logger.info('sample log message')

#
# standard_attributes = (
#     "name",
#     "msg",
#     "args",
#     "levelname",
#     "levelno",
#     "pathname",
#     "filename",
#     "module",
#     "exc_info",
#     "exc_text",
#     "stack_info",
#     "lineno",
#     "funcName",
#     "created",
#     "msecs",
#     "relativeCreated",
#     "thread",
#     "threadName",
#     "processName",
#     "process",
#     "message",
#     "asctime",
# )
#
#
# def _extra_attributes(record: logging.LogRecord) -> Dict[str, Any]:
#     return {
#         name: record.__dict__[name]
#         for name in set(record.__dict__).difference(standard_attributes)
#     }
#
#
# def _value(record: logging.LogRecord, field_name_or_value: Any) -> Any:
#     """
#     Retrieve value from record if possible. Otherwise use value.
#     :param record: The record to extract a field named as in field_name_or_value.
#     :param field_name_or_value: The field name to extract from record or the default value to use if not present.
#     """
#     try:
#         return getattr(record, field_name_or_value)
#     except:
#         return field_name_or_value
#
#
# def default_converter(obj: Any) -> str:
#     if isinstance(obj, datetime.datetime):
#         return obj.isoformat()
#     return str(obj)
#
#
# class JSONFormatter(logging.Formatter):
#     def __init__(
#             self,
#             *args,
#             fields: Dict[str, Any] = None,
#             message_field_name: str = "msg",
#             **kwargs,
#     ):
#         # Allow to provide any formatter setting (useful to provide a custom date format)
#         super().__init__(*args, **kwargs)
#         self.fields = fields or {}
#         self.usesTime = lambda: "asctime" in self.fields.values()
#         self.message_field_name = message_field_name
#
#     def format(self, record: logging.LogRecord):
#         # Let python set every additional record field
#         super().format(record)
#
#         message = {
#             field_name: _value(record, field_value)
#             for field_name, field_value in self.fields.items()
#         }
#         if isinstance(record.msg, collections.abc.Mapping):
#             message.update(record.msg)
#         else:
#             message[self.message_field_name] = super().formatMessage(record)
#
#         message.update(_extra_attributes(record))
#
#         if record.exc_info:
#             message["exception"] = {
#                 "type": record.exc_info[0].__name__,
#                 "message": str(record.exc_info[1]),
#                 "stack": self.formatException(record.exc_info),
#             }
#
#         if len(message) == 1 and self.message_field_name in message:
#             return super().formatMessage(record)
#
#         return json.dumps(message, default=default_converter)
#
#     def formatMessage(self, record: logging.LogRecord) -> str:
#         # Speed up this step by doing nothing
#         return ""
#
# #
# #
# #
# #
# logger = logging.getLogger(os.path.basename(__file__))
# logging.Formatter()
# #
# #
# logger.setLevel(logging.DEBUG)
# loggingStreamHandler = logging.StreamHandler()
# logger.addHandler(loggingStreamHandler)
# loggingStreamHandler.setFormatter(JSONFormatter())
# logger.info("check")
# #
#
# #
# # logger.addHandler(x)
# # y = logging.Formatter()
# #
# # class JSONFormatter(logging.Formatter):
# #
# #
# #     def __init__(self, log_param=None, fields: Dict[str, Any] = None, message_field_name: str = "msg", ):
# #         super().__init__()
# #         self.fields = fields or {}
# #         self.usesTime = lambda: "asctime" in self.fields.values()
# #         self.message_field_name = message_field_name
# #         self.format_x = logging.Formatter("%(asctime)-15s, %(levelname)-8s, %(message)s")
# #         if log_param is None:
# #             self.log_param = ("time", "level", "message")
# #
# #     def format(self, record) :
# #         logs = {}
# #         record.message = record.getMessage()
# #         if self.usesTime():
# #             record.asctime = self.formatTime(record, self.datefmt)
# #         s = self.formatMessage(record)
# #         logs["message"] = s
# #         if record.exc_info:
# #             # Cache the traceback text to avoid converting it multiple times
# #             # (it's constant anyway)
# #             if not record.exc_text:
# #                 record.exc_text = self.formatException(record.exc_info)
# #
# #         if record.exc_text:
# #             if s[-1:] != "\n":
# #                 s = s + "\n"
# #             s = s + record.exc_text
# #             logs["exc_text"] = s
# #         if record.stack_info:
# #             if s[-1:] != "\n":
# #                 s = s + "\n"
# #             s = s + self.formatStack(record.stack_info)
# #             logs["stack_info"] = self.formatStack(record.stack_info)
# #         return str(logs)
# #
# #
# #     def format1(self, record):
# #         logs  = {}
# #         print(self.format_x.format(record=record))
# #         logs["time"] = record.asctime
# #         logs["message"] = record.msg
# #         print(logs)
# #         # x = self.format_x.format(record=record).strip().split("    ,    ")
# #
# #
# #
# #         record.msg = (record.msg)
# #         # print(record.msg, 'check')
# #         # return record.msg
# #         return super().format(record)
# #
# #     def format1(self, record, format_keys):
# #         """
# #         Format the specified record as text.
# #
# #         The record's attribute dictionary is used as the operand to a
# #         string formatting operation which yields the returned string.
# #         Before formatting the dictionary, a couple of preparatory steps
# #         are carried out. The message attribute of the record is computed
# #         using LogRecord.getMessage(). If the formatting string uses the
# #         time (as determined by a call to usesTime(), formatTime() is
# #         called to format the event time. If there is exception information,
# #         it is formatted using formatException() and appended to the message.
# #         """
# #
# #         for i in format_keys:
# #             if i in record:
# #                 pass
# #                 record.message = record.getMessage()
# #                 if self.usesTime():
# #                     record.asctime = self.formatTime(record, self.datefmt)
# #                 s = self.formatMessage(record)
# #                 if record.exc_info:
# #                     # Cache the traceback text to avoid converting it multiple times
# #                     # (it's constant anyway)
# #                     if not record.exc_text:
# #                         record.exc_text = self.formatException(record.exc_info)
# #                 if record.exc_text:
# #                     if s[-1:] != "\n":
# #                         s = s + "\n"
# #                     s = s + record.exc_text
# #                 if record.stack_info:
# #                     if s[-1:] != "\n":
# #                         s = s + "\n"
# #                     s = s + self.formatStack(record.stack_info)
# #                 return s
# # # print(x)
# # logger.info("check something")
# #
# #
