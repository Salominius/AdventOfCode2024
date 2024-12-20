from helpers.importHelpers import *

grid = {i + j*1j: c for j, row in enumerate(getInput().splitlines()) for i, c in enumerate(row)}
start = [coord for coord, value in grid.items() if value == "S"][0]
end = [coord for coord, value in grid.items() if value == "E"][0]

def bfs(start, grid):
  queue = [(start, 0)]
  costs = {}
  while queue:
    coord, cost = queue.pop()
    if grid[coord] == "#" or costs.setdefault(coord, float("inf")) <= cost:
      continue
    costs[coord] = cost
    for direction in [1, -1, 1j, -1j]:
      queue.append((coord + direction, cost + 1))
  return costs

def findGoodCheats(cheatLength, minGain):
  distancesToStart = bfs(start, grid)
  distancesToEnd = bfs(end, grid)
  normalCost = distancesToStart[end]
  res = 0
  for cheatStart in grid.keys():
    if grid[cheatStart] == "#":
      continue
    for r in range(2, cheatLength+1): # cheat distance is at least 2 (otherwise no wall is skipped), max cheatLength
      for x in range(r+1):
        y = r - x
        for cheatEnd in set([cheatStart + x + y*1j, cheatStart - x + y*1j, cheatStart + x - y*1j, cheatStart - x - y*1j]):
          if cheatEnd not in grid or grid[cheatEnd] == "#":
            continue
          cheatCost = distancesToEnd[cheatEnd] + distancesToStart[cheatStart] + r
          if cheatCost <= normalCost - minGain:
            res += 1
  return res

print("Part 1: ", findGoodCheats(2, 100))
print("Part 2: ", findGoodCheats(20, 100))