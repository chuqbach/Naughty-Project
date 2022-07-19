import logging


log_format = "%(levelname)s %(asctime)s - %(message)s"
log_file = "crawlers/logs/crawl.log"
logging.basicConfig(filename=log_file,
                    level=logging.DEBUG,
                    format=log_format,
                    filemode="a")

logger = logging.getLogger()
