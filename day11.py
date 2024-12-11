from helpers.importHelpers import *

stones = getInput().split()

for i in range(25):
  nextIt = []
  for stone in stones:
    if stone == '0':
      nextIt.append('1')
    elif len(stone) % 2 == 0:
      nextIt.append(stone[:len(stone)//2])
      nextIt.append(str(int(stone[len(stone)//2:])))
    else:
      nextIt.append(str(int(stone)*2024))
  stones = nextIt

print("Part 1: ", len(stones))
print("Part 2: ", 0)