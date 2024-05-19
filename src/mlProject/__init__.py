"""Logging functionality"""

from pathlib import Path
import logging
import sys

LOGGING_STR = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = Path("logs")
log_filepath = log_dir / "running_logs.log"
log_dir.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=LOGGING_STR,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("mlProjectLogger")