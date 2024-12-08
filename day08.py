from helpers.importHelpers import *

def withinBounds(xy, bounds):
  return 0 <= xy[0] < bounds[0] and 0 <= xy[1] < bounds[1]

antennas = dict()
stringInput = getInput().splitlines()
bounds = (len(stringInput[0]), len(stringInput))
for y, line in enumerate(stringInput):
  for x, char in enumerate(line):
    if char != '.':
      antennas.setdefault(char, []).append((x, y))

antinodes1 = set()
antinodes2 = set()
for aType in antennas:
  for i, a in enumerate(antennas[aType]):
    for b in antennas[aType][i+1:]:
      xDiff, yDiff = b[0] - a[0], b[1] - a[1]
      # Part 1:
      if withinBounds(outsideA := (a[0] - xDiff, a[1] - yDiff), bounds):
        antinodes1.add(outsideA)
      if withinBounds(outsideB := (b[0] + xDiff, b[1] + yDiff), bounds):
        antinodes1.add(outsideB)
      # Part 2:
      i = 0
      while withinBounds(outsideA := (a[0] - xDiff*i, a[1] - yDiff*i), bounds):
        antinodes2.add(outsideA)
        i += 1
      i = 0
      while withinBounds(outsideB := (b[0] + xDiff*i, b[1] + yDiff*i), bounds):
        antinodes2.add(outsideB)
        i += 1

print("Part 1: ", len(antinodes1))
print("Part 2: ", len(antinodes2))