import os
import sys
import logging

logging_formate = "[%(asctime)s]: %(levelname)s: %(module)s:  %(message)s"
dir = "log"
os.makedirs(dir, exist_ok=True)
filepath = os.path.join(dir,"logs.log")



logging.basicConfig(
    level=logging.INFO,
    format=logging_formate,
    handlers=[
        logging.FileHandler(filepath),
        logging.StreamHandler(sys.stdout)
    ]   
)

logger = logging.getLogger("textSummarizer")

