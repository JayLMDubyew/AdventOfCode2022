file = open('input.txt', 'r')
items = file.read()
file.close()

elves = items.split("\n\n")


def getmostcals(elves):
    maxval = 0
    for calories in elves:
        calorielist = calories.split("\n")
        totalcal = sum(list(map(int, calorielist)))
        maxval = max(totalcal, maxval)

    return maxval


def rankelvesbycal(elves):
    caloriesum = []
    for calories in elves:
        calorielist = calories.split("\n")
        totalcal = sum(list(map(int, calorielist)))
        caloriesum.append(totalcal)
        # print(caloriesum)
        caloriesum.sort(reverse=True)
    return caloriesum


print(getmostcals(elves))
print(sum(rankelvesbycal(elves)[0:3]))
