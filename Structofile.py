#Writing structures to a file

import pickle
f=open('file4','wb')
pickle.dump(['hello','world'],f) #pickling when structures are written to a file
pickle.dump({1:'One',2:'Two'},f)
f.close() #converting structure to byte strem
f=open('file4','rb')
value1=pickle.load(f) #unpickling converting byte stream to original struture
value2=pickle.load(f)
print(value1,value2)
f.close()


#OUTPUT

'''
['hello', 'world'] {1: 'One', 2: 'Two'}
'''
