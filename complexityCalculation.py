import time
import sys
import os
import psutil

def time_estimator(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

def memory_estimator(func, *args, **kwargs):
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss / 1024.0 / 1024.0  # Convert bytes to MB
    result = func(*args, **kwargs)
    mem_after = process.memory_info().rss / 1024.0 / 1024.0
    return mem_after - mem_before

def complexity_estimator(func, input_generator, n_values):
    times = []
    memory = []
    for n in n_values:
        input_data = input_generator(n)
        elapsed_time = time_estimator(func, *input_data)
        mem_used = memory_estimator(func, *input_data)
        times.append(elapsed_time)
        memory.append(mem_used)
    return times, memory


# Example Usage - Copy in Separate File

from complexity_estimator import complexity_estimator

def example_function(data):
    s = sum(data)
    return s

def input_gen(n):
    return ([i for i in range(n)],)

n_values = [10**i for i in range(1, 7)]
times, memory = complexity_estimator(example_function, input_gen, n_values)

print("N-values:", n_values)
print("Times:", times)
print("Memory (MB):", memory)
