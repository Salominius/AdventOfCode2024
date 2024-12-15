from helpers.importHelpers import *

unparsedGrid, moves = getInput().split("\n\n")
moves = moves.replace("\n", "")
directions = {"<": -1, ">": 1, "^": -1j, "v": 1j}

def parseGrid(unparsedGrid):
  grid = {i + j*1j: c for j, row in enumerate(unparsedGrid.split("\n")) for i, c in enumerate(row)} # grid is dict with coordinates as keys in form of complex numbers
  robot = next(coord for coord, c in grid.items() if c == "@")
  return grid, robot

def part1(unparsedGrid, moves, directions):
  grid, robot = parseGrid(unparsedGrid)

  def move(coord, direction):
    coord += direction
    if grid[coord] == "#":
      return False
    if grid[coord] == "." or move(coord, direction):
      grid[coord] = grid[coord-direction]
      grid[coord-direction] = "."
      return True
    return False

  for command in moves:
    if move(robot, directions[command]):
      robot += directions[command]
  
  return int(sum(coord.real + 100*coord.imag for coord, c in grid.items() if c == "O"))

def part2(unparsedGrid, moves, directions):
  unparsedGrid = unparsedGrid.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
  grid, robot = parseGrid(unparsedGrid)

  def move(coord, direction):
    coord += direction
    if grid[coord] == "#":
      return False
    if grid[coord] == "."\
    or (grid[coord] == "[" and move(coord+1, direction) and move(coord, direction))\
    or (grid[coord] == "]" and move(coord-1, direction) and move(coord, direction)):
      grid[coord] = grid[coord-direction]
      grid[coord-direction] = "."
      return True
    return False
  
  for command in moves:
    copy = grid.copy()
    if move(robot, directions[command]):
      robot += directions[command]
    else:
      grid = copy
  
  return int(sum(coord.real + 100*coord.imag for coord, c in grid.items() if c == "["))

print("Part 1: ", part1(unparsedGrid, moves, directions))
print("Part 2: ", part2(unparsedGrid, moves, directions))