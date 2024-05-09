import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import csv

# connect to PostgreSQL
conn = 'postgresql://thh:root@127.0.0.1:5432/postdb'

db_connection = create_engine(conn)

csv_file_paths = ["C:\\Users\\Huy Hoang\\Desktop\\Postgres\\hrloc.csv", "C:\\Users\\Huy Hoang\\Desktop\\Postgres\\hrjbtl.csv", "C:\\Users\\Huy Hoang\\Desktop\\Postgres\\humres.csv"]
table_names = ["hrloc", "hrjbtl", "humres"]

for csv_file_path, table_name in zip(csv_file_paths, table_names):
    df = pd.read_csv(csv_file_path, low_memory=False)
    #create table in PostgreSQL
    df.head(0).to_sql(table_name, db_connection, index=False, if_exists='replace')  #truncates the table
    # Convert from DataFrame to DB PostgreSQL
    df.to_sql(table_name, db_connection, index=False, if_exists='replace')

# close connection
db_connection.dispose()
