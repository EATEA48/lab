fname=input("Файл:")
infile = open(fname, 'r')
char = 0
k = 0
c = 0
array=[]
a = infile.read()
for i in range(len(a)):
    array.append(a[i])
    if array[0] ==array[i]:
        char =char+1
    else:
        c=c+char
    i=i+1
b= len(array)
p=c/b
print(array)
print(c)
print(b)
