import time
import numpy as np

numbers = list(np.random.randint(low = 1, high = 10, size = 100000))
numbers_array = np.array(numbers)
numbers_tuple = tuple(numbers)
start_time = time.time()

for i, number in enumerate(numbers):
    number_is_in_tail = number in numbers[i+1:]
print("--- %s секунд у алгоритма 1 (список с простым перебором) ---" % (time.time() - start_time))

start_time = time.time()
number_is_in_tail = [(True,i,number)  for i,number in enumerate(numbers) if  number in numbers[i+1:]]
print("--- %s секунд у алгоритма 2 (список с перебором через генератор списков) ---" % (time.time() - start_time))

start_time = time.time()
for i, number in enumerate(numbers_array):
    number_is_in_tail = number in numbers_array[i+1:]
print("--- %s секунд у алгоритма 3 (массив с простым перебором)---" % (time.time() - start_time))   

start_time = time.time()
number_is_in_tail = [(True,i,number)  for i,number in enumerate(numbers_array) if  number in numbers_array[i+1:]]
print("--- %s секунд у алгоритма 4 (массив с перебором через генератор списков)---" % (time.time() - start_time))   

start_time = time.time()
for i, number in enumerate(numbers_tuple):
    number_is_in_tail = number in numbers_tuple[i+1:]
print("--- %s секунд у алгоритма 5 (кортеж с простым перебором)---" % (time.time() - start_time))   

start_time = time.time()
number_is_in_tail = [(True,i,number)  for i,number in enumerate(numbers_tuple) if  number in numbers_tuple[i+1:]]
print("--- %s секунд у алгоритма 6 (кортеж с перебором через генератор списков)---" % (time.time() - start_time))  
