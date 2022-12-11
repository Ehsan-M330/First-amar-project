class Cal:

    @staticmethod
    def average(data):
        sum = 0
        for number in data:
            sum += number

        return sum / len(data)

    @staticmethod
    def variance(discreteData):
        average = Cal.average(discreteData)
        numberMinusAverage = 0
        for number in discreteData:
            numberMinusAverage += pow(number - average, 2)
        return numberMinusAverage / (len(discreteData) - 1)

    @staticmethod
    def quantile(discreteData, p):
        size = len(discreteData)
        discreteData.sort()
        while p > 1:
            p /= 10
        r = int((size + 1) * p)
        w = (size + 1) * p - r
        r -= 1
        quantileP = ((1 - w) * discreteData[r]) + (w * discreteData[r + 1])
        return quantileP

    @staticmethod
    def mode(arr):
        n = len(arr)
        Hash = dict()
        for i in range(n):
            if arr[i] in Hash.keys():
                Hash[arr[i]] += 1
            else:
                Hash[arr[i]] = 1

        max_count = 0
        for i in Hash:
            if max_count < Hash[i]:
                max_count = Hash[i]
        response = []
        for i in Hash:
            if max_count == Hash[i]:
                response.append(i)

        if len(response) > 2:
            return None
        elif len(response) == 1:
            return response[0]
        else:
            return response

    @staticmethod
    def medianD(discreteData):
        size = len(discreteData)
        discreteData.sort()
        print(size)
        print(discreteData)
        if size % 2 == 1:
            return discreteData[int((size - 1) / 2)]
        else:
            return (discreteData[int(size / 2)] + discreteData[int(size / 2 - 1)]) / 2

    @staticmethod
    def medianC(continuousData, size, w):
        i = 0
        while i < len(continuousData):
            if continuousData[i].si >= 0.5:
                break
            i += 1

        if i != 0:
            return continuousData[i].first + ((0.5 * size - continuousData[i - 1].gi) * w) / continuousData[i].fi

    @staticmethod
    def modeC(continuousData, w):
        maxFi = 0
        i = 0
        for j in range(continuousData):
            if maxFi < continuousData[j].fi:
                i = j
                maxFi = continuousData[j].fi

        lm = continuousData[i].first
        d1 = continuousData[i].fi - continuousData[i - 1].fi
        d2 = continuousData[i].fi - continuousData[i + 1].fi

        return lm + (d1 / (d1 + d2)) * w

    @staticmethod
    def quantileC(continuousData, w, n, p):
        i = 0
        while p > 1:
            p /= 10
        for j in range(continuousData):
            if p >= continuousData[j].si:
                i = j
                break
        lp = continuousData[i].first
        gp = continuousData[i - 1].gi
        fp = continuousData[i].fi

        return lp + ((n * p - gp) * w) / fp

    @staticmethod
    def boxPlotC(continuousData, size, w):
        q2 = Cal.medianC(continuousData, size, w)
        q1 = Cal.quantileC(continuousData, w, size, 25)
        q3 = Cal.quantileC(continuousData, w, size, 75)
        iqr = q3 - q1
        minNum = q1 - 1.5 * iqr
        maxNum = q3 + 1.5 * iqr
        print(' -----------------')
        print('|                 |')
        print('|                 |')
        print(' -----------------')
        print(minNum, q1, q2, q3, maxNum)

    @staticmethod
    def boxPlotD(data):
        q1 = Cal.quantile(data, 25)
        q2 = Cal.medianD(data)
        q3 = Cal.quantile(data, 75)
        iqr = q3 - q1
        minNum = q1 - 1.5 * iqr
        maxNum = q3 + 1.5 * iqr
        print(' -----------------')
        print('|                 |')
        print('|                 |')
        print(' -----------------')
        print(minNum, q1, q2, q3, maxNum)
