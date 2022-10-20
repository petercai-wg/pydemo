##  This compare python thread vs process

# 1. find out system CPU
import multiprocessing
import os
import time
import datetime
import  concurrent.futures 

print("CPU #",multiprocessing.cpu_count(), os.cpu_count())

def sleep_task(seconds):
    print(f"{datetime.datetime.now()} : sleeping {seconds} seconds .....")
    time.sleep(seconds)
    result = f"{datetime.datetime.now()} : done sleeping {seconds}"
    print( result)
    return result

start_time = time.perf_counter()

# The asynchronous execution using ThreadPoolExecutor with threads, OR using ProcessPoolExecutor with separate processes
# concurrent.futures.ProcessPoolExecutor is a wrapper around a multiprocessing.Pool.

# with concurrent.futures.ProcessPoolExecutor() as executor:
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = [ executor.submit(sleep_task, i ) for i in range(6, 0, -1) ]

#     for f in concurrent.futures.as_completed(results):
#         print(f.result())

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     sleep_seconds = [6,5,4,3,2,1]
#     results = executor.map(sleep_task, sleep_seconds )
#     for result in results:
#         print(result)

procs = []
start_time = time.perf_counter()

for i in range(6,0, -1):
    proc = multiprocessing.Process(target=sleep_task, args=[i])
    procs.append(proc)
    proc.start()

for proc in procs:
    proc.join()


print(f"Finished in {round( time.perf_counter() - start_time , 2) } seconds ")



