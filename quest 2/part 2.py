with open("./quest 2/part 2.txt", "r") as raw_input:
    wordline, inscription = raw_input.read().split("\n\n")
    words = wordline.split(":")[1].split(",")
    inscriptions = inscription.split("\n")

count = 0


# Not correct
for line in inscriptions:
    for word in words:
        num = line.count(word) + line[::-1].count(word)
        count += num

print(count)