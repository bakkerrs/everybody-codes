with open("./quest 2/part 1.txt", "r") as raw_input:
    wordline, inscription = raw_input.read().split("\n\n")
    words = wordline.split(":")[1].split(",")

count = 0
for word in words:
    num = inscription.count(word)
    count += num

print(count)