filename = 'input.txt'

def get_doodle_meta(program: list):
    X = 1
    op_count = 1

    num_cycles = {'noop': 1,
                  'addx': 2}
    pixels_by_cycle = {op_count: X}

   # print(program)
    for instruction in program:
        operation = instruction.strip().split()
       # print(operation)
        for numops in range(1, num_cycles[operation[0]] + 1):
            op_count += 1
            if numops == 2:
                X += int(operation[1])
            pixels_by_cycle[op_count] = X
    #return pixels_by_cycle
    doodley_doo(pixels_by_cycle, 40)




def doodley_doo(metadata: dict, line_length: int):

    line_length = line_length
    height = 6
    data = []
    line = ""
    for i in range(line_length):
        line = line + "."
    for line_no in range(height):
        data.append(line)
    for cycle, x_val in metadata.items():
        line_no = (cycle//line_length) - 1
        line = list(data[line_no])

        actual_index = [x_val - 1,x_val,x_val +1]
        line_val = cycle - (1 + (line_length * (line_no+1)))
        print(line_val, line_no)
        if(line_val) in actual_index:
            try:
                line[line_val] = '#'
            except:
                continue



        line = "".join(line)

        data[line_no] = line
        print(cycle, x_val, actual_index)
        print(line)
    #print("********")
    for i in data:
        print(i)



def get_signal_strength(program: list) -> dict:
    X = 1
    op_count = 1
    num_cycles = {'noop': 1,
                  'addx': 2}
    signal_by_cycle = {op_count: X}

    #print(program)
    for instruction in program:
        operation = instruction.strip().split()
       # print(operation)
        for numops in range(1, num_cycles[operation[0]] + 1):
            op_count += 1
            if numops == 2:
                X += int(operation[1])
            signal_by_cycle[op_count] = X * op_count

    return signal_by_cycle


def main():
    with open(filename, 'r') as f:
        program = f.readlines()

    signal_str = get_signal_strength(program)
    total = 0
    for i in [20, 60, 100, 140, 180, 220]:
        total += signal_str[i]
    print(total)
    get_doodle_meta(program)



main()
