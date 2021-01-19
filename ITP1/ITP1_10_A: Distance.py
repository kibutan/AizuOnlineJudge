from decimal import Decimal
import math
x1,y1,x2,y2 = list(map(Decimal,input().split()))
print('{:.8f}'.format( Decimal( math.sqrt(  (Decimal(x2)-Decimal(x1))**2 + ( Decimal(y2)-Decimal(y1) )**2  ))))
