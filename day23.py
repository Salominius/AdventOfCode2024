from helpers.importHelpers import *

connections = {}
for line in getInput().splitlines():
  a, b = line.split("-")
  connections.setdefault(a, set()).add(b)
  connections.setdefault(b, set()).add(a)

components = set()
for a, bList in connections.items():
  maxSize = max([len(group) for group in components], default=0)
  aGroups = [{a} | bList]
  for b in bList:
    withB = [group.intersection(connections[b] | {b}) for group in aGroups]
    withoutB = [group - {b} for group in aGroups]
    aGroups = withB + withoutB
  for group in aGroups:
    components.add(tuple(sorted(group)))

print("Part 1: ", sum([1 for group in components if len(group) == 3 and any([x[0] == "t" for x in group])]))
print("Part 2: ", ",".join(sorted(max(components, key=len))))