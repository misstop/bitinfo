# -*- coding: utf-8 -*-
import scrapy
from bitinfo.items import BitinfoItem
import json
import time

from lxml import etree


def html_to_str(data):
    if data:
        html = etree.HTML(data)
        return ''.join(html.xpath('//text()'))
    else:
        return ''


class BitnoSpider(scrapy.Spider):
    name = 'bitno'
    allowed_domains = ['bitinfocharts.com']
    jiaoyi_list = ['Batcoin', 'BitConnect', 'Siacoin', 'Bitgem', 'DigiByte',
                   'Whitecoin_', 'Syscoin', 'AIRcoin', 'Cloakcoin', 'Viacoin',
                   'Einsteinium', 'Potcoin', 'Iconomi', 'WhiteCoin', 'Navajocoin', 'Unobtanium',
                   'Netcoin', 'Korecoin', 'Gridcoin', 'Vericoin', 'Energycoin', 'Unbreakablecoin',
                   'AC3', 'Dopecoin', 'Solarcoin', 'Pesetacoin', 'Rubycoin',
                   'ElectronicGulden', 'Mintcoin', 'Stealthcoin', 'BitcoinDark', 'TrustPlus',
                   'Bitstar', 'Argentum', 'Leafcoin', 'Terracoin', 'Lottocoin', 'Catcoin',
                   'Phoenixcoin', 'Megacoin', 'Colbertcoin', 'Worldcoin', 'Pandacoin',
                   'Nyancoin', 'Ultracoin', 'Quatloo', 'Quarkcoin', 'Sexcoin', 'Polcoin',
                   ]

    def start_requests(self):
        for jiaoyisuo in self.jiaoyi_list:
            yield scrapy.Request(url='https://bitinfocharts.com/zh/%s/c.json' % jiaoyisuo,
                                 callback=self.parse)

    def parse(self, response):
        data = json.loads(response.body.decode('utf8'))
        item = BitinfoItem()
        item['Name'] = data['coin']
        item['Total'] = data['total']

        price = html_to_str(data['price'])
        item['Price'] = price

        cap = html_to_str(data['cap'])
        item['Market_Capitalization'] = cap

        item['Transactions_last_24h'] = ''
        item['Transactions_avg_per_hour'] = ''
        item['Sent_last_24h'] = ''
        item['Sent_avg_per_hour'] = ''
        item['Avg_Transaction_Value'] = ''
        item['Median_Transaction_Value'] = ''

        time = html_to_str(data['time'])
        item['Block_Time'] = time
        item['Blocks_Count'] = data['blocks']
        item['Blocks_last_24h'] = data['blocks24']
        item['Blocks_avg_per_hour'] = data['blocksPerH']
        item['Reward_Per_Block'] = ''
        item['Reward_last_24h'] = ''

        diff = html_to_str(data['diff'])
        item['Difficulty'] = diff

        hash = html_to_str(data['hash'])
        item['Hashrate'] = hash
        item['Mining_Profitability'] = ''
        item['Top_100_Richest'] = ''
        item['Wealth_Distribution'] = ''
        item['Addresses_richer_than'] = ''
        item['Active_Addresses_last_24h'] = ''
        item['Largest_Transactions_100'] = ''
        item['First_Block'] = data['first']
        item['Blockchain_Size'] = ''

        reddit = html_to_str(data['reddit'])
        item['Reddit_subscribers'] = reddit

        twitter = html_to_str(data['twitter'])
        item['Tweets_per_day'] = twitter

        githubrelease = html_to_str(data['githubrelease'])
        item['Github_release'] = githubrelease

        githubstars = html_to_str(data['githubstars'])
        item['Github_stars'] = githubstars

        githubcommit = html_to_str(data['githubcommit'])
        item['Github_last_commit'] = githubcommit

        # print(item)
        yield item
