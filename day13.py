from helpers.importHelpers import *
import re

# Pressing aButton a times and bButton b times will result in the following equations:
# a*x_a + b*x_b = x_p
# a*y_a + b*y_b = y_p
# In matrix form:
# | x_a  x_b | | a | = | x_p |
# | y_a  y_b | | b | = | y_p |
# Solve for a and b:
# | a | = | x_a  x_b |^-1 | x_p |
# | b | = | y_a  y_b |    | y_p |
# The inverse of a 2x2 matrix is:
# | a  b |^-1 = 1/(ad-bc) |  d  -b |
# | c  d |                | -c   a |
# Thus:
# | a | = 1/(x_a*y_b - x_b*y_a) |  y_b  -x_b | | x_p |  
# | b |                         | -y_a   x_a | | y_p |
# Or:
# a = (y_b*x_p - x_b*y_p)/(x_a*y_b - x_b*y_a)
# b = (-y_a*x_p + x_a*y_p)/(x_a*y_b - x_b*y_a)
# If a and b are integers, the solution is valid
def findWinningCost(x_a, y_a, x_b, y_b, x_p, y_p):
  a = (y_b*x_p - x_b*y_p)/(x_a*y_b - x_b*y_a)
  b = (-y_a*x_p + x_a*y_p)/(x_a*y_b - x_b*y_a)
  if a.is_integer() and b.is_integer():
    return int(3*a + b)
  return 0

part1 = 0
part2 = 0
pattern = re.compile(r"X[=|+]?(\d+), Y[=|+]?(\d+)")
for machine in getInput().split("\n\n"):
  a, b, prize = map(lambda t: (int(t[0]), int(t[1])), pattern.findall(machine)) # don't forget to map tuples of string-matches to tuples of integers
  part1 += findWinningCost(*a, *b, *prize)
  part2 += findWinningCost(*a, *b, prize[0]+1e13, prize[1]+1e13)

print("Part 1: ", part1)
print("Part 2: ", part2)