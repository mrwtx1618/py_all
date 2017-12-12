
import datetime
the_time = datetime.datetime.fromtimestamp(1496405874)
print(the_time)
import timeit


import numpy as np
import random
def the_test_time_np_sort():
    the_list = [random.randint(1,200) for i in range(100)]
    (sorted(the_list))
the_list = []
for i in range(10):

    print(timeit.timeit('the_test_time_np_sort()','from __main__ import the_test_time_np_sort',number = 100000))
    the_list.append(timeit.timeit('the_test_time_np_sort()','from __main__ import the_test_time_np_sort',number = 100000))
print(sum(the_list))