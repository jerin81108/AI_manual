traits = ["Croaks", "Sings", "Green", "Yellow"]
species = ["Frog", "Canary"]

print("=== Backward Chaining Logic ===\n1. Frog\n2. Canary")
choice = int(input("Select a Goal (1-2): ")) - 1

if choice in (0, 1):
    c = int(input(f"Checking {species[choice]}...\nIs it: 1. Green or 2. Yellow? ")) - 1
    if c == choice:
        print(f"Goal Confirmed: It is a {species[choice]}.\nVerified: {traits[choice+2]} and will {traits[choice]}")
    else:
        print("Goal Failed: Knowledge does not match.")
else:
    print("Invalid Selection.")