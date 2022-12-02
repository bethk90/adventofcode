'''
This list represents the Calories of the food carried by the Elves:

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
'''

with open('dayone.txt', 'r') as f:
    elf_list = f.read().split('\n\n')
    calories = [sum([eval(i) for i in elf.split()]) for elf in elf_list]
    max_calories = max(calories)
    max_elf = calories.index(max(calories)) + 1
    print(f'The {max_elf}th elf is carrying the most calories, with {max_calories} calories.')
    exit()