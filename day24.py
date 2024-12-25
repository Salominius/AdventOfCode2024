from helpers.importHelpers import *
import re
import networkx as nx
import matplotlib.pyplot as plt

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

def part1(gates, variables):
  while gates:
    for gate in gates:
      if gate.execute(variables):
        gates.remove(gate)

  zVariables = {name: value for name, value in variables.items() if name.startswith("z")}
  zVariablesSorted = sorted(zVariables.items(), key=lambda x: int(x[0][1:]), reverse=True)
  bits = map(lambda x: str(x[1]), zVariablesSorted)
  return int("".join(bits), 2)

def part2(gates):
  # The input is a misconfigured 45-bit Ripple Carry Adder
  # => 45 1-bit full adders, each connected to the carry bit of the previous one
  # => bits: x1 XOR y1 XOR carry1 = z1
  # => bits: (x1 and y1) OR ((x1 XOR y1) and carry1) = carry2
  #    BUT: carry45 replaced with z45
  # This means: 1. if the output of a gate is z, the operation must be XOR   (unless last bit, which is just the previous carry)
  #             2. all XOR gates must either have x and y as input or z as output
  #             3. all XOR gates with inputs x and y must be input to another XOR gate (except first bit, which doesn't have a carry)
  #             4. any AND gate must be input to another OR gate (except first bit, which doesn't have a carry)
  # alternative rules could surely be found, but this is the smallest set I came up with that works with my input

  faultyGates = set()
  for gate in gates:
    # Rule 1:
    if gate.c != "z45": # except last bit
      if gate.c[0] == "z" and gate.op != "XOR":
        faultyGates.add(gate)
    # Rule 2:
    if gate.op == "XOR" and {gate.a[0], gate.b[0]} != {"x", "y"} and not gate.c[0] == "z":
      faultyGates.add(gate)
    # Rule 3:
    if {gate.a, gate.b} != {"x00", "y00"}: # except first bit
      if gate.op == "XOR" and {gate.a[0], gate.b[0]} == {"x", "y"} and not any(gate.c in {other.a, other.b} for other in gates if other.op == "XOR"):
        faultyGates.add(gate)
    # Rule 4:
    if {gate.a, gate.b} != {"x00", "y00"}:
      if gate.op == "AND" and not any(gate.c in {other.a, other.b} for other in gates if other.op == "OR"):
        faultyGates.add(gate)
  return ",".join(sorted([gate.c for gate in faultyGates]))

print("Part 1: ", part1(gates.copy(), variables))
print("Part 2: ", part2(gates))