with open("./quest 1/part 3.txt", "r") as raw_input:
    input = raw_input.read()


potions = 0
for i in range(0, len(input), 3):
    battle = input[i:i+3]
    for monster in battle:
        match monster:
            case "A": continue
            case "B": potions += 1
            case "C": potions += 3
            case "D": potions += 5
    
    match battle.count('x'):
        case 0: potions += 6
        case 1: potions += 2
        case 2: potions += 0

print(potions)