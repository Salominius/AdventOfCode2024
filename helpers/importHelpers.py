import sys
import re

def getInput(noStrip = False): #get input from file
  fileName = sys.argv[0] #get filename
  day = re.findall(r"\d+", fileName)[-1] #get day number from filename
  with open(f'./inputs/input{day}.txt') as inputFile:
    return inputFile.read() if noStrip else inputFile.read().strip()