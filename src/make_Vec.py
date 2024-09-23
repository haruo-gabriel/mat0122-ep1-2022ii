from vec import Vec
from int2GF2 import int2GF2

def make_Vec(primeset, factors):
    factors_set = {x:int2GF2(y) for (x,y) in factors} 
    return Vec(primeset, factors_set)

if __name__ == "__main__":
    print(make_Vec({2,3,5,7,11}, [(2,17), (3,0), (5,1), (11,3)]))