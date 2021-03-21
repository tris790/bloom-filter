import bloom_filter
import tracemalloc
import time

print("---------------- Bloom filters benchmark ----------------")

words = []
with open("words.txt") as f:
    words = f.read().splitlines()
print(f"Loaded: {len(words)} words")

tracemalloc.start()
print("Creating the bloom filter data structure")
start_time = time.time_ns()
bf = bloom_filter.BloomFilter(64, 3)

print(f"Adding {len(words)} elements")
for word in words:
    bf.add(word)

end_time = time.time_ns()
elapsed_time = end_time - start_time
print(f"Time to add all elements: {elapsed_time}ns")

print(f"Looking up every element")
start_time = time.time_ns()
for word in words:
    if bf.exists(word) == False:
        print(f"Error: {word} wasn't found")

end_time = time.time_ns()
elapsed_time = end_time - start_time
print(f"Time to know if the elements were present: {elapsed_time}ns")

current, peak = tracemalloc.get_traced_memory()
print(
    f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()
