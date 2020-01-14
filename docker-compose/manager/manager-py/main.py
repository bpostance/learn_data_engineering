#!/usr/bin/env python

"""main.py: Populates database and elasticsearch with wine-data"""

import os
import time
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

print('manager.py is running')
print(f'cwd: {os.getcwd()}')


def connect_to_postgres(server_string,db_name):
    """connect to postgres"""
    engine = create_engine('{}/{}'.format(server_string,db_name))
    connection = engine.connect()
    return connection

try:
    # create db on server
    server_string = "postgresql+psycopg2://postgres:postgres@192.168.1.156:5433"
    db_name = 'db'

    #conn = connect_to_postgres(server_string,'')
    #conn.execute("commit")

    #try:
    #    conn.execute(f"create database {db_name}")
    #except:
    #    pass
    #conn.close()

    # read data 
    df = pd.read_csv('/home/working-dir/data/wine-reviews/winemag-data-130k-v2.csv',index_col=0)

    for attempt in [1,2,3]:
        try:
            # push data to db
            df.to_sql(name='wine_reviews',
                      con=connect_to_postgres(server_string,db_name),
                      index=False,
                      if_exists='replace',
                      chunksize=5000)
        except:
            time.sleep(60)
            print(f'try {attempt}: sleeping')

    print('Upload Data Done')
except Exception as error:
    print(error)
    print('\n\ndb fail')
