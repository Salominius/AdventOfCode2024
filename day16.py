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
points = {start: {1: 0}}

while queue:
  pos, oldPoints, oldDir = queue.pop()
  directions = [1, -1j, -1, 1j]
  for newDir in directions:
    newPos = pos + newDir
    if newPos in walls:
      continue
    rightTurns = (directions.index(newDir) - directions.index(oldDir)) % 4
    leftTurns = (4 - rightTurns) % 4
    points[pos][newDir] = min(points[pos].get(newDir, float("inf")), oldPoints + min(leftTurns, rightTurns)*1000)
    newPoints = points[pos][newDir] + 1
    if newPos not in points or points[newPos].get(newDir, float("inf")) > newPoints:
      points.setdefault(newPos, {})[newDir] = newPoints
      queue.add((newPos, newPoints, newDir))
  
part1 = min(points[end].values())

# Part 2:
part2 = set([end],)
queue = set([(end, *next((key, value) for key, value in points[end].items() if value == part1))],)
while queue:
  pos, oldDir, oldPoints = queue.pop()
  directions = [1, -1j, -1, 1j]
  for newDir in directions:
    newPos = pos - newDir
    rightTurns = (directions.index(newDir) - directions.index(oldDir)) % 4
    leftTurns = (4 - rightTurns) % 4
    if newPos in points and points[newPos][newDir] == oldPoints - 1 - min(leftTurns, rightTurns)*1000:
      part2.add(newPos)
      queue.add((newPos, newDir, points[newPos][newDir]))

print("Part 1: ", part1)
print("Part 2: ", len(part2))