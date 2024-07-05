a=input()
n=int(input())
length=len(a)%n
a="0"*(n-length)+a 
list_a=[]
for i in range(0,len(a),3):
    list_a.append(a[i:i+3])
for i in list_a:
    c=int(i, 2)
    print(c,end="")
#inputs
#10110101010010001010011
#3