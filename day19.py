from helpers.importHelpers import *
from functools import lru_cache

towels, patterns = getInput().split("\n\n")
towels = towels.split(", ")
patterns = patterns.split("\n")

@lru_cache(maxsize=None)
def part1(pattern):
  if pattern == "":
    return 1
  for towel in towels:
    if pattern.startswith(towel):
      if part1(pattern[len(towel):]):
        return 1
  return 0

@lru_cache(maxsize=None)
def part2(pattern):
  if pattern == "":
    return 1
  res = 0
  for towel in towels:
    if pattern.startswith(towel):
      res += part2(pattern[len(towel):])
  return res

print("Part 1: ", sum([part1(pattern) for pattern in patterns]))
print("Part 2: ", sum([part2(pattern) for pattern in patterns]))