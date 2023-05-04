# hashtable.py
from typing import NamedTuple, Any

class Pair(NamedTuple):
    key: Any
    value: Any

class HashTable:
    def __init__(self, capacity):
        '''Create an empty hash table sized by capacity'''
        self._pairs = capacity * [None]

    def _index(self, key):
        '''Uses Python hash function to hash and 
           contrain resulting value within size of table'''
        return hash(key) % len(self._pairs)

    def __iter__(self):
        '''Allows hash table keys to be iterated over using a loop'''
        yield from self.keys

    def __len__(self):
        '''Return length of occupied spaces in hash table'''
        return len(self.pairs)
    
    def __contains__(self, key):
        '''Returns True if a key exists in hash table'''
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True
        
    def __setitem__(self, key, value):
        ''' 1. Turn an arbitrary key into a numeric hash value
            2. Use the modulo op to constrain the resulting index within the space
            3. Assign the value to the table at the new index'''
        index = self._index(key)
        self._pairs[index] = Pair(key, value)  # Uses namedtuple

    def __delitem__(self, key):
        '''Deletes an item from hash table if key exists in table'''
        index = self._index(key)
        if key in self:  # Calls on contains method
            self._pairs[index] = None
        else:
            raise KeyError(key)

    def __getitem__(self, key):
        '''Retrieve a value from the hash table with indexing notation'''
        index = self._index(key)
        pair = self._pairs[index]
        if pair is None:
            raise KeyError(key)
        return pair.value

    def get(self, key, default=None):
        '''Return value from hash table'''
        try:
            return self[key]
        except KeyError:
            return default

    # These are getters that will avoid accessing the table data directly
    @property
    def values(self):
        '''Access and return values from hash table'''
        return [pair.value for pair in self.pairs]

    @property
    def pairs(self):
        '''Access pairs and filter out any instances of None'''
        return {pair for pair in self._pairs if pair}

    @property
    def keys(self):
        '''Access and return keys from hash table'''
        return {pair.key for pair in self.pairs}

    @property
    def capacity(self):
        '''Returns total capacity of hash table'''
        return len(self._pairs)
    

def main():
    # Create instance of HashTable
    table = HashTable(100)

    # Add different types of values to table
    table['hola'] = 'hello'
    table[True] = False
    table[37.5] = 75

    # Print pairs, keys, and values
    print(table.pairs)
    print(table.keys)
    print(table.values)

    # Test __contains__ method
    print('hola' in table)

    # Test get method
    print(table.get(37.5))

    # Be able to get by indexing
    print(table[37.5])

    # Delete an item from the hash table
    del table['hola']
    print('hola' in table)

    # Check initial capacity of hash table
    print(table.capacity)

if __name__ == '__main__':
    main()

