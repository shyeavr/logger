import json
import logging
import os
import sys
from streamjson_handler import StreamJsonHandler

root_logger = logging.getLogger()


class Logger:
    def __init__(self, json_file_name, log_file):
        self.logger = logging.getLogger(os.path.basename(__file__))
        print(self.logger)
        self.json_file_name = json_file_name
        self.log_file_name = log_file

    def write_json_logs_to_console(self):
        with open(self.log_file_name) as log_file:
            logs = log_file.read().splitlines()
            json_logs_format = json.dumps(logs)
            sys.stdout.write(json_logs_format)

    def set_file_handler(self, log_format):
        file_handler = logging.FileHandler(self.log_file_name)
        file_formatter = logging.Formatter(log_format)
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

    def set_stream_handler(self, log_format):
        stream_handler = logging.StreamHandler()
        stream_formatter = logging.Formatter(log_format)
        stream_handler.setFormatter(stream_formatter)
        self.logger.addHandler(stream_handler)

    def set_json_stream_handler(self, log_format):
        json_stream_handler = StreamJsonHandler()
        json_stream_formatter = logging.Formatter(log_format)
        json_stream_handler.setFormatter(json_stream_formatter)
        self.logger.addHandler(json_stream_handler)


shay = Logger('shay.json', 'check.log')
shay.logger.setLevel(logging.DEBUG)
# handler1 = shay.set_stream_handler('%(asctime)-15s %(levelname)-8s %(message)s')

handler2 = shay.set_json_stream_handler('%(asctime)-15s %(levelname)-8s %(message)s')
shay.logger.error("the class working")

# handler2 = shay.set_file_handler('%(asctime)-15s %(levelname)-8s %(message)s')


# shay.write_json_logs_to_console()
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
#
# file_handler = logging.FileHandler('foo.log')
# stream_handler = logging.StreamHandler()
#
# stream_formatter = logging.Formatter(
#     '%(asctime)-15s %(levelname)-8s %(message)s')
#
# file_formatter = logging.Formatter(
#     "{'level': '%(levelname)s', 'message': '%(message)s'}"
# )
#
# file_handler.setFormatter(file_formatter)
# stream_handler.setFormatter(stream_formatter)
#
# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)
#
# logger.info("erorrrrrrr----->111111>")
#
# loggingsFile = 'test.json'
# with open('foo.log') as f:
#     logs = f.read().splitlines()
# print(logs)
# for l in logs:
#     with open(loggingsFile, 'w') as f:
#         json.dump(l, f)

#     print(l)
#     for key, value in eval(l):
#         logs_data = {key:value}
#         print(key)
#         print(value)
#         print(logs_data)
#         logs_file_data = {}
#         for key1, value1 in logs_data:
#             logs_file_data[key1] = value1
#             print("final data======" ,logs_file_data)

# with open(loggingsFile, 'w') as f:
#     json.dump(logs_data, f)
