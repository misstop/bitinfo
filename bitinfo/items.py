# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BitinfoItem(scrapy.Item):
    # define the fields for your item here like:
    Name=scrapy.Field()
    Total = scrapy.Field()
    Price = scrapy.Field()
    Market_Capitalization = scrapy.Field()
    Transactions_last_24h = scrapy.Field()
    Transactions_avg_per_hour = scrapy.Field()
    Sent_last_24h = scrapy.Field()
    Sent_avg_per_hour = scrapy.Field()
    Avg_Transaction_Value = scrapy.Field()
    Median_Transaction_Value = scrapy.Field()
    Block_Time = scrapy.Field()
    Blocks_Count = scrapy.Field()
    Blocks_last_24h = scrapy.Field()
    Blocks_avg_per_hour = scrapy.Field()
    Reward_Per_Block = scrapy.Field()
    Reward_last_24h = scrapy.Field()
    Difficulty = scrapy.Field()
    Hashrate = scrapy.Field()
    Mining_Profitability = scrapy.Field()
    Top_100_Richest = scrapy.Field()
    Wealth_Distribution = scrapy.Field()
    Addresses_richer_than = scrapy.Field()
    Active_Addresses_last_24h = scrapy.Field()
    Largest_Transactions_100 = scrapy.Field()
    First_Block = scrapy.Field()
    Blockchain_Size = scrapy.Field()
    Reddit_subscribers = scrapy.Field()
    Tweets_per_day = scrapy.Field()
    Github_release = scrapy.Field()
    Github_stars = scrapy.Field()
    Github_last_commit = scrapy.Field()


