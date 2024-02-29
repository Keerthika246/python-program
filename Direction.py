def final(n, moves):
    """
    Compute the final position
    
    Argument:
        n: int
        moves: string
    Return:
        (x, y): tuple
    """
    
    pos_x, pos_y = 1, 1
    
    for direction in moves:
        if direction == 'N' and pos_y < n:
          pos_y += 1
        elif direction == 'E' and pos_x < n:
          pos_x += 1
        elif direction == 'S' and pos_y > 1:
          pos_y -= 1
        elif direction == 'W' and pos_x > 1:
          pos_x -= 1
          
    return(pos_x, pos_y)     
