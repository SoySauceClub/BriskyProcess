__author__ = 'Daniel'

import pandas
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement

cluster = Cluster()
session = cluster.connect("briskyprocess")
query = session.prepare("insert into stockdata (stock_id, time, open_price, high_price, low_price, close_price, volumne, adj_close) values(?, ?, ?, ?, ?, ?, ?, ?)")
batch = BatchStatement()

csvData = pandas.io.parsers.read_csv('Data/sampleData.csv', sep=',', skiprows=1)
for index, row in csvData.iterrows():
    batch.add(
        query, ('AAPL', pandas.to_datetime(row[0]), row[1], row[2], row[3], row[4], row[5], row[6])
    )
session.execute(batch)

result = session.execute("Select * from stockdata")
print(result)
