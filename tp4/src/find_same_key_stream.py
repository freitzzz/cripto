from data import *


def used_same_key_stream(l1, l2):
    zip_list = zip(l1, l2)

    return next((x for x in zip_list if int(x[0] ^ x[1]) >= 128), None) == None


packets_using_same_key_stream = set()

for i in range(0, len(packets)):
    for j in range(i+1, len(packets)):
        if(used_same_key_stream(packets[i], packets[j])):
            packets_using_same_key_stream.add(i)
            packets_using_same_key_stream.add(j)

packets_using_same_key_stream = sorted(packets_using_same_key_stream)

print('Found the following packets using the same keystream: (# -> index)')
for x in packets_using_same_key_stream:
    print('Packet: #{}'.format(x))
