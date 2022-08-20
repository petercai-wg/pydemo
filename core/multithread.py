
# example of one producer and multiple consumers with threads
# multi-thread has better performance than multi-process
from concurrent.futures import process
import time
import random
from threading import Thread
from queue import Queue
import numpy as np
from multiprocessing import Process, Pool, cpu_count
import os

# # producer task
# def producer(q, food):
#     # generate items
#     for i in range(2):
#         res = f'{food} {i}'
#         print(f'Produce {res}')
#         q.put(res)


# # consumer task
# def consumer(q):
#     while True:
#         res = q.get()
#         print(f'Consumer got {res}')
#         if res is None:
#             # add the signal back for other consumers
#             q.put(res)
#             # stop running
#             break


# foods = ['apple', 'banana', 'melon', 'salad', 'orange', 'grape', 'cherry']
# n_jobs = 20

# start_time = time.perf_counter()

# # create the shared queue
# queue = Queue()

# consumers = []
# for n in range(n_jobs):
#     t = Thread(target=consumer, args=(queue,))
#     t.setDaemon(True)
#     consumers.append(t)
#     t.start()

# # start the producer
# producers = [Thread(target=producer,  args=(
#     queue, random.choice(foods))) for _ in range(n_jobs)]


# for p in producers:
#     p.start()

# for p in producers:
#     p.join()

# queue.put(None)
# print('Done')

# for consumer in consumers:
#     consumer.join()
# end_time = time.perf_counter()

# print(f'It took {end_time- start_time: 0.2f} second(s) to complete. ')


print(f" system cpu {cpu_count()}, os cpu: { os.cpu_count() }")
n_jobs = 20


def cpu_task(n):
    start_time = time.perf_counter()
    total = 0
    num = random.randint(0, 9)
    for i in range(10000000):
        total += num
    end_time = time.perf_counter()
    print(
        f" taske {n} completed with sum = { total }, takes {end_time- start_time: 0.2f} second(s)")


start_time = time.perf_counter()

cpu_task(0)
end_time = time.perf_counter()

print(
    f'single task call took {end_time- start_time: 0.2f} second(s) to complete. ')


threads = []
start_time = time.perf_counter()

for i in range(n_jobs):
    t = Thread(target=cpu_task, args=(i,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

end_time = time.perf_counter()

print(
    f'Multi threads (non-parallel) took {end_time- start_time: 0.2f} second(s) to complete. ')
