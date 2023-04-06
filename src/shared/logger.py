import logging
import colorlog
import sys

# Create a formatter with colors
formatter = colorlog.ColoredFormatter(
    '[%(asctime)s] [%(log_color)s%(levelname)s%(reset)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white'
    }
)

# Configure logging
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)

logging.basicConfig(
    level=logging.INFO,
    handlers=[handler]
)

# Create a logger instance
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
