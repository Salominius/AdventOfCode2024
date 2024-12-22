from helpers.importHelpers import *

secretNums = list(map(int, getInput().splitlines()))

def evolve(num):
  def mixAndPrune(a, b):
    return (a ^ b) % 16777216

  mult64 = num << 6
  num = mixAndPrune(num, mult64)
  div32 = num >> 5
  num = mixAndPrune(num, div32)
  mult2048 = num << 11
  num = mixAndPrune(num, mult2048)

  return num

for i in range(2000):
  secretNums = list(map(evolve, secretNums))

print("Part 1: ", sum(secretNums))
print("Part 2: ", 0)