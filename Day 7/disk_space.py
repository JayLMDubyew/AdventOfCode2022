class Node():
    def __init__(self):
        self.parent = None
        self.name = None
        self.size = 0
        self.children = []

def parse_and_populate() -> Node:
    filename = "input.txt"
    head = None
    current = None
    with open(filename) as challenge_input:
        items = challenge_input.readlines()
        for command in items:
            match command.split():
                case '$', 'cd', directory:
                    if directory == '/':
                        head = Node()
                        head.name = directory
                        current = head
                    elif directory == "..":
                        current = current.parent
                    else:
                        for child in current.children:
                            if child.name == directory:
                                current = child
                                break
                case '$', 'ls':
                    continue
                case 'dir', dir_name:
                    baby = Node()
                    baby.name = dir_name
                    baby.parent = current
                    current.children.append(baby)
                case size, file:
                    the_file = Node()
                    the_file.name = file
                    the_file.size = size
                    the_file.parent = current
                    current.children.append(the_file)
    calculate_sizes(head, head.size)
    return head

def calculate_sizes(head: Node, size: int) -> (Node, int):
    if len(head.children) == 0:
        return head, head.size
    else:
        for child in head.children:
            child_node, child_size = calculate_sizes(child, child.size)
            head.size = int(head.size) + int(child_size)
            #print(head.size)
        return head, head.size


def get_sum_less_hundred_thous(head: Node, total) -> (Node, int):
    if len(head.children) == 0:
        return head, total
    else:
        if head.size <= 100000:
            total += head.size
        else:
            total += 0
        for child in head.children:
            baby, total = get_sum_less_hundred_thous(child, total)
        return head, total

def get_sum_all(head: Node, total) -> (Node, int):
    if len(head.children) == 0:
        return head, total
    else:
        total += head.size
        for child in head.children:
            baby, total = get_sum_less_hundred_thous(child, total)
        return head, total


def get_shrinky_dinks(head: Node, size :int, size_needed :int) -> (Node, int, int):
    #if you can't tell, this is the part where I got bored.
    if len(head.children) == 0:
        return head, size, size_needed
    else:
        if size == 0:
            if head.size >= size_needed:
                size = max(size, head.size)
            else:
                size = size
        else:
            if head.size >= size_needed:
                size = min(size, head.size)
            else:
                size = size
        for child in head.children:
           baby, size, size_needed = get_shrinky_dinks(child, size, size_needed)

        return head, size, size_needed





tree_head = parse_and_populate()
#this was initially gonna be a binary tree, but then i decided against it.
print(tree_head.name)
#head1, total = get_sum_less_hundred_thous(tree_head,0)
#head1, total = get_sum_all(tree_head,0)

print(tree_head.size)
size_needed = 30000000 - (70000000 - tree_head.size)
print(size_needed)
print(get_shrinky_dinks(tree_head,0,size_needed))




