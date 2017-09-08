# script which will generate a math problem of varying difficulty based on user input
# Kevin O'Neill

import random, os

import mathsolver as ms

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
# all supported is ['+','-','*','/','^']


#######################



def ScaleXtoY(x,xmax,ymax,ymin):
  return max(int(round((1.0*x/xmax)*ymax)),ymin)


def GenerateEquationAndAnswer(lvl):
  if lvl == '': lvl = 1
  current_level=int(lvl)
  
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
    
  eq=s
  
  
  correct_ans = ms.solve(s)
  
  return (eq,correct_ans)

