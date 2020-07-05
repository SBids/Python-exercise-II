# 20. Write a Python class to find the three elements that sum to zero  from a list of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]


class TripletsZero:

    def __init__(self, real_list):
        self.real_list = real_list

    def find_triplets(self):
        results = []
        arr_size = len(self.real_list)
        for i in range(0, arr_size - 2):
            for j in range(i + 1, arr_size - 1):
                for k in range(j + 1, arr_size):
                    if self.real_list[i] + self.real_list[j] + self.real_list[k] == 0:
                        results.append([self.real_list[i], self.real_list[j], self.real_list[k]])

        for result in results:
            result.sort()

        output = [list(x) for x in set(tuple(x) for x in results)]
        return output


input_array = [-25, -10, -7, -3, 2, 4, 8, 10]
find_num = TripletsZero(input_array)
print(find_num.find_triplets())

