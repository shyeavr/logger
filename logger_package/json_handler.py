import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('foo.log')
stream_handler = logging.StreamHandler()

stream_formatter = logging.Formatter(
    '%(asctime)-15s %(levelname)-8s %(message)s')
file_formatter = logging.Formatter(
    "{'level': '%(levelname)s', 'message': '%(message)s'}"
)

file_handler.setFormatter(file_formatter)
stream_handler.setFormatter(stream_formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.info("erorrrrrrr")
loggingsFile = 'test.json'
with open('foo.log') as f:
    logs = f.read().splitlines()
    print(logs)
for l in logs:
    with open(loggingsFile, 'w') as f:
        json.dump(l, f)

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