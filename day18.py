from helpers.importHelpers import *

obstacleList = [int(i) + int(j)*1j for line in getInput().splitlines() for i, j in [line.split(",")]]

def inDim(c):
  return 0 <= c.real <= 70 and 0 <= c.imag <= 70

def A_Star(start = 0+0j, goal = 70+70j, numBytes = 1024, h = lambda a, b: abs(a - b)): # h is a heuristic function estimating the cost to reach the goal from the given node
  obstacles = set(obstacleList[:numBytes])
  openSet = {start}
  gScore = {start: 0}
  fScore = {start: h(start, goal)}
  while openSet:
    current = min(openSet, key = lambda x: fScore[x])
    if current == goal:
      return gScore[goal]
    openSet.remove(current)
    for neighbor in {current + 1, current - 1, current + 1j, current - 1j}:
      if neighbor in obstacles or not inDim(neighbor):
        continue
      tentative_gScore = gScore[current] + 1
      if tentative_gScore < gScore.get(neighbor, float("inf")):
        gScore[neighbor] = tentative_gScore
        fScore[neighbor] = tentative_gScore + h(neighbor, goal)
        openSet.add(neighbor)
  return False

def part2(): # Do a binary search to find the first obstacle where the goal can not be reached anymore
  lower, upper = 1024, len(obstacleList)
  while lower < upper:
    mid = (lower + upper) // 2
    if A_Star(numBytes=mid):
      lower = mid + 1
    else:
      upper = mid
  return f"{int(obstacleList[lower-1].real)},{int(obstacleList[lower-1].imag)}"

print("Part 1: ", A_Star())
print("Part 2: ", part2())