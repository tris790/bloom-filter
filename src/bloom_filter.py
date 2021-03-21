# murmur3 hashing
import mmh3


class BloomFilter:
    def __init__(self, bit_count=8, hash_count=4):
        self.bit_count = bit_count
        self.hash_count = hash_count
        self.seeds = range(hash_count)
        self.bit_field = [0 for x in range(bit_count)]

    def add(self, value):
        # Hash value hash_count times and set the correct bit to 1
        for idx in range(self.hash_count):
            hashed_result = mmh3.hash(value, self.seeds[idx])
            position = hashed_result % self.bit_count
            self.bit_field[position] = 1

    def exists(self, value):
        for idx in range(self.hash_count):
            hashed_result = mmh3.hash(value, self.seeds[idx])
            position = hashed_result % self.bit_count

            # If there there is one bit that doesn't match, we are sure that the value isn't present
            # This is where we can get a false positive (if two value share the same bit signature)
            if self.bit_field[position] == 0:
                return False

        return True

    def clear(self):
        self.bit_field = [0 for x in range(self.bit_count)]
