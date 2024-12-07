from helpers.importHelpers import *

part1 = 0
part2 = 0
stringInput = getInput()
for line in stringInput.splitlines():
  result, numbers = line.split(":")
  numbers = list(map(int, numbers.split()))
  previousResults = [[numbers[0]]]
  for i in range(len(numbers)-1):
    previousResults.append([])
    for j in range(len(previousResults[i])):
      previousResults[i+1].append(previousResults[i][j] + numbers[i+1])
      previousResults[i+1].append(previousResults[i][j] * numbers[i+1])
  if int(result) in previousResults[-1]:
    part1 += int(result)

for line in stringInput.splitlines():
  result, numbers = line.split(":")
  numbers = list(map(int, numbers.split()))
  previousResults = [[numbers[0]]]
  for i in range(len(numbers)-1):
    previousResults.append([])
    for j in range(len(previousResults[i])):
      previousResults[i+1].append(previousResults[i][j] + numbers[i+1])
      previousResults[i+1].append(previousResults[i][j] * numbers[i+1])
      previousResults[i+1].append(int(str(previousResults[i][j]) + str(numbers[i+1])))
  if int(result) in previousResults[-1]:
    part2 += int(result)

print("Part 1: ", part1)
print("Part 2: ", part2)