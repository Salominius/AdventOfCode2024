from helpers.importHelpers import *

def inGrid(grid, x, y):
  if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
    return True
  return False

part1 = 0
part2 = 0
grid = [list(line) for line in getInput().splitlines()]
# Find starting position:
posX, posY = next((x, y) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == '^')

direction = (0, -1) # Up (x, y)
grid[posY][posX] = 'X'
while True:
  newX, newY = posX + direction[0], posY + direction[1]
  while inGrid(grid, newX, newY) and grid[newY][newX] == '#':
    direction = (-direction[1], direction[0]) # Turn right
    newX, newY = posX + direction[0], posY + direction[1]
  if inGrid(grid, newX, newY):
    posX = newX
    posY = newY
    grid[posY][posX] = 'X'
  else:
    break

part1 = sum([line.count('X') for line in grid])

print("Part 1: ", part1)
print("Part 2: ", part2)