import time
from collections import Counter
import math
def ent(message):
    letters = 0
    ent = 0
    a = list(Counter(message).values())
    for letters in a:
        freq = letters/len(message)
        log2 = math.log2(freq) * freq
        ent = ent + log2
    return -ent
def file():
    f = open('ent.txt')
    data = f.read()
    return(data)
start_time = time.time()
doc = file()
print(doc)
print(ent(doc))
print("--- %s seconds ---" % (time.time() - start_time))
