#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _mysql
import time
table_name = "sent_message"

def get_max(db, init = 0):
    db.query("""SELECT id FROM %s order by id desc limit 1
             """ % (table_name))

    r=db.store_result()

    row= r.fetch_row()
    return int(row[0][0])

# ======= main start ===========
if __name__ == "__main__":
    max = 100
    cons = [];
    for i in range(0, max):
        db=_mysql.connect(db="test")
        cons.append(db)
        print "%dth conntion" % i

    while 1:
        time.sleep(10000)
