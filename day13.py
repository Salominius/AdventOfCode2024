from helpers.importHelpers import *
import re

def findWinningCost(a, b, prize):
  minCost = float("inf")
  for aPresses in range(0, prize[0] // a[0] + 1):
    # Press button a i times and check if result can be divided by b
    xRemaining, yRemaining = prize[0] - a[0] * aPresses, prize[1] - a[1] * aPresses
    bPresses = xRemaining // b[0]
    if b[0] * bPresses == xRemaining and b[1] * bPresses == yRemaining:
      minCost = min(minCost, aPresses*3 + bPresses)
  return minCost

part1 = 0
for machine in getInput().split("\n\n"):
  pattern = re.compile(r"X[=|+]?(\d+), Y[=|+]?(\d+)")
  a, b, prize = map(lambda t: (int(t[0]), int(t[1])), pattern.findall(machine)) # don't forget to map tuples of string-matches to tuples of integers
  minCost = findWinningCost(a, b, prize)
  if minCost != float("inf"):
    part1 += minCost

print("Part 1: ", part1)
print("Part 2: ", 0)