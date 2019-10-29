example = ['left', 'right', 'up', 'down']

for i in range(len(example)):
    print(i, example[i])

# this is the same as above

for i, j in enumerate(example):
    print(i, j)
