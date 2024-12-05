from helpers.importHelpers import *

part1 = 0
part2 = 0

ruleList, updateList = getInput().split("\n\n")
rules = {}
for rule in ruleList.splitlines():
  left, right = rule.split("|")
  rules.setdefault(left, []).append(right)

for update in updateList.splitlines():
  update = update.split(",")
  previousPages = set()
  valid = True
  for page in update:
    if page not in rules or all([laterPage not in previousPages for laterPage in rules[page]]):
      previousPages.add(page)
    else:
      valid = False
      break
  if valid:
    part1 += int(update[len(update)//2])
  else:
    newUpdate = [0]*len(update)
    for i in range(len(update)-1, -1, -1): # fill new update from right to left
      for elem in update:
        if elem not in rules or all([laterPage not in update for laterPage in rules[elem]]):
          newUpdate[i] = elem
          update.remove(elem)
          break
    part2 += int(newUpdate[len(newUpdate)//2])

print("Part 1: ", part1)
print("Part 2: ", part2)