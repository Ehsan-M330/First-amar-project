import math
from ContinuousData import Data
from tkinter import *
from Calculation import Cal


class ContinuousData:

    def __init__(self, data):
        self.data = data
        self.data.sort()
        self.w = 0
        self.size = len(data)
        self.table = []
        self.__createTheTable()

    def calculateW(self):
        k = int(1 + 3.2 * math.log10(self.size)) + 1
        r = (self.data[self.size - 1]) - (self.data[0])
        return r / k

    def __createTheTable(self):
        size = len(self.data)
        k = int(1 + 3.2 * math.log10(size)) + 1
        r = (self.data[size - 1]) - (self.data[0])
        self.w = r / k
        firstNum = self.data[0]
        while k > 0:
            temp = Data(firstNum, firstNum + self.w)
            self.table.append(temp)
            k -= 1
            firstNum += self.w
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

    def printTheTable(self):
        print('first', 'second', 'xi', 'fi', 'ri', 'ji', 'si')
        for i in self.table:
            print(f"{i.first:.2f}", f"{i.second:.2f}", f"{i.xi:.2f}", i.fi, f"{i.ri:.2f}", i.gi, f"{i.si:.2f}")

    def calculateModeC(self):
        return Cal.modeC(self.table, self.calculateW())

    def calculateQuantileC(self, p):
        return Cal.quantileC(self.table, self.w, len(self.data), p)

    def calculateMedianC(self):
        return Cal.medianC(self.table, self.size, self.w)
