import math
a,b = map(int, input().split())
ap,bp = math.lgamma(a + 1)/math.log(10),math.lgamma(b + 1)/math.log(10)
o = math.gcd(int(ap)+1,int(bp)+1)
print(o,ap,bp)