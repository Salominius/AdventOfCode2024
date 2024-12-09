from helpers.importHelpers import *

def part1f(diskMap):
  diskMap = diskMap.copy() # diskMap gets modified, so its best to copy it first
  i = 0
  j = len(diskMap) - 1
  while i < j:
    # yield id of file that has always been here: 
    for _ in range(diskMap[i]):
      yield i//2
    i += 1
    # yield ids of files that can be fitted in empty slots:
    for _ in range(diskMap[i]):
      yield j//2
      diskMap[j] -= 1
      if diskMap[j] == 0:
        j -= 2
    i += 1
  # yield remaining ids that are in the middle of the disk:
  for _ in range(diskMap[i]):
    yield i//2

def part2f(diskMap):
  diskMap = diskMap.copy() # diskMap gets modified, so its best to copy it first
  i = 0
  j = len(diskMap) - 1
  vacant = [0] * len(diskMap)
  while i < j:
    # yield 0 if slot once held a file, but it has been removed:
    for _ in range(vacant[i]):
      yield 0
    # yield id of file that has always been here: 
    for _ in range(diskMap[i]):
      yield i//2
    i += 1
    # Try to fill empty slot:
    for candidate in range(j, i, -2):
      if 0 < diskMap[candidate] <= diskMap[i]: # 0 == diskMap[candidate] would mean that the candidate has already been moved
        # yield id of candidate if it fits in empty slot:
        for _ in range(diskMap[candidate]):
          yield candidate//2
        diskMap[i] -= diskMap[candidate] # reduce empty slot size by candidate size
        vacant[candidate] = diskMap[candidate] # remember to yield 0s instead of candidate id for the candidate later
        diskMap[candidate] = 0 # mark candidate as moved
    # yield remaining empty slots:
    for _ in range(diskMap[i]):
      yield 0
    i += 1
  # yield remaining ids at the end of the disk:
  for _ in range(diskMap[i]):
    yield i//2

intInput = [int(x) for x in getInput()]
print("Part 1: ", sum(i*id for i, id in enumerate(part1f(intInput))))
print("Part 2: ", sum(i*id for i, id in enumerate(part2f(intInput))))