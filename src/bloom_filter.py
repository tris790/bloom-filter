# murmur3 hashing
import mmh3


class BloomFilter:
    def __init__(self, bit_count=8, hash_count=4):
        self.bit_count = bit_count
        self.hash_count = hash_count
        self.seeds = range(hash_count)
        self.bit_field = [0 for x in range(bit_count)]

    def Add(self, value):
        for idx in range(self.hash_count):
            hashed_result = mmh3.hash(value, self.seeds[idx])
            position = hashed_result % self.bit_count
            self.bit_field[position] = 1

    def Exists(self, value):
        for idx in range(self.hash_count):
            hashed_result = mmh3.hash(value, self.seeds[idx])
            position = hashed_result % self.bit_count
            if self.bit_field[position] == 0:
                return False
        return True
