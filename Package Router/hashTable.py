
# ChainingHashTable class houses methods to work with the hash table.
class ChainingHashTable:

    # Initializes the capacity at 10 and Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Method to insert into the hashTable, or updates if item already exists in the table. O(1) time
    # /space complexity.
    def insert(self, key, item):
        bucket = hash(key) % 10
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Tries to locate the item in the hashtable using the inputted key, returns nothing if not found.
    # O(1) space/time complexity.
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    # Locates and removes item from hashtable if it exists. O(1) space/time complexity.
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])




