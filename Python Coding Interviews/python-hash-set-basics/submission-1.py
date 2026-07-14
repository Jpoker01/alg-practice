from typing import List, Set


def build_hash_set(keys: List[str]) -> Set[str]:
    hash_set = {key for key in keys}
    return hash_set
    


def check_keys(hash_set: Set[str], keys: List[str]) -> List[bool]:
    element_match_list = [True if key in hash_set else False for key in keys]
    return element_match_list

# do not modify below this line

output1 = build_hash_set(["Alice", "Bob", "Charlie"])
print(type(output1))         # check the type of the output
print(sorted(list(output1))) # set order is not guaranteed so we need to sort the list

output2 = build_hash_set(["XY", "XX", "YY", "XY", "YX"]) 
print(type(output2))         # check the type of the output
print(sorted(list(output2))) # set order is not guaranteed so we need to sort the list

print(check_keys({"Alice", "Bob", "Charlie"}, ["Alice", "Bob", "Charlie", "David"]))
print(check_keys({'a', 'b', 'c'}, ['a', 'd', 'c']))
print(check_keys({'a', 'c'}, ['d', 'c']))
