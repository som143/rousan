# import time
# start = time.process_time()
# lst = []
# for i in range(5):
#     lst.append(i)
# print(lst)
# end = time.process_time()
# print(start-end)
#
# start = time.process_time()
# x = [n for n in range(5)]
# end = time.process_time()
# print(x)
# print(start-end)
import requests
import json
a = requests.get('http://127.0.0.1:8000/customer/')
print(a.json())

print(type(a.json()))