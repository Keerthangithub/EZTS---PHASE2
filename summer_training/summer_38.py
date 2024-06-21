'''str="Move-Hyphens-to-Front"
s=""
d=str.count('-')
str=str.split('-')
for i in str:
    s+=i
x='-'*d
e=x+s
print(e)'''
num1=[0,2,2]
num2=[5,6,3]
num1.reverse()
num2.reverse()
c=0
for i in range(len(num1)):
    d=num1[i]+num2[i]
    if d>9:
        c+=2
print(c)