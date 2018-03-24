'''
def triangle(a,b):
    for i in range(a):
        for j in range(b):
            print ('*',end='')
        print ()
        
triangle(3,4)
'''

'''
append = []
with open('class_scores.txt','r') as file:        
    for i in file.readlines():
        l = i.split(' ')
        l[1] = str(int(l[1])+5)
        s = str(l[0])+' '+str(l[1])
        append.append(s)

with open('scores2.txt','w') as file:
    for i in append:
        file.write(i+'\n')
'''
total = 0
with open('grades.txt','r') as file:        
    for i in file.readlines():
        count = 3
        l = i.split(' ')
        for j in l:
            if j != l[0]:
                if int(j) > 34:
                    continue
                else:
                    count -= '1'
        if count == 3:
            total += 1
            
print ("students passed all three: ",total)