# -*- coding: utf-8 -*-

import time
import psycopg2
import logging
import datetime
from elasticsearch import Elasticsearch
from elasticsearch import NotFoundError
import config

# 通过下面的方式进行简单配置输出方式与日志级别
# logging.basicConfig(filename='infoq_indexer.log', level=logging.INFO)
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)

CategoryLiteral = {
        "article":"文章",
        "carbon":"碳积分",
        "realestate":"房产",
        "insurance":"保险",
        "proof":"证明"
        }
def get_category_literal(category):
    return CategoryLiteral[category]

class MyETL():
    def __init__(self, db_host, db_port, db_name, db_user, db_passwd):
        self.conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_passwd)
        self.cur = self.conn.cursor()
        self.indexClient = Elasticsearch(
                config.ES_HOSTS,
                sniff_on_start=True,
                sniff_on_connection_fail=True,
                sniff_timeout=60)

    def process(self):
        try:
            # 获取应用条目的总数
            self.cur.execute("SELECT count(1) FROM asset")
            row = self.cur.fetchone()
            totalNum = int(row[0])
            logging.info("Assets Total Num: {0}".format(totalNum))

            # 计算pageNum
            pageSize = 100
            pageNum = 0
            if totalNum > 0 and totalNum <= pageSize:
                pageNum = 1
            elif totalNum % pageSize != 0:
                pageNum = int(totalNum / pageSize) + 1
            else:
                pageNum = int(totalNum / pageSize)

            logging.debug("pageNum={0}".format(pageNum))

            # 分页读取企业条目
            for i in range(pageNum):
                self.cur.execute("""SELECT asset_did,
                                        asset_name,
                                        intro,
                                        metadata,
                                        endpoint,
                                        tags,
                                        owner_did,
                                        owner_name,
                                        source,
                                        category,
                                        tx_id,
                                        hash,
                                        doc_id,
                                        valuation,
                                        visibility,
                                        updated_at
                                        FROM asset
                                        ORDER BY created_at
                                        LIMIT {0} OFFSET {1}
                                        """.format(pageSize, i * pageSize))
                rows = self.cur.fetchall()
                for row in rows:
                   asset_did = row[0]

                   try:
                       res = self.indexClient.get(index=config.IndexName, id=asset_did)
                       if res['found']:
                           logging.debug("{0} has already indexed".format(asset_did))
                           continue
                   except NotFoundError:
                           logging.debug("{0} has not indexed".format(asset_did))

                   docInfo = {"asset_did": asset_did,
                       "name": row[1],
                       "intro": row[2],
                       "metadata": row[3],
                       "endpoint": row[4],
                       "tags": row[5],
                       "owner_did": row[6],
                       "owner_name": row[7],
                       "source": row[8],
                       "category": row[9],
                       "category_literal": get_category_literal(row[9]),
                       "tx_id": row[10],
                       "hash": row[11],
                       "doc_id": asset_did,
                       "valuation": row[13],
                       "visibility": row[14],
                       "updated_at": int(row[15].strftime("%s"))}
                   logging.debug("{0}".format(docInfo))

                   res = self.indexClient.index(
                       index=config.IndexName,
                       id=asset_did,
                       body=docInfo)
                   logging.debug("create index {0} result: {1}".format(asset_did, res['result']))
                   time.sleep(1)

        except Exception as err:
            logging.error(err)

def main():
    etl = MyETL(config.DB_HOST, config.DB_PORT, config.DB_NAME, config.DB_USER, config.DB_PASSWD)

    oldtime=datetime.datetime.now()

    etl.process()

    newtime=datetime.datetime.now()

    logging.info('elapsed time: {0}'.format(newtime-oldtime))

if __name__=="__main__":
    main()

