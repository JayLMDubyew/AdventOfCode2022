
losedrawwin = ['X', 'Y', 'Z']
opposition_ldw = {'A':['S','R','P'], 'B':['R','P','S'], 'C':['P','S','R']}
points = {'R': 1, 'P':2, 'S':3}
score = 0

with open("input.txt", 'r') as input:
    for thisRound in input.readlines():
        them, me = thisRound.split()
        roundresult = losedrawwin.index(me)
        picks = opposition_ldw[them]
        weapon = picks[roundresult]
        pickPoints = points[weapon]
        print(f"{roundresult * 3}+{pickPoints}")
        pointsToAdd = pickPoints + (roundresult * 3)
        score = score + pointsToAdd

print(score)

