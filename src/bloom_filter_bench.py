import bloom_filter
import tracemalloc
import time

print("---------------- Bloom filters benchmark ----------------")

words = []
with open("words.txt") as f:
    words = f.read().splitlines()
print(f"Loaded: {len(words)} words")

desired_false_prob = 0.01
size = bloom_filter.optimal_bit_size(desired_false_prob, len(words))
hash_count = bloom_filter.optimal_hash_count(size, len(words))
print(f"{desired_false_prob} error => {size} bits and {hash_count} hash")

tracemalloc.start()
print("Creating the bloom filter data structure")
start_time = time.time_ns()
bf = bloom_filter.BloomFilter(size, hash_count)

print(f"Adding {len(words)} elements")
for word in words:
    bf.add(word)

end_time = time.time_ns()
elapsed_time = end_time - start_time
print(f"Time to add all elements: {elapsed_time}ns ({elapsed_time / 1000000000}s)")

print(f"Looking up every element")
start_time = time.time_ns()
for word in words:
    if bf.exists(word) == False:
        print(f"Error: {word} wasn't found")

end_time = time.time_ns()
elapsed_time = end_time - start_time
print(f"Time to know if the elements were present: {elapsed_time}ns ({elapsed_time / 1000000000}s)")

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(
    f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")

print(f"Clearing the bloomfilter")
bf.clear()

print(f"Validating the error count")
errorCount = 0
for word in words:
    if bf.exists(word) == True:
        errorCount += 1
    bf.add(word)

print(f"There was {errorCount} error(s) [error rate: {errorCount / len(words)}]")
