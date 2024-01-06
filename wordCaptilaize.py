#WA python function that will extract a line/s frome the file and Capitalize first letter of each word of the line/s

f=open('file3','w')
s=input('Enter a String')
while True:
    if s=='':
        break
    else:
        f.write(s)
        f.write('\n')
        s=input('Enter string')
f.close()
f=open('file3','r')
s=f.readline()
while s:
    print(s.title())
    s=f.readline()

#OUTPUT

'''
Enter a Stringhello
Enter stringhi
Enter stringwelcome
Enter stringpython
Enter string
Hello

Hi

Welcome

Python
'''
