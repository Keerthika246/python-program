def insert(L, x):
    """
    insert an element x into a sorted list L

    Arguments:
        L: list
        x: integers
    Return:
        sorted_L: list
    """
   
    sorted_L = L[:]
  
    for i in range(len(sorted_L)):
      if sorted_L[i] > x:
          sorted_L.insert(i, x)
          return sorted_L
    
    sorted_L.append(x)
    return sorted_L
