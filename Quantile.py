class Quantile:

    @staticmethod
    def quantile(discreteData, p):
        size = len(discreteData)
        discreteData.sort()
        while p > 1:
            p /= 10
        r = int((size + 1) * p)
        w = (size + 1) * p - r
        r -= 1
        quantileP = ((1 - w) * discreteData[r]) + (w * discreteData[r+1])
        return quantileP

