def solution (S):
    count=0
    N=len(S)
    i=0
    while i < N:
        if S[i] == "X":
            count += 1
            i+= 2
        else:i+= 1
        return count
    print (solution(".X..XX"))
