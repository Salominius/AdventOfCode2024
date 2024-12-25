from helpers.importHelpers import *

numericKeypad = { "7": -2-3j, "8": -1-3j, "9": -3j,
                  "4": -2-2j, "5": -1-2j, "6": -2j,
                  "1": -2-1j, "2": -1-1j, "3": -1j,
                  " ": -2   , "0": -1   , "A": 0}

directionalKeypad = { " ": -2   , "^": -1,    "A": 0,
                      "<": -2+1j, "v": -1+1j, ">": 1j}

lookup = {}
def localMove(pos, to, depth, keypad):
  if (pos, to, depth) in lookup:
    return lookup[(pos, to, depth)]
  
  if to.real > pos.real:
    moveX = ">" * int(to.real - pos.real)
  else:
    moveX = "<" * int(pos.real - to.real)
  if to.imag > pos.imag:
    moveY = "v" * int(to.imag - pos.imag)
  else:
    moveY = "^" * int(pos.imag - to.imag)

  possiblePaths = [moveX + moveY, moveY + moveX]
  if pos.imag == keypad[" "].imag and to.real == keypad[" "].real: # if pos is in same line as gap and target is in same column as gap:
    possiblePaths.remove(moveX + moveY) # don't more horizontally first
  elif to.imag == keypad[" "].imag and pos.real == keypad[" "].real: # if pos is in same column as gap and target is in same line as gap:
    possiblePaths.remove(moveY + moveX) # don't move vertically first

  res = min([getPathLen(path+"A", depth-1, directionalKeypad) for path in possiblePaths])
  lookup[(pos, to, depth)] = res
  return res

def getPathLen(code, depth, keypad):
  if depth == 0:
    return len(code)
  pos = keypad["A"]
  steps = 0
  for c in code:
    to = keypad[c]
    steps += localMove(pos, to, depth, keypad)
    pos = to
  return steps

def solve(codes, maxDepth):
  ans = 0
  for code in codes:
    n = getPathLen(code, maxDepth, numericKeypad)
    ans += n * int(code[:3])
  return ans

codes = getInput().splitlines()
print("Part 1: ", solve(codes, 3))
print("Part 2: ", solve(codes, 26))