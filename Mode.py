import math as mt


class Mode:
    @staticmethod
    def mostFrequent(arr, n):

        Hash = dict()
        for i in range(n):
            if arr[i] in Hash.keys():
                Hash[arr[i]] += 1
            else:
                Hash[arr[i]] = 1

        # find the max frequency
        max_count = 0
        res = -1
        for i in Hash:
            if max_count < Hash[i]:
                max_count = Hash[i]
        response = []
        place = []
        index = 0
        for i in Hash:
            if max_count == Hash[i]:
                response.append(i)

        if len(response) > 2:
            return None
        elif len(response) == 1:
            return response[0]
        else:
            return response
