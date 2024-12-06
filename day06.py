from helpers.importHelpers import *

def inDimensions(dimensions, x, y):
  return 0 <= x < dimensions[0] and 0 <= y < dimensions[1]

def testObstacle(x, y, direction, obstacles):
  newObstacle = (x + direction[0], y + direction[1])
  obstacles.add(newObstacle) # Add obstacle about to be tested
  visitedDirections = set() # loop exists, if we visit a location twice with same direction

  while (x, y, direction) not in visitedDirections:
    visitedDirections.add((x, y, direction))
    newX, newY = x + direction[0], y + direction[1]
    if (newX, newY) in obstacles:
      direction = (-direction[1], direction[0]) # Turn right
      continue
    if not inDimensions(dimensions, newX, newY):
      obstacles.remove(newObstacle)
      return False
    x, y = newX, newY

  obstacles.remove(newObstacle)
  return True

stringInput = getInput().splitlines()
dimensions = (len(stringInput[0]), len(stringInput))
obstacles = set()
posX, posY = 0, 0
for y, line in enumerate(stringInput):
  for x, char in enumerate(line):
    if char == '#':
      obstacles.add((x, y))
    elif char == '^':
      posX, posY = x, y
direction = (0, -1) # Up

visited = {(posX, posY)}
newObstacles = set()
while True:
  # Calculate next position:
  newX, newY = posX + direction[0], posY + direction[1]
  if not inDimensions(dimensions, newX, newY):
    break
  if (newX, newY) in obstacles:
    direction = (-direction[1], direction[0]) # Turn right
    continue

  # Part 2:
  if (newX, newY) not in visited and (newX, newY) not in newObstacles:
    if testObstacle(posX, posY, direction, obstacles):
      newObstacles.add((newX, newY))

  # Update position:
  posX, posY = newX, newY
  visited.add((posX, posY))

print("Part 1: ", len(visited))
print("Part 2: ", len(newObstacles))