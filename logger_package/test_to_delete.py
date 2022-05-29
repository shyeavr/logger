import json
import logging
import sys

import json_logging


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

json_logging.init_non_web(custom_formatter=CustomJSONLog, enable_json=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stderr))

logger.info('sample log message')


def create_logger(log_formatter=None):
    """
    Generic utility function to get logger object with fixed configurations
    :return:
    logger object
    """
    json_logging.ENABLE_JSON_LOGGING = True
    json_logging.init_non_web(custom_formatter=CustomJSONLog, enable_json=True)
    logger = logging.getLogger(__name__)
    logging.basicConfig()
    json_logging.config_root_logger()
    logger.setLevel(logging.DEBUG)
    logging.addLevelName(logging.ERROR, 'error')
    logging.addLevelName(logging.WARNING, 'warning')
    logging.addLevelName(logging.INFO, 'info')
    logging.addLevelName(logging.DEBUG, 'debug')
    logger.addHandler(logging.NullHandler())
    return logger

