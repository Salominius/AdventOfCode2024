from helpers.importHelpers import *

WIDTH = 101
HEIGHT = 103

class Robot:
  def __init__(self, x, y, dx, dy):
    self.x = int(x)
    self.y = int(y)
    self.dx = int(dx)
    self.dy = int(dy)
  
  def move(self, seconds=1):
    self.x += self.dx * seconds
    self.x %= WIDTH
    self.y += self.dy * seconds
    self.y %= HEIGHT

def quadrant(x, y):
  xHalfLow = WIDTH//2
  xHalfHigh = WIDTH/2
  yHalfLow = HEIGHT//2
  yHalfHigh = HEIGHT/2
  if y < yHalfLow:
    if x < xHalfLow:
      return 0
    if x > xHalfHigh:
      return 1
  if y > yHalfHigh:
    if x < xHalfLow:
      return 2
    if x > xHalfHigh:
      return 3
  return None

robots = []
for line in getInput().splitlines():
  # pass format p=<int>,<int> v=<int>,<int>
  pos, vel = line.split()
  pos = pos.split("=")[1].split(",")
  vel = vel.split("=")[1].split(",")
  robots.append(Robot(*pos, *vel))

robotsInQuadrants = [0]*4
for robot in robots:
  robot.move(100)
  if (q := quadrant(robot.x, robot.y)) is not None:
    robotsInQuadrants[q] += 1

part1 = 1
for i in range(4):
  part1 *= robotsInQuadrants[i]

# Displaying only states where all robots are in different positions, quickly shows the christmas tree.
# Looking at it, the additional condition that at least 31 robots are in a row has been determined.
part2 = 100
while True: 
  for robot in robots:
    robot.move()
  part2 += 1
  if len(set([(r.x, r.y) for r in robots])) == len(robots): # All robots are in different positions
    if any([sum([1 for r in robots if r.y == y]) > 30 for y in range(HEIGHT)]): # At least 31 robots are in a row
      break

# Print christmas tree:
robotPositions = set((r.x, r.y) for r in robots)
for y in range(HEIGHT):
  for x in range(WIDTH):
    if (x, y) in robotPositions:
      print("#", end="")
    else:
      print(".", end="")
  print()

print("Part 1: ", part1)
print("Part 2: ", part2)