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

max_digits=3
# the maximum number of digits in a single number

max_terms=4
# the maximum number of numbers one is asked to do operations on


operations=['+','-','*','/']

#######################

def ScaleXtoY(x,xmax,ymax,ymin):
  return max(int(round((1.0*x/xmax)*ymax)),ymin)

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
  
  number_sum=[]
  
  for x in range(terms):
    number_sum.append(random.randrange(-10**digits,10**digits))
  
  
  s=""
  for t in number_sum:
    if t<0:
      s=s[:-1]
    s+=str(t)+"+"
    
  print(s[:-1])
  
  
  answer = input("answer:")
  if answer=="":
    answer="0"
  if int(answer)==sum(number_sum):
    print("correct!")
  else:
    print("incorrect, sum is "+str(sum(number_sum)))
  
  
  
