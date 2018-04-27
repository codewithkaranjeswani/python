def inverse(here):
    inverse = []
    det = determinant(here)
    for f in range(len(here)):
        temp = []
        for g in range(len(here[f])):
            temp.append(0)
        inverse.append(temp)
    
    for i in range(len(here)):
        for j in range(len(here[i])):
            if (i + j) % 2 == 0:
                inverse[j][i] = 1 / det * determinant(submatrix(here, i, j))
            else:
                inverse[j][i] = -1 / det * determinant(submatrix(here, i, j))
    return inverse

def submatrix(hi, i, j):
    eleven = []
    for f in range(len(hi)):
        temp = []
        for g in range(len(hi[f])):
            temp.append(hi[f][g])
        eleven.append(temp)

    del eleven[i]
    for h in range(len(eleven)):
        del eleven[h][j]

    return eleven

def determinant(thatone):
# evaluating determinant using first row ie. row number 0
    if len(thatone) == 1:
        return thatone[0][0]
    else:
        ans = 0
        for i in range(len(thatone[0])):
            if i % 2 == 0:
                ans += thatone[0][i] * determinant(submatrix(thatone, 0, i))
            else:
                ans -= thatone[0][i] * determinant(submatrix(thatone, 0, i))
    return ans

def transpose(samehere):
# len(samehere[0]) give the number of columns in the matrix
# len(samehere) gives the number of rows in the matrix
    thisone = []
    for j in range(len(samehere[0])):
        temp = []
        for i in range(len(samehere)):
            temp.append(samehere[i][j])
        thisone.append(temp)
    return thisone

def display(taking):
    for i in range(len(taking)):
        for j in range(len(taking[i])):
            print(repr(taking[i][j]).rjust(5), end=" ")
        print()

def main():
    given = [[2, -1,  0],
             [1,  2,  3],
             [-4, 1, -1]]
    detval = determinant(given)
    inversed = inverse(given)

    print('\nGiven matrix:')
    display(given)
    print()
    print('determinant = ' + str(detval))
    print()
    print('Inverse:')
    print()
    display(inversed)
    
if __name__ == '__main__':
        main()
