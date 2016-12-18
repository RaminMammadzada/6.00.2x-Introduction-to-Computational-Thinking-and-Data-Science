import pylab
import sys
f=open('julyTemps.txt','r')
count=1
fields=[]
info=[]
list_low=[]
list_high=[]

while(count==1):
    line=f.readline()
    fields=line.split(' ')
    print fields
    if len(fields)<3 or not fields[0].isdigit():
        print 'a'
    elif not len(fields)<3 or fields[0].isdigit():
        list_low.append(fields[1])
        list_high.append(fields[2])
    if fields==['']:
        count=0
listhigh=list_high[:]
list_high=[]
for ww in listhigh:
    list_high.append(ww[:-1])


print 'List low'+ str(list_low)
print 'List high'+ str(list_high)

lowTemps=[]
for word_l in list_low:
    lowTemps.append(int(word_l))

highTemps=[]
for word_h in list_high:
    highTemps.append(int(word_h))

def producePlot(lowTemps, highTemps):
    diffTemps=[]
    for num in range(len(highTemps)):
        diffTemps.append(highTemps[num]-lowTemps[num])
        
    pylab.plot(range(1,32), diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()


producePlot(lowTemps, highTemps)

             
"""
for a in line_1: field.append

word=''
a=0
b=0

for letter in line_1:
        
    if letter!=' ':
        word+=str(letter)
        a=a+1
        print 'birinci' + str(a)
        print letter
    elif (letter==' ')|(word[-2:]=='\n'):
        b=b+1
        print 'ikinci' + str(b)
        print letter
        field.append(word)
        word=''
        


list_low=[]
list_high=[]
row=0
s=''
for letter in a:
    if (s[-2:]=='\n'):
        s=''

    s+=str(letter)        
    if s[-1:]==' ':
        print s
        if (s[:-1]).isdigit:
            row+=1
        if row==2:
            list_low.append(s)
        elif row==3:
            list_high.append(s)
            row=0
        s=''
"""
