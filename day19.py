from helpers.importHelpers import *
from functools import lru_cache

towels, patterns = getInput().split("\n\n")
towels = towels.split(", ")
patterns = patterns.split("\n")

@lru_cache(maxsize=None)
def checkPattern(pattern):
  if pattern == "":
    return 1
  res = 0
  for towel in towels:
    if pattern.startswith(towel):
      res += checkPattern(pattern[len(towel):])
  return res

print("Part 1: ", sum([checkPattern(pattern)>0 for pattern in patterns]))
print("Part 2: ", sum([checkPattern(pattern) for pattern in patterns]))