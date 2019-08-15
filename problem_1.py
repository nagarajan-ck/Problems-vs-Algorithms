def root(number,start,end):
	mid=(start+end)//2
	
	
	if((mid**2)<=number and ((mid+1)**2)>number):
		return mid
	elif((mid**2)>number):
		return root(number,start,mid-1)
	else:
		return root(number,mid+1,end)
	


def sqrt(number):    
    if(number<0):
    	return "Negative number do not have a square root"
 
    return root(number,0,number//2+1)
    

    
print(sqrt(27)) #prints 5
print(sqrt(49)) #prints 7
print(sqrt(-1)) #prints 'Negative number do not have a square root'
print(sqrt(0)) #prints 0
