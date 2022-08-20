import queue
import random
from multiprocessing import JoinableQueue, Process
import time


def consumer(q: JoinableQueue):
    while True:
        try:
            res = q.get(block=False)
            print(f'Consume {res}')
            q.task_done()
        except queue.Empty:
            pass


def producer(q: JoinableQueue, food):
    for i in range(2):
        res = f'{food} {i}'
        print(f'Produce {res}')
        q.put(res)
    q.join()


def cpu_task(n):
    start_time = time.perf_counter()
    total = 0
    num = random.randint(0, 9)
    for i in range(10000000):
        total += num
    end_time = time.perf_counter()
    print(
        f" taske {n} completed with sum = { total }, takes {end_time- start_time: 0.2f} second(s)")


if __name__ == "__main__":
    n_jobs = 20

    # foods = ['apple', 'banana', 'melon', 'salad', 'orange', 'grape', 'cherry']

    # q = JoinableQueue()

    # producers = [
    #     Process(target=producer, args=(q, random.choice(foods)))
    #     for _ in range(n_jobs)
    # ]

    # # daemon=True is important here
    # consumers = [
    #     Process(target=consumer, args=(q, ), daemon=True)
    #     for _ in range(n_jobs)
    # ]

    # start_time = perf_counter()

    # # + order here doesn't matter
    # for t in consumers + producers:
    #     t.start()

    # for t in producers:
    #     t.join()

    # end_time = perf_counter()

    # print(f'It took {end_time- start_time: 0.2f} second(s) to complete. ')

    start_time = time.perf_counter()
    proc = Process(target=cpu_task, args=(0,))
    proc.start()
    proc.join()
    end_time = time.perf_counter()

    print(
        f'single-process took {end_time- start_time: 0.2f} second(s) to complete. ')

    procs = []
    start_time = time.perf_counter()

    for i in range(n_jobs):
        proc = Process(target=cpu_task, args=(i,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
    end_time = time.perf_counter()

    print(
        f'multi-process took {end_time- start_time: 0.2f} second(s) to complete. ')
