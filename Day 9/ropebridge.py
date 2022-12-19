filename = "test2.txt"
import numpy as np


# T and H must touch. diagonal, adjacent, or overlapping.

def check_and_move_tail(head, tail, isX):
    x_diff = head[0]-tail[0]
    y_diff = head[1]-tail[1]
    diff = list(np.subtract(head, tail))
    if diff[1] > 1 and abs(diff[0]) == 1:
    #    print("woooo")
        if diff[0] < 0:
            tail[0] -= 1
        else:
            tail[0] += 1
        tail[1] += 1
    elif diff[1] < -1 and abs(diff[0]) == 1:
    #    print("woooo")
        if diff[0] < 0:
            tail[0] -= 1
        else:
            tail[0] += 1
        tail[1] -= 1
    elif diff[0] > 1 and abs(diff[1]) == 1:
      #  print("weee?")
        tail[0] += 1
        if diff[1] < 0:
            tail[1] -= 1
        else:
            tail[1] += 1
    elif diff[0] < -1 and abs(diff[1]) == 1:
     #   print("weee?")
        tail[0] -= 1
        if diff[1] < 0:
            tail[1] -= 1
        else:
            tail[1] += 1
    else:
        if diff[0] > 1:
            tail[0] += 1
        if diff[0] < -1:
            tail[0] -= 1
        if diff[1] > 1:
            tail[1] += 1
        if diff[1] < -1:
            tail[1] -= 1
   # print(diff)
    diff = list(np.subtract(head, tail))
  #  print(diff)

    return tail

def move_head(instructions):
    unique_coord = set()
    current_head_coord = [0, 0]
    current_tail_coord = [0, 0]


    unique_coord.add(tuple(current_tail_coord))
    print(unique_coord)
    for instruction in instructions:
        direction, times = instruction.split()[0], int(instruction.split()[1])
        print("******")
        print(direction, times)

        match direction:
            case 'L':
                for _ in range(times):
                    current_head_coord[0] -= 1
                    current_tail_coord = check_and_move_tail(current_head_coord, current_tail_coord, True)
                    unique_coord.add(tuple(current_tail_coord))
                    print(f"head: {current_head_coord} tail: {current_tail_coord}")
                    print("----")

                #subtract x
            case 'R':
                for _ in range(times):
                    current_head_coord[0] += 1
                    current_tail_coord = check_and_move_tail(current_head_coord, current_tail_coord, True)
                    unique_coord.add(tuple(current_tail_coord))
                    print(f"head: {current_head_coord} tail: {current_tail_coord}")
                    print("----")
                #add x
            case 'U':
                for _ in range(times):
                    current_head_coord[1] += 1
                    current_tail_coord = check_and_move_tail(current_head_coord, current_tail_coord, False)
                    unique_coord.add(tuple(current_tail_coord))
                    print(f"head: {current_head_coord} tail: {current_tail_coord}")
                    print("----")
                #add y
            case 'D':
                for _ in range(times):
                    current_head_coord[1] -= 1
                    current_tail_coord = check_and_move_tail(current_head_coord, current_tail_coord, False)
                    unique_coord.add(tuple(current_tail_coord))
                    print(f"head: {current_head_coord} tail: {current_tail_coord}")
                    print("----")
                #subtract y
    print(unique_coord)
    print(len(unique_coord))
    return unique_coord

def move_head(instructions, size):
    unique_coord = set()
    the_rope = []
    for _ in range(size):
        the_rope.append([0, 0])
    print(the_rope)
    current_head_coord = the_rope[0]
    current_tail_coord = the_rope[size - 1]


    unique_coord.add(tuple(current_tail_coord))
    print(unique_coord)
    for instruction in instructions:
        direction, times = instruction.split()[0], int(instruction.split()[1])
        print("******")
        print(direction, times)

        match direction:
            case 'L':
                for _ in range(times):
                    current_head_coord[0] -= 1
                    for i in range(1, size):
                        the_rope[i] = check_and_move_tail(the_rope[i-1], the_rope[i], True)
                    #
                 #   print(f"head: {current_head_coord} tail: {current_tail_coord}")
                 #   print("----")
                print(the_rope)
                print(the_rope[size-1])
                unique_coord.add(tuple(the_rope[size - 1]))
                #subtract x
            case 'R':
                for _ in range(times):
                    current_head_coord[0] += 1
                    #current_tail_coord = check_and_move_tail(current_head_coord, current_tail_coord, True)
                    for i in range(1, size):
                        the_rope[i] = check_and_move_tail(the_rope[i - 1], the_rope[i], True)
                    # unique_coord.add(tuple(current_tail_coord))
                 #   print(f"head: {current_head_coord} tail: {current_tail_coord}")
                 #   print("----")
                print(the_rope)
                unique_coord.add(tuple(the_rope[size - 1]))
            case 'U':
                for _ in range(times):
                    current_head_coord[1] += 1
                   # current_tail_coord = check_and_move_tail(current_head_coord, current_tail_coord, False)
                    for i in range(1, size):
                        the_rope[i] = check_and_move_tail(the_rope[i - 1], the_rope[i], True)
                    # unique_coord.add(tuple(current_tail_coord))
                   # print(f"head: {current_head_coord} tail: {current_tail_coord}")
                   # print("----")
                print(the_rope)
                unique_coord.add(tuple(the_rope[size - 1]))
                #add y
            case 'D':
                for _ in range(times):
                    current_head_coord[1] -= 1
                   # current_tail_coord = check_and_move_tail(current_head_coord, current_tail_coord, False)
                    for i in range(1, size):
                        the_rope[i] = check_and_move_tail(the_rope[i - 1], the_rope[i], True)
                    # unique_coord.add(tuple(current_tail_coord))
                   # print(f"head: {current_head_coord} tail: {current_tail_coord}")
                  #  print("----")
                print(the_rope)
                unique_coord.add(tuple(the_rope[size - 1]))
                #subtract y
    print(unique_coord)
    print(len(unique_coord))
    return unique_coord

def main():
    with open(filename) as f:
        instruction_list = f.readlines()
       # move_head(instruction_list)
        move_head(instruction_list, 10)

main()