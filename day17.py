from helpers.importHelpers import *

a, b, c, *prog = map(int, re.findall(r'\d+', getInput()))

def part1(a, b, c):
  getComboOp = lambda op: [0, 1, 2, 3, a, b, c][op]
  instPointer = 0
  while instPointer < len(prog):
    opcode, op = prog[instPointer], prog[instPointer+1]
    instPointer+=2
    match opcode:
      case 0: a = a >> getComboOp(op)
      case 1: b = b ^ op
      case 2: b = getComboOp(op) & 0b111
      case 3: instPointer = op if a != 0 else instPointer
      case 4: b = b ^ c
      case 5: yield getComboOp(op) & 0b111
      case 6: b = a >> getComboOp(op)
      case 7: c = a >> getComboOp(op)

def part2():
  i, a = 1, 0
  while i < len(prog):
    for a in range(a, a+8):
      if list(part1(a, 0, 0)) == prog[-i:]:
        i, a = i+1, a*8
        break
  return a

print("Part 1: ", ",".join(str(x) for x in part1(a, b, c)))
print("Part 2: ", part2())