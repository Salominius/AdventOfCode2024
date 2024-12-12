from helpers.importHelpers import *

plantID = 0
garden = [list(line) for line in getInput().splitlines()]
fields = {} # plantID: (area, perimeter, sides)

def inBounds(x, y):
  return 0 <= x < len(garden[0]) and 0 <= y < len(garden) # garden has same width and height

def floodill(plant, x, y):
  if not inBounds(x, y):
    return 0, 1 # out of bounds
  if garden[y][x] == plantID:
    return 0, 0 # already covered
  if garden[y][x] != plant:
    return 0, 1 # different plant
  garden[y][x] = plantID
  area, perimeter = 1, 0
  for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    a, p = floodill(plant, x + dx, y + dy)
    area += a
    perimeter += p
  return area, perimeter

for y in range(len(garden)):
  for x in range(len(garden[0])):
    if not isinstance(garden[y][x], int):
      area, perimeter = floodill(garden[y][x], x, y)
      fields[plantID] = (area, perimeter, perimeter) # perimeter is default for number of sides. reduced later
      plantID += 1

for y in range(len(garden)):
  for x in range(len(garden[0])):
    currentPlant = garden[y][x] # for each cell
    for movex, movey in [(1, 0), (0, 1)]: # move right and down
      if not inBounds(x+movex, y+movey) or garden[y+movey][x+movex] != currentPlant: # if leaving the field, nothing happens
        continue
      # If next cell is part of same field, check sides of originial cell and next cell.
      for sidex, sidey in [(movey, movex), (-movey, -movex)]: # sides are calculated with offset perpendicular to the direction of movement
        if not inBounds(x+sidex, y+sidey) or (currentPlant != garden[y+sidey][x+sidex] and currentPlant != garden[y+movey+sidey][x+movex+ sidex]):
          # if side of previous cell and side of next cell are both not part of field, number of sides is reduced by one
          fields[currentPlant] = (fields[currentPlant][0], fields[currentPlant][1], fields[currentPlant][2] - 1)

print("Part 1: ", sum(area*perimeter for area, perimeter, _ in fields.values()))
print("Part 2: ", sum(area*sides for area, _, sides in fields.values()))