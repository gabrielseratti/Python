def convert_hash_to_array(hash):
    print(sorted(map(list, hash.items())))


convert_hash_to_array({name: 'Jeremy', 'age': 24, 'role': 'Software Engineer'})