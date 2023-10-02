import datetime

def videnty(x):
 if x != 12:
  return(f'failed to fetch data due to unvalid-NIC!{x}')
 else:
   vres=x.isdigit()
   if vres == false:
    return(f'failed to fetch data due to unvalid-NIC!{x}')
   else:
    print('fetch-data-progress!')
	  
def cyear(a):
	da=int(a)
	fid=videnty(da)
	
	fyear=fid[0:4]
	print(fyear)
	sef=int(fyear)
	print(sef)
	#dfyear=int(fyear)
	fmonths=a[5:7]
	dfmonths=int(fmonths)
	jfirst=datetime.date(fyear,1,1)
	if dfmonths > 500:
	 	dfmonths=dfmonths-500
	 	print('Female')
	else:
	   	dfmonths=dfmonths
	   	print('male') 	
	
	bday=jfirst + datetime.timedelta(dfmonths-1)
	
	print(fyear)
	print(bday)

fnic=input('enter_nic_here!')
dfnic=int(fnic)
videnty(dfnic)
cyear(fnic)	
		  
	    
