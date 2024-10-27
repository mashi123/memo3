import random
import string
import time
import pandas as pd

from genlist import gen2dlist


class Dtstore:
    def __init__(self, listnum, strlen):
        self.listnum = listnum
        self.strlen = strlen
        self.dt2d = None
        # self.dtdf = None
        self.gen2dlist()

    def genlist(self, n=5):
        r = []
        for _ in range(n):
            r.append(''.join(random.choice(string.ascii_lowercase +
                     string.digits) for _ in range(self.strlen)))
        return r

    def gen2dlist(self):
        r = []
        for _ in range(self.listnum):
            r.append(self.genlist())

        self.dt2d = r
        self.dtdf = pd.DataFrame(self.dt2d, columns=["a", "b", "c", "d", "e",])

    """
        Return 2d array
    """

    def get2dlist(self):
        return self.dt2d

    """
        Pandas DataFrame
    """

    def getDataFrame(self):
        return self.dtdf


if __name__ == '__main__':
    print(Dtstore(1, 10).get2dlist())
