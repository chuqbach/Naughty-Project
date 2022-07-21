from crawlers.Hentai2ReadCrawler import Hentai2ReadCrawler


def main():
    url = "https://hentai2read.com/hentai-list/all/any/all/last-added"
    crawler = Hentai2ReadCrawler(url)
    crawler.crawl()


if __name__ == '__main__':
    main()
