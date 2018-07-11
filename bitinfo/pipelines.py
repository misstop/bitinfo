import json, yaml, os, logging, datetime, time

from kafka import KafkaProducer

# 解析yaml
cur_path = os.path.dirname(os.path.realpath(__file__))
x = yaml.load(open('%s/config.yml' % cur_path))
kafka_con = x['QUEUES']['KAFKA']['HOST']
kafka_topic = x['QUEUES']['KAFKA']['topic']


# 时间戳转换为时间
def cur_time():
    now = datetime.datetime.now()
    cur_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return cur_time


# 13位时间戳
def cur_timest():
    t1 = time.time()
    t2 = int(t1) * 1000
    return t2


# 连接kafka
producer = KafkaProducer(bootstrap_servers=kafka_con, value_serializer=lambda v: json.dumps(v).encode('utf-8'))


class BitinfoPipeline(object):

    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=kafka_con, api_version=(0, 10, 1),
                                     value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def process_item(self, item, spider):
        d = dict(item)
        # time.sleep(1)
        if d:
            dic = {
                "type": 1,
                "explain": "INFO_CHARTS",
                "createTime": cur_timest(),
                "infoData": d,
            }
            self.producer.send(kafka_topic, dic)
            self.producer.flush()
            logging.info('success to kafka--%s' % spider.name)
            print('success to kafka--%s' % spider.name)
        else:
            logging.info("msg is null --%s" % spider.name)

