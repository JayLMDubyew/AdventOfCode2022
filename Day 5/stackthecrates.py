import re


def go_thru_file() -> list:
    with open('input.txt') as file:
        data = file.read()
        lines = data.splitlines()
        index = 0
        for i in lines:
            if i == '':
                crateinfo = lines[:index - 1]
                directions_meta = lines[index + 1:]
                return populate_crates(crateinfo), parse_directions(directions_meta)
            else:
                index = index + 1


def populate_crates(crateinfo: list) -> list:
    numdocks = len(crateinfo[-1].split())
    stacks = [[] for _ in range(numdocks)]
    for crates in crateinfo:
        for index, k in enumerate(range(1, len(crates), 4)):
            if crates[k].strip():
                stacks[index].append(crates[k])
    return stacks


def parse_directions(metadata: list) -> list:
    pattern = re.compile(r'move (\d+) from (\d+) to (\d+)')
    directions = []
    for direction in metadata:
        step = []
        x = pattern.match(direction)
        amount_to_move = int(x.group(1))
        source = int(x.group(2)) - 1
        dest = int(x.group(3)) - 1
        step.append(amount_to_move)
        step.append(source)
        step.append(dest)
        directions.append(step)
    return directions


def move_crates(crates: list, instructions: list) -> str:
    for direction in instructions:
        amount_to_move = direction[0]
        source = direction[1]
        dest = direction[2]

        for i in range(0, amount_to_move):
            crate_to_move = crates[source].pop(0)
            crates[dest].insert(0, crate_to_move)
    finished = ""
    for stack in crates:
        finished = finished + stack[0]
    return finished


def cratemover_9001(crates: list, instructions: list) -> str:
    for direction in instructions:
        amount_to_move = direction[0]
        source = direction[1]
        dest = direction[2]
        items_to_move = crates[source][:amount_to_move]
        source_after_move = crates[source][amount_to_move:]
        crates[dest] = items_to_move + crates[dest]
        crates[source] = source_after_move

    finished = ""
    for items in crates:
        finished = finished + items[0]
    return finished


def main():
    crates, instructions = go_thru_file()
    print(move_crates(crates, instructions))  # part 1
    crates, instructions = go_thru_file()
    print(cratemover_9001(crates, instructions))


if __name__ == "__main__":
    main()
