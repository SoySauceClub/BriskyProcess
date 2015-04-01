
CREATE KEYSPACE briskyprocess WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': '1'
};

USE briskyprocess;
CREATE TABLE briskyprocess.stockdata (
  stock_id text,
  time timestamp,
  adj_close double,
  close_price double,
  high_price double,
  low_price double,
  open_price double,
  volumne double,
  PRIMARY KEY (stock_id, time)
) WITH CLUSTERING ORDER BY (time ASC) AND
  bloom_filter_fp_chance=0.010000 AND
  caching='KEYS_ONLY' AND
  comment='' AND
  dclocal_read_repair_chance=0.100000 AND
  gc_grace_seconds=864000 AND
  read_repair_chance=0.000000 AND
  replicate_on_write='true' AND
  populate_io_cache_on_flush='false' AND
  compaction={'class': 'SizeTieredCompactionStrategy'} AND
  compression={'sstable_compression': 'LZ4Compressor'};
