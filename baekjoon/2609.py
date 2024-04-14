import math
a, b = map(int, input().split())
gcd = math.gcd(a, b)
lcm = math.lcm(a, b)
print(gcd)
print(lcm)