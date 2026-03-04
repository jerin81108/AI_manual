from itertools import permutations

def solve_cryptarithmetic():
    # Iterate over all possible 9-digit combinations for our variables
    for p in permutations(range(10), 9):
        c, r, o, s, a, d, n, g, e = p
        
        if c == 0 or r == 0 or d == 0:
            continue
            
        cross = 10000*c + 1000*r + 100*o + 10*s + s
        roads = 10000*r + 1000*o + 100*a + 10*d + s
        danger = 100000*d + 10000*a + 1000*n + 100*g + 10*e + r
  
        # Check if the sum holds true
        if cross + roads == danger:
            return cross, roads, danger           
    return "No solution found"
print(solve_cryptarithmetic())
