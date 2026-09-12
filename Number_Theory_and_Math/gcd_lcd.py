import math

def gcd_lcm(a,b):
    g = math.gcd(a,b)
    l = math.lcm(a,b)
    return g,l

g, l = gcd_lcm(12,18)
print(f"GCD(12,18) = {g}, LCM(12,18) = {l}")
