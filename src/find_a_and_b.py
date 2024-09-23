from factoring_support import prod, intsqrt, gcd
from GF2 import one
from vec import Vec

def find_a_and_b(v, roots, N):
    #print(f"v = {v}")
    alist = [roots[x] for x in v.D if v[x] != 0]
    #print(f"alist = {alist}")
    # alist = [v.f[k] for k in v.D if v.f[k] != 0]
    a = prod(alist)
    c = prod({x*x - N for x in alist})
    b = intsqrt(c)
    assert b*b == c
    return (a,b)


if __name__ == "__main__":
    x = find_a_and_b( Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},{0: 0, 1: 0, 10: one, 2: one}), [51, 52, 53, 58, 61, 62, 63, 67, 68, 71, 77, 79], 2419)
    print("(a,b) = a,b")
    print(gcd(x[0] - x[1], 2419))