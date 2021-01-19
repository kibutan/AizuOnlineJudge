import math
from decimal import Decimal
a,b,c = list(map(int,input().split()))
s = Decimal(a * b * Decimal(math.sin(math.radians(c))) / 2)
l = Decimal(a + b + Decimal( math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(c)))))
h = b*math.sin(math.radians(c))
print(s)
print(l)
print(h)
