def hash(char1):

  long = 0
  k = 433
  for i in range(len(char)):
    long += ord(char[i])*(k*i)
  return long


char = ['h','e','l','l','o','w','o','r','l','d']
print("вх: ",char)
print("вых: ",hash(char))
