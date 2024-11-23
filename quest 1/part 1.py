
with open("./quest 1//part 1.txt", "r") as raw_input:
    input = raw_input.read()

potions = 0
for monster in input:
    match monster:
        case "A": continue
        case "B": potions += 1
        case "C": potions += 3
print(potions)