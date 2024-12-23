from helpers.importHelpers import *

connections = {}
for line in getInput().splitlines():
  a, b = line.split("-")
  connections.setdefault(a, set()).add(b)
  connections.setdefault(b, set()).add(a)

tripleConnections = set()
for a, bList in connections.items():
  for b in bList:
    if b > a:
      for c in connections[b]:
        if c > b and c in bList:
          tripleConnections.add((a, b, c))

# sum if any starts with "t"
print("Part 1: ", sum([1 for a, b, c in tripleConnections if any([x[0] == "t" for x in [a, b, c]])]))
print("Part 2: ", 0)