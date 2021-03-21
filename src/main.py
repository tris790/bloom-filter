import bloom_filter

print("hello world!")
bf = bloom_filter.BloomFilter()
val1 = "test1"
val2 = "test2"
print(f"'{val1}' exists? {bf.Exists(val1)}")
bf.Add(val1)
print(f"'{val1}' exists? {bf.Exists(val1)}")
print(f"'{val2}' exists? {bf.Exists(val2)}")
