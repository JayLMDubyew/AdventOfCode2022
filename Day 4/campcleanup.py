filename = 'input.txt'


# yes, i know my style is changing. It's a good opportunity to play around.

def get_complete_overlaps(file_name: str) -> int:
    overlaps = 0
    with open(file_name) as sections:
        for pairings in sections.readlines():
            assignment = pairings.strip().split(',')
            a, b = assignment[0].split('-')
            c, d = assignment[1].split('-')
            onea, oneb, twoa, twob = int(a), int(b), int(c), int(d)

            if (onea <= twoa) and (oneb >= twob):
                overlaps = overlaps + 1
            elif (twoa <= onea) and (twob >= oneb):
                overlaps = overlaps + 1
            else:
                continue

    return overlaps


def get_any_overlaps(file_name: str) -> int:
    overlaps = 0
    with open(file_name) as sections:
        for pairings in sections.readlines():
            assignment = pairings.strip().split(',')
            a, b = assignment[0].split('-')
            c, d = assignment[1].split('-')
            onea, oneb, twoa, twob = int(a), int(b), int(c), int(d)

            first_range = range(onea, oneb+1, 1)
            second_range = range(twoa, twob+1, 1)
            if (onea in second_range) or (oneb in second_range):
                overlaps = overlaps + 1
            elif (twoa in first_range) or (twob in first_range):
                overlaps = overlaps + 1
            else:
                continue
    return overlaps


print(f"result for part 1: {get_complete_overlaps(filename)}")
print(f"result for part 2: {get_any_overlaps(filename)}")
