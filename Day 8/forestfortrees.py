from collections import defaultdict

filename = "input.txt"


def get_visible_trees(items: list) -> int:
    height = len(items)
    width = len(items[0].strip())
    num_perim_trees = (2 * (height - 2)) + (2 * width)
    non_perim_trees = set()

    # top
    for col in range(1, width - 1):
        big_boi = int(items[0][col])
        # print(big_boi)
        for row in range(1, height - 1):
            if int(items[row][col]) > big_boi:
                big_boi = int(items[row][col])
                meta = f"{big_boi}, {col}, {row}"
                non_perim_trees.add(meta)
        #	print(meta)

    # bottom
    for col in range(1, width - 1):
        big_boi = int(items[height - 1][col])
        # print(big_boi)
        for row in range(height - 2, 0, -1):
            if int(items[row][col]) > big_boi:
                big_boi = int(items[row][col])
                meta = f"{big_boi}, {col}, {row}"
                non_perim_trees.add(meta)
    # print(meta)

    # left
    for row in range(1, height - 1):
        big_boi = int(items[row][0])
        #	print(big_boi)
        for col in range(1, width - 1):
            if int(items[row][col]) > big_boi:
                big_boi = int(items[row][col])
                meta = f"{big_boi}, {col}, {row}"
                non_perim_trees.add(meta)
        #	print(meta)
    # right
    for row in range(1, height - 1):
        big_boi = int(items[row][width - 1])
        print(f"biggy: {big_boi}")
        for col in range(width - 2, 0, -1):
            if int(items[row][col]) > big_boi:
                big_boi = int(items[row][col])
                meta = f"{big_boi}, {col}, {row}"
                non_perim_trees.add(meta)
                print(meta)
    print(non_perim_trees)
    print(len(non_perim_trees) + num_perim_trees)
    return len(non_perim_trees) + num_perim_trees


def calc_best_tree_score(items: list) -> int:
    height = len(items)
    width = len(items[0].strip())
    num_perim_trees = (2 * (height - 2)) + (2 * width)
    scores = defaultdict(list)

    # top
    for col in range(1, width - 1):
        big_boi = int(items[0][col])
        # print(big_boi)
        for row in range(1, height - 1):
            if int(items[row][col]) > big_boi:
                big_boi = int(items[row][col])
                meta = f"{big_boi}, {col}, {row}"
                non_perim_trees.add(meta)
        #	print(meta)

    # bottom
    for col in range(1, width - 1):
        big_boi = int(items[height - 1][col])
        # print(big_boi)
        for row in range(height - 2, 0, -1):
            if int(items[row][col]) > big_boi:
                big_boi = int(items[row][col])
                meta = f"{big_boi}, {col}, {row}"
                non_perim_trees.add(meta)
    # print(meta)

    # left
    for row in range(1, height - 1):
        big_boi = int(items[row][0])
        #	print(big_boi)
        for col in range(1, width - 1):
            if int(items[row][col]) > big_boi:
                big_boi = int(items[row][col])
                meta = f"{big_boi}, {col}, {row}"
                non_perim_trees.add(meta)
        #	print(meta)
    # right
    for row in range(1, height - 1):
        big_boi = int(items[row][width - 1])
        print(f"biggy: {big_boi}")
        for col in range(width - 2, 0, -1):
            if int(items[row][col]) > big_boi:
                big_boi = int(items[row][col])
                meta = f"{big_boi}, {col}, {row}"
                non_perim_trees.add(meta)
                print(meta)
    print(non_perim_trees)
    print(len(non_perim_trees) + num_perim_trees)
    return len(non_perim_trees) + num_perim_trees


def main():
    with open(filename) as f:
        items = f.readlines()
        print(items)
        get_visible_trees(items)


if __name__ == "__main__":
    main()
