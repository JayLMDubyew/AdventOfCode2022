

losedrawwin = {'X': ['B', 'A', 'C'], 'Y': ['C', 'B', 'A'], 'Z': ['A', 'C', 'B']}
points = {'X': 1, 'Y':2, 'Z':3}
score = 0

with open("input.txt", 'r') as input:
    for thisRound in input.readlines():
        them, me = thisRound.split()
        pointsToAdd = points[me] + (losedrawwin[me].index(them) * 3)
        score = score + pointsToAdd


print(score)

