from bs4 import BeautifulSoup
import requests
import logging
import os


def main():
    current_path = os.getcwd()
    # Create and configure logger
    log_format = '%(levelname)s %(asctime)s - %(message)s'
    log_file = "G:/Self Projects/Naughty Project/crawlers/logs/crawl.log"
    logging.basicConfig(filename=log_file,
                        level=logging.DEBUG,
                        format=log_format,
                        filemode='a')

    logger = logging.getLogger()


    # Create and configure logger
    url = "https://alonhadat.com.vn/nha-dat/can-ban/nha-mat-tien/ho-chi-minh/138/quan-7"

    logger.info(f"Sending request to {url}")
    response = requests.get(url)


if __name__ == "__main__":
    main()