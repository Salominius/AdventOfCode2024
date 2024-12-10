from helpers.importHelpers import *

def inBounds(x, y, bounds):
  return 0 <= x < bounds[0] and 0 <= y < bounds[1]

grid = [list(map(int, line)) for line in getInput().splitlines()]
bounds = (len(grid[0]), len(grid))

reachableEnds = [[set() for _ in range(bounds[0])] for _ in range(bounds[1])] # For each grid-cell, the set of reachable ends
numPathsToEnds = [[0 for _ in range(bounds[0])] for _ in range(bounds[1])] # For each grid-cell, the number of paths to reachable ends

part1 = 0
part2 = 0
for y in range(bounds[1]):
  for x in range(bounds[0]):
    if grid[y][x] == 9:
      reachableEnds[y][x] = set([(x, y)]) # The end is reachable from itself
      numPathsToEnds[y][x] = 1 # There is one path from the end to the end

for i in range(9, 0, -1): # For each number from 9 to 1
  for y in range(bounds[1]):
    for x in range(bounds[0]):
      if grid[y][x] == i: # If the cell contains the current number
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # Go through neighbours
          newX, newY = x + direction[0], y + direction[1]
          if inBounds(newX, newY, bounds) and grid[newY][newX] == i - 1: # If neighbour can reach the current cell
            reachableEnds[newY][newX] |= reachableEnds[y][x] # All current reachable ends can be reached by the neighbour
            numPathsToEnds[newY][newX] += numPathsToEnds[y][x] # All current paths can be reached by the neighbour

for y in range(bounds[1]):
  for x in range(bounds[0]):
    if grid[y][x] == 0: # For each trail head
      part1 += len(reachableEnds[y][x]) # Count the number of reachable ends
      part2 += numPathsToEnds[y][x] # Count the number of paths to reachable ends

print("Part 1: ", part1)
print("Part 2: ", part2)