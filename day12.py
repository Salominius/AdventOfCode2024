from helpers.importHelpers import *

garden = [list(line) for line in getInput().splitlines()]
covered = [[False]*len(garden) for _ in range(len(garden))] # garden is a square

def floodill(plant, x, y):
  if x < 0 or x >= len(garden[0]) or y < 0 or y >= len(garden):
    return 0, 1 # out of bounds
  if garden[y][x] != plant:
    return 0, 1 # different plant
  if covered[y][x]:
    return 0, 0 # already covered
  covered[y][x] = True
  area, perimeter = 1, 0
  for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    a, p = floodill(plant, x + dx, y + dy)
    area += a
    perimeter += p
  return area, perimeter

part1 = 0
for y in range(len(garden)):
  for x in range(len(garden[0])):
    if not covered[y][x]:
      area, perimeter = floodill(garden[y][x], x, y)
      part1 += area*perimeter

print("Part 1: ", part1)
print("Part 2: ", 0)