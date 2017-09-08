# script which will generate a math problem of varying difficulty based on user input
# Kevin O'Neill

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import random
=======
import random, time, os
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
=======
import random, time, os
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
=======
import random, time, os
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree

import mathsolver as ms

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

<<<<<<< HEAD
def ScaleXtoY(x,xmax,ymax,ymin):
  return max(int(round((1.0*x/xmax)*ymax)),ymin)

<<<<<<< HEAD
<<<<<<< HEAD
=======

=======
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
=======
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
def WriteHeader(logfile):
  c=',' # for csv
  s = ''
  s+='subject_id'+c
  s+='difficulty_level'+c
  s+='time_when_presented'+c
  s+='problem'+c
  s+='correct_answer'+c
  s+='subject_answer'+c
  s+='time_when_answered'
  logfile.write(s+'\n')

def WriteLine(logfile,difficulty_level,presented_time,problem,correct_answer,subj_ans,answered_time):
  c=',' # for csv
  s=''
  s+=str(subj_id)+c
  s+=str(difficulty_level)+c
  s+=str(presented_time)+c
  s+=str(problem)+c
  s+=str(correct_answer)+c
  s+=str(subj_ans)+c
  s+=str(answered_time)
  logfile.write(s+'\n')

def Create_Logfile(subj_id):
  if not os.path.exists('./logs/'):
    os.makedirs('./logs/')
  f = open('./logs/logfile_' + subj_id + '.csv','w')
  WriteHeader(f)
  return f

def ScaleXtoY(x,xmax,ymax,ymin):
  return max(int(round((1.0*x/xmax)*ymax)),ymin)




start_time = time.time()
presented,answered=0,0

subj_id = raw_input('enter subject id: ')

logf=Create_Logfile(subj_id)

  
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
=======
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
=======
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
  
while(1):
  
  while(1):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    current_level=int(input("Difficulty Level? "))
=======
    lvl = input("Difficulty Level? ")
    if lvl == '': lvl = 1
    current_level=int(lvl)
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
=======
    lvl = input("Difficulty Level? ")
    if lvl == '': lvl = 1
    current_level=int(lvl)
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
=======
    lvl = input("Difficulty Level? ")
    if lvl == '': lvl = 1
    current_level=int(lvl)
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
=======
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
  eq=s
  presented = time.time() - start_time
  
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
  
  correct_ans = ms.solve(s)
  
  
  answer = input("answer:")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
  answered = time.time() - start_time
  
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
=======
  answered = time.time() - start_time
  
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
=======
  answered = time.time() - start_time
  
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
  if answer=="":
    answer="0"
  if int(answer)==correct_ans:
    print("correct!")
  else:
    print("incorrect, sum is "+str(correct_ans))
  
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
  
  
=======
=======
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
=======
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
  WriteLine(logf,current_level,presented,eq,correct_ans,answer,answered)
  
  
  
logf.close()
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
=======
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
=======
>>>>>>> parent of 90dfbef... Fixed up math solver code so it plays nice with otree
