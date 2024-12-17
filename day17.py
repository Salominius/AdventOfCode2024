from helpers.importHelpers import *

regs, prog = getInput().split("\n\n")
regs = [int(l[12:]) for l in regs.split("\n")]
prog = [int(p) for p in prog[9:].split(",")]

def getComboOp(op):
  if op <= 3:
    return op
  return regs[op-4]

def part1():
  instPointer = 0
  while instPointer < len(prog):
    opcode, op = prog[instPointer], prog[instPointer+1]
    instPointer+=2
    match opcode:
      case 0: # "adv"
        regs[0] = regs[0] >> getComboOp(op)
      case 1: # "bxl"
        regs[1] = regs[1] ^ op
      case 2: # "bst"
        regs[1] = getComboOp(op) % 8
      case 3: # "jnz"
        if regs[0] != 0:
          instPointer = op
      case 4: # "bxc"
        regs[1] = regs[1] ^ regs[2]
      case 5: # "out"
        yield getComboOp(op) % 8
      case 6: # "bdv"
        regs[1] = regs[0] >> getComboOp(op)
      case 7: # "cdv"
        regs[2] = regs[0] >> getComboOp(op)

print("Part 1: ", ",".join(str(x) for x in part1()))
print("Part 2: ", 0)