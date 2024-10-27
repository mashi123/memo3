import random
import string
import time
import pandas as pd

tmarray = []
STRLEN = 10
DTLISTNUM = 100000


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


if __name__ == '__main__':
    save_tm("st")
    array = gen2dlist(1000000)
    save_tm("1")

    df = pd.DataFrame(array, columns=["a", "b", "c", "d", "e",])
    save_tm("2")

#    print(df.to_json(orient='records'))
#    save_tm("3")

    # existOrNot = df.apply(lambda x: x.str.contains('.*a.*', regex=True), axis=1)
    # existOrNot = df['a'].map(lambda x: "aaaaaaaaaaa" in x)
    # print(existOrNot)
    print("before:" + str(time.time()))
    d = df[((df.a.str.contains('.*a.*', regex=True)) | (df.b.str.contains('.*a.*',
            regex=True)) | (df.c.str.contains('.*a.*', regex=True)))]
    print("after:" + str(time.time()))
    # print(d)
    save_tm("4")

    # print(df[existOrNot])
    save_tm("5")

    out_tm()
