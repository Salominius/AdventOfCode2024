from helpers.importHelpers import *

walls = set()
start, end = None, None
for j, row in enumerate(getInput().splitlines()):
  for i, c in enumerate(row):
    if c == "#":
      walls.add(i + j*1j)
    elif c == "S":
      start = i + j*1j
    elif c == "E":
      end = i + j*1j

# Part 1:
queue = set([(start, 0, 1)],)
points = {start: (0, 1)}

while queue:
  pos, oldPoints, oldDir = queue.pop()
  directions = [1, -1j, -1, 1j]
  for newDir in directions:
    newPos = pos + newDir
    if newPos in walls:
      continue
    rightTurns = (directions.index(newDir) - directions.index(oldDir)) % 4
    leftTurns = (4 - rightTurns) % 4
    newPoints = oldPoints + 1 + min(leftTurns, rightTurns)*1000
    if newPos not in points or points[newPos][0] > newPoints:
      points[newPos] = newPoints, newDir
      queue.add((newPos, newPoints, newDir))
  
part1 = points[end][0]

print("Part 1: ", part1)
print("Part 2: ", 0)