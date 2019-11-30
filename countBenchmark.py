import time
start_time = time.time()

for i in range(0, 100000001):
    print(i)

print("--- %s seconds ---" % (time.time() - start_time))