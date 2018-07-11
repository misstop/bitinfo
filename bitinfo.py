from  scrapy import  cmdline
import random
import time
import os
import json
import subprocess

CYCLE_TIME = 1 * 60

# cmdline.execute("scrapy crawl huobipro.com".split())
spiders = 'bit bitno'.split(' ')


cmd = 'scrapy crawl {}'

i = 0
while True:
    for s in spiders:
        subprocess.Popen(cmd.format(s), shell=True if os.name == 'posix' else False)
    i += 1
    print("第{}轮执行".format(i))
    time.sleep(CYCLE_TIME)
