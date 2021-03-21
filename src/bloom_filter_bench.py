import bloom_filter
import tracemalloc
import time


print("---------------- Bloom filters benchmark ----------------")

words = []
with open("words.txt") as f:
    words = f.read().splitlines()
print(f"Loaded: {len(words)} words")

tracemalloc.start()
start_time = time.time_ns()
print("Creating the bloom filter data structure")
bf = bloom_filter.BloomFilter(64, 5)

print(f"Adding {len(words)} elements")
for word in words:
    bf.add(word)

current, peak = tracemalloc.get_traced_memory()
print(
    f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()
end_time = time.time_ns()
elapsed_time = end_time - start_time
print(f"Total time: {elapsed_time}ns")
