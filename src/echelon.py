# Copyright 2013 Philip N. Klein
from vec import Vec
import GF2
from vecutil import list2vec

def transformation_rows(rowlist_input, col_label_list = None):
    """Given a matrix A represented by a list of rows
        optionally given the unit field element (1 by default),
        and optionally given a list of the domain elements of the rows,
        return a matrix M represented by a list of rows such that
        M A is in echelon form
    """
    #one = GF2.one # replace this with 1 if working over R or C
    one = GF2.one
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
    #print(zero_vec)
    for s in new_M_rowlist:
        #print(s)
        if s == zero_vec:
            zero_count += 1

    return new_M_rowlist, zero_count

def main():
    #v1 = list2vec([0,GF2.one, GF2.one])
    #v2 = list2vec([0, 0, GF2.one])
    v1 = list2vec([0,0,0])
    v2 = list2vec([0, 0, 0])
    v3 = list2vec([0, 0, 0])
    r, z = transformation_rows([v1,v2,v3])
    print(f"z = {z}")
    print()
    for i in r:
        print(i)


if __name__ == "__main__":
    main()
