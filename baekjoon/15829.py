# Bronze 2

L = int(input())
string = list(input().strip())
index_word = "abcdefghijklmnopqrstuvwxyz"
mod = 1234567891
hash_number = 0
for l in range(L):
    temp = index_word.index(string[l]) + 1
    hasp_part = (temp * (31**l)) % mod
    hash_number += hasp_part
    if hash_number >= mod:
        hash_number -= mod

print(hash_number)