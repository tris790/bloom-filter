import tracemalloc
import time

print("---------------- Set benchmark ----------------")

words = []
with open("words.txt") as f:
    words = f.read().splitlines()
print(f"Loaded: {len(words)} words")

tracemalloc.start()
start_time = time.time_ns()
print("Creating the set data structure")
set_struct = set([])

print(f"Adding {len(words)} elements")
for word in words:
    set_struct.add(word)

current, peak = tracemalloc.get_traced_memory()
print(
    f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()
end_time = time.time_ns()
elapsed_time = end_time - start_time
print(f"Total time: {elapsed_time}ns")
