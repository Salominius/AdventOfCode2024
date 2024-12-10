from helpers.importHelpers import *

def inBounds(x, y, bounds):
  return 0 <= x < bounds[0] and 0 <= y < bounds[1]

grid = [list(map(int, line)) for line in getInput().splitlines()]
bounds = (len(grid[0]), len(grid))

reachable1 = [[set() for _ in range(bounds[0])] for _ in range(bounds[1])]
reachable2 = [[0 for _ in range(bounds[0])] for _ in range(bounds[1])]

part1 = 0
part2 = 0
for y in range(bounds[1]):
  for x in range(bounds[0]):
    if grid[y][x] == 9:
      reachable1[y][x] = set([(x, y)])
      reachable2[y][x] = 1

for i in range(9, 0, -1):
  for y in range(bounds[1]):
    for x in range(bounds[0]):
      if grid[y][x] == i:
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
          newX, newY = x + direction[0], y + direction[1]
          if inBounds(newX, newY, bounds) and grid[newY][newX] == i - 1:
            reachable1[newY][newX] |= reachable1[y][x]
            reachable2[newY][newX] += reachable2[y][x]

for y in range(bounds[1]):
  for x in range(bounds[0]):
    if grid[y][x] == 0:
      part1 += len(reachable1[y][x])
      part2 += reachable2[y][x]

print("Part 1: ", part1)
print("Part 2: ", part2)