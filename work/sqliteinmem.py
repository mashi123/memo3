import random
import string
import time
import pandas as pd
import sqlite3

tmarray = []
DTLISTNUM = 10
STRLEN = 10


def save_tm(id):
    tmarray.insert(0, (id, time.time()))


def out_tm():
    print("\n")
    for i in range(len(tmarray) - 1):
        print(f'{tmarray[i][0]}: {tmarray[i][1] - tmarray[i+1][1]}')


def genlist(n=5):
    r = []
    for _ in range(n):
        r.append(''.join(random.choice(string.ascii_lowercase + string.digits)
                 for _ in range(STRLEN)))

    return r


def gen2dlist(m=DTLISTNUM):
    r = []
    for _ in range(m):
        r.append(genlist())

    return r


con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE test(AA, BB, CC, DD, EE)")

list2d = gen2dlist(1000000)
save_tm("1")

con.executemany(
    "INSERT INTO test(AA, BB, CC, DD, EE) VALUES(?, ?, ?, ?, ?)", list2d)
save_tm("2")

print("before:" + str(time.time()))
cursor = con.execute(
    'SELECT * from test WHERE AA LIKE ? or BB LIKE ? or CC LIKE ?', ('%a%', '%a%', '%a%'))
a = cursor.fetchall()
print("after :" + str(time.time()))
save_tm("3")

out_tm()
