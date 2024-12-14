import logging

def setup_logger():
    """
    Set up the logger for the application.

    This function initializes a logger that outputs log messages to the console.
    It sets the logging level and defines the format for the log messages.

    Returns:
        logger: The configured logger instance.
    """
    logger = logging.getLogger('application_logger')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
