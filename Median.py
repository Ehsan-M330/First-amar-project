class Median:

    @staticmethod
    def median(discreteData):
        size = len(discreteData)
        discreteData.sort()
        print(size)
        print(discreteData)
        if size % 2 == 1:
            return discreteData[int((size - 1) / 2)]
        else:
            return (discreteData[int(size / 2)] + discreteData[int(size / 2 - 1)]) / 2

