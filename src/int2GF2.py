from GF2 import one

def int2GF2(x): return 0 if x%2 == 0 else one

if __name__ == "__main__":
    print(int2GF2(10))