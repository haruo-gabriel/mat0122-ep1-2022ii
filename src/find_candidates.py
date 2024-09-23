from factoring_support import primes, intsqrt, dumb_factor
from make_Vec import make_Vec

def find_candidates(N, primeset):
    roots = []
    rowlist = []

    #print(primeset)

    len_primeset = len(primeset) + 1
    x = intsqrt(N)+2

    while len(roots) < len_primeset:
        factors_of_x = dumb_factor(x**2 - N, primeset)
        #print(f"x = {x}")
        #print(f"factors_of_x = {factors_of_x}")
        if factors_of_x: # returns True if x can be factored completely over primeset i.e. if the list is not empty
            roots.append(x)
            rowlist.append(make_Vec(primeset, factors_of_x))
        x += 1

    # print(len(roots) == len(primeset)+1)

    return roots, rowlist

if __name__ == "__main__":
    x,y = find_candidates(2419, primes(32))

    print(x,"\n")
    for i in range(len(y)):
        print(y[i])


