with open("./quest 1//part 2.txt", "r") as raw_input:
    input = raw_input.read()


potions = 0
for i in range(0, len(input), 2):
    pair = input[i:i+2]
    pots = 0
    for monster in pair:
        match monster:
            case "A": continue
            case "B": pots += 1
            case "C": pots += 3
            case "D": pots += 5
    if "x" not in input[i:i+2]:
        pots += 2
    
    potions += pots

print(potions)