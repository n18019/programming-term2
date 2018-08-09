import time
start_time = time.time()
print(start_time)
data = list(map(lambda x : x * 2, range(1000000)))
end_time = time.time()
print(end_time)
execution_time = end_time - start_time
print(execution_time)
