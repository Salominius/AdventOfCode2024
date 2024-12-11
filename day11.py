from helpers.importHelpers import *

stones = {stone: 1 for stone in getInput().split()}

def step(stones):
  nextState = {}
  for stone, num in stones.items():
    if stone == '0':
      nextState['1'] = nextState.setdefault('1', 0) + num
    elif len(stone) % 2 == 0:
      leftHalf, rightHalf = stone[:len(stone)//2], str(int(stone[len(stone)//2:]))
      nextState[leftHalf] = nextState.setdefault(leftHalf, 0) + num
      nextState[rightHalf] = nextState.setdefault(rightHalf, 0) + num
    else:
      nextState[str(int(stone)*2024)] = nextState.setdefault(str(int(stone)*2024), 0) + num
  return nextState

for i in range(25):
  stones = step(stones)
part1 = sum(stones.values())
for i in range(50):
  stones = step(stones)
part2 = sum(stones.values())

print("Part 1: ", part1)
print("Part 2: ", part2)