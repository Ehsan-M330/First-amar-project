import math
from ContinuousData import Data


class ContinuousData:

    def __init__(self, data):
        self.data = data
        self.data.sort()
        self.table = []
        self.__createTheTable()

    def __createTheTable(self):
        size = len(self.data)
        k = int(1 + 3.2 * math.log10(size)) + 1
        r = (self.data[size - 1]) - (self.data[0])
        w = (r / k)
        firstNum = self.data[0]
        while k > 0:
            temp = Data(firstNum, firstNum + w)
            self.table.append(temp)
            k -= 1
            firstNum += w
        self.__calculateFi()
        self.__calculateRi()
        self.__calculateGi()
        self.__calculateSi()

    def __calculateFi(self):
        size = len(self.data)
        for i in self.table:
            for j in range(size):
                if i.first <= self.data[j] <= i.second:
                    i.fi += 1
                    self.data[j] = -1

    def __calculateRi(self):
        size = len(self.data)
        for i in self.table:
            i.ri = i.fi / size

    def __calculateGi(self):
        size = len(self.table)
        for i in range(size):
            if i == 0:
                self.table[i].gi = self.table[i].fi
                continue
            self.table[i].gi = self.table[i - 1].gi + self.table[i].fi

    def __calculateSi(self):
        size = len(self.table)
        for i in range(size):
            if i == 0:
                self.table[i].si = self.table[i].ri
                continue
            self.table[i].si = self.table[i - 1].si + self.table[i].ri

        # size = len(data)
        # for i in range(size):
        #
        #     data[i].ri = data[i].fi / size
        #     if i != 0:
        #         data[i].gi = data[i].fi + data[i-1].gi
        #         data[i].si = data[i].ri + data[i-1].si
        #     else:
        #         data[i].gi = data[i].fi
        #         data[i].si = data[i].ri
        # return data
