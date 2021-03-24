# murmur3 hashing
import mmh3
import math


def optimal_hash_count(size, element_count):
    return int(math.ceil((size / element_count) * math.log(2.0)))


def optimal_bit_size(falsePositiveProbability, element_count):
    return int(math.ceil((-1.0 * element_count * math.log(falsePositiveProbability)) / math.pow(math.log(2.0), 2.0)))


class BloomFilter:
    def __init__(self, bit_count=8, hash_count=4):
        self.bit_count = bit_count
        self.hash_count = hash_count
        self.seeds = range(hash_count)
        self.bit_field = [0 for x in range(math.ceil(bit_count/8))]

    def add(self, value):
        # Hash value hash_count times and set the correct bit to 1
        for idx in range(self.hash_count):
            hashed_result = mmh3.hash(value, self.seeds[idx])
            position = hashed_result % self.bit_count

            byte_position = int(position/8)
            bit_mask = 1 << (position % 8)

            self.bit_field[byte_position] |= bit_mask

    def exists(self, value):
        for idx in range(self.hash_count):
            hashed_result = mmh3.hash(value, self.seeds[idx])
            position = hashed_result % self.bit_count

            byte_position = int(position/8)
            bit_mask = 1 << (position % 8)

            # If there there is one bit that doesn't match, we are sure that the value isn't present
            # This is where we can get a false positive (if two value share the same bit signature)
            if self.bit_field[byte_position] & bit_mask == 0:
                return False

        return True

    def clear(self):
        self.bit_field = [0 for x in range(self.bit_count)]
