def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    Length=[]
    if L==[]:
        return float('NaN')
        
    else:
        for str in L:
            Length.append(len(str))
        X=Length    
        mean = sum(X)/float(len(X))
        tot = 0.0
        for x in X:
            tot += (x - mean)**2
        return (tot/len(X))**0.5
