#WA Fumction that reads a file and display the number of odds and number of vowel present in the file

f=open('file1','r')
vtotal=0
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in f.read():
    if i in vowels:
        vtotal+=1
print("number of vowels is",vtotal)
f.seek(0)
s=f.read()
words=s.split()
print(words)
print(len(words))


#OUTPUT
'''
number of vowels is 7
['Hello', 'How', 'are', 'you?']
4
'''
