a=input()
n=int(input())
length=len(a)%n
a="0"*(n-length)+a 
list_a=[]
for i in range(0,len(a),4):
    list_a.append(a[i:i+4])
list_b=[]
for i in list_a:
    c=int(i,2)
    hex_num=hex(c)
    list_b.append(hex_num)
list_c=[]
for i in list_b:
    d=i.split("x")
    list_c.append(d[1])
print(*list_c)
#10110111000010010011011001010111111000111010010010000
#4