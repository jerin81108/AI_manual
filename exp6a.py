facts = ["Croaks", "Eat Flies", "Shrimps", "Sings"]
animals, colors = ["Frog", "Canary"], ["Green", "Yellow"]

print("\n".join(f"{i+1}. {f}" for i, f in enumerate(facts)))
x = int(input("Select Fact (1-4): ")) - 1

if 0 <= x <= 3:
    idx = 0 if x < 2 else 1
    print(f"Chance of: {animals[idx]}\nSelected Fact: {facts[x]}")
    k = int(input("Select Color (1. Green, 2. Yellow): ")) - 1
    
    if k == idx:
        print(f"Confirmed! It is a {animals[idx]} and color is {colors[idx]}.")
    else:
        print("Invalid Knowledge Database Match.")
else:
    print("Invalid Option.")