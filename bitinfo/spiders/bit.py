# -*- coding: utf-8 -*-
import scrapy
from bitinfo.items import BitinfoItem


class BitSpider(scrapy.Spider):
    name = 'bit'
    allowed_domains = ['bitinfocharts.com']
    start_urls = ['https://bitinfocharts.com/']

    def parse(self, response):
        tr_list = response.xpath('//*[@id="main_body"]//tr')
        one_list = []
        for i in range(1, 20):
            for tr in tr_list[0:-1]:
                td = tr.xpath('./td')[i]
                td_str = td.xpath('.//text()').extract()
                td_str = ''.join(td_str).strip()
                print(td_str)
                one_list.append(td_str)
            print(one_list)
            item = BitinfoItem()
            item['Name'] = one_list[0]
            item['Total'] = one_list[1]
            item['Price'] = one_list[2]
            item['Market_Capitalization'] = one_list[3]
            item['Transactions_last_24h'] = one_list[4]
            item['Transactions_avg_per_hour'] = one_list[5]
            item['Sent_last_24h'] = one_list[6]
            item['Sent_avg_per_hour'] = one_list[7]
            item['Avg_Transaction_Value'] = one_list[8]
            item['Median_Transaction_Value'] = one_list[9]
            item['Block_Time'] = one_list[10]
            item['Blocks_Count'] = one_list[11]
            item['Blocks_last_24h'] = one_list[12]
            item['Blocks_avg_per_hour'] = one_list[13]
            item['Reward_Per_Block'] = one_list[14]
            item['Reward_last_24h'] = one_list[15]
            item['Difficulty'] = one_list[16]
            item['Hashrate'] = one_list[17]
            item['Mining_Profitability'] = one_list[18]
            item['Top_100_Richest'] = one_list[19]
            item['Wealth_Distribution'] = one_list[20]
            item['Addresses_richer_than'] = one_list[21]
            item['Active_Addresses_last_24h'] = one_list[22]
            item['Largest_Transactions_100'] = one_list[23]
            item['First_Block'] = one_list[24]
            item['Blockchain_Size'] = one_list[25]
            item['Reddit_subscribers'] = one_list[26]
            item['Tweets_per_day'] = one_list[27]
            item['Github_release'] = one_list[28]
            item['Github_stars'] = one_list[29]
            item['Github_last_commit'] = one_list[30]
            # print(item)
            one_list = []
            yield item
