# Bronze 4
from collections import Counter

array = list(map(int, input().strip().split()))

counter = Counter(array)

if len(counter) == 3:
    print(max(array)*100)
    exit()

if len(counter) == 2:
    for key, value in counter.items():
        if value == 2:
            print(1000+100*key)
    exit()
if len(counter) == 1:
    print(10000 + array[0]*1000)
    exit()