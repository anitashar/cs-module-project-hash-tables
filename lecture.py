# def my_hash(s):
#     for c in s:
#         print(c)

# my_hash("hello world")

def my_hash(s):
    sb = s.encode()
    total = 0
    for b in sb:
        total +=b
    return total
my_array = [None]*8
print(f'my_array {my_array}')
# print(my_array)

# storing a value
hash_index = my_hash("hello world") % 8 #1116
print(f'hash_index {hash_index}')

my_array[hash_index] = 'my value'
print(f'my_array {my_array}')

# get a value
hash_index = my_hash("hello world") % 8
print(my_array[hash_index])

# deleting a value
hash_index = my_hash("hello world") % 8
my_array[hash_index] = None
print(my_array)

