import tracemalloc
import time


def bench_set(file_path):
    print("---------------- Set benchmark ----------------")

    words = []
    with open(file_path) as f:
        words = f.read().splitlines()
    print(f"Loaded: {len(words)} words")

    tracemalloc.start()
    print("Creating the set data structure")
    start_time = time.time_ns()
    set_struct = set([])

    print(f"Adding {len(words)} elements")
    for word in words:
        set_struct.add(word)

    end_time = time.time_ns()
    elapsed_time = end_time - start_time
    print(f"Time to add all elements: {elapsed_time}ns ({elapsed_time / 1000000}ms)")

    start_time = time.time_ns()
    for word in words:
        if word not in set_struct:
            print(f"Error: {word} wasn't found")

    end_time = time.time_ns()
    elapsed_time = end_time - start_time
    print(f"Time to know if the elements were present: {elapsed_time}ns ({elapsed_time / 1000000}ms)")

    print(f"Clearing the set")
    start_time = time.time_ns()
    set_struct.clear()
    end_time = time.time_ns()
    elapsed_time = end_time - start_time
    print(f"Clearing the set took: {elapsed_time}ns ({elapsed_time / 1000000}ms)")

    current, peak = tracemalloc.get_traced_memory()
    print(
        f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()
