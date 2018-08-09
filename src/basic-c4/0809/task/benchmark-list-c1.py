import time
start_time = time.time()
print(start_time)
data = []
for i in range(1000000):
    data.append(i * 2)
end_time = time.time()
print(end_time)
execution_time = end_time - start_time
print(execution_time)
