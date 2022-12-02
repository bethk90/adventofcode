'''
The winner of the whole tournament is the player with the highest score.
Your total score is the sum of your scores for each round.
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
Their play:
A for Rock, B for Paper, and C for Scissors.
Your play:
X for Rock, Y for Paper, and Z for Scissors.
'''

scores_dict = {'X': 1, 'Y': 2, 'Z': 3}
result_dict = {'A X': 3, 'A Y': 6, 'A Z': 0,
               'B X': 0, 'B Y': 3, 'B Z': 6,
               'C X': 6, 'C Y': 0, 'C Z': 3}

with open('daytwo.txt', 'r') as f:
    move_list = f.read().split('\n')
    scores = [scores_dict[move[2]] + result_dict[move] for move in move_list]
    total = sum(scores)
    print(f'Your total scores would be {total}')
    exit()