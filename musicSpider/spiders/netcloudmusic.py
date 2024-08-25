import scrapy


class NetcloudmusicSpider(scrapy.Spider):
    name = "netcloudmusic"
    allowed_domains = ["music.163.com"]
    start_urls = ["https://music.163.com/#/search/m/?%23%2Fdiscover%2Fartist=&s=%E8%90%A7%E4%BA%9A%E8%BD%A9&type=1"]

    def parse(self, response):
        pass
