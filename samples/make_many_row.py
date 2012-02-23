#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _mysql
table_name = "simples"

def get_max(db, init = 0):
    db.query("""SELECT id FROM %s order by id desc limit 1
             """ % (table_name))

    r=db.store_result()

    row= r.fetch_row()
    return int(row[0][0])

# ======= main start ===========

db=_mysql.connect(host="127.0.0.1", port=5000, db="clusterdb", user="root")

total = 100000000

start = get_max(db, 0)
end = start + total

cnt = 1;
for i in range(start, end):
    cnt = cnt + 1
    if cnt % 10000 == 0: print cnt
    db.query("""INSERT INTO %s(data) VALUES(
            'data_%d'
        )
         """ % (table_name, i))

db.query("""SELECT count(*) FROM %s
         """ % (table_name))

r=db.use_result()

row = r.fetch_row()
num = r.num_rows()

print row[0][0] 

