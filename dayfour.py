def find_overlap(text):
    with open(text, 'r') as f:
        total = 0
        assignments = f.readlines()
        pairs = [assignment.split(',') for assignment in assignments]
        items = [[pair[0].split('-'), pair[1].split('-')] for pair in pairs]
        for item in items:
            if int(item[0][0]) >= int(item[1][0]) and int(item[0][1]) <= int(item[1][1]):
                # print('Match',item)
                total += 1
            elif int(item[1][0]) >= int(item[0][0]) and int(item[1][1]) <= int(item[0][1]):
                # print('Match',item)
                total += 1
            else:
                # print('No match', item)
                continue
    return total


print(find_overlap('dayfour.txt'))

