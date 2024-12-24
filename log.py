import logging

# Configure the logger
logging.basicConfig(
    level=logging.DEBUG,  # Set the log level to DEBUG, can be: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
    handlers=[
        logging.FileHandler('app.log'),  # Log to a file named app.log
        logging.StreamHandler()  # Also print logs to the console
    ]
)

# Example usage of different log levels
logger = logging.getLogger(__name__)