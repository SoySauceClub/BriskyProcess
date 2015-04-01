__author__ = 'Daniel'

from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect("briskyprocess")
result = session.execute("Select * from stockdata")
print(result)