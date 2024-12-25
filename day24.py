from helpers.importHelpers import *
import re

class Gate:
  def __init__(self, a, op, b, c):
    self.a = a
    self.b = b
    self.c = c
    self.op = op
  
  def execute(self, variables):
    if self.a not in variables or self.b not in variables:
      return False
    match self.op:
      case "AND":
        variables[self.c] = variables[self.a] & variables[self.b]
      case "OR":
        variables[self.c] = variables[self.a] | variables[self.b]
      case "XOR":
        variables[self.c] = variables[self.a] ^ variables[self.b]
    return True

initialValues, gates = getInput().split("\n\n")
variables = {name: int(value) for name, value in [line.split(": ") for line in initialValues.splitlines()]}
gates = [Gate(*re.match(r"(\w+) (\w+) (\w+) -> (\w+)", gate).groups()) for gate in gates.splitlines()]

while gates:
  for gate in gates:
    if gate.execute(variables):
      gates.remove(gate)

def getZ(variables):
  zVariables = {name: value for name, value in variables.items() if name.startswith("z")}
  zVariablesSorted = sorted(zVariables.items(), key=lambda x: int(x[0][1:]), reverse=True)
  bits = map(lambda x: str(x[1]), zVariablesSorted)
  return int("".join(bits), 2)

print("Part 1: ", getZ(variables))
print("Part 2: ", 0)