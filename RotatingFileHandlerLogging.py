import logging
import time
from logging.handlers import RotatingFileHandler


# ----------------------------------------------------------------------
def create_rotating_log(path):
    """
    Creates a rotating log
    """
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    # add a rotating handler
    handler = RotatingFileHandler(path, maxBytes=20,
                                  backupCount=2)
    logger.addHandler(handler)

    for i in range(10):
        logger.info("This is test log line %s" % i)
        time.sleep(1.5)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    import os
    path = os.getcwd()
    log_dir = os.path.abspath(os.path.join(path, os.pardir))

    log_file = os.path.join(log_dir,"test.log")
    print(log_file)
    create_rotating_log(log_file)