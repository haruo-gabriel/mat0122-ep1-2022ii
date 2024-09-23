#------------------------------------------------------------------------------
# # MAT0122 ÁLGEBRA LINEAR I
# Aluno: <GABRIEL HARUO HANAI TAKEUCHI>
# Numero USP: <13671636>
# Tarefa: <EP1>
# Data: <16/12/2022>
# 
# Baseado em ... (breve e se aplicável)
# 
# DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESTE PROGRAMA.  TODAS AS 
# PARTES DO PROGRAMA, EXCETO AS QUE SÃO BASEADAS EM MATERIAL FORNECIDO  
# PELO PROFESSOR OU COPIADAS DO LIVRO OU DO MATERIAL DIDÁTICO DE MAT0122, 
# FORAM DESENVOLVIDAS POR MIM.  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS 
# AS CÓPIAS DESTE PROGRAMA E QUE NÃO DISTRIBUÍ NEM FACILITEI A DISTRIBUIÇÃO
# DE CÓPIAS DESTA PROGRAMA.
#------------------------------------------------------------------------------

import sys
import GF2
from GF2 import one
from vec import Vec
from factoring_support import intsqrt, dumb_factor, primes, prod, gcd

def int2GF2(x): return 0 if x%2 == 0 else one


def make_Vec(primeset, factors):
    return Vec(primeset, {x:int2GF2(y) for (x,y) in factors})


def find_candidates(N, primeset):
    roots = []
    rowlist = []

    len_primeset = len(primeset) + 1
    len_roots = 0
    x = intsqrt(N) + 2

    while len_roots < len_primeset:
        factors_of_x = dumb_factor(x**2 - N, primeset)
        if factors_of_x: # returns True if x can be factored completely over primeset i.e. if the list is not empty
            roots.append(x)
            len_roots += 1
            rowlist.append(make_Vec(primeset, factors_of_x))
        x += 1

    return roots, rowlist


def transformation_rows(rowlist_input, col_label_list = None):
    """Given a matrix A represented by a list of rows
        optionally given the unit field element (1 by default),
        and optionally given a list of the domain elements of the rows,
        return a matrix M represented by a list of rows such that
        M A is in echelon form
    """
    one = GF2.one # replace this with 1 if working over R or C
    rowlist = list(rowlist_input)
    if col_label_list == None: col_label_list = sorted(rowlist[0].D, key=repr)
    m = len(rowlist)
    row_labels = set(range(m))
    M_rowlist = [Vec(row_labels, {i:one}) for i in range(m)]
    new_M_rowlist = []
    rows_left = set(range(m))
    for c in col_label_list:
        rows_with_nonzero = [r for r in rows_left if rowlist[r][c] != 0]
        if rows_with_nonzero != []:
            pivot = rows_with_nonzero[0]
            rows_left.remove(pivot)
            new_M_rowlist.append(M_rowlist[pivot])
            for r in rows_with_nonzero[1:]:
                multiplier = rowlist[r][c]/rowlist[pivot][c]
                rowlist[r] -= multiplier*rowlist[pivot]
                M_rowlist[r] -= multiplier*M_rowlist[pivot]
    for r in rows_left: new_M_rowlist.append(M_rowlist[r])
    # return new_M_rowlist

    # count the new matrix's zero vecs
    zero_count = 0
    zero_vec = Vec(new_M_rowlist[0].D, {x:0 for x in new_M_rowlist[0].D})
    for s in new_M_rowlist:
        if s == zero_vec:
            zero_count += 1

    return new_M_rowlist, zero_count


def find_a_and_b(v, roots, N):
    alist = [roots[x] for x in v.D if v[x] != 0]
    a = prod(alist)
    c = prod([x**2 - N for x in alist])
    b = intsqrt(c)
    assert (b**2 == c)
    return a, b


def main():
    modo_verborragico = 0

    # Inputs
    len_inputs = len(sys.argv)
    N = int(sys.argv[1]) 
    U = int(sys.argv[2]) if len_inputs >= 3 else 10000
    if len_inputs >= 4:
        modo_verborragico = 1 

    # Execution
    primelist = primes(U)
    roots, rowlist = find_candidates(N, primelist)
    M_rows, n_zero_rows = transformation_rows(rowlist, sorted(primelist, reverse=True))
    len_M_rows = len(M_rows) 

    for i in reversed(range(len_M_rows)): 
        a, b = find_a_and_b(M_rows[i], roots, N)
        
        if modo_verborragico == 1:
            print(f"{len_M_rows - i - 1}: a = {a} / b = {b}")

        n_zero_rows -= 1
        gcdiv = gcd(a - b, N)
        if gcdiv == 1:
            print("Failed")
            break
        elif gcdiv != N:
            print(f"factor = {gcdiv}")
            break


if __name__ == "__main__":
    main()
