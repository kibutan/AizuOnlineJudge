from decimal import Decimal
import math
x1,y1,x2,y2 = list(map(int,input().split()))
print(Decimal( math.sqrt(  (Decimal(x2)-Decimal(x1))**2 + ( Decimal(y2)-Decimal(y1) )**2  ))) 
