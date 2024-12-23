from helpers.importHelpers import *

def evolve(num):
  num ^= num << 6 & 0xFFFFFF # * 64 == << 6,  XOR == ^,  %16777216 == & 0xFFFFFF
  num ^= num >> 5 & 0xFFFFFF # / 32 == >> 5
  return num ^ num << 11 & 0xFFFFFF # * 2048 == << 11

part1 = 0
part2 = {}
for num in map(int, getInput().splitlines()):
  # Part 1:
  prices = [num] + [num := evolve(num) for _ in range(2000)]
  part1 += prices[-1]

  # Part 2:
  prices = [num % 10 for num in prices]
  priceChanges = [prices[i] - prices[i-1] for i in range(1, len(prices))]
  seenSeqs = set()
  for i in range(len(priceChanges)-3):
    seq = tuple(priceChanges[i:i+4])
    if seq not in seenSeqs:
      seenSeqs.add(seq)
      part2[seq] = part2.get(seq, 0) + prices[i+4]

print("Part 1: ", part1)
print("Part 2: ", max(part2.values()))