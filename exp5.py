def dpll(clauses, symbols, model={}):
    # Base cases: success (no clauses left) or failure (empty clause exists)
    if not clauses: return model
    if any(not c for c in clauses): return False

    P = symbols[0]
    rest = symbols[1:]

    # Path 1: Assume P is True
    # Remove clauses with P, and remove "-P" from remaining clauses
    true_clauses = [[l for l in c if l != f"-{P}"] for c in clauses if P not in c]
    res = dpll(true_clauses, rest, {**model, P: True})
    if res: return res

    # Path 2: Assume P is False
    # Remove clauses with "-P", and remove "P" from remaining clauses
    false_clauses = [[l for l in c if l != P] for c in clauses if f"-{P}" not in c]
    return dpll(false_clauses, rest, {**model, P: False})


# --- Execution ---
KB = [['A', 'B'], ['A', '-C'], ['-A', 'B', 'D']]

# Extract unique variables cleanly without importing Regex
symbols = list({lbl.lstrip('-') for clause in KB for lbl in clause})

print("Result:", dpll(KB, symbols))