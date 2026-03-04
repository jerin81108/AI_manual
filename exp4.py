def is_safe(region, color, assignment, edges):
    for u, v in edges:
        if (u == region and assignment.get(v) == color) or \
           (v == region and assignment.get(u) == color):
            return False
    return True

def solve(regions, colors, edges, assignment):
    if len(assignment) == len(regions):
        return assignment
    # Get the first unassigned region
    unassigned = [r for r in regions if r not in assignment][0]
    
    for color in colors:
        if is_safe(unassigned, color, assignment, edges):
            assignment[unassigned] = color
            
            # Recurse
            if solve(regions, colors, edges, assignment):
                return assignment
                
            # Backtrack
            del assignment[unassigned]
            
    return None

regions = ["WA", "NT", "SA", "Q", "NSW", "VIC", "T"]
colors = ["red", "green", "blue"]
edges = [("WA", "NT"), ("WA", "SA"), ("SA", "NT"), ("Q", "NT"), ("Q", "SA"), 
         ("Q", "NSW"), ("NSW", "SA"), ("VIC", "SA"), ("VIC", "NSW"), ("VIC", "T")]

print("Solution:", solve(regions, colors, edges, {}))