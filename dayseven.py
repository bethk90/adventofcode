"""
The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files).
The outermost directory is called /.
You can navigate around the filesystem,
moving into or out of directories and listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
cd / switches the current directory to the outermost directory, /.
ls means list. It prints out all of the files and directories immediately contained by the current directory:
123 abc means that the current directory contains a file named abc with size 123.
dir xyz means that the current directory contains a directory named xyz.

Find all of the directories with a total size of at most 100000.
What is the sum of the total sizes of those directories?
"""

def sum_directories(text):

    current_dir = 'top'
    current_file_path = current_dir
    file_paths = [[current_dir]]
    dir_contents = {current_dir: []}

    for line in text:
        line = line.split()
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '..' or line[2] == '/':
                    current_dir = 'top'
                    current_file_path = [current_dir]
                else:
                    current_dir = line[2]
                    dir_contents.setdefault(current_dir, [])
                    current_file_path.append(current_dir)
                    file_paths.append(current_file_path)

        elif line[1] == 'ls':
            continue

        elif line[0] == 'dir':
            continue

        else:
            dir_contents[current_dir].append(int(line[0]))

        all_file_paths = []
        [all_file_paths.append(x) for x in file_paths if x not in all_file_paths]

    file_sizes = dict()

    for k in dir_contents:
        file_sizes[k] = sum(dir_contents[k])


    overall_size = dict()

    for combo in all_file_paths:
        while combo:
            overall_size[' '.join(combo)] = sum([file_sizes[a] for a in combo])
            combo = combo[1:]

    outermost_size = 0

    for combo in all_file_paths:
        outermost_size += sum([file_sizes[b] for b in combo])

    overall_size['outermost'] = sum(file_sizes.values())

    final_dict = {k:v for (k,v) in overall_size.items() if not k.startswith('top')}

    total = 0

    for size in final_dict.values():
        if size <= 100000:
            total += size

    return total


day_seven_input = open('dayseven.txt').readlines()

print(sum_directories(day_seven_input))

#Returned 677333 - too low :(
