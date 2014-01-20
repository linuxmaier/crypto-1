import random

k = ''
while (len(k) < 5):
    k += str(random.randint(0, 1))

def prf(key, message):
    return_string = ''
    for char in message:
        t = key[0]
        for i in range(1,4):
            if (message[i-1] == 1):
                t = t ^ k[i]
        return_string += t
    return return_string

