import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import csv

# connect to PostgreSQL
conn = 'postgresql://thh:root@127.0.0.1:61157/postdb'

db_connection = create_engine(conn)

csv_file_paths = ["C:\\Users\\huyho\\OneDrive\\Desktop\\Postgres\\hrloc.csv", "C:\\Users\\huyho\\OneDrive\\Desktop\\Postgres\\hrjbtl.csv", "C:\\Users\\huyho\\OneDrive\\Desktop\\Postgres\\humres.csv"]
table_names = ["hrloc", "hrjbtl", "humres"]

for csv_file_path, table_name in zip(csv_file_paths, table_names):
    df = pd.read_csv(csv_file_path, low_memory=False)

    # Convert from DataFrame to DB PostgreSQL
    df.to_sql(table_name, db_connection, index=False, if_exists='replace')

# close connection
db_connection.dispose()
