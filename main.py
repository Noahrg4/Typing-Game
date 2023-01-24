#Noah Reuter-Gushow
#10 word typing test

import csv
import random
import time
from time import perf_counter
word_list = ['for','okay','block','ball','tornado','loss','turn','track','fine','gone','chip','salsa','good','tan','torn','mastery','typing','science','went','for','why','horse','time','hour','okay','popcorn','mom','sister','went','computer','code','bike','run','trail','python','hello']
typeL = []
x = 0
for word in range(10):
    x = random.randint(0,35)
    typeL.append(word_list[x])
typeL = str(typeL)
typeL = typeL.replace('[','')
typeL = typeL.replace(']','')
typeL = typeL.replace(',','')
typeL = typeL.replace('\'','')
q = input('push enter when ready to start')
print(typeL)
t1_start = perf_counter()
user_typing = input('start typing:')
empty_string = '                             '
user_typing = user_typing + empty_string
t1_stop = perf_counter()
s = (int(t1_stop)-int(t1_start))
correct = 0
total = 0
count = 0
for letter in typeL:
    if letter==user_typing[count]:
        correct=correct+1
    total+=1
    count+=1
percent = (correct/total)
percent = round(percent,2)
percent = int(percent * 100)
print('You had',percent,'percent accuracy')
print('Your time was:',s,'seconds')
wpm = int((60/s) * 10)
print('You can type',wpm,'words per minute')
score = int(percent)/s
print('Your score was:',score)
if score>=10:
    name = input('You made the Hall of Fame! What is your name?')
    score = str(score)
    final = (name,':',score)
    final = str(final)
    final = final.replace('(','')
    final = final.replace(')','')
    final = final.replace(',','')
    final = final.replace('\'','')
    with open('Hall Of Fame.csv','a') as file:
        file.write(final+'\n')
else:
    print('Nice try, you need a score of 10+ to be added to hall of fame!')







