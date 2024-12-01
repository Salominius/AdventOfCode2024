from helpers.importHelpers import *

stringInput = getInput()
x = []
y = []
for line in stringInput.split("\n"):
  x.append(int(line.split(" ")[0]))
  y.append(int(line.split(" ")[-1]))

x.sort()
y.sort()
part1 = sum([abs(a - b) for a, b in zip(x, y)])

part2 = 0
for firstNum in x:
  occ = y.count(firstNum)
  part2 += occ * firstNum

print("Part 1: ", part1)
print("Part 2: ", part2)