A = 1
B = 2
C = 3
D = 4

rfl=open('/home/kali/Documents/outp.txt','r')
exd=rfl.read(25)
print(exd)

x=exd.isdigit()
#print(x)
if x == False:
  print('extracting...not a pure numeric')
else :
  print('processing')
d1=exd[1]
d1c=exd[4]
d2=exd[7]
d2c=exd[10]
d3=exd[13]
d3c=exd[16]

print(d1,d1c,',',d2,d2c,',',d3,d3c)

def calcconf(p):

   if p=='1':
    res='1red'
    return res
   
   elif p=='2':
    res='2green'
    #print(res) 
    return res
    
   else :
    res='3blue'
    #print(res)
    return res 
  
  
da=calcconf(d1) 
db=calcconf(d2)
dc=calcconf(d3) 

print(da,db,dc)
#print(1,d2c,d3c)
