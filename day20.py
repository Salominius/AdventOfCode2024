from helpers.importHelpers import *

grid = {i + j*1j: c for j, row in enumerate(getInput().splitlines()) for i, c in enumerate(row)}
start = [coord for coord, value in grid.items() if value == "S"][0]
end = [coord for coord, value in grid.items() if value == "E"][0]
dimensions = (max(grid, key=lambda x: x.real).real, max(grid, key=lambda x: x.imag).imag)

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

def part1():
  distancesToStart = bfs(start, grid)
  distancesToEnd = bfs(end, grid)
  normalCost = distancesToStart[end]
  part1 = 0
  for coord, value in grid.items():
    if value != "#":
      continue
    if 0 < coord.real < dimensions[0] and 0 < coord.imag < dimensions[1]:
      if coord+1 in distancesToEnd and coord-1 in distancesToEnd:
        if abs(distancesToEnd[coord+1] + distancesToStart[coord-1]) + 2 <= normalCost - 100:
          part1 += 1
        elif abs(distancesToEnd[coord-1] + distancesToStart[coord+1]) + 2 <= normalCost - 100:
          part1 += 1
      if coord+1j in distancesToEnd and coord-1j in distancesToEnd:
        if abs(distancesToEnd[coord+1j] + distancesToStart[coord-1j]) + 2 <= normalCost - 100:
          part1 += 1
        elif abs(distancesToEnd[coord-1j] + distancesToStart[coord+1j]) + 2 <= normalCost - 100:
          part1 += 1
  return part1

print("Part 1: ", part1()) # 1441 too low
print("Part 2: ", 0)