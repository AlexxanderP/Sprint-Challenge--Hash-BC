#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)


    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)

    for i in range(len(weights)):
        new_value = limit - weights[i]
        checker = None

        if hash_table_retrieve(ht, new_value):
            checker = i
            new_value = hash_table_retrieve(ht, new_value)

            if checker > new_value:
                return (checker, new_value)
            else:
                return (new_value, checker)



    return None


