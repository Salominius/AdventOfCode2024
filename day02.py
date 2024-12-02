from helpers.importHelpers import *

def isValid(levels):
  diffs = [b-a for a, b in zip(levels[:-1], levels[1:])]
  # minimum and maximum should not be on opposite sides of 0, and all absolute differences should be between 1 and 3
  return not min(diffs) < 0 < max(diffs) and all(1 <= abs(diff) <= 3 for diff in diffs)

part1 = 0
part2 = 0
for line in getInput().splitlines():
  levels = [int(level) for level in line.split()]
  if isValid(levels):
    part1 += 1
    part2 += 1
  else:
    for i in range(len(levels)):
      if isValid(levels[:i] + levels[i+1:]):
        part2 += 1
        break

print("Part 1: ", part1)
print("Part 2: ", part2)