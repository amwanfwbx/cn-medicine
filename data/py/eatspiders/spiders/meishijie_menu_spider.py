
import scrapy
from scrapy import signals
import hashlib
import time
import copy
from pymongo import MongoClient

class MSJ_YuanLiaoSpider(scrapy.Spider):

    name = "MSJ_MenuSpider"
    # handle_httpstatus_list = [301, 302]
    #start_urls = ['https://www.meishichina.com/YuanLiao/category/rql/']
    start_urls = ['https://www.meishij.net/chufang/diy/',
                  'https://www.meishij.net/china-food/caixi/',
                  'https://www.meishij.net/china-food/xiaochi/',
                  'https://www.meishij.net/chufang/diy/guowaicaipu1/',
                  'https://www.meishij.net/hongpei/']

    exchangeobj = None
    db = MongoClient('localhost', 27017).eat

    # def __init__(self):
    #     # self.config = self.load_config()
    #     print(self.config)
    #     self.name = self.config["name"]
    #     self.start_urls = self.config["start_urls"]

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(MSJ_YuanLiaoSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def generate_doc(self, response):
        body_abs = hashlib.md5(response.body).hexdigest()
        doc = {"url": response.url, "data": str(response.body, response.encoding), "abs": body_abs, "createtime": time.time(), "latest": 1, "spidername": self.name}
        if 'u-ref' in response.request.headers:
            doc["ref"] =  response.request.headers['u-ref']
        if 'u-tag' in response.request.headers:
            doc["tag"] = response.request.headers['u-tag']
        return doc

    # 关闭事件
    def spider_closed(self, spider):
        spider.logger.info('Spider closed: %s', spider.name)

    # 当页面被获取时【框架提供】
    def parse(self, response):

        doc_db = self.db["ori_webpageinfo"].find_one({"url": response.url})
        doc_new = self.generate_doc(response)

        # 没抓过的
        if not doc_db:
            self.db["ori_webpageinfo"].insert_one(doc_new)
        # 抓过，但有变更
        elif doc_db["abs"] != doc_new["abs"]:
            # self.db["ori_webpageinfo"].insert_one(doc_new)
            # doc_db_new = copy.deepcopy(doc_db)
            # doc_db_new["latest"] = 0
            self.db["ori_webpageinfo"].update_one(doc_db, {"$set": {"data": doc_new['data'], 'abs': doc_new["abs"]}})
        # else:
        #     return
        # 分析链接_目录
        if response.url in self.start_urls:
            quotes = response.css(".listnav_con dd a")
            for quote in quotes:
                newurl = quote.attrib["href"]
                self.logger.info("找到分类连接：%s", newurl)
                req1 = response.follow(newurl, self.parse)
                req1.headers["u-ref"] = str(response.url)
                req1.headers["u-tag"] = "catlog"
                yield req1
        # elif hasattr(response, "tag") and response.tag == "catlog":
        elif 'u-tag' in response.request.headers and response.request.headers['u-tag'].decode("utf-8") == "catlog":
            # 下一页
            quotes = response.css(".listtyle1_page_w .next")
            for quote in quotes:
                newurl = quote.attrib["href"]
                self.logger.info("找到分类连接：%s", newurl)
                req1 = response.follow(newurl, self.parse)
                req1.headers["u-ref"] = str(response.url)
                req1.headers["u-tag"] = "catlog"
                yield req1
            # 当前页的菜
            quotes = response.css(".listtyle1_list .listtyle1 a")
            for quote in quotes:
                newurl = quote.attrib["href"]
                self.logger.info("找到菜谱：%s", newurl)
                req1 = response.follow(newurl, self.parse)
                req1.headers["u-ref"] = str(response.url)
                req1.headers["u-tag"] = "menu"
                yield req1
        # elif response.tag == "menu":
        #     return
        # for target in self.config["targets"]:
        #     # self.logger.info("新增结点：%s", nid)
        #     if self.start_urls.__contains__(response.url) or re.match(target["target"]["refurl_pattern"], response.url, re.I):
        #         self.logger.info("%s提取链接：%s", response.url, target["target"]["name"])
        #
        #         if target["target"]["href_pattern"]["mode"] == "css":
        #             quotes = response.css(target["target"]["href_pattern"]["value"])
        #             for quote in quotes:
        #                 try:
        #                     url = quote.root.attrib["href"]
        #                     self.logger.info("找到连接：%s", url)
        #                     req = response.follow(url, self.parse);
        #                     req.refurl = response.url
        #                     yield req
        #                 except KeyError:
        #                     self.logger.warning("找不到连接：%s", quote)
        #         elif target["target"]["href_pattern"]["mode"] == "filter":
        #             quotes = response.css('a')
        #             for quote in quotes:
        #                 try:
        #                     url = quote.root.attrib["href"]
        #                     if re.match(target["target"]["href_pattern"]["value"], url):
        #                         self.logger.info("找到连接：%s", url)
        #                         req = response.follow(url, self.parse);
        #                         req.refurl = response.url
        #                         yield req
        #                 except KeyError:
        #                     self.logger.warning("找不到连接：%s", quote)
        #         elif target["target"]["href_pattern"]["mode"] == "exec":
        #             exec(target["target"]["href_pattern"]["value"])
        #             for url in self.exchangeobj:
        #                 req = response.follow(url, self.parse)
        #                 req.refurl = response.url
        #                 req.headers["u-ref"] = str(response.url)
        #                 yield req
        #
        # self.parse_content(response)

    def parse_content(self, response):

        pass
    # 加载配置文件
    # def load_config(self, file="conf.yml"):
    #     # 获取当前文件路径 D:/WorkSpace/StudyPractice/Python_Yaml/YamlStudy
    #     filePath = os.path.dirname(__file__)
    #     # 获取当前文件的Realpath  D:\WorkSpace\StudyPractice\Python_Yaml\YamlStudy\YamlDemo.py
    #     # fileNamePath = os.path.split(os.path.realpath(__file__))[0]
    #     # print(fileNamePath)
    #     # 获取配置文件的路径 D:/WorkSpace/StudyPractice/Python_Yaml/YamlStudy\config.yaml
    #     yamlPath = os.path.join(filePath, file)
    #     print("开始读取配置文件: ", yamlPath)
    #     # 加上 ,encoding='utf-8'，处理配置文件中含中文出现乱码的情况。
    #     f = open(yamlPath, 'r', encoding='utf-8')
    #     cont = f.read()
    #
    #     return yml_load(cont, Loader=Loader)

