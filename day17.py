from helpers.importHelpers import *
from math import log2

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
        regs[1] = getComboOp(op) & 0b111
      case 3: # "jnz"
        if regs[0] != 0:
          instPointer = op
      case 4: # "bxc"
        regs[1] = regs[1] ^ regs[2]
      case 5: # "out"
        yield getComboOp(op) & 0b111
      case 6: # "bdv"
        regs[1] = regs[0] >> getComboOp(op)
      case 7: # "cdv"
        regs[2] = regs[0] >> getComboOp(op)

def part2():
  regs = [0, 0, 0]
  instPointer = len(prog) - 1
  outputPointer = len(prog) - 1
  while True:
    if instPointer < 0:
      instPointer = len(prog) - 1
    opcode, op = prog[instPointer-1], prog[instPointer]
    #print regs[0] in bitcoding:
    print(f"{regs[0]:b}")
    print(f"Instruction: {opcode} {op}")
    match opcode:
      case 0: # "adv"
        regs[0] = regs[0] << getComboOp(op)
      case 1: # "bxl"
        regs[1] = regs[1] ^ op
      case 2: # "bst"
        if op <= 3 and op != regs[1] & 0b111:
          raise Exception("Part 2 failed")
        regs[op-4] = (regs[op-4] & ~0b111) | regs[1]
      case 3: # "jnz"
        if instPointer != len(prog)-1 or op != 0:
          raise Exception("Part 2 failed") # Assumption that jnz is only at end of program with op 0
      case 4: # "bxc"
        regs[1] = regs[1] ^ regs[2]
      case 5: # "out"
        if op <= 3 and op != prog[outputPointer]:
          raise Exception("Part 2 failed")
        regs[op-4] = (regs[op-4] & ~0b111) | prog[outputPointer]
        outputPointer -= 1
      case 6: # "bdv"
        if regs[0] == 0:
          regs[op-4] = 0
        else:
          for i in range(int(log2(regs[0])+1)):
            if regs[0] >> i == regs[1]:
              if op <= 3 and op != i:
                raise Exception("Part 2 failed")
              regs[op-4] = i
              break
      case 7: # "cdv"
        if regs[0] == 0:
          regs[op-4] = 0
        else:
          for i in range(int(log2(regs[0])+1)):
            if regs[0] >> i == regs[2]:
              if op <= 3 and op != i:
                raise Exception("Part 2 failed")
              regs[op-4] = i
    instPointer-=2
    if outputPointer < 0 and instPointer < 0:
      break

  return regs[0]

print("Part 1: ", ",".join(str(x) for x in part1()))
print("Part 2: ", part2())