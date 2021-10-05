# -*- coding: utf-8 -*-
"""
Created on 2021-02-08 16:06:12
---------
@summary:
---------
@author: Boris
"""

import feapder
import pandas as pd
import json
from items import *


class TestSpider(feapder.Spider):
    def start_requests(self):

        df = pd.read_json('../09_getNFTData.json', dtype={"tokenId": object})
        # for i in range(1):
        #     yield feapder.Request(f"https://www.baidu.com#{i}", callback=self.parse)

        for row in df.iterrows():
            yield feapder.Request(row[1]['tokenURI'], job=row[1].to_json(), callback=self.parse)


    # def validate(self, request, response):
    #     if response.status_code != 200:
    #         raise Exception("response code not 200")  # 重试
    #         #return False  # 抛弃当前请求
    #     # if "哈哈" not in response.text:
    #     #     return False # 抛弃当前请求

    def parse(self, request, response):
        response.encoding = 'utf8'

        job = json.loads(request.job)

        item = spider_data_item.SpiderDataItem()  # 声明一个item
        item.createTime = job['createTime']  # 给item属性赋值
        item.creator = job['creator']  # 给item属性赋值
        item.name = job['name']  # 给item属性赋值
        item.tokenContractAddress = job['tokenContractAddress']  # 给item属性赋值
        item.tokenId = job['tokenId']  # 给item属性赋值
        item.tokenURI = job['tokenURI']  # 给item属性赋值
        item.tokenURIType = job['tokenURIType']  # 给item属性赋值
        item.statusCode = response.status_code
        if response.status_code == 200:
            item.data = json.loads(response.text)

        yield item  # 返回item， item会自动批量入库


if __name__ == '__main__':
    spider = TestSpider(redis_key="feapder3:test_spider", thread_count=100)
    spider.start()