from Average import Average


class Variance:

    @staticmethod
    def variance(discreteData):
        average = Average.average(discreteData)
        numberMinusAverage = 0
        for number in discreteData:
            numberMinusAverage += pow(number - average, 2)
        return numberMinusAverage / (len(discreteData) - 1)
