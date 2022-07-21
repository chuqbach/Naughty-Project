import logging
from datetime import datetime


log_time = datetime.now().strftime("%H_%M_%d_%m_%Y")
log_format = "%(levelname)s %(asctime)s - %(message)s"
log_file = f"crawler/logs/crawler_{log_time}.log"
logging.basicConfig(filename=log_file,
                    level=logging.DEBUG,
                    format=log_format,
                    filemode="w")

logger = logging.getLogger()
