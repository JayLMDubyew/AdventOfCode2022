import string
import itertools
import more_itertools

from collections import defaultdict

priorities = {}
def populate_priorities():
    priority = 1
    for letter in string.ascii_letters:
        priorities[letter] = priority
        priority = priority + 1

def get_dupe_priority(items: str) -> int:
    combined_priorities = 0
    compartment_size = len(items)//2
    first_compartment, second_compartment = items[:compartment_size], items[compartment_size:]
    #print(first_compartment, second_compartment)

    for i in set(first_compartment):
        if i in second_compartment:
            combined_priorities = combined_priorities + priorities[i]


    return combined_priorities

populate_priorities()

with open("input.txt") as input:
    totalPriority = 0
    for i in input.readlines():
        totalPriority = totalPriority + get_dupe_priority(i)
    print(totalPriority)


with open("input.txt") as input:
    items = input.readlines()
    badgeTotal = 0
    for chunk in range(0,len(items),3):
       one = set(items[chunk].strip())
       two = set(items[chunk+1].strip())
       three = set(items[chunk+2].strip())

       badgeTotal = badgeTotal + priorities[one.intersection(two, three).pop()]
    print(badgeTotal)



