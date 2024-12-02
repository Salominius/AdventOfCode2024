from helpers.importHelpers import *

stringInput = getInput()

part1 = 0
part2 = 0
for line in stringInput.split("\n"):
  levels = [int(i) for i in line.split()]
  diffs = [b-a for a, b in zip(levels[:-1], levels[1:])]

  if not min(diffs) < 0 < max(diffs) and all(1 <= abs(diff) <= 3 for diff in diffs):
    part1 += 1
    part2 += 1
  else:
    for index in range(len(levels)): # Performance is horrible, but idc for now
      ignoreProb = levels[:index] + levels[index+1:]
      diffs = [b-a for a, b in zip(ignoreProb[:-1], ignoreProb[1:])]
      if not min(diffs) < 0 < max(diffs) and all(1 <= abs(diff) <= 3 for diff in diffs):
        part2 += 1
        break

print("Part 1: ", part1)
print("Part 2: ", part2)