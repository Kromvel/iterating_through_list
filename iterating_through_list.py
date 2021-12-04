import timeit

code_to_test = """
import numpy as np
numbers = list(np.random.randint(low = 1, high = 10, size = 100000))
for i, number in enumerate(numbers):
    number_is_in_tail = number in numbers[i+1:]
"""

code_to_test_2 = """
import numpy as np
numbers = list(np.random.randint(low = 1, high = 10, size = 100000))
number_is_in_tail = [True if number in numbers[i+1:] else False for i, number in enumerate(numbers)]
"""
elapsed_time = timeit.timeit(code_to_test, number=3)
elapsed_time_2 = timeit.timeit(code_to_test_2, number=3)

if __name__ == "__main__":
  print('elapsed_time:    ' + str(elapsed_time))
  print('elapsed_time_2:  ' + str(elapsed_time_2))
