import bloom_filter

print("---------------- Bloom filters test ----------------")
print("Creating the bloom filter data structure")
bf = bloom_filter.BloomFilter(8, 5)

val1 = "Monkey"
val2 = "Computer"

print(f"Making sure that the word '{val1}' isn't in the bloom filter yet")
print(f"'{val1}' exists? {bf.exists(val1)}")

print(f"\nAdding the word '{val1}' to the bloom filter")
bf.add(val1)

print(f"\nMaking sure the word '{val1}' is present in the bloom filter")
print(f"'{val1}' exists? {bf.exists(val1)}")

print(f"\nMaking sure the word'{val2}' isn't present in the bloom filter")
print(f"'{val2}' exists? {bf.exists(val2)}")
