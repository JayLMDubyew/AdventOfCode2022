import numpy
class Monkey:
    def __init__(self, name: str, items: list, operation: str, test: int, true_target: 'Monkey',
                 false_target: 'Monkey'):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.true_target = true_target
        self.false_target = false_target
        self.times_inspected = 0

    def check_and_throw(self):
        while self.items:
            old = self.items.pop(0)
            old = int(old)
            # print(f"{self.name} inspects an item with worry level of {old}.")
            new = eval(self.operation)
            # print(f"Worry level changes to {new}.")
            new //= 3

            #  print(f"{self.name} gets bored with item. worry level is changed to {new} using formula \"{self.operation}\".")

            if new % self.test == 0:
                #  print(f"Current worry level is divisible by {self.test}.\nItem with worry level {new} is thrown to {self.true_target.name}.\n\n")
                self.true_target.items.append(new)
            else:
                # print(f"Current worry level is not divisible by {self.test}.\nItem with worry level {new} is thrown to {self.true_target.name}.\n\n")
                self.false_target.items.append(new)
            self.times_inspected += 1

    def check_and_throw_but_worried(self, modulo):
        while self.items:
            old = self.items.pop(0)
            old = int(old)
            old = old % modulo
            # print(f"{self.name} inspects an item with worry level of {old}.")

            new = eval(self.operation)
            # print(f"Worry level changes to {new}.")

            #  print(f"{self.name} gets bored with item. worry level is changed to {new} using formula \"{self.operation}\".")

            if new % self.test == 0:
                #  print(f"Current worry level is divisible by {self.test}.\nItem with worry level {new} is thrown to {self.true_target.name}.\n\n")
                self.true_target.items.append(new)
            else:
                # print(f"Current worry level is not divisible by {self.test}.\nItem with worry level {new} is thrown to {self.true_target.name}.\n\n")
                self.false_target.items.append(new)
            self.times_inspected += 1


filename = 'input.txt'
mean_monkeys = []
with open(filename, 'r') as f:
    text = f.read()
    monkey_data = text.split("\n\n")
    for monkey_meta in monkey_data:
        monkey_info = monkey_meta.split("\n")
        # print(monkey_info)
        name = monkey_info[0].split(':')[0]
        data = monkey_info[1].split(':')[1].strip()
        data = data.split(',')
        operation = monkey_info[2].split('=')[1].strip()
        test = monkey_info[3].split(' ')[-1]
        test = int(test)
        new_monkey = Monkey(name, data, operation, test, None, None)
        # print(new_monkey.operation)
        mean_monkeys.append(new_monkey)
    for i in range(len(monkey_data)):
        monkey_info = monkey_data[i].split("\n")

        true_index = int(monkey_info[4].split(' ')[-1])
        mean_monkeys[i].true_target = mean_monkeys[true_index]
        # print(true_index)
        false_index = int(monkey_info[5].split(' ')[-1])
        mean_monkeys[i].false_target = mean_monkeys[false_index]
    # print(false_index)

test_info = [monkey.test for monkey in mean_monkeys]
modulo = numpy.product(test_info)
for _ in range(10000):
    for monkey in mean_monkeys:
        monkey.check_and_throw_but_worried(modulo)
# for monkey in mean_monkeys:
# print(monkey.times_inspected)
monkey_inspections = [monkey.times_inspected for monkey in mean_monkeys]
monkey_inspections = sorted(monkey_inspections, reverse=True)
y = monkey_inspections[0]
z = monkey_inspections[1]
print(y, z)
x = y * z
print(f"answer to part 2 is {x}")

# jimmy = Monkey(1,[79, 98], "old * 19", 23, None, None)
# jonny = Monkey(2,[], "old * 19", 23, None, None)
# timmy = Monkey(3,[], "old * 19", 23, None, None)
#
#
# jimmy.true_target = jonny
# jimmy.false_target = timmy
# jimmy.check_and_throw()
# print(jimmy.items)
# print(jonny.items)
# print(timmy.items)
