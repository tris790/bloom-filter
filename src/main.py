import bloom_filter_bench
import set_bench

file_path = "10_000.txt"
bloom_filter_bench.bench_bloomfilter(file_path)
set_bench.bench_set(file_path)
