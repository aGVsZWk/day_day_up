from singleton import Logger

logger_object = Logger("/var/log/class_logger.log")
logger_object.info("This is an info message")
