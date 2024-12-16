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

directions = [1, -1j, -1, 1j]
def getTurnCost(oldDir, newDir):
  rightTurns = (directions.index(newDir) - directions.index(oldDir)) % 4
  leftTurns = (4 - rightTurns) % 4
  return min(leftTurns, rightTurns)*1000

# Part 1:
queue = {(start, 1, 0)} # (position, direction, points)
points = {start: {1: 0}} # for each coordinate, store a dict with directions as keys and points as values
while queue:
  pos, oldDir, oldPoints = queue.pop()
  for newDir in directions:
    if (newPos := pos+newDir) in walls:
      continue
    # Update cost to look in newDir at current position:
    points[pos][newDir] = min(points[pos].get(newDir, float("inf")), oldPoints + getTurnCost(oldDir, newDir))
    # Cost to move in newDir from current position: 
    newPoints = points[pos][newDir] + 1
    # If we reach a point we havn't reached before, or if we reach it cheaper then before, store new cost and add point to queue:
    if newPos not in points or points[newPos].get(newDir, float("inf")) > newPoints:
      points.setdefault(newPos, {})[newDir] = newPoints
      queue.add((newPos, newDir, newPoints))
part1 = min(points[end].values())

# Part 2:
part2 = {end} # set of all positions that are part of an optimal path
queue = {(end, min(points[end], key=points[end].get), part1)} # (position, direction, points)
while queue:
  pos, curDir, curPoints = queue.pop()
  for prevDir in directions:
    prevPos = pos - prevDir # walk backwards
    # If currentPos, direction and cost can be achieved from prevPos, prevPos must be part of an optimal path 
    if prevPos in points and points[prevPos][prevDir] == curPoints - 1 - getTurnCost(prevDir, curDir):
      part2.add(prevPos)
      queue.add((prevPos, prevDir, points[prevPos][prevDir]))

print("Part 1: ", part1)
print("Part 2: ", len(part2))