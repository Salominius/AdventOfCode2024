from helpers.importHelpers import *

connections = {}
for line in getInput().splitlines():
  a, b = line.split("-")
  connections.setdefault(a, set()).add(b)
  connections.setdefault(b, set()).add(a)

# Part 1 separately for better performance:
trippleComponents = set()
for a, bList in connections.items():
  for b in bList:
    if b > a:
      for c in connections[b]:
        if c > b and c in bList and any([x[0] == "t" for x in [a, b, c]]):
          trippleComponents.add((a, b, c))

# Part 2 (Find biggest connected component):
biggestComponent = tuple()
for a, bList in connections.items():
  aGroups = [{a} | bList]
  for b in bList:
    withB = [group.intersection(connections[b] | {b}) for group in aGroups]
    withoutB = [group - {b} for group in aGroups]
    aGroups = withB + withoutB
    aGroups = [g for g in aGroups if len(g) > len(biggestComponent)]
  for group in aGroups:
    if len(group) > len(biggestComponent):
      biggestComponent = sorted(group)

print("Part 1: ", len(trippleComponents))
print("Part 2: ", ",".join(biggestComponent))