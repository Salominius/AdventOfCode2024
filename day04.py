from helpers.importHelpers import *

lines = getInput().splitlines()

def getChar(lines, y, x):
  if y < 0 or x < 0 or y >= len(lines) or x >= len(lines[y]):
    return ''
  return lines[y][x]

part1 = 0
part2 = 0
for y in range(len(lines)):
  for x in range(len(lines[y])):
    if lines[y][x] == 'X':
      # Part 1:
      for direction in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
        if "".join([getChar(lines, y + direction[0] * i, x + direction[1] * i) for i in range(1, 4)]) == 'MAS':
          part1 += 1
    elif lines[y][x] == 'A':
      # Part 2:
      hits = 0
      for direction in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
        if "".join([getChar(lines, y + direction[0] * i, x + direction[1] * i) for i in range(-1, 2)]) == 'MAS':
          hits += 1
      if hits == 2:
        part2 += 1

print("Part 1: ", part1)
print("Part 2: ", part2)