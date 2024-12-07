from helpers.importHelpers import *

part1 = 0
part2 = 0

for line in getInput().splitlines():
  result, numbers = line.split(":")
  result = int(result)
  numbers = list(map(int, numbers.split()))
  # Part 1
  previousResults = {numbers[0]}
  for nextNum in numbers[1:]:
    previousResults = {result for prev in previousResults for result in (prev+nextNum, prev*nextNum)}
  if result in previousResults:
    part1 += result
    part2 += result
    continue
  # Part 2
  previousResults = {numbers[0]}
  for nextNum in numbers[1:]:
    previousResults = {result for prev in previousResults for result in (prev+nextNum, prev*nextNum, int(f'{prev}{nextNum}'))}
  if result in previousResults:
    part2 += result

print("Part 1: ", part1)
print("Part 2: ", part2)