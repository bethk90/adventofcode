# After the rearrangement procedure completes, what crate ends up on top of each stack?

def get_stack(a,arr):
    for i in range(len(arr)):
        try:
            return [x[a] for x in arr[i:]]
        except IndexError:
            continue


def rearrangement(file):
    stacks, orders = open(file).readlines()[:8], open(file).readlines()[10:]
    indices = [1,5,9,13,17,21,25,29,33]
    stack_list = [get_stack(index, stacks) for index in indices]

    for stack in stack_list:
        stack[:] = [value for value in stack if value != ' ']

    instructions = []

    for order in orders:
        order = order.split(' ')
        amount, f, s = int(order[1]), int(order[3]) - 1, int(order[5]) - 1
        instructions.append([amount,f,s])

    for instruction in instructions:
        order_amount, order_first, order_second = instruction[0], instruction[1], instruction[2]
        while order_amount > 0:
            stack_list[order_second].insert(0, stack_list[order_first][0])
            stack_list[order_first].remove(stack_list[order_first][0])
            order_amount -= 1

    top_of_the_stacks = [x[0] for x in stack_list]

    return top_of_the_stacks


print('The item on the top of each stack is:', rearrangement('dayfive.txt'))