import numpy as np


arr = [1, 1, 0, -1, -1]
counters = [0, 0, 0]
# for e in arr:
#     if e>0:
#         counters[0] += 1
#     elif e < 0:
#         counters[1] += 1
#     elif e == 0:
#         counters[2] += 1
#
# print(format( counters[0] / len(arr), '.5f'))
#
# print(format( counters[1] / len(arr), '.5f'))
#
# print(format( counters[2] / len(arr), '.5f'))


print(len([x for x in arr if x < 0]) / len(arr))
print(len([x for x in arr if x > 0]) / len(arr))
print(len([x for x in arr if x == 0]) / len(arr))
