def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

def solve(N):
    import time
    import random
    rng = random.Random()   # Instantiate a generator
    start_time = time.time()
    bd = list(range(N))     # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10 :
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd):
           print("{2}x{2} problem: Found solution {0} in {1} tries.".format(bd, tries, N))
           tries = 0
           num_found += 1
    end_time = time.time()
    print(end_time - start_time)

def main():
    for N in [4, 12, 16]:
        solve(N)

main()