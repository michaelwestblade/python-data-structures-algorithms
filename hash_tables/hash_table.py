class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is None:
            return None

        for i in range(len(self.data_map[index])):
            if self.data_map[index][i][0] == key:
                return self.data_map[index][i][1]

        return None

    def keys(self):
        all_keys = []
        for outer_index in range(len(self.data_map)):
            if self.data_map[outer_index] is not None:
                for inner_index in range(len(self.data_map[outer_index])):
                    all_keys.append(self.data_map[outer_index][inner_index][0])
        return all_keys

    def print_table(self):
        for i, value in enumerate(self.data_map):
            print(f'{i}: {value}')


hash_table = HashTable()

hash_table.set_item('bolts', 1400)
hash_table.set_item('washers', 50)
hash_table.set_item('lumber', 70)

hash_table.print_table()

print(hash_table.get_item('bolts'))
print(hash_table.get_item('washers'))
print(hash_table.get_item('anything else'))

print(hash_table.keys())


def item_in_common_inneficient(list1, list2):
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True
    return False

def item_in_common(list1, list2):
    key_dict = {}
    for item1 in list1:
        key_dict[item1] = True

    for item2 in list2:
        if item2 in key_dict:
            return True

    return False

list1 = [1,3,5]
list2 = [2,4,5]

print(item_in_common(list1, list2))
