__author__ = 'Daniel'

from cassandra.cluster import Cluster
import timeit

def SelectAllTest():
    cluster = Cluster()
    session = cluster.connect("briskyprocess")
    "select all test"
    result = session.execute("select stock_id, time, open_price, high_price, low_price,close_price,volumne, adj_close from stockdata limit 200000 ALLOW FILTERING")

def SelectOneTest():
    cluster = Cluster()
    session = cluster.connect("briskyprocess")
    "select one test"
    result = session.execute("select stock_id, time, open_price, high_price, low_price,close_price,volumne, adj_close from stockdata where stock_id = 'IBM' limit 200000 ALLOW FILTERING")

def SelectAllByTimeRangeTest():
    cluster = Cluster()
    session = cluster.connect("briskyprocess")
    "select all by time range test"
    result = session.execute("select stock_id, time, open_price, high_price, low_price,close_price,volumne, adj_close from stockdata where time >= '1990-01-01' and time <= '2016-01-01' limit 200000 ALLOW FILTERING")

def SelectOneByTimeRangeTest():
    cluster = Cluster()
    session = cluster.connect("briskyprocess")
    "select one by time range test"
    result = session.execute("select stock_id, time, open_price, high_price, low_price,close_price,volumne, adj_close from stockdata where stock_id = 'IBM'and time >= '1990-01-01' and time <= '2016-01-01' limit 200000 ALLOW FILTERING")

numberOfRepeat = 10
print("Repeat select all 10 times")
print(timeit.timeit("SelectAllTest()", setup = "from __main__ import SelectAllTest", number = numberOfRepeat))

print("Repeat select one 10 times")
print(timeit.timeit("SelectOneTest()", setup = "from __main__ import SelectOneTest", number = numberOfRepeat))

print("Repeat select all by time range 10 times")
print(timeit.timeit("SelectAllByTimeRangeTest()", setup = "from __main__ import SelectAllByTimeRangeTest", number = numberOfRepeat))


print("Repeat select one by time range 10 times")
print(timeit.timeit("SelectOneByTimeRangeTest()", setup = "from __main__ import SelectOneByTimeRangeTest", number = numberOfRepeat))

print("Benchmark execute finish")
