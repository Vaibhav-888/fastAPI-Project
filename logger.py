# import logging
# import sys
#
# # getLogger
# logger = logging.getLogger()
#
# # create formatter
# """
# Responsible for converting a LogRecord to an output
# string to be interpreted by a human or external system.
# """
# formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")
#
# # create handlers
# """
# sys.stdout:
# Writes output to the standard output stream and allows low-level control over printed output.
# """
# stream_handler = logging.StreamHandler(sys.stdout)
# file_handler = logging.FileHandler("app.log")
#
# # set formatters
# stream_handler.setFormatter(formatter)
# file_handler.setFormatter((formatter))
#
# # add handlers to logger
# logger.handlers = [stream_handler, file_handler]
#
# # set log-level
# logger.setLevel(logging.INFO)

import logging
import sys

# get logger
get_logger = logging.getLogger(__name__)

# create formatters
log_formatter = logging.Formatter(fmt="%(levelname)s - %(asctime)s - %(message)s")

# create handlers
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("server.log")

# set handlers to logger
stream_handler.setFormatter(log_formatter)
file_handler.setFormatter(log_formatter)

# add handlers to logger
get_logger.handlers = [stream_handler, file_handler]

# set log-level
get_logger.setLevel(logging.INFO)


# def handle_exception(exc_type, exc_value, exc_traceback):
#     if issubclass(exc_type, KeyboardInterrupt):
#         sys.__excepthook__(exc_type, exc_value, exc_traceback)
#         return
#     get_logger.error("Uncaught Exception", exc_info=(exc_type, exc_value, exc_traceback))
#
#     # sys.excepthook = handle_exception()
#     handle_exception()