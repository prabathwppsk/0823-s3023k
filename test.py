path='/home/kali/Documents/redy.txt'
afile=open(path,'r')
edata=afile.read(24)
print(f'Extracted Data : {edata}')
def encraspv0(value): 
    pedata1=0 
    pedata2=0 
    pedata3=0 
    pedata4=0 
    A=1 
    B=2 
    C=3 
    D=4 
    
    if 'A' in edata: 
      A=1 
      n1=edata.count('A') 
      pedata1+=1 
      print(pedata1,n1) 
    
    if 'B' in edata: 
      n2=edata.count('B') 
      pedata2+=2 
      print(pedata2,n2) 
    
    if 'C' in edata: 
      n3=edata.count('C') 
      pedata3+=3 
      print(pedata3,n3) 
      
    if 'D' in edata: 
      n4=edata.count('D') 
      pedata4+=4 
      print(pedata4,n4) 

    expath='/home/kali/Documents/outp.txt' 
    exfile=open(expath,'w')  
    list1=[pedata1,n1,pedata2,n2,pedata3,n3,pedata4,n4,'A1','B2','C3','D4'] 
    print(list1)              
    row=str(list1) 
    exfile.write(row) 

encraspv0(edata)

'''def encraspv1(value): pv1=int(value) result1=bin(pv1) print(f'Proccess Data: {result1}')
encraspv1(edata) '''
