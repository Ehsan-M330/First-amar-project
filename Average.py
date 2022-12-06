class Average:

    @staticmethod
    def average(data):
        sum = 0
        for number in data:
            sum += number

        return sum / len(data)
