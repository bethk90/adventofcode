# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

# The list of items for each rucksack is given as characters all on a single line.
# A given rucksack always has the same number of items in each of its two compartments,
# so the first half of the characters represent items in the first compartment,
# while the second half of the characters represent items in the second compartment.

# Find the item type that appears in both compartments of each rucksack.
# What is the sum of the priorities of those item types?

#Version totalling all items - correct answer:

def sum_priorities(text):

    with open(text, 'r') as f:
        total = 0
        rucksacks = f.readlines()
        for rucksack in rucksacks:
            l = int((len(rucksack)-1)/2)
            first_half, second_half = rucksack[:l], rucksack[l:]
            for item in first_half:
                if item in second_half and item.islower():
                    total += ord(item) - 96
                    break
                if item in second_half and item.isupper():
                    total += ord(item) - 38
                    break
    return total

#Version using sets:

def sum_priorities_two(text):

    with open(text, 'r') as f:
        total = 0
        rucksacks = f.readlines()
        item_set = set()
        for rucksack in rucksacks:
            l = int((len(rucksack)-1)/2)
            first_half, second_half = rucksack[:l], rucksack[l:]
            for item in first_half:
                if item in second_half:
                    item_set.add(item)
        for priority in item_set:
            if priority.islower():
                total += ord(priority) - 96
            if priority.isupper():
                total += ord(priority) - 38
    return total


print(sum_priorities('daythree.txt'))
print(sum_priorities_two('daythree.txt'))


