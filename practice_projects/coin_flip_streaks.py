import random

number_of_streaks = 0
results = []
h_streak = ['h', 'h', 'h', 'h', 'h', 'h']
t_streak = ['t', 't', 't', 't', 't', 't']

for experiment_number in range(10000):
    if random.randint(0, 1) == 0:
        results.append('h')
    else:
        results.append('t')

    if len(results) >= 6:
        if results[-6:] == h_streak or results[-6:] == t_streak:
            number_of_streaks += 1

print('Chance of streak: %s%%' % (number_of_streaks / 100))