__author__ = 'Daniel'

import pandas
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement

def loadDataIntoDatabase(stockId, dbSession):
    "save data to databaes"
    query = dbSession.prepare("insert into stockdata (stock_id, time, open_price, high_price, low_price, close_price, volumne, adj_close) values(?, ?, ?, ?, ?, ?, ?, ?)")
    batch = BatchStatement()
    csvData = pandas.io.parsers.read_csv('Data/sampleData.csv', sep=',', skiprows=1)
    for index, row in csvData.iterrows():
        batch.add(
            query, (stockId, pandas.to_datetime(row[0]), row[1], row[2], row[3], row[4], row[5], row[6])
        )
    dbSession.execute(batch)
    print("save data for stock:" + stockId)
    return

cluster = Cluster()
session = cluster.connect("briskyprocess")
#loadDataIntoDatabase("GOOG", session)
#loadDataIntoDatabase("MSFT", session)
#loadDataIntoDatabase("ORCL", session)
#loadDataIntoDatabase("IBM", session)
#loadDataIntoDatabase("SAP", session)
#loadDataIntoDatabase("SNE", session)
#loadDataIntoDatabase("VOXX", session)
#loadDataIntoDatabase("ADBE", session)
#loadDataIntoDatabase("CSCO", session)
result = session.execute("Select count(*) from stockdata limit 200000")
print(result)
