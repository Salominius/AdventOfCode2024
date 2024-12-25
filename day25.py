from helpers.importHelpers import *

keys, locks = [], []
for lockOrKey in getInput().split("\n\n"):
  columns = [0, 0, 0, 0, 0]
  for line in lockOrKey.splitlines():
    for i, char in enumerate(line):
      if char == "#":
        columns[i] += 1
  if lockOrKey.startswith("#####"):
    locks.append(columns)
  else:
    keys.append(columns)

part1 = 0
for key in keys:
  for lock in locks:
    for i in range(5):
      if key[i] + lock[i] > 7:
        break
    else:
      part1 += 1

print("Part 1: ", part1)
print("Part 2: ", "Already done :)")