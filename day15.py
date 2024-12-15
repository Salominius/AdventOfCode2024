from helpers.importHelpers import *

inputParts = getInput().split("\n\n")
boxes = set()
walls = set()
robot = None
for y, line in enumerate(inputParts[0].splitlines()):
  for x, c in enumerate(line):
    if c == "O":
      boxes.add((x, y))
    elif c == "#":
      walls.add((x, y))
    elif c == "@":
      robot = (x, y)

def movePart1(command):
  global robot
  direction = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}[command]
  nextPos = (robot[0] + direction[0], robot[1] + direction[1])
  if nextPos in walls:
    return
  if nextPos not in boxes:
    robot = nextPos
    return
  firstObstacle = nextPos
  i = 2
  while True:
    nextPos = (robot[0] + direction[0]*i, robot[1] + direction[1]*i)
    if nextPos in walls:
      return
    if nextPos not in boxes:
      boxes.remove(firstObstacle)
      boxes.add(nextPos)
      robot = firstObstacle
      return
    i += 1

for command in inputParts[1].replace("\n", ""):
  movePart1(command)
part1 = sum([x + y*100 for x, y in boxes])

# ---- Part 2 ----
boxes = set()
walls = set()
robot = None
for y, line in enumerate(inputParts[0].splitlines()):
  for x, c in enumerate(line):
    if c == "O":
      boxes.add((x, y))
    elif c == "#":
      walls.add((x, y))
    elif c == "@":
      robot = (x, y)
boxes = {(x*2, y) for x, y in boxes}
walls = {(x*2+i, y) for x, y in walls for i in range(2)}
robot = (robot[0]*2, robot[1])

def movePart2(command):
  global robot
  global boxes
  direction = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}[command]
  nextBoxes = boxes.copy()
  nextPos = (robot[0] + direction[0], robot[1] + direction[1])
  if nextPos in walls:
    return
  if nextPos not in boxes and (nextPos[0]-1, nextPos[1]) not in boxes:
    robot = nextPos
    return
  # while nextBoxes not in walls:
  recentlyMoved = set()
  if nextPos in boxes:
    recentlyMoved.add((nextPos[0] + direction[0], nextPos[1] + direction[1]))
    nextBoxes.remove(nextPos)
  elif command != ">" and (nextPos[0] - 1, nextPos[1]) in nextBoxes:
    recentlyMoved.add((nextPos[0] - 1 + direction[0], nextPos[1] + direction[1]))
    nextBoxes.remove((nextPos[0] - 1, nextPos[1]))
  elif command != "<" and (nextPos[0] + 1, nextPos[1]) in nextBoxes:
    recentlyMoved.add((nextPos[0] + 1 + direction[0], nextPos[1] + direction[1]))
    nextBoxes.remove((nextPos[0] + 1, nextPos[1]))
  nextBoxes.update(recentlyMoved)
  while not any([b in walls for b in nextBoxes]) and not any([(x+1, y) in walls for x, y in nextBoxes]):
    for moved in recentlyMoved:
      nextRecentlyMoved = set()
      if moved in boxes:
        nextRecentlyMoved.add((moved[0] + direction[0], moved[1] + direction[1]))
      else: 
        if command != "<" and (moved[0] + 1, moved[1]) in nextBoxes:
          nextRecentlyMoved.add((moved[0] + 1 + direction[0], moved[1] + direction[1]))
          nextBoxes.remove((moved[0] + 1, moved[1]))
        if command != ">" and (moved[0] - 1, moved[1]) in nextBoxes:
          nextRecentlyMoved.add((moved[0] - 1 + direction[0], moved[1] + direction[1]))
          nextBoxes.remove((moved[0] - 1, moved[1]))
    recentlyMoved = nextRecentlyMoved
    nextBoxes.update(nextRecentlyMoved)
    if recentlyMoved == set():
      boxes = nextBoxes
      robot = nextPos
      if robot in boxes:
        boxes.remove(robot)
      return
  return

for command in inputParts[1].replace("\n", ""):
  movePart2(command)
part2 = sum([x + y*100 for x, y in boxes])
  # Print state:
for y in range(50):
  for x in range(100):
    if (x, y) in walls:
      print("#", end="")
    elif (x, y) in boxes:
      print("[", end="")
    elif (x-1, y) in boxes:
      print("]", end="")
    elif (x, y) == robot:
      print("@", end="")
    else:
      print(".", end="")
  print()

print("Part 1: ", part1)
print("Part 2: ", part2)