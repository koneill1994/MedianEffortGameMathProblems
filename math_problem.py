# script which will generate a math problem of varying difficulty based on user input
# Kevin O'Neill

import random

# python2 compatibility##
try:
   input = raw_input
except NameError:
   pass
########################

## parameters


no_of_levels = 7
# determines the number of difficulty levels

max_digits=2
# the maximum number of digits in a single number

max_terms=4
# the maximum number of numbers one is asked to do operations on


max_operations=['+','-','*','/']
# different operations to be performed on the numbers, in order of increasing difficulty

#######################

def ScaleXtoY(x,xmax,ymax,ymin):
  return max(int(round((1.0*x/xmax)*ymax)),ymin)

def char_to_operation(a,b,char):
  if char == '+':
    return a+b
  elif char == '-':
    return a-b
  elif char == '*':
    return a*b
  elif char == '/':
    return a/b
  else:
    return float('nan')



def ComputeAnswer(nums,ops):
  
  if len(nums) not == len(ops)+1:
    print("ERROR: Number of NUMS and OPS do not correspond")
  
  #interleave the two lists
  eq=[]
  
  for x in range(ops):
    eq.append(nums[x])
    eq.append(ops[x])
  eq.append(nums[-1])
  
  # nums are on the odd numbers, ops are on the evens
  
  # pemdas
   
  # m
  mults=[]
  for x in range(len(eq)):
    if eq[x]=="*":
      mults.append(x)
  
  ### this is a work in progress, find a way to make it work
  
  
  
while(1):
  
  while(1):
    current_level=int(input("Difficulty Level? "))
    if current_level<=0 or current_level >no_of_levels:
      print("error: difficulty level out of range")
      print("Allowed levels: 1 through "+str(no_of_levels))
    else:
      break
  
  # generate equation & answer
  terms=ScaleXtoY(current_level,no_of_levels,max_terms,2)
  digits=ScaleXtoY(current_level,no_of_levels,max_digits,1)
  operations=max_operations[:ScaleXtoY(current_level,no_of_levels,len(max_operations),1)]
  
  numbers=[]
  ops=[]
  
  for x in range(terms):
    numbers.append(random.randrange(0,10**digits))
  
  for x in range(terms-1):
    ops.append(operations[random.randrange(0,len(operations))])
  
  
  s=""
  for t in range(len(numbers)):
    s+=str(numbers[t])
    if t<len(ops):
      s+=ops[t]
    
  print(s)
  
  
  answer = input("answer:")
  if answer=="":
    answer="0"
  if int(answer)==sum(numbers):
    print("correct!")
  else:
    print("incorrect, sum is "+str(sum(numbers)))
  
  
  
