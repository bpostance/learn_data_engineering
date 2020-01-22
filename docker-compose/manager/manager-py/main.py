#!/usr/bin/env python
"""main.py: Populates database and elasticsearch with wine-data"""

import os
import time
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from elasticsearch import Elasticsearch, helpers

print('manager.py is running')
print(f'cwd: {os.getcwd()}')

def connect_to_postgres(server_string="postgresql+psycopg2://postgres:postgres@192.168.1.156:5433",
                        db_name='db'):
    """connect to postgres"""
    engine = create_engine('{}/{}'.format(server_string,db_name))
    return engine

def create_index(elastic_instance,index_name):
    # create index with settings file
    import json
    with open('./manager-py/elastic-settings.json') as jsfile:
        indexsettings = json.load(jsfile)
    
    try: 
        elastic_instance.indices.create(index=index_name,body=indexsettings)
    except Exception as error:
        print(error)
        pass

def create_db(db_name='db'):
    print("\tcreating db on server")
    try:
        engine = connect_to_postgres(server_string,'')
        conn = engine.connect()
        conn.execute("commit")
        conn.execute(f"\t\tcreate database {db_name}")
        conn.close()
        engine.dispose()
    except:
        print(f'\t\tdb exists: {db_name}')
        pass

def upload_data(db_name='db',index_name='wine-reviews'):
    print("\tuploading data to db...")
    server_string = "postgresql+psycopg2://postgres:postgres@192.168.1.156:5433"
    engine = connect_to_postgres(server_string,db_name)
    conn = engine.connect()

    # read data
    df = pd.read_csv('/home/working-dir/data/wine-reviews/winemag-data-130k-v2.csv',index_col=0)

    # push data to db
    df.to_sql(name='wine_reviews',
                con=conn,
                index=True,
                if_exists='replace',
                chunksize=10000)
    conn.close()
    engine.dispose()
    print("\tdata uploaded to db.")

    # upload to elastic
    print("\tupload to elastic...")
    df.fillna(value=0,inplace=True)
    es = Elasticsearch([{'host':'192.168.1.156','port':9200}])
    
    create_index(es,index_name=index_name)

    actions = [{
                "_index": index_name,
                "_type": "review",
                "_id": k,
                "_source": v['description']
                }
                for k,v in df.to_dict(orient='index').items()]
    helpers.bulk(es, actions)
    print("\tindexed in elastic.")

if __name__ == "__main__":
    create_db()
    upload_data()