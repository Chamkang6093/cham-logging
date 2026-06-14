import datetime
import logging
import os


class MicrosecondFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.datetime.fromtimestamp(record.created, datetime.timezone.utc).astimezone()
        return dt.strftime(datefmt) if datefmt else dt.isoformat()


FORMATTER = MicrosecondFormatter("%(asctime)s - %(levelname)s - %(message)s")


def init_logger():
    log_level = os.environ.get("LOG_LEVEL", "INFO").upper()

    logger = logging.getLogger()
    logger.setLevel(log_level)

    handler = logging.StreamHandler()
    handler.setLevel(log_level)
    handler.setFormatter(FORMATTER)
    logger.addHandler(handler)

    log_file = os.environ.get("LOG_FILE")
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(log_level)
        file_handler.setFormatter(FORMATTER)
        logger.addHandler(file_handler)
